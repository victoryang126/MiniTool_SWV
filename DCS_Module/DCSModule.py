import pandas as pd


def GetDCSModule(ExcelDir, ObjectType):
    # pd.set_option('display.max_columns', None)
    pd.set_option('max_colwidth', 8000)
    df = pd.read_excel(ExcelDir, ObjectType, dtype=str)
    # print(df)
    case_start = 0;
    case_end = 0
    df_case_list =[]
    for ind in df.index:
        if df.loc[ind,"CaseIndex"] == "CaseStart":

            if case_start != 0:
                pass # 如果再找到caseStart的时候已经被赋值了，说明配置有问题，需要报错
            case_start = ind
        elif df.loc[ind,"CaseIndex"] == "CaseEnd":
            case_end = ind
            if case_start ==0:
                pass
                #如果先找到caseEnd则报错误
        #获取了case 的数据段
        if case_start != 0 and case_end !=0:
            print(case_start,case_end)
            df_case = df[case_start:case_end]
            df_case_list.append(df_case)
            # print(df_case)
            # 继续寻找新的case
            case_start = 0
            case_end = 0;
    for df_case in df_case_list:
        print("$"*30)
        print(df_case)


if __name__ == "__main__":
    pass

    ExcelDir = r"C:\Users\victor.yang\Desktop\Work\CHT_SYV_Geely_GEAA2_HX11_DCS_Test Specification.xlsm"
    ObjectType = "DCS_Matrix"
    GetDCSModule(ExcelDir, ObjectType)