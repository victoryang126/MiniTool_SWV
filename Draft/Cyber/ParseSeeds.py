'''
Author: your name
Date: 2022-02-17 08:52:13
LastEditTime: 2022-02-17 09:20:20
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \Scriptse:\Project_Test\Geely_Geea2_HX11\Cyber\ENT\ParseSeeds.py
'''
import os
import sys
import struct
import time

def GetSeeds():
    file = open( r"E:\Project_Test\Geely_Geea2_HX11\Cyber\ENT\Logging.asc", "r" )
    lines = file.readlines()
    file.close()
    
    SeedParser = ""
    for line in lines:
        line = line.strip()
        # print(line)
        if '0e 80 1c 01 40 05 00 05 67 01' in line:
            AsdmResponseSeeds = line.split(" 0e 80 1c 01 40 05 00 05 67 01 ")[1].split(" ")[:3]
            # print(AsdmResponseSeeds)
            for parse in AsdmResponseSeeds:
               SeedParser += parse
    
    seedsFile = open("E:\Project_Test\Geely_Geea2_HX11\Cyber\ENT\SeedsFromTRNG.txt", "w+")
    seedsFile.write(SeedParser)
    seedsFile.close()

def Convert2Bin():    
    stringFile = open('E:\Project_Test\Geely_Geea2_HX11\Cyber\ENT\SeedsFromTRNG.txt','r')
    binaryFile = open('E:\Project_Test\Geely_Geea2_HX11\Cyber\ENT\SeedsFromTRNG.bin','wb')

    a = stringFile.read()
    count = 0
    while count<len(a):
        str1 = a[count:count+2] #two characters in one  (from 1 E => 0x1E)
        count = count + 2
        b = int(str1, 16) #from hex to integer  (from 0x1E =>030)
        c = struct.pack('B', b)  #from integer to ASCII  'B' unsigned char integer
        binaryFile.write(c)
    stringFile.close()
    binaryFile.close()

def RunEntTool():    
    os.system('cmd /k "E:\Project_Test\Geely_Geea2_HX11\Cyber\ENT\ent.exe E:\Project_Test\Geely_Geea2_HX11\Cyber\ENT\SeedsFromTRNG.bin"')
    
GetSeeds()
Convert2Bin()
RunEntTool()
