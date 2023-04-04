import pandas as pd
import os
import numpy as np
from Util.LogCFG import *

import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
def get_cb_id_fromdf(x, df):

    if x.strip() in df.index:
        Monitor_Logger.debug(f'test case name :{x.strip()},id: {df.loc[x.strip(), "id"]}')
        return df.loc[x.strip(), "id"]
    else:
        return ""
#2023/3/2 add to check if the value is nan
def is_nan(value):
    if isinstance(value,float):
        if np.isnan(value):
            return True
        else:
            return False
    else:
        return False


def is_cb_id(ID):
    """
    检查是否是codebeamer 的需求ID
    :param ID: 需求ID
    :return:True or false
    """
    pattern = re.compile(r'^\d+$')
    return pattern.match(ID)


def convert_ptc_result_to_cb_result(result):
    """
    :param result: the cell value of _VerificationStatus in TableOfContent
    :return: return the corresonding value in CB
    """
    if result.strip().upper() == "OK":
        return "PASSED"
    elif result.strip().upper() == 'NOK':
        return "FAILED"
    else:
        return "NOT RUN YET"




def convert_id_inexcel_to_cbid_and_nonecbid(cellvalue, cbid_flag):
    # print(type(cellvalue))

    if cbid_flag: # 获取CBid
        if cellvalue != "":

            cellvalue = cellvalue.strip()
            cell_vaule_list = cellvalue.split("\n")
            cell_vaule_list = list(set([int(x) for x in cell_vaule_list if is_cb_id(x)]))
            # cellvalue= "\n".join(cell_vaule_list)
            return cell_vaule_list
        else:
            return []
    else: # 获取非CBID的需求
        if cellvalue != "":
            cellvalue = cellvalue.strip()
            cell_vaule_list = cellvalue.split("\n")
            cell_vaule_list = list(set([x for x in cell_vaule_list if not is_cb_id(x)]))
            # cellvalue = "\n".join(cell_vaule_list)
            return cell_vaule_list
        else:
            return []

@func_monitor
def read_table_of_content(ptc_excel):
    """
    读取Test specification 的TableOfContent
    然后将一个 case 对应一个单元格里面需求ID
    根据单元格的需求ID的数量,
    转换成多行case（名字相同） 对应多行单元格的需求ID 的DataFrame
    :param Spec: Test specification
    :return:Df_PTC_Spec 多行case（名字相同） 对应多行单元格的需求ID 的DataFrame
    """
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)
    # pd.set_option('max_colwidth', 200)

    df_ptc = pd.read_excel(ptc_excel, "Table Of Contents", dtype='str')

    # 读取模块名字
    df_config = pd.read_excel(ptc_excel,"ConfigInfo",dtype='str')

    if "Test Method" not in df_ptc.columns:  # 兼容旧的模板，如果没有Test Method 列，自动添加，且赋值为空
        df_ptc["Test Method"] = ""

    column_list = ["Object Text", "_VerificationStatus", "_VerifiesDOORSRequirements", "_Comment","Test Method"]
    excel_info = {}

    excel_info["test_information"]= df_ptc.iloc[0, 4]
    excel_info["testrun_trackerid"] = df_config.iloc[24, 3]
    excel_info["testcase_trackerid"] = df_config.iloc[21, 3]
    excel_info["testcase_folderid"] = df_config.iloc[22, 3]
    excel_info["release"] = df_config.iloc[23, 3]
    excel_info["AAU"] = df_config.iloc[7,3]
    excel_info["working_set"] =df_config.iloc[25, 3] #2023/3/3 add working set for smart project

    #2023/3/3 Add logic to check if  related id  is not nan,or will raise exception
    if is_nan(excel_info["testcase_trackerid"]):
        raise Exception(f"testcase_trackerid is empty")
    if is_nan(excel_info["testcase_folderid"]):
        raise Exception(f"testcase_folderid is empty")
    if is_nan(excel_info["testrun_trackerid"]):
        raise Exception(f"testrun_trackerid is empty")
    if is_nan(excel_info["release"]):
        raise Exception(f"release is empty")

    df_ptc = df_ptc[column_list]
    df_ptc = df_ptc.iloc[7:, :]
    df_ptc.dropna(subset = ["Object Text"], inplace = True)
    df_ptc["_VerifiesDOORSRequirements"] = df_ptc["_VerifiesDOORSRequirements"].str.rstrip()



    df_ptc.columns = ["name", "status", "Verifies", "Incident ID", "Test Method"]
    df_ptc.fillna("", inplace = True)
    df_ID = df_ptc["Verifies"]
    df_ptc["Verifies"] = df_ID.apply(convert_id_inexcel_to_cbid_and_nonecbid, cbid_flag = True)
    df_ptc["_VerifiesNonCbRequirements"] = df_ID.apply(convert_id_inexcel_to_cbid_and_nonecbid, cbid_flag =False)
    df_ptc["Test Method"] = df_ptc["Test Method"].apply(convert_id_inexcel_to_cbid_and_nonecbid, cbid_flag=True)
    df_ptc["status"] =  df_ptc["status"].apply(convert_ptc_result_to_cb_result)
    df_ptc["Incident ID"] = df_ptc["Incident ID"].apply(convert_id_inexcel_to_cbid_and_nonecbid, cbid_flag=True)

    #检查是否有case名称重复
    df_case_duplicated = df_ptc.duplicated(subset=['name'])
    if True in df_case_duplicated.values:
        Monitor_Logger.info("Same Case")
        Monitor_Logger.info(df_ptc.loc[df_case_duplicated]["name"])
        Debug_Logger.debug("Same Case")
        Debug_Logger.debug(df_ptc.loc[df_case_duplicated]["name"])
        raise Exception("Duplicated test case name, Please check table of content sheet")

    return df_ptc, excel_info





@func_monitor
def generate_cb_case(df_ptc,testcase_list):
    """

    Args:
        df_ptc:  read_table_of_content返回的数据
        testcase_list:从codebeamer 里面根据testcase_folderid 获取的元素

    Returns:
        df .col名字如下
        "name", 根据ptc的excel和cb 文件夹里面的数据结合
        "status", 对于不在ptc的excel 的case，会将status设置为obsolete，其他的都依据ptc excel 的结果转换为test run的
        "Verifies", 全部根据ptc的excel
        "Incident ID",全部根据ptc的excel，但是后期再上传的时候需要访问原来的incident id去extend方式添加
        "Test Method",全部根据ptc的excel
        "id" 根据名称匹配cb文件夹下面case 的id

    """
    if len(testcase_list) == 0: #如果casefodlder下面没有case表示是新的数据全部重新上传即可
        df_ptc["id"] = ""
        Monitor_Logger.info("NONE CASE in CB")
        return df_ptc
    else:
        # 将testcase字典的list转换为df，
        Monitor_Logger.info("Update case")
        casevalue_list = [list(x.values())[0:-1] for x in testcase_list]
        Debug_Logger.debug(f"casevalue_list: {casevalue_list}")
        df_testcase = pd.DataFrame(np.array(casevalue_list),columns=['id','name'])
        df_testcase.set_index("name",inplace=True,drop= False)
        Monitor_Logger.info("get the test case id by the name")
        Debug_Logger.debug("get the test case id by the name")
        df_ptc["id"] = df_ptc["name"].apply(get_cb_id_fromdf,df = df_testcase) # 根据testase的df获取同样名字的id

        # 查找不在df_ptc 里面的case,对不在里面的case Status设置成Obsolete
        obsolte_case_list = [x for x in df_testcase.index if x not in df_ptc["name"].values]
        Debug_Logger.debug(f"obsolte_case_list: {obsolte_case_list}")
        columns = ["id", "name", "status", "Verifies", "Incident ID", "Test Method"]
        empty_list = ["" for x in columns]
        for obsolte_case in obsolte_case_list:
            df_obsolete = pd.DataFrame([empty_list],columns = columns)
            df_obsolete.iloc[0,0] = df_testcase.loc[obsolte_case,"id"]
            df_obsolete.iloc[0,1] = obsolte_case
            df_obsolete.iloc[0,2] = "Obsolete"
            df_ptc = pd.concat([df_ptc,df_obsolete])

        df_ptc.reset_index(inplace=True,drop=True)
        return df_ptc





if __name__ == '__main__':
    pass
    Spec = r"C:\PyCharmProject\CHT_SWV_Geely_GEEA2_HX11_TVV_Test Result.xlsm"
    df_SpecCB_FromCB, excel_info =  read_table_of_content(Spec)
    print(excel_info)
    print(df_SpecCB_FromCB["_VerifiesNonCbRequirements"])
  #   # df_SpecCB_Generate = pd.read_excel(CB_Spec_Generate, "Export")
  #   # SpecCB_Modify = r"C:\Users\victor.yang\Desktop\Work\CB\CHT_SWV_GMW_D30_2S_DCS_Test_Result_CodeBeamer_Modify.xlsx"
  #   #
  #   #
  #   # GenerateSpec_CB_Modify2(df_SpecCB_Generate, Df_ID_Case_FromCB, df_SpecCB_FromCB,Release,
  #   #                                 SpecCB_Modify)
