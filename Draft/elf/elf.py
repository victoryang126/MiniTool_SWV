from elftools.elf.elffile import ELFFile
from elftools.dwarf import dwarf_util
import binascii
import struct
import subprocess

def get_info_from_elf(e_file):  # e_file为需要读取的elf文件
    tmp_dict = {} # 这个字典用于存放变量名和变量地址的对应关系
    file = open(e_file, 'rb')
    elf_file_obj = ELFFile(file)
    for section in elf_file_obj.iter_sections():
        ...
        # 此处把地址以16进制的字符串形式存入字典，可选择自己需要的格式。
        tmp_dict[section.name] = str(hex(section.entry["st_value"]))
    file.close()
    return tmp_dict


class EDI:
    def __init__(self, elf_file_path):
        file_obj = open(elf_file_path, 'rb')
        self.elf_info = ELFFile(file_obj)
        self.dwarf_info = self.elf_info.get_dwarf_info()

    def get_die_by_name(self, die_name, tag_type):
        for cu in self.dwarf_info.iter_CUs():
            print(cu)
            ...
            # 根据name找到对应的die
            # return die
        return None

    # def get_variable_size_by_name(self, var_name):
    #     found_die = self.get_die_by_name(var_name, "variable")
    #     die = found_die
    #     while True:
    #         ...
    #         # 根据条件找到size
    #         type_size = die.value
    #         break
    #     return type_size

if __name__ == "__main__":
    file = r"C:\Users\victor.yang\Desktop\Work\S37\AlgoVar1FixedCal_APPRISe.elf"
    # edi = EDI(file)
    # edi.get_die_by_name("A","B")
    result = subprocess.run(['readelf','-s','-w',file],stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    lines = output.split("\n")
    for line in lines:
        # print(line)
        if "StartAddress" in line:
            parts = line.split()
            print(parts)