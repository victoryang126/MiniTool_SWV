import xml.etree.ElementTree as ET
# 解析ARXML文件
import cantools
armfile = r"C:\Project\SAIC_ZP22\ARiA_Configuration\P10_02\20220930_gx2_ZP22_HEV_EP2_SDM-V01.arxml"
from lxml import etree
db = cantools.database.load_file(armfile)
# db.get
print(db.messages)
print(dir(db.messages[0]))
msg = db.get_message_by_name('SDM_PTEXTCANFD_FrP05')
print(f"is_container: {msg.is_container},senders: {msg.senders},receivers :{msg.receivers}, Cycle:{msg.cycle_time},frame_id:{msg.frame_id:x}")
print(f"is_multiplexed: {msg.is_multiplexed},send_type :{msg.send_type}, protocol:{msg.protocol},is_fd:{msg.is_fd}")
print(f"contained_messages:{msg.contained_messages}")
pdu =msg.contained_messages[0]
print(f"senders: {pdu.senders},receivers :{pdu.receivers}, Cycle:{pdu.cycle_time},frame_id:{pdu.frame_id:x} header_id:{pdu.header_id:x}")
print(f"send_type :{pdu.send_type}, protocol:{pdu.protocol},is_fd:{pdu.is_fd}")
print(pdu.signal_tree)

# print(db.nodes[0].autosar)
# at = db.nodes[0].autosar
# print(type(at))
# db2 = cantools.database.load_file(db.nodes[0].autosar)


# msg = db.get_message_by_name('SCS_PTEXTCANFD_FrP01')
# print(f"is_container: {msg.is_container},senders: {msg.senders},receivers :{msg.receivers}, Cycle:{msg.cycle_time},frame_id:{msg.frame_id:x}")
# print(f"is_multiplexed: {msg.is_multiplexed},send_type :{msg.send_type}, protocol:{msg.protocol},is_fd:{msg.is_fd}")
# print(f"contained_messages:{msg.contained_messages}")
# print(msg.senders,,msg.cycle_time,msg.frame_id,msg.gather_container)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
 '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 '__weakref__', '_assert_signal_values_valid', '_autosar',
 '_bus_name', '_check_mux', '_check_signal', '_check_signal_lengths',
 '_check_signal_tree', '_codecs', '_comments', '_contained_messages',
 '_create_codec', '_create_signal_tree', '_cycle_time', '_dbc',
 '_decode', '_encode', '_encode_container', '_frame_id',
 '_get_mux_number', '_header_byte_order', '_header_id',
 '_is_extended_frame', '_is_fd', '_length', '_name',
 '_protocol', '_send_type', '_senders', '_signal_dict'
    , '_signal_groups', '_signal_tree', '_signals'
    , '_strict', '_unused_bit_pattern'
                 'assert_container_encodable', 'assert_signals_encodable',
 'autosar', 'bus_name', 'comment', 'comments', 'contained_messages',
 'cycle_time', 'dbc', 'decode', 'decode_container', 'decode_simple', 'encode',
 'frame_id', 'gather_container',
 'gather_signals', 'get_contained_message_by_header_id',
 'get_contained_message_by_name',
 'get_signal_by_name', 'header_byte_order',
 'header_id', 'is_container''is_extended_frame', 'is_fd',
 'is_multiplexed', 'length', 'name', 'protocol', 'receivers', 'refresh', 'send_type',
 'senders', 'signal_groups', 'signal_tree', 'signals', 'unpack_container', 'unused_bit_pattern']

# print(dir(db))
'add_arxml', 'add_arxml_file', 'add_arxml_string', 'add_dbc', 'add_dbc_file', 'add_dbc_string', 'add_kcd', 'add_kcd_file', 'add_kcd_string', 'add_sym', 'add_sym_file', 'add_sym_string', 'as_dbc_string', 'as_kcd_string', 'as_sym_string', 'autosar', 'buses', 'dbc', 'decode_message', 'encode_message', 'get_bus_by_name', 'get_message_by_frame_id',
# , 'get_node_by_name', 'messages', 'nodes', 'refresh', 'version'
# print(db.nodes)
# print(dir(db.nodes[0]))
# dbc = r"C:\Project\Geely_GEEA_HX11\ARiA_Configuration\P30_03\SDB21203_HX11_Low_PropulsionCAN_211112.dbc"
# db2 =  cantools.database.load_file(dbc)
# print(db2.messages)
# 打开ARXML文件
# tree = ET.parse(armfile)
# root = tree.getroot()
# print(root)
# for child in root:
#     print(child.tag, child.attrib)
#     for sunzi in child :
#           print(sunzi.tag, sunzi.attrib)
# ns = {'ar':"http://autosar.org/schema/r4.0",
#       'xsi':"http://www.w3.org/2001/XMLSchema-instance"}
#
# nodes = root.findall('./ar:ECU',ns)
# print(nodes)
# for child in root:
#   print(child)
# ecu = root[0].find("./{http://autosar.org/schema/r4.0}AR-PACKAGES")
# print(ecu)
# 获取所有节点
# print(tree)
# nodes = tree.xpath('AR-PACKAGES')
# print(nodes)
# nodes = tree.xpath('.//AR-PACKAGE/ECU-INSTANCE/*')
# # 遍历所有节点
# print(nodes)
# for node in nodes:
#   # 获取节点名称和ID
#   name = node.get('SHORT-NAME')
#   id = node.get('UUID')
#   print('Node: %s, ID: %s' % (name, id))
#   # 获取节点下的所有Frame
#   frames = node.findall('.//CAN-FRAME/FRAME')
#   for frame in frames:
#     # 获取Frame名称和ID
#     fname = frame.get('SHORT-NAME')
#     fid = frame.get('UUID')
#     print('\tFrame: %s, ID: %s' % (fname, fid))
#     # 获取Frame下的所有PDU
#     pdus = frame.findall('.//CAN-PDU/PDU')
#     for pdu in pdus:
#       # 获取PDU名称和ID
#       pname = pdu.get('SHORT-NAME')
#       pid = pdu.get('UUID')
#       print('\t\tPDU: %s, ID: %s' % (pname, pid))
#       # 获取PDU下的所有Signal
#       signals = pdu.findall('.//CAN-SIGNAL/SIGNAL')
#       for signal in signals:
#         # 获取Signal名称和ID
#         sname = signal.get('SHORT-NAME')
#         sid = signal.get('UUID')
#         print('\t\t\tSignal: %s, ID: %s' % (sname, sid))