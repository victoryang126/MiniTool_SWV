import re

from EDR.ImportModule import *



def CreatFile(file, lmode):
    """
    根据mode创建/打开一个文件
    """
    fileHandle = open(file, mode=lmode)
    return fileHandle


def CloseFile(filehandle):
    """
    关闭文件
    """
    filehandle.close()

def WriteLine(filehandle, desc):
    """
    往文件写入字符串
    """
    filehandle.writelines(desc)


def WritreBBParameter(Para,output):
    """
    写入BB_Parameter文件
    """
    Path = output
    filehandle = CreatFile(Path, "a+")
    filehandle.close()   # 如果没有文件需要重新创建一个，如果有了则不处理
    w_flag = 0
    file = open(Path, "r")
    # 判断是否有存在的参数需要被写入，如果已经存在了则不写入
    # for line in file.readlines():
    #     if(line == (Para + "\n")):
    #         w_flag = 1
    # file.close()
    if(w_flag != 1):
        filehandle = CreatFile(Path, "a+")
        WriteLine(filehandle, Para + "\n")
        filehandle.close()

def transformat_0x(_str):
    """
    字符串转化，将HHHH..HH转化为0xHH 0xHH ... 0xHH
    """
    #剔除含有support的字符串
    pattern = re.compile(r'support', re.I)
    # 剔除含有{的字符串
    pattern_2 = re.compile(r'{', re.I)
    # print(pattern.findall(_str).__len__())
    # print(pattern_2.findall(_str).__len__())
    if(pattern.findall(_str).__len__() != 0):
        return _str
    elif(pattern_2.findall(_str).__len__() != 0):
        return _str
    else:
        pat = re.compile(r'(\s|0x)', re.I)
        r_str = re.sub(pat, "", _str)
        f_srt = ""
        for i in range(0, len(r_str), 2):
            f_srt = f_srt + "0x" + r_str[i: i + 2] + " "
        return f_srt.rstrip()



def CreatEDRdict(input, output):

    sheet_name = "EDR Uploading Data"

    can_id = "CAN_ID"
    evt_id = "EVT_ID"
    signal_name = "SignalShortName"
    start_bit = "Startbit"
    signal_length = "SignalLength"
    signal_source = "SgnalResouce"
    comment = "Comment"


    ColumnsList = [can_id, evt_id, signal_name, start_bit, signal_length, signal_source, comment]
    df = pd.read_excel(input, sheet_name=sheet_name, dtype='str', engine='openpyxl')

    df_total = df[ColumnsList]
    # print(df_total[signal_name])
    # 对每列进行对应的处理
    # df_total = df_total_C.dropna(subset=['SignalShortName'])
    # df_total = df_total_C[~df_total_C[signal_name].isin(["nan", "NAN", "NaN", "", "na"])]

    # print(df_total[signal_name])
    # print(df_total[signal_name])

    df_total[start_bit] = df_total[start_bit].astype('int64')
    df_total[signal_length] = df_total[signal_length].astype('int64')
    df_total[can_id] = df_total[can_id].fillna(method='ffill')
    df_total[evt_id] = df_total[evt_id].fillna(method='ffill')
    df_total[comment] = df_total[comment].astype('string')

    index = 0

    for i in df_total[evt_id]:
        df_total[evt_id][index] = str(i).replace(" ", "").replace("0x", "").replace("0X", "")
        index = index + 1

    index = 0
    # print(df[comment])
    for i in df_total[comment]:
        if "[" in i:
            did_value = i.split("[")[1]
            if "]" in did_value:
                did_value = did_value.split("]")[0].replace("0x", "").replace("0X", "").replace(" ", "")
                did_value = "[" + did_value + "]"
            else:
                did_value = str(i)
                # print("comment value not format [xx]: ")
                # print(did_value)
        elif "N =" in i or "N=" in i:
            # print("++" + i)
            did_value = i.split("=")[1].replace(" ", "").replace("0x", "").replace("0X", "")
            # print("value: " + did_value)
            did_value = transformat_0x(did_value)
        else:
            did_value = str(i)
            # print("comment value not format [xx] or N = xx: ")
            # print(did_value)
        df_total[comment][index] = str(did_value)
        index = index + 1
    # print(df[comment])

    df_evtid = df_total[ColumnsList]
    df_canid = df_evtid.pivot_table(index=[can_id], columns=[evt_id], values=[signal_name, start_bit, signal_length, signal_source, comment], aggfunc=lambda x: x.to_dict(orient="index"))

    # print(df_canid)
    df_canid_dict = df_canid.to_dict(orient="index")
    data = json.dumps(df_canid_dict, indent=4)
    WritreBBParameter("BB_EDR_Dict = ", output)
    WritreBBParameter(data, output)
    WritreBBParameter("", output)

def process_not_support_value(s):
    s = s.replace(" ","")
    if "N=" in s:
        return s.split("=")[1]
    else:
        return "undefined"

def process_other_doc_reqid(s):
    reqid_pattern =  r'(\w+)_(Element|Signal|List)_(\d+)'
    # SAIC_ZP22_EDR_Element_584  GB_EDR_Signal_5 Data_Uploading_Signal_7  ZP22_OEM_EDR_List_12
    search_result = re.search(reqid_pattern,s)
    if search_result:
        return search_result.group()
    else:
        return "undefined"


class EDR_Upload_Config:

    def __init__(self,excel,sheet):
        self.excel = excel
        self.sheet = sheet
        self.df_evt_id = pd.DataFrame()
        self.df = pd.DataFrame()


    def refresh(self):

        columns = ["ID","CAN_ID","EVT_ID","SIGNALSHORTNAME","STARTBIT","SIGNALLENGTH","COMMENT_SWV","TYPE","START","LENGTH","PARAMETER"]
        final_columns = ["ID","CAN_ID","EVT_ID","SIGNALSHORTNAME","STARTBIT","SIGNALLENGTH","TYPE","START","LENGTH","PARAMETER","NOT_SUPPORT","OTHER_ID"]
        df = pd.read_excel(self.excel,self.sheet,dtype='str')
        df.columns = strip_upper_columns(df.columns)
        validate_columns(df.columns,columns, self.sheet)
        df = df[columns]
        #向上填充数据


        #TODO 检测是否有重复的需求id

        df["NOT_SUPPORT"]  = df["COMMENT_SWV"].apply(process_not_support_value)
        df["OTHER_ID"] =  df["COMMENT_SWV"].apply(process_other_doc_reqid)

        self.df_evt_id = df[["CAN_ID","EVT_ID"]].dropna()
        self.df_evt_id.reset_index(inplace=True,drop=True)

        self.df = df[final_columns]
        # print(df.head(5))

    #将id 作为参数，后续从loag 里面拿到相关数据以后，去得到对应的数据
    def generate_evtid(self,parameterfile):
        temp_dict = self.df_evt_id.to_dict(orient="index")
        fileUtil.dumps_object_to_js_parameter_bypath(temp_dict, f"var GBB_EDR_Upload_EVT_ID = ", parameterfile, mode="w")


    def generate_uploading_obj(self,parameterfile):
        df = self.df.copy()
        df["CAN_ID"] = df["CAN_ID"].fillna(method='ffill')
        df["EVT_ID"] = df["EVT_ID"].fillna(method='ffill')
        df.set_index("ID",inplace=True)
        # df.astype({'CAN_ID': 'string',"EVT_ID":'string',"STARTBIT":'int32',"SIGNALLENGTH":'int32',"START":'int32'})
        # df.astype(
        #     {  "STARTBIT": 'int32', "SIGNALLENGTH": 'int32', "START": 'int32'})
        df["EXPECT"] ="undefined"
        df["TIMESTAMP"] = "undefined"
        df.fillna("undefined", inplace=True)
        temp_dict = df.to_dict(orient="index")
        fileUtil.dumps_object_to_js_parameter_bypath(temp_dict,f"var GBB_EDR_Upload_Obj = ",parameterfile,mode="w")

if __name__ == "__main__":
    pass
    excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\CHT_SAIC_ZP22_EDR_Uploading.xlsx"
    sheet = "EDR Uploading Data"
    parameterfile = 'EDR_Upload_Parameters'
    edr_upload = EDR_Upload_Config(excel,sheet)
    edr_upload.refresh()
    # edr_upload.generate_evtid(parameterfile)
    edr_upload.generate_uploading_obj(parameterfile)
