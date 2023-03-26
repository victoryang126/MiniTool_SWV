
from elftools.elf.elffile import ELFFile
from elftools.dwarf import dwarf_util
import binascii
import struct
if __name__ == "__main__":
    file = r"C:\Users\victor.yang\Desktop\Work\S37\AlgoVar1FixedCal_APPRISe.elf"
    with open(file, 'rb') as f:
        # 创建ELF文件解析器
        elf = ELFFile(f)
        dwarf = elf.get_dwarf_info()
        print(dwarf)
    # Cal_AlgoVar1DataConfig.AlgoSectionHeader.StartAddress
        debug_info = elf.get_section_by_name(".debug_info")
        # print(dir(debug_info)
        print(debug_info.header)
        print(debug_info.data())
        # print(debug_info.header)
        # compressed  data  data_alignment  data_size  elffile  get_string  header  is_null  name stream structs
        # for symbol in debug_info.iter_symbols():
        #     # 获取符号名称
        #     name = symbol.name
        #     # 获取符号地址
        #     address = symbol.entry.st_value
        #     # 获取符号大小
        #     size = symbol.entry.st_size
        #     # 获取符号类型
        #     type = symbol.entry.st_info.type
        #     # 获取符号绑定类型
        #     bind = symbol.entry.st_info.bind
        #     # 获取符号可见性
        #     visibility = symbol.entry.st_other.visibility
        #     # 获取符号索引
        #     index = symbol.entry.st_shndx
        #     # 获取符号名称对应的字符串
        #     string = debug_info.get_string(symbol.entry.st_name)
        #     # 输出符号信息
        #     # print(name, address, size, type, bind, visibility, index, string)
        #     print('Name: %s, Address: %x, Size: %s, Type: %s, Bind: %s, Visibility: %s, Index: %s, String: %s' % \
        #           (name, address, size, type, bind, visibility, index, string))
