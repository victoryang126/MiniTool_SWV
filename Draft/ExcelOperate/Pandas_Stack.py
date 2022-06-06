import pandas as pd


def Handler_MutilSameIndex(ExcelPath,Sheet_Name):
    df = pd.read_excel(ExcelPath, Sheet_Name, dtype='str')
    print(df)
    print("*" * 30)
    print(df.unstack())
    # df_new = df.pivot_table(index=['ID'], aggfunc=lambda x: ','.join(x))
    # print(df_new.reset_index())


   


def Handler_MutilValueInOneCell(ExcelPath, Sheet_Name):
    df = pd.read_excel(ExcelPath, Sheet_Name, dtype='str')
    print(df)
    df["DID"] = df["DID"].str.rstrip()

    # 判断 _VerifiesDOORSRequirements  split为多个元素的时候，拓展元素
    df_DID = df["DID"].str.split('\n', expand=True)
    print("*" * 30)
    # print(df_DID.shape)
    print(df_DID)
    print("df_DID.stack()" + "*" * 30)
    df_DID = df_DID.stack()
    print(df_DID)
    df_DID = df_DID.reset_index(level=1, drop=True)  # 剔除二级index
    df_DID.name = "DID"
    print("*" * 30)
    print(df_DID)
    print("*" * 30)
    df = df.drop(['DID'], axis=1).join(df_DID)  # 根据index 添加 _VerifiesDOORSRequirements
    print(df)


if __name__ == '__main__':
    ExcelPath = "Test.xlsx"
    Sheet_Name = "2"
    Handler_MutilValueInOneCell(ExcelPath, Sheet_Name)
    Sheet_Name1 = "1"
    # Handler_MutilSameIndex(ExcelPath, Sheet_Name1)