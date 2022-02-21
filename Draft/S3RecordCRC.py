data = "25A00640001D053F3C00400680FFFF1780000000001300485831315F5032312E3031000104"


def S3RecordCRC(data):
    HexData = 0x00
    for i in range(len(data)//2):
        # print(data[i*2:i*2+2])
        # print(hex(int(data[i*2:i*2+2],16)))
        HexData += int(data[i*2:i*2+2],16)

    CRC_Data = hex(0xFF-HexData&0xFF)
    print(CRC_Data)
    return CRC_Data

if __name__ == '__main__':
    S3RecordCRC(data)