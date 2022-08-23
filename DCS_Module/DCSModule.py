import pandas as pd


def GetDCSModule(ExcelDir, ObjectType):
    # pd.set_option('display.max_columns', None)
    pd.set_option('max_colwidth', 8000)
    df = pd.read_excel(ExcelDir, ObjectType, dtype=str)
    print(df)

if __name__ == "__main__":
    pass

    ExcelDir = r"E:\Project_Test\Geely_Geea2_HX11\DCS\CHT_SYV_Geely_GEAA2_HX11_DCS_Test Specification.xlsm"
    ObjectType = "DCS_Matrix"
    GetDCSModule(ExcelDir, ObjectType)