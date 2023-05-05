import pandas as pd

from ErrorHandler.ImportModule import *
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)



@dataclass
class Case_Col_Config:
    action_list:List[Any] = field(default_factory=list)
    result_list:List[Any]= field(default_factory=list)

class TSMatrix:
    """
    单个测试Spec的矩阵图
    """
    def __init__(self,df:pd.DataFrame = None,case_start = None,case_name= None ,case_policy= None,case_type = None,case_col_config:Case_Col_Config = Case_Col_Config()):
        self.df_matrix =df
        # print(self.df_matrix)
        # self.case_pre_start = case_pre_start
        self.ts_matrix_support = False # 改矩阵图默认不支持
        self.case_start = case_start
        self.case_name = case_name
        self.case_policy = case_policy
        self.case_type = case_type
        self.case_args = ""
        self.case_col_config = case_col_config
        self.case_list = []

    def __repr__(self):
        return f"case_start: {self.case_start},\n" \
               f"case_name: {self.case_name},case_policy:{self.case_policy},\n" \
               f"ts_matrix_support :{self.ts_matrix_support},\n"\
               f"case_type:{self.case_type},\n" \
               f"sensor_list:{self.case_list},\n" \
               f"case_col_config:{asdict(self.case_col_config)}\n" \




    def update_case_name(self):
        # print(self.df_matrix.iloc[1,0],self.df_matrix.iloc[1,1])
        self.case_name = self.df_matrix.iloc[1,0]

    def update_case_policy(self):
        self.case_policy = self.df_matrix.iloc[1, 1]

    def update_case_list(self):
        # if self.df_matrix.iloc[1, 2] ==''
        self.case_list = self.df_matrix.iloc[1, 2].split(",")

    def update_case_type(self):
        self.case_type = self.df_matrix.iloc[1, 3]
    def update_ts_matrix_support(self):
        # print()
        self.ts_matrix_support = regCompare.is_equal(self.df_matrix.iloc[1,4],"Support")


    def update_case_col(self):
        # self.case_start 为case_col_config 的行
        #self.case_start + 1 为action和result的行
        df_cal_col = self.df_matrix.loc[self.case_start:self.case_start + 1]
        df_cal_col.columns = df_cal_col.iloc[0]
        self.case_col_config.action_list =  list(df_cal_col.loc[self.case_start + 1, "Action_Start":"Action_End"].values)
        self.case_col_config.result_list = list(df_cal_col.loc[self.case_start + 1, "Result_Start":"Result_End"].values)

    def update_matrix_args(self):
        self.case_args = self.df_matrix.iloc[2, 0]
        # print(self.args)

    def update_matrix(self):
        self.df_matrix.columns =  self.df_matrix.loc[self.case_start + 1,:]
        self.df_matrix = self.df_matrix.loc[self.case_start + 2:]
        self.df_matrix.fillna("undefined",inplace = True)

    def refresh(self):
        self.update_case_policy()
        self.update_case_name()
        self.update_case_list()
        self.update_case_type()
        self.update_matrix_args()
        self.update_case_col()
        self.update_ts_matrix_support()
        self.update_matrix()



class SpecSheet:
    """
    一个sheet 里面的数据
    """
    def __init__(self,excel = None,sheet = None,matrixs:List[Any] =None):
        self.excel = excel
        self.sheet = sheet
        self.matrixs = matrixs
        # print(matrixs)
        # print(self.matrixs)

    def update_matrixs(self):
        """
        遍历Sheet去寻找TestCase区域
        Returns:
        """
        if self.matrixs == None:
            self.matrixs = []
        df = pd.read_excel(self.excel, self.sheet, dtype=str)
        Debug_Logger.debug(df)
        case_pre_start = 0
        case_start = 0
        case_end = 0
        # 从上到下一个个遍历数据
        for indx in df.index:
            if df.loc[indx, "CaseIndex"] == "CasePreStart":
                if case_pre_start != 0:
                    raise Exception(
                        f"CasePreStart Config err at index: {indx + 2}"
                    )
                case_pre_start = indx
            elif df.loc[indx, "CaseIndex"] == "CaseStart":
                if case_pre_start == 0:
                    raise Exception(
                        f"CaseStart Config err at index: {indx + 2} not config CasePreStart"
                    )
                case_start = indx
            elif df.loc[indx, "CaseIndex"] == "CaseEnd":
                if case_pre_start == 0 or case_start == 0:
                    raise Exception(
                        f"CaseEnd Config err at index: {indx + 2} not config CasePreStart or CaseStart"
                    )
                case_end = indx
            if case_start != 0 and case_end != 0 and case_pre_start != 0:
                Monitor_Logger.info(f"Get a test case matrix from {case_start + 1} to {case_end + 1}")
                ts_matrix = TSMatrix(df.iloc[case_pre_start + 1:case_end,1:],case_start)
                ts_matrix.refresh()
                Monitor_Logger.info(ts_matrix)
                self.matrixs.append(ts_matrix)
                case_start = 0
                case_end = 0
                case_pre_start = 0

class TestExcel:
    dcs_config_sheet = "DCS_Config"
    func_mapping_sheet = "Function_Mapping"
    def __init__(self, excel=None,sheets =None):
        self.excel = excel
        self.sheets = sheets







if __name__ == "__main__":
    excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\Errorandler\CHT_SWV_SAIC_ZP22_ErrorHandler_Test Specification.xlsm"
    # config = r"C:\Users\victor.yang\Desktop\Work\DCS_Config.xlsx"
    sheet = "DTCStatus2"

    spec_sheet = SpecSheet(excel,sheet)
    spec_sheet.update_matrixs()
    print(spec_sheet.matrixs[0])



    # did_config = DID_Config(config,"DCS_internal_DID")
    # did_config.generate_did_config(r"C:\Users\victor.yang\Desktop\Work")
    #
    # customer_did_config =  DID_Config(config,"DCS_Customer_DID")
    # customer_did_config.generate_did_config(r"C:\Users\victor.yang\Desktop\Work")
    # #
    # signal_config = Singal_Config(config, "DCS_Signal")
    # signal_config.generate_signal_config(r"C:\Users\victor.yang\Desktop\Work")
    #
    # dcs_config = DCS_Config(config,"DCS_Config")
    # dcs_config.get_df_dcs_config(r"C:\Users\victor.yang\Desktop\Work")
    # testSpec.update_matrixs()
    # print(testSpec.matrixs)
    # test_excel = TestExcel(excel)

    # test_excel.get_func_mapping()

    # dcs_config = DCS_Config(excel,"DCS_Config")
    # dcs_config.refresh()

