import pandas as pd

from ImportModule import *

class EDR_PBCT:

    def __init__(self,pbct):
        self.pbct = pbct

    def generate_deploytab(self,lop_cfg,file):
        df = pd.read_excel(self.pbct,"Vehicle Fixed Calibration",dtype="str",)
        df = df.iloc[9:]
        df = df[["PARAMETER NAME","VALUE"]]
        df = df[df["PARAMETER NAME"].apply(lambda x:x.startswith("LOP_CFG_CH"))]
        # print(df)
        df["VALUE"] = df["VALUE"].apply(lambda x:lop_cfg[x])
        df.reset_index(inplace=True)
        # print(df)
        ret = dict(zip(df["VALUE"].values,df.index))
        fileUtil.dumps_object_to_js_parameter_bypath(ret,"var GBB_DeployTable = ",file,mode="w")
        return ret




def get_lop_cfg(excel):
    df = pd.read_excel(excel,"LOP_CFG",dtype="str")

    ret = dict(zip(df["LOP_CFG_Values"].values,df["Loop"].values))
    # print(ret)
    return ret


def get_fltmonrmap(fltmonr_Configurator,internal_flt_sheet,file):
    """
    提取FltMonr_Configurator的ACCT Autoliv Faults的信息 和 Data sheet的信息
    获取外部DTC ，内部Veoneer Code 和名字的列表
    :param FltMonr_Excel: 提取FltMonr_Configurator的ACCT的Excel
    :return:DTCDefine_List "VeonnerCodeName","DTCRecord","VeoneerCode_Dec","VeoneerCode_Hex","WL","Permanent_Latched","Latched_KeyCycle"的列表
    """
    # 去读ACCT Autoliv Faults参数信息
    # Veoneer Faults

    # *******************************************************************
    df_internalcode = pd.read_excel(fltmonr_Configurator, internal_flt_sheet, dtype='str', header=0)
    df_internalcode = df_internalcode.iloc[2:,[4]]

    df_internalcode.columns = ["VeoneerCode_Hex"]
    df_internalcode.reset_index(inplace=True,drop=True)

    ret = dict(zip(df_internalcode["VeoneerCode_Hex"],df_internalcode.index))
    fileUtil.dumps_object_to_js_parameter_bypath(ret, "var GBB_FltMonrTable = ", file, mode="a")

    # return DTCDefine_List;



if __name__ == "__main__":
    pbct = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\PBCT_SAIC_ZP22_P20_02.xlsm"
    excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\LOP_CFG.xlsx"
    file = "BB_EDR_Parameter_Define.ts"
    # edr_pbct = EDR_PBCT(pbct)
    # lop_cfg = get_lop_cfg(excel)
    # edr_pbct.generate_deploytab(lop_cfg,file)

    fltmonr_Configurator =  r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\FltMonr_Configurator_SAIC_ZP22_P31.00.xlsm"
    internal_flt_sheet = "Veoneer Faults"
    get_fltmonrmap(fltmonr_Configurator,internal_flt_sheet,file)

