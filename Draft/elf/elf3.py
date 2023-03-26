from elftools.elf.elffile import ELFFile
# 解析ELF文件
import struct
file = r"C:\Users\victor.yang\Desktop\Work\S37\AlgoVar1FixedCal_APPRISe.elf"
with open(file, 'rb') as f:
  elffile = ELFFile(f)
  # 获取包含结构体信息的节段
  struct_section = elffile.get_section_by_name('.rodata')
  if struct_section is None:
    print("No struct info found!")
  else:
    # 读取节段数据
    data = struct_section.data()
    # 模拟结构体的定义格式，以uint32_t和char[]为例
    struct_format = "I16s"
    struct_size = struct_section.entsize
    num_structs = len(data) // struct_size
    # 解析每个结构体的参数名
    for i in range(num_structs):
      struct_data = data[i*struct_size:(i+1)*struct_size]
      struct_values = struct.unpack(struct_format, struct_data)
      param1 = struct_values[0]
      param2 = struct_values[1].decode('ascii').rstrip('\0')
      print("Struct {}: Parameter 1: {}, Parameter 2: {}".format(i+1, param1, param2))