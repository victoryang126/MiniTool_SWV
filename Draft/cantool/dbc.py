import canmatrix
# 解析DBC文件
file = r"C:\Project\Geely_GEEA_HX11\ARiA_Configuration\P30_03\SDB21203_HX11_Low_PropulsionCAN_211112.dbc"
matrix = canmatrix.formats.loadp(file)

# print(matrix)
# # 查找所有的node节点
# for node in matrix.nodes:
#  node_id = node
#  node_name = matrix.nodes[node]['comment']
#  print("Node ID: {}, Node Name: {}".format(node_id, node_name))
#  # 查找node发送和接收的frame节点
#  send_frames = matrix.frames_by_tx(node_id)
#  recv_frames = matrix.frames_by_rx(node_id)
#  for frame in send_frames + recv_frames:
#   # 提取frame的属性信息
#   frame_id = frame.frame_id
#   frame_name = frame.name
#   frame_length = frame.size
#   print(" Frame ID: {}, Frame Name: {}, Frame Length: {}".format(frame_id, frame_name, frame_length))
#   # 查找frame包含的signal
#   for signal in frame.signals:
#    # 提取signal的属性信息
#    signal_name = signal.name
#    signal_length = signal.size
#    signal_startbit = signal.get_startbit(bit_numbering=1)
#    print("Signal Name: {}, Length: {}, Start Bit: {}".format(signal_name, signal_length, signal_startbit))