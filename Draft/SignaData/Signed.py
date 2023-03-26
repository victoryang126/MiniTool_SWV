

"""原码original code
反码 AntiCode
补码：Complement Code
若已知补码为 1111 1000，如何求其原码呢？
1. 方法1：求负数 原码—>补码 的逆过程。
注意：符号位保持不变！
（A）先 - 1，得到 1111 0111
（B）取反（符号位保持不变，其他位置按位取反 ），得到 1000 1000
2. 方法2：
注意：符号位保持不变！
（A）将这个二进制数中（即 1111 1000），除了符号位，其余位置按位取反，得 1000 0111
（B）+ 1，得到 1000 1000
————————————————
版权声明：本文为CSDN博主「我真不会嘤语」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qk233/article/details/108715207
"""

def original_to_complement(data,bit_length):
    return '{:X}'.format(data & (2 ** bit_length - 1))

def complement_to_original(data,bit_length):
    max_value = 2** (bit_length - 1) - 1
    # print(max_value)
    xor = 2 ** bit_length - 1
    # print(xor)
    if data > max_value: #means it is negative
        # data is complement
        anti = data - 1
        original = 0 - (anti ^ xor)
        return original
    else:
        return data

print(complement_to_original(0x800,12))
