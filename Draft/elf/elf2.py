from elftools.elf.elffile import ELFFile
# 打开ELF文件
import struct
file = r"C:\Users\victor.yang\Desktop\Work\S37\AlgoVar1FixedCal_APPRISe.elf"
with open(file, 'rb') as f:
  elffile = ELFFile(f)
  # 获取符号表
  symtab = elffile.get_section_by_name('.symtab')
  # 获取字符串表
  strtab = elffile.get_section_by_name('.strtab')
  # 遍历符号表中的符号信息
  for symbol in symtab.iter_symbols():
    # 获取符号名称
    name = symbol.name
    if name == "Cal_AlgoVar1DataConfig":
      break;
    # 获取符号地址
    address = symbol.entry.st_value
    # 获取符号大小
    size = symbol.entry.st_size
    # 获取符号类型
    type = symbol.entry.st_info.type
    # 获取符号绑定类型
    bind = symbol.entry.st_info.bind
    # 获取符号可见性
    visibility = symbol.entry.st_other.visibility
    # 获取符号索引
    index = symbol.entry.st_shndx
    # 获取符号名称对应的字符串
    string = strtab.get_string(symbol.entry.st_name)
    # 输出符号信息
    # print(name, address, size, type, bind, visibility, index, string)
    print('Name: %s, Address: %x, Size: %s, Type: %s, Bind: %s, Visibility: %s, Index: %s, String: %s' % \
       (name, address, size, type, bind, visibility, index, string))

  print(dir(symbol.entry))
  # print(strtab.data)
  # compressed  data  data_alignment  data_size  elffile  get_string  header  is_null  name stream structs

  # for i in range(strtab.num_symbols()):
  #   offset = strtab.get_symbol(i)["st_name"]
  #   name = strtab.get_string(offset)
  #   print(name)