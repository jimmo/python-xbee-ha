# HA Spec -- http://www.zigbee.org/zigbee-for-developers/applicationstandards/zigbeehomeautomation/
# ZCL Spec -- http://www.zigbee.org/download/standards-zigbee-cluster-library/
# Zigbee & Zigbee Pro -- http://www.zigbee.org/zigbee-for-developers/network-specifications/zigbeepro/
# ZLL -- http://www.zigbee.org/zigbee-for-developers/applicationstandards/zigbee-light-link/

# Direct document downloads:
# HA Spec -- http://www.zigbee.org/?wpdmdl=2129
# Zigbee Pro Stack Profile -- http://www.zigbee.org/wp-content/uploads/2014/11/docs-07-4855-05-0csg-zigbee-pro-stack-profile-2.pdf
# Zigbee Spec -- http://www.zigbee.org/wp-content/uploads/2014/11/docs-05-3474-20-0csg-zigbee-specification.pdf
# ZCL Spec -- http://www.zigbee.org/?wpdmdl=2177
# ZLL - http://www.zigbee.org/?wpdmdl=2132

from enum import IntEnum


class Endpoint(IntEnum):
  ZDO = 0x00


class Profile(IntEnum):
  ZIGBEE = 0x0000
  HA = 0x0104
  ZLL = 0xC05E


class Cluster(IntEnum):
  # Zigbee Spec -- "2.4.3.1.5 Simple_Desc_req"
  ZIGBEE_ZDO_SIMPLE_DESCRIPTOR = 0x0004
  # Zigbee Spec -- "2.4.4.1.5 Simple_Desc_resp"
  ZIGBEE_ZDO_SIMPLE_DESCRIPTOR_RESPONSE = 0x8004

  #  Zigbee Spec -- "2.4.3.1.6 Active_EP_req"
  ZIGBEE_ZDO_ACTIVE_ENDPOINTS = 0x0005
  #  Zigbee Spec -- "2.4.4.1.6 Active_EP_resp"
  ZIGBEE_ZDO_ACTIVE_ENDPOINTS_RESPONSE = 0x8005

  #  Zigbee Spec -- "2.4.3.1.7 Match_Desc_req"
  ZIGBEE_ZDO_MATCH_DESCRIPTORS = 0x0006
  #  Zigbee Spec -- "2.4.4.1.7 Match_Desc_resp"
  ZIGBEE_ZDO_MATCH_DESCRIPTORS_RESPONSE = 0x8006

  # Zigbee Spec -- "2.4.3.2.2 Bind_req"
  ZIGBEE_ZDO_BIND = 0x0021
  # Zigbee Spec -- "2.4.4.2.2 Bind_rsp"
  ZIGBEE_ZDO_BIND_RESPONSE = 0x8021

  #  Spec -- "2.4.3.1.11 Device_annce"
  ZIGBEE_ZDO_DEVICE_ANNOUNCE = 0x0013

  # Zigbee Spec -- "2.4.4.3.9 Mgmt_NWK_Update_notify"
  ZIGBEE_ZDO_NETWORK_UPDATE = 0x8038

  # HA Spec -- "2.2.2.1 General"
  HA_BASIC = 0x0000
  HA_POWER_CONFIGURATION = 0x0001
  HA_IDENTIFY = 0x0003
  HA_GROUPS = 0x0004
  HA_SCENES = 0x0005
  HA_ONOFF = 0x0006
  HA_ONOFF_CONFIGURATION = 0x0007
  HA_LEVEL_CONTROL = 0x0008
  HA_POLL_CONTROL = 0x0020
  # HA Spec -- "2.2.2.4 Lighting"
  HA_COLOR = 0x0300

  ZLL_COMMISIONING = 0x1000

  HA_ELECTRICITY_MEASUREMENT = 0x0b04
  HA_DIAGNOSTICS = 0x0b05


class ZclCommand(IntEnum):
  # ZCL Spec -- "2.4 General Command Frames"
  READ_ATTRIBUTES = 0x00
  READ_ATTRIBUTES_RESPONSE = 0x01
  WRITE_ATTRIBUTES = 0x02
  WRITE_ATTRIBUTES_UNDIVIDED = 0x03
  WRITE_ATTRIBUTES_RESPONSE = 0x04
  WRITE_ATTRIBUTES_NO_RESPONSE = 0x05
  CONFIGURE_REPORTING = 0x06
  CONFIGURE_REPORTING_RESPONSE = 0x07
  READ_REPORTING_CONFIGURATION = 0x08
  READ_REPORTING_CONFIGURATION_RESPONSE = 0x09
  REPORT_ATTRIBUTES = 0x0a
  DEFAULT_RESPONSE = 0x0b
  DISCOVER_ATTRIBUTES = 0x0c
  DISCOVER_ATTRIBUTES_RESPONSE = 0x0d
  READ_ATTRIBUTES_STRUCTURED = 0x0e
  WRITE_ATTRIBUTES_STRUCTURED = 0x0f
  WRITE_ATTRIBUTES_STRUCTURED_RESPONSE = 0x10

  # ZCL Spec -- "3.8.2.3 -- Commands Received" (On/Off)
  HA_ONOFF_OFF = 0x00
  HA_ONOFF_ON = 0x01
  HA_ONOFF_TOGGLE = 0x02

  # ZCL Spec -- "3.10.2.3 -- Commands Received" (Level Control)
  HA_LEVEL_CONTROL_MOVE_TO_LEVEL = 0x00
  HA_LEVEL_CONTROL_MOVE = 0x01
  HA_LEVEL_CONTROL_STEP = 0x02
  HA_LEVEL_CONTROL_STOP = 0x03
  HA_LEVEL_CONTROL_MOVE_TO_LEVEL_ON_OFF = 0x04
  HA_LEVEL_CONTROL_MOVE_ON_OFF = 0x05
  HA_LEVEL_CONTROL_STEP_ON_OFF = 0x06
  HA_LEVEL_CONTROL_STOP_ON_OFF = 0x07

  # ZCL Spec -- "5.2.2.3 Commands Received" (Color)
  HA_COLOR_MOVE_TO_HUE = 0x00
  HA_COLOR_MOVE_TO_SATUATION = 0x03
  HA_COLOR_MOVE_TO_HUE_SATURATION = 0x06
  HA_COLOR_MOVE_TO_COLOR_TEMPERATURE = 0x0a


class ZclAttribute(IntEnum):
  # HA Spec -- "3.2.2.2 Attributes" (Basic)
  HA_BASIC_ZCLVERSION = 0x0000
  HA_BASIC_APPLICATION_VERSION = 0x0001
  HA_BASIC_STACK_VERSION = 0x0002
  HA_BASIC_HW_VERSION = 0x0003
  HA_BASIC_MANUFACTURER_NAME = 0x0004
  HA_BASIC_MODEL_ID = 0x0005
  HA_BASIC_DATE_CODE = 0x0006
  HA_BASIC_POWER_SOURCE = 0x0007

  # HA Spec -- "3.8.2.2 Attributes" (On/Off)
  HA_ONOFF_ONOFF = 0x0000

  # HA Spec -- "3.10.2.2 Attributes" (Level Control)
  HA_LEVEL_CONTROL_CURRENT_LEVEL = 0x0000
  HA_LEVEL_CONTROL_REMAINING_TIME = 0x0001
  HA_LEVEL_CONTROL_ON_OFF_TRANSITION_TIME = 0x0010
  HA_LEVEL_CONTROL_ON_LEVEL = 0x0011

  # HA Spec -- "5.2.2.2 Attributes" (Color)
  HA_COLOR_HUE = 0x0000
  HA_COLOR_SATURATION = 0x0001
  HA_COLOR_REMAINING_TIME = 0x0002
  HA_COLOR_TEMPERATURE = 0x0007

  # ATTRIBUTE_NAMES = {
  #   Profile.HA: {
  #     Cluster.HA_BASIC: {
  #       HA_BASIC_ZCLVERSION: 'ZCL version',
  #       HA_BASIC_APPLICATION_VERSION: 'Application version',
  #       HA_BASIC_STACK_VERSION: 'Stack version',
  #       HA_BASIC_HW_VERSION: 'Hardware version',
  #       HA_BASIC_MANUFACTURER_NAME: 'Manufacturer',
  #       HA_BASIC_MODEL_ID: 'Model',
  #       HA_BASIC_DATE_CODE: 'Date',
  #       HA_BASIC_POWER_SOURCE: 'Power',
  #     }
  #   }
  # }


class FrameControl(IntEnum):
  # ZCL Spec - "2.3.1.1 Frame Control Field"

  # 0 == entire profile, 1 == cluster specific.
  FRAME_TYPE_MASK = 1 << 0
  FRAME_TYPE_PROFILE_COMMAND = 0
  FRAME_TYPE_CLUSTER_COMMAND = 1 << 0

  # Is this a manufacturer-specific frame?
  MANUFACTURER_SPECIFIC_MASK = 1 << 2
  MANUFACTURER_SPECIFIC = 1 << 2

  # Direction (0 == client to server 1 == server to client).
  DIRECTION_MASK = 1 << 3
  DIRECTION_CLIENT_TO_SERVER = 0
  DIRECTION_SERVER_TO_CLIENT = 1

  # Disable the default response (1 == only default response if error).
  DISABLE_DEFAULT_RESPONSE_MASK = 1 << 4


class Status(IntEnum):
  SUCCESS = 0x00


class DataType(IntEnum):
  # ZCL Spec -- "2.5.2 Data Types"
  BOOLEAN = 0x10
  UINT8 = 0x20
  UINT16 = 0x21
  UINT64 = 0x27
  ENUM8 = 0x30
  ENUM16 = 0x31
  CHARACTER_STRING = 0x42
