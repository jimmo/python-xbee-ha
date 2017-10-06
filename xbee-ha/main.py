import asyncio
import struct
import serial

from xbee.asyncio import ZigBee

#from . import spec
import spec

class XBeeHA:
  def __init__(self):
    self._serial = serial.Serial('/dev/ttyUSB0', 115200)
    self._xbee = ZigBee(self._serial, escaped=True)
    self._frame_id = 0x7a

  def stop(self):
    self._xbee.halt()
    self._serial.close()

  def next_frame_id(self):
    f = self._frame_id
    self._frame_id = (self._frame_id % 255) + 1
    return bytes((f,))

  async def at(self, command, unpack):
    self._xbee.at(frame_id=self.next_frame_id(), command=command)
    frame = await self._xbee.wait_read_frame()
    return struct.unpack(unpack, frame['parameter'])

  async def run(self):
    addr32h, = await self.at('SH', '>I')
    addr32l, = await self.at('SL', '>I')
    pan_id, = await self.at('OP', '>Q')
    print('XBee status: 0x{:016x} 0x{:08x}{:08x}'.format(pan_id, addr32h, addr32l))

    asyncio.get_event_loop().create_task(self.ping())

    while True:
      frame = await self._xbee.wait_read_frame()
      if frame['id'] == 'at_response':
        self._on_xbee_at_response(frame)
      elif frame['id'] == 'tx_status':
        self._on_xbee_tx_status(frame)
      elif frame['id'] == 'rx_explicit':
        self._on_xbee_rx_explicit(frame)
      else:
        print('Unknown frame ID {}'.format(frame['id']))

  async def ping(self):
    while True:
      await asyncio.sleep(1.0)
      self._xbee.at(frame_id=self.next_frame_id(), command='CH')

  def _on_xbee_rx_explicit(self, frame):
    profile_id, = struct.unpack('>H', frame['profile'])
    cluster_id, = struct.unpack('>H', frame['cluster'])
    source_endpoint_id, = struct.unpack('>B', frame['source_endpoint'])
    dest_endpoint_id, = struct.unpack('>B', frame['dest_endpoint'])
    source_addr16, = struct.unpack('>H', frame['source_addr'])
    source_addr64, = struct.unpack('>Q', frame['source_addr_long'])

    if profile_id == spec.Profile.ZIGBEE.value and dest_endpoint_id == spec.Endpoint.ZDO.value:
      self._on_zdo(source_addr64, source_addr16, source_endpoint_id, cluster_id, frame['rf_data'])
    else:
      self._on_zcl(source_addr64, source_addr16, source_endpoint_id, dest_endpoint_id, profile_id, cluster_id, frame['rf_data'])

  def _on_zdo(self, source_addr64, source_addr16, source_endpoint_id, cluster_id, data):
    if cluster_id == spec.Cluster.ZIGBEE_ZDO_DEVICE_ANNOUNCE.value:
      # ZigBee Spec -- "2.4.3.1.11 Device_annce"
      seq, addr16, addr64, cap = struct.unpack('<BHQB', data)
      d = None
      print('zdo device announce (addr64: 0x{:016x}, addr16: 0x{:04x})'.format(addr64, addr16))
    else:
      seq, = struct.unpack('<B', data[:1])
      data = data[1:]
      print('zdo (addr64: 0x{:016x}, addr16: 0x{:04x}, cluster_id: 0x{:04x})'.format(source_addr64, source_addr16, cluster_id), seq, data)

  def _on_zcl(self, source_addr64, source_addr16, source_endpoint_id, dest_endpoint_id, profile_id, cluster_id, data):
    print('zcl (addr64: 0x{:016x}, addr16: 0x{:04x}, profile_id: 0x{:04x}, cluster_id: 0x{:04x}, sep: 0x{:02x}, dep: 0x{:02x})'.format(source_addr64, source_addr16, profile_id, cluster_id, source_endpoint_id, dest_endpoint_id))

  def _on_xbee_at_response(self, frame):
    command = frame['command'].decode()
    status, = struct.unpack('>B', frame['status'])
    print('at command ', status, command)

  def _on_xbee_tx_status(self, frame):
    discover_status, = struct.unpack('>B', frame['discover_status'])
    dest_addr16, = struct.unpack('>H', frame['dest_addr'])
    deliver_status, = struct.unpack('>B', frame['deliver_status'])
    frame_id, = struct.unpack('>B', frame['frame_id'])
    retries, = struct.unpack('>B', frame['retries'])
    print('tx status', frame_id)

if __name__ == '__main__':
  x = XBeeHA()
  loop = asyncio.get_event_loop()
  loop.create_task(x.run())
  loop.run_forever()
  loop.close()
  x.stop()
