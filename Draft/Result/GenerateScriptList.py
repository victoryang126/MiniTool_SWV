import os

a = r"C:\Project\Geely_GEEA2_HX11\ARiA_Configuration\P31_02\Scripts\EDR\Victor.txt"
b = r"C:\Project\Geely_GEEA2_HX11\ARiA_Configuration\P31_02\Scripts\EDR\Victor_2.txt"
with open(a, 'r', encoding='UTF-8') as f:
    a_List = f.readlines()
b_List = []
for i in a_List:
    i = i.split(";")[0] +";False;;No result\n"
    print(i)
    b_List.append(i)

with open(b, 'w', encoding='UTF-8') as f:
    f.writelines(b_List)