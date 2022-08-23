import re
import pandas as pd
from openpyxl import Workbook, load_workbook


def GetMsgFromDBC(FilePath):
    """
    根据DBC文件获取相关测节点的信号
    Args:
        FilePath - DBC 文件路径
    Returns:
        MsgObj - Msg的字典，包含Msg 的所有信息
    Raises:
        KeyError - raises an exception
    """
    SignalKeys = ["StartBit", "Length", "Format", "Unsigned","Factor", "Offset", "Min", "Max", "Unit","Node"]
    MsgKeys = ["MsgName", "Length"]
    MsgObj = {}
    ''' 得到dbc文件的绝对路径'''
    if FilePath:
        # print(FilePath)
        f = open(FilePath, "r",encoding = "GBK")  # 设置文件对象
    else:
        # print("读取文件失败！")
        raise Exception("No DBC files")
        return 0

    """

    NodesPattern:节点
    MessagePattern：消息
    SignalPattern：信号
    """
    # NodesPattern = re.compile(r"BU_: (.*)", re.S)
    # BO_ 1296 TIHU_IHU_15: 8 Vector__XXX ID,MSgName, Msg Length.Node
    # MessagePattern = re.compile(r"BO_ (.*?) (.*?): (.*?) (.*)", re.S)
    # ID_Dec , MSgName, MsgLength
    MessagePattern = re.compile(r"BO_ (.*?) (.*?): (.*?) ", re.S)
    # SG_ CurrentTimeSecond : 47|6@0+ (1,0) [0|59] ""  ABM
    # 信号名字,起始bit.信号长度，信号格式，是否符号位 精确度，偏移量 最小值，最大值，单位  节点
    # 0        1          2      3        4        5       6     7         8    9  10

    # SG_　　　　　　　　　　　代表一个信号信息的起始标识
    # ABM3_VehVerticalAcc  代表信号名
    # SG_ ABM3_VehVerticalAcc:23|16@0+(0.00098,-21.592)[-21.592|21.592]"m/s^2"GW
    # @0表示是Motorola格式（Intel格式是1），+表示是无符号数据
    SignalPattern = re.compile('''SG_ (.*?) : (.*?)\|(.*?)@(\d)(\+|\-) \((.*?),(.*?)\) \[(.*?)\|(.*?)\] "(.*?)" (.*)''', re.S)
    DefaultValue = '''BA_ "GenSig(.*?)" SG_ (\d+) signalname (\d+);'''
    # BA_ "GenMsgCycleTime" BO_ 250 10;
    CycleTimePattern = re.compile('''BA_ "GenMsgCycleTime" BO_ (.*?) (.*?);''', re.S)
    line = f.readline()
    while line:

        """ 匹配出节点 """
        # NodesSearched = re.search(NodesPattern, line.strip())
        # if NodesSearched:
        #     node = NodesSearched.group(1).split(" ")
        #     #print(node)
        """ 匹配出消息 """
        MessageSearched = re.search(MessagePattern, line.strip())

        if MessageSearched:
            """如果匹配到了message，则获取到message的相关参数 
             这四个参数分别是 messgage ID ;message name ; messgae dataLenth ,message sender
            """
            Message = list(MessageSearched.groups())  # ('1296', 'TIHU_IHU_15', '8', 'Vector__XXX')
            TmpKey = hex(int(Message[0]))  # 将10 进制ID转换位16进制，作为key
            MsgObj[TmpKey] = dict(zip(MsgKeys, Message[1:]))
            MsgObj[TmpKey]["Signal"] = {}
            MsgObj[TmpKey]["CycleTime"] = "undefined"
            """读取下一行"""
            line = f.readline()
            """因为有些message并没有定义signal，所以 下一行还是message"""
            MessageSearched = re.search(MessagePattern, line.strip())
            SignalSearched = re.search(SignalPattern, line.strip())
            """下一行如果不是message的内容 就一定是signal的内容了，且是这个message下面的signal"""
            if not MessageSearched:
                while SignalSearched:
                    """获取信号的参数追加到改信号Signal的字典里面去。如果没有匹配到信号，必定空行"""
                    signal = list(SignalSearched.groups())
                    SignObjTemp = {}
                    SignObjTemp[signal[0]] = dict(zip(SignalKeys, signal[1:]))
                    # print(SignObjTemp)
                    MsgObj[TmpKey]["Signal"].update(SignObjTemp)
                    # 再次解析信号，直到这个message下的信号全部解析完毕
                    line = f.readline()
                    SignalSearched = re.search(SignalPattern, line.strip())
        else:
            line = f.readline()
            CycleTimeSearched = re.search(CycleTimePattern, line)
            if CycleTimeSearched:
                Cycle = list(CycleTimeSearched.groups())
                TmpKey = hex(int(Cycle[0]))
                MsgObj[TmpKey]["CycleTime"] = Cycle[1]
            # MessageSearched = re.search(MessagePattern, line.strip()) #space line
            # print(line)
    f.close()  # 将文件关闭
    # print(MsgObj)
    # # ObjectDict, f, indent = 4
    # with open("C:\Python\MiniTool\DataSource\msg.txt", 'a', encoding='UTF-8') as f:
    #     json.dump(MsgObj,f,indent = 4)
    return MsgObj


def ImportDataIntoExcel(DBCPath, ExcelPath):
    """
    根据DBC文件获取相关测节点的信号
    将Msg对象根据特定格式导入到Excel
    Args:
        DBCPath - DBC 文件路径
        ExcelPath - 将Msg对象根据特定格式导入到Excel
    Returns:
        NONE
    Raises:
        KeyError - raises an exception
    """
    MsgObj = GetMsgFromDBC(DBCPath)
    # print(MsgObj)
    MsgIDList = []
    MsgLengthList = []
    MsgNameList = []
    MsgCycleList = []
    SignaNameList = []
    for MsgID in MsgObj:
        TempID = [MsgID for Signal in MsgObj[MsgID]["Signal"]]
        TempLength = [MsgObj[MsgID]["Length"] for Signal in MsgObj[MsgID]["Signal"]]
        TempMsg = [MsgObj[MsgID]["MsgName"] for Signal in MsgObj[MsgID]["Signal"]]
        TempSig = [Signal for Signal in MsgObj[MsgID]["Signal"]]
        TempCycle = [MsgObj[MsgID]["CycleTime"] for Signal in MsgObj[MsgID]["Signal"]]
        MsgIDList.extend(TempID)
        MsgLengthList.extend(TempLength)
        MsgNameList.extend(TempMsg)
        SignaNameList.extend(TempSig)
        MsgCycleList.extend(TempCycle)

    # data = {"Abbreviation":MsgIDList,"MsgName":MsgNameList,"MsgID":MsgIDList,
    #         "MsgDLC":MsgLengthList,"CycleTime":MsgCycleList,"InValidSg":SignaNameList}
    # print(data.values())
    # df = DataFrame(data)
    # print(MsgIDList.__len__(),MsgNameList.__len__(),MsgLengthList.__len__(),MsgCycleList.__len__(),SignaNameList.__len__())
    data = [["ID" + MsgIDList[i], MsgNameList[i], MsgIDList[i], MsgLengthList[i], MsgCycleList[i], SignaNameList[i]] for
            i in range(len(MsgIDList))]
    book = load_workbook(ExcelPath)
    ws = book["Communication"]

    for row in data:
        ws.append(row)
    rows = ws.rows
    for row in rows:
        line = [col.value for col in row]
    try:
        book.save(ExcelPath)
    except Exception:
        raise Exception("Reg_Excel is used by other programs, Please closed")

if __name__ == '__main__':
    # ImportDataIntoExcel(DBCPath,ExcelPath)
    pass
    FilePath = "C:\Python\MiniTool\DataSource\SC2_A55_HSCAN_P30.dbc"
    print(GetMsgFromDBC(FilePath))

