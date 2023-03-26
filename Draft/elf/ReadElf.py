
from elftools.elf.elffile import ELFFile
from elftools.dwarf import dwarf_util
import binascii
import struct
if __name__ == "__main__":
    file = r"C:\Users\victor.yang\Desktop\Work\S37\AlgoVar1FixedCal_APPRISe.elf"
    # with open(file,'rb') as f:
    #     e = ELFFile(f)
    #     # x04\xc2\x02\x00\x17Cal_AlgoCalDataConfigTypeTag\x00_}\x10\x9c\xf8\x01\x12AlgoSectionHeader\x00\xdb4\x02\x00$\x02
    #     # \x00\x12AlgoVarAefFileNameCalData\x00\xd1\x1d\x02\x00
    #     # x00Mt\x10$\x12StartAddress\x00\xcc4\x02\x00\x04\x02  # \x00\x12EndAddress\x00\xcc4\x02\x00\x04\x02#\x04\x12
    #     # Cal_AlgoVar1DataConfig.AlgoSectionHeader.StartAddress
    #     # segments 就是 sectiion Cal_algovar1Dataconfig的数据
    #     # for se in e.iter_segments():
    #     #     with open("elf_segments.txt","w") as f:
    #     #         f.writelines(str(se.header) +"\n")
    #     #         f.writelines(str(se.data()))
    #     # print(e.header)
    #     # Container({'e_ident': Container(
    #     #     {'EI_MAG': [127, 69, 76, 70], 'EI_CLASS': 'ELFCLASS32', 'EI_DATA': 'ELFDATA2LSB',
    #     #      'EI_VERSION': 'EV_CURRENT', 'EI_OSABI': 'ELFOSABI_SYSV', 'EI_ABIVERSION': 0}), 'e_type': 'ET_EXEC',
    #     #            'e_machine': 'EM_TRICORE', 'e_version': 'EV_CURRENT', 'e_entry': 0,
    #     #            'e_phoff': 52, program header table 在elf文件的偏移
    #     #            'e_shoff': 266796,('0x4122c') section header table 在elf 文件的偏移量
    #     #            'e_flags': 1048576, 'e_ehsize': 52,
    #     #            'e_phentsize': 32,  programm header table 中，每个表项的长度
    #     #            'e_phnum': 1,   program header table 一共有多少个表项
    #     #            'e_shentsize': 40,  section 中每一个表项的长度
    #     #            'e_shnum': 23, section table 中 一共有多少个表项Entry
    #     #            'e_shstrndx': 1}) 字符串表在节区表中的索引
    #     # print(e.num_segments())
    #     # print(e.num_sections())
    #     # if e.has_dwarf_info():
    #     #     print(1)
    #     #     dwarfinfo = e.get_dwarf_info()
    #     #     print(dir(dwarfinfo))
    #     #     for cu in dwarfinfo.iter_CUs():
    #     #         print(cu.header,cu.cu_offset)
    #     # print(e.get_dwarf_info())
    #     # section = e.get_section(4)
    #     # print(section.header)
    #     # section = e.get_section_by_name(".rodata.CalHndler_Lcfg.Cal_AlgoVar1DataConfig")
    #     # 0x8003c000
    #     # 0x7c1c.rodata.CalHndler_Lcfg.Cal_AlgoVar1DataConfig
    #     # print(section.header)
    #     # print(section.data())
    #     # """
    #     # print(hex(section['sh_addr']), hex(section['sh_size']), section.name)
    #     a = []
    #     # """
    #     i = 0
    #     for section in e.iter_sections():
    #         print(str(i) + ":" + "*"*30)
    #         # print(section.header)
    #         if section.name == ".rodata.CalHndler_Lcfg.Cal_AlgoVar1DataConfig": # Algo整个sheet的地址区域
    #             # print(section.header)
    #             # Container({'sh_name': 6, 'sh_type': 'SHT_PROGBITS', 'sh_flags': 536870914, 'sh_addr': 2147729408,
    #             #            'sh_offset': 628 (0x274), 'sh_size': 31772, 'sh_link': 0, 'sh_info': 0, 'sh_addralign': 4,
    #             #            'sh_entsize': 0})
    #             # print(section.structs)
    #             with open("elf_Cal_AlgoVar1DataConfig.txt", "w") as f:
    #                 f.write(str(section.header) + "\n")
    #                 f.write(str(section.data()))
    #         if section.name == ".debug_info": # 可能包含了一些对象地址的相关信息，能找到algo 里面的某些结构体的前缀
    #             # print(section.header)
    #             #改sectoin 里面的属性
    #             # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
    #             #  '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
    #             #  '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
    #             #  '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_compressed', '_decompressed_align',
    #             #  '_decompressed_size', 'compressed', 'data', 'data_alignment', 'data_size', 'elffile', 'header',
    #             #  'is_null', 'name', 'stream', 'structs']
    #             # print(dir(section.structs))
    #             #结构体里面的数据
    #             # ['Elf_Attr_Subsection_Header', 'Elf_Attribute_Tag', 'Elf_Chdr', 'Elf_Dyn', 'Elf_Ehdr', 'Elf_Hash',
    #             #  'Elf_Nhdr', 'Elf_Nt_File', 'Elf_Phdr', 'Elf_Prop', 'Elf_Prpsinfo', 'Elf_Rel', 'Elf_Rela', 'Elf_Relr',
    #             #  'Elf_Shdr', 'Elf_Stabs', 'Elf_Sunw_Syminfo', 'Elf_Sym', 'Elf_Verdaux', 'Elf_Verdef', 'Elf_Vernaux',
    #             #  'Elf_Verneed', 'Elf_Versym', 'Elf_abi', 'Elf_addr', 'Elf_byte', 'Elf_half', 'Elf_ntbs', 'Elf_offset',
    #             #  'Elf_sword', 'Elf_sxword', 'Elf_ugid', 'Elf_uleb128', 'Elf_word', 'Elf_word64', 'Elf_xword',
    #             #  'Gnu_Hash', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
    #             #  '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
    #             #  '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
    #             #  '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
    #             #  '_create_arm_attributes', '_create_chdr', '_create_dyn', '_create_ehdr', '_create_elf_hash',
    #             #  '_create_gnu_abi', '_create_gnu_debugaltlink', '_create_gnu_hash', '_create_gnu_property',
    #             #  '_create_gnu_verdef', '_create_gnu_verneed', '_create_gnu_versym', '_create_leb128', '_create_note',
    #             #  '_create_ntbs', '_create_phdr', '_create_rel', '_create_shdr', '_create_stabs', '_create_sunw_syminfo',
    #             #  '_create_sym', 'create_advanced_structs', 'create_basic_structs', 'e_ident_osabi', 'e_machine',
    #             #  'e_type', 'elfclass', 'little_endian']
    #             # Container({'sh_name': 93, 'sh_type': 'SHT_PROGBITS', 'sh_flags': 0, 'sh_addr': 0,
    #             # 'sh_offset': 38598, (0x96c6)
    #             #            'sh_size': 181443, 'sh_link': 0, 'sh_info': 0, 'sh_addralign': 0, 'sh_entsize': 0})
    #             # print(section.structs)
    #             print(dir(section.elffile)) # 这里面还是一共映射到ELF的section 里面
    #             # section.elffile 下面的数据
    #             # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__',
    #             #  '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__',
    #             #  '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
    #             #  '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
    #             #  '_decompress_dwarf_section', '_get_section_header', '_get_section_header_stringtable',
    #             #  '_get_section_name', '_get_segment_header', '_identify_file', '_make_elf_hash_section',
    #             #  '_make_gnu_hash_section', '_make_gnu_verdef_section', '_make_gnu_verneed_section',
    #             #  '_make_gnu_versym_section', '_make_section', '_make_section_name_map', '_make_segment',
    #             #  '_make_sunwsyminfo_table_section', '_make_symbol_table_index_section', '_make_symbol_table_section',
    #             #  '_parse_elf_header', '_read_dwarf_section', '_section_header_stringtable', '_section_name_map',
    #             #  '_section_offset', '_segment_offset', 'address_offsets', 'close', 'e_ident_raw', 'elfclass',
    #             #  'get_dwarf_info', 'get_ehabi_infos', 'get_machine_arch', 'get_section', 'get_section_by_name',
    #             #  'get_section_index', 'get_segment', 'get_shstrndx', 'get_supplementary_dwarfinfo', 'has_dwarf_info',
    #             #  'has_ehabi_info', 'header', 'iter_sections', 'iter_segments', 'little_endian', 'load_from_path',
    #             #  # 'num_sections', 'num_segments', 'stream', 'stream_len', 'stream_loader', 'structs']
    #             # print(dir(section))
    #             # for subsection in section.elffile.iter_sections():
    #             #     print(hex(subsection['sh_addr']),hex(subsection['sh_size']),subsection.name)
    #             #     print(subsection.data())
    #             # with open("elf_debug_info.txt","w") as f:
    #             #     f.write(str(section.header) + "\n")
    #             #     f.write(str(section.data()))
    #         if section.name == ".symtab":
    #             print("symtab")
    #             for sym in section.iter_symbols():
    #                 # print(sym.name,sym.entry)
    #                 if sym.name == ".rodata.CalHndler_Lcfg.Cal_AlgoVar1DataConfig": # 看起里还是对应的section 里面的表头信息
    #                     print(sym.entry.items)
    #             # with open("elf_symtab.txt", "w") as f:
    #             #     f.write(str(section.header) + "\n")
    #             #     f.write(str(section.data()))
    #         if section.name == ".strtab":
    #             print("strtab")
    #             # with open("elf_strtab.txt", "w") as f:
    #             #     f.write(str(section.header) + "\n")
    #             #     f.write(str(section.data()))
    #         if section.name == ".note":
    #             print("note")
    #             with open("elf_note.txt", "w") as f:
    #                 f.write(str(section.header) + "\n")
    #                 f.write(str(section.data()))
    #         if section.name == ".shstrtab":
    #             print("shstrtab")
    #             with open("elf_shstrtab.txt", "w") as f:
    #                 f.write(str(section.header) + "\n")
    #                 f.write(str(section.data()))
    #         if section.name == "csa_tc0":
    #             print("0x1000 csa_tc0")
    #             with open("elf_csa_tco.txt", "w") as f:
    #                 f.write(str(section.header) + "\n")
    #                 f.write(str(section.data()))
    #         if section.name == ".debug_line":
    #             print("debug_line")
    #             with open("elf_debug_line.txt", "w") as f:
    #                 f.write(str(section.header) + "\n")
    #                 f.write(str(section.data()))
    #         if section.name == ".debug_abbrev":
    #             print("debug_abbrev")
    #             with open("elf_debug_abbrev.txt", "w") as f:
    #                 f.write(str(section.header) + "\n")
    #                 f.write(str(section.data()))
    #             # print(section.data())
    #         print(hex(section['sh_addr']),hex(section['sh_size']),section.name)
    #         print(section.header)
    #         i = i+1
    #         # if section.data():
    #         #     a.append(str(section.data()))
    #     # print(a[5])
    #     # """
    #     # with open("elf.txt","w") as f:
    #     #     for i ,data in enumerate(a):
    #     #         f.writelines(["*"*20])
    #     #         f.writelines([data])
    #     #         f.write("\n")
    #     # # """
    #         # print(section.data())
    #     # # print(section.structs)
    #     # # print(section.get_symbol(1))
    #     # print(section.data_size)
    #     # print(section.data_alignment)
    #
    #     # print(dir(section.structs))
    #     # stru = section.structs
    #     # print(stru.Elf_Chdr)
    #     # print(dir(stru.Elf_Stabs))
    #     # print(stru.Elf_Chdr.FLAG_COPY_CONTEXT)
    #     # print(section.data())
    #     # for se in e.iter_segments():
    #     #     print(se.header)
    #     # for i in section.structs:
    #     #     print(i)
    #     # Cal_AlgoVar1DataConfig
    #     # Cal_AlgoVar1DataConfig.AlgoSectionHeader.StartAddress
    #     # print(section.get_string(2))
    #     # for se in section.iter_symbols():
    #     #     print(se.header)
    #     # print("$" * 10)
    #
    #     # for section in e.iter_sections():
    #     #     # print(dir(section.elffile))
    #     #     print(hex(section['sh_addr']),section.name,section.header)
    #     #     # print(section.data())
    #         # print(dir(section.data))
    #         # print(dir(section.structs.Elf_Attr_Subsection_Header))
    #         # print(dir(section.structs.Elf_Phdr))
    #         # if hasattr(section, "stringtable"):
    #         #     print(section.stringtable)
    #         # if hasattr(section, "iter_subsections"):
    #         #     for s in section.__getitem__("Address"):
    #         #         print(s.header)
    #         # if hasattr(section, "iter_subsections"):
    #         #     for s in section.iter_subsections():
    #         #         print(s.header)
    #         # if hasattr(section,"iter_symbols"):
    #         #     for s in section.iter_symbols():
    #         #         print(s.name)
    # from elftools.elf.elffile import ELFFile

    # 打开ELF文件
    with open(file, 'rb') as f:
        # 创建ELF文件解析器
        elf = ELFFile(f)
        for se in elf.iter_segments():
            print(se.header)
            data = se.data()
            with open("../elf_segments.txt", "w") as f:
                # f.writelines(str(se.header) +"\n")
                f.writelines(str(se.data()))
        # 获取ELF文件中的.symtab节

        symtab = elf.get_section_by_name('.symtab')
         # 遍历.symtab节中的符号
        for symbol in symtab.iter_symbols():
             # 如果符号是一个结构体
            # print(symbol.entry.st_info)
            # if symbol.entry.st_info.type == 'STT_OBJECT' and symbol.entry.st_shndx != 'SHN_UNDEF' and symbol.entry.st_size > 0:
            #     data = elf.get_section(symbol.entry.st_shndx).data()[symbol.entry.st_value:]
            #     struct_fmt = '<' + 'I' * (symbol.entry.st_size // 4)
            #     struct_data = struct.unpack(struct_fmt, data)
            #     print(f'{symbol.name}:')
            #     for i, member in enumerate(struct_data):
            #          member_name = f'member{i}'
            #     print(f' {member_name}: {member}')
            #  # """
             # elf 文件中，符号表中的每个符号都有一个st_info字段，改字段包含了符号的类型信息，
             # #STT_OBJECT 表示符号类型为对象类型，
             # STB_GLOBAL 是指符号的绑定类型为全局绑定，即符号的地址可以在elf文件的任何位置访问到，
             # """
            if symbol.entry.st_info.type == 'STT_OBJECT' and symbol.entry.st_info.bind == 'STB_GLOBAL' and symbol.entry.st_size > 0:
                # 获取结构体的地址和大小
                print(dir(symbol.entry))

                print(symbol.entry.items)
                print(type(symbol.entry.values))
                addr = symbol.entry.st_value
                size = symbol.entry.st_size
                # with open(file, 'rb') as f:
                #     # f.seek(addr)
                #     # f.seek(0,1)
                #     data = f.read(size)
                #     # print(data)
                print(hex(addr),hex(size))
                    # f.seek(addr)
                    # f.seek(0,1)
                    # data = f.read(size)
                # print(data)
                # struct_fmt = '<' + 'I' * (size // 4)
                # struct_data = struct.unpack(struct_fmt, data)
                # for i, member in enumerate(struct_data):
                #     print('\tmember{0}: {1:x}'.format(i, member))
               #  print(data)
               # # 输出结构体的成员变量的值
               # #  print(symbol.name,addr,size)
               #  struct_fmt = '<'
               #  # struct_fmt 是一个字符串，使用<字符来指定数据的字节顺序为endian
               #  #然后根据结构体中的每个成员变量类型来指定对应的格式字符，例如I表示
               #  for i in range(len(data)):
               #      if i % 4 == 0:
               #          struct_fmt += 'I'
               #      elif i % 2 == 0:
               #          struct_fmt += 'H'
               #      else:
               #          struct_fmt += 'B'
               #  struct_fmt = '<' + 'I' * (size // 4)
               #  struct_data = struct.unpack('<' + 'I' * (size // 4), f.read(symbol.entry.st_size))
               #  struct_size = struct.calcsize('<' + 'I' * (symbol.entry.st_size // 4))
               #  print(struct_size)
               #  print(symbol.entry.st_size)
               #  data = elf.get_section(symbol.entry.st_shndx).data()[
               #         symbol.entry.st_value:symbol.entry.st_value + symbol.entry.st_size]
               #  struct_data = struct.unpack('<' + 'I' * (symbol.entry.st_size // 4), data)
               #  for i, member in enumerate(struct_data):
               #      print('\tmember{}: {}'.format(i, member))

