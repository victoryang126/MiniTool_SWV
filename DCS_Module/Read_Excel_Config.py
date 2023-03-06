import pandas as pd

from DCS_Module.ImportModule import *
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

def DealQualiyOrQualifyTime(df) -> pd.DataFrame:
    """
    处理Excel中的qualify和disqualify 时间
    当前的规则是在单元格里面填写 1000, 2000 或者1000,
    然后将单元格弄从两个元素的列表
    Parameters:
        df - DataFrame 包含qualify和disqualify 的数据
    Returns:
        df - 处理了qualifytime和disqualifytime 以后的DataFrane
    Raises:
        NONE
    """
    for col in df:
        if col.find("Qualify") >= 0:
            # df[col] = df[col].apply(lambda x: x.split(","))
            df[col] = df[col].str.split(",")
    return df

class Func_Mapping:
    def __init__(self, excel=None,sheet = None):
        self.excel = excel
        self.sheet = sheet

    @property
    def func_mapping(self):
        return self._func_mapping

    @func_mapping.setter
    def func_mapping(self, value):
        self._func_mapping = value

    @func_mapping.getter
    def func_mapping(self):
        return self._func_mapping


    def get_func_mapping(self):
        df = pd.read_excel(self.excel, "Function_Mapping")
        self.func_mapping = dict(zip(df["Abbreviation"], df["FunctionName"]))
        Debug_Logger.debug(f"self.func_mapping {self.func_mapping}")
        return self.func_mapping


class DCS_Config:
    def __init__(self,excel = None,sheet = None):
        self.excel = excel
        self.sheet = sheet

    @property
    def dcs_config(self):
        return self._dcs_config

    @dcs_config.setter
    def dcs_config(self,value):
        self._dcs_config = value

    @dcs_config.getter
    def dcs_config(self):
        return self._dcs_config

    @property
    def faults(self):
        return self._faults

    @faults.setter
    def faults(self, value):
        self._faults = value

    @faults.getter
    def faults(self):
        return self._faults

    def get_df_dcs_config(self):
        self.dcs_config = {}
        header_row = 9
        header_col = 12
        df = pd.read_excel(self.excel,self.sheet,dtype='str')

        df.set_index("Abbreviation", inplace=True, drop=False)
        df.drop(["SensorType"], inplace=True, axis=1)
        # del df["SensorType"]
        # print(df.head(5))
        # 1.********** 获取头部配置信息字典
        df_header_config = df.iloc[0:header_row, 0:header_col]
        # 去除空白的区域 并获取头部信息的字典
        df_header_config = df_header_config[df_header_config["Abbreviation"].notnull()]
        df_header_config = df_header_config.set_index("Abbreviation")  # 将Abbreviation 设置为index
        df_header_config = df_header_config.fillna("undefined")  # 将空白区域填充为undefined
        # 获取头部区域文件的属性，主要是读取Sensor的开始行，Status 状态获取的列，Fault状态获取的列
        # print(HeaderDict)
        # 2.********** 根据Header字典的内容循环处理信息，每个sensor的相关属性
        # dcs_row_start	dcs_row_end	NormalCol	StatusColStart	StatusColEnd	FaultColStart	FaultColEnd

        for indx in df_header_config.index:

            # 获取头部每行数据的信息，然后用来抓取
            # 根据头部信息抓取对应行的数据段
            dcs_row_start = df_header_config.loc[indx, 'RowStart']
            dcs_row_end = df_header_config.loc[indx, 'RowEnd']
            df_temp = df.loc[dcs_row_start:dcs_row_end, ]
            df_temp.columns = df_temp.loc[dcs_row_start,:]

            fault_col_start = df_header_config.loc[indx,"FaultColStart"]
            fault_col_end =df_header_config.loc[indx,"FaultColEnd"]
            faults = df_temp.loc[dcs_row_start, fault_col_start:fault_col_end].to_list()
            fault_cycle = [500 for i in faults]
            self.faults = dict(zip(faults, fault_cycle))

            # 5.******** 对dataframe进行数据处理，重新以 该df的0行为列索引，
            df_temp = df_temp[df_temp["Config"] == "Yes"]
            df_temp.drop(["Config"], inplace=True, axis=1)
            df_temp.drop([dcs_row_start], inplace=True, axis=1)
            df_temp.fillna("undefined", inplace=True)  # 填充空白区域 为undefined

            DealQualiyOrQualifyTime(df_temp)

            dcs_config = df_temp.to_dict(orient="index")

            self.dcs_config.update(dcs_config)


    def refresh(self):
        self.get_df_dcs_config()
        Debug_Logger.debug(f"self.dcs_config {self.dcs_config}")
        Debug_Logger.debug(f"self.faults {self._faults}")


@dataclass
class Case_Col_Config:
    action_list:List[Any] = field(default_factory=list)
    result_list:List[Any]= field(default_factory=list)

class TSMatrix:
    def __init__(self,df:pd.DataFrame = None,case_start = None,case_name= None ,case_policy= None,case_type = None,case_col_config = Case_Col_Config()):
        self.df_matrix =df
        # print(self.df_matrix)
        # self.case_pre_start = case_pre_start
        self.case_start = case_start
        self.case_name = case_name
        self.case_policy = case_policy
        self.case_type = case_type
        self.case_col_config = case_col_config
        self.sensor_list = []

    def __repr__(self):
        return f"case_start: {self.case_start}," \
               f"case_name: {self.case_name},case_policy:{self.case_policy}," \
               f"case_type:{self.case_type}," \
               f"sensor_list:{self.sensor_list}," \
               f"case_col_config:{asdict(self.case_col_config)}" \


    def update_case_name(self):
        self.case_name = self.df_matrix.iloc[1,0]

    def update_case_policy(self):
        self.case_policy = self.df_matrix.iloc[1, 1]

    def update_sensor_list(self):
        self.sensor_list = self.df_matrix.iloc[1, 2].split(",")

    def update_case_type(self):
        self.case_type = self.df_matrix.iloc[1, 3]


    def update_case_col(self):
        # self.case_start 为case_col_config 的行
        #self.case_start + 1 为action和result的行
        df_cal_col = self.df_matrix.loc[self.case_start:self.case_start + 1]
        df_cal_col.columns = df_cal_col.iloc[0]
        self.case_col_config.action_list =  list(df_cal_col.loc[self.case_start + 1, "Action_Start":"Action_End"].values)
        self.case_col_config.result_list = list(df_cal_col.loc[self.case_start + 1, "Result_Start":"Result_End"].values)


    def update_matrix(self):
        self.df_matrix.columns =  self.df_matrix.loc[self.case_start + 1,:]
        self.df_matrix = self.df_matrix.loc[self.case_start + 2:]
        self.df_matrix.fillna("undefined",inplace = True)

    def refresh(self):
        self.update_case_policy()
        self.update_case_name()
        self.update_sensor_list()
        self.update_case_type()
        self.update_case_col()
        self.update_matrix()




class TestSpec:

    def __init__(self,excel = None,sheet = None,matrixs =[]):
        self.excel = excel
        self.sheet = sheet
        self.matrixs = matrixs

    def update_matrixs(self):
        """
        遍历Sheet去寻找TestCase区域
        Returns:
        """
        df = pd.read_excel(self.excel, self.sheet, dtype=str)
        case_pre_start = 0
        case_start = 0
        case_end = 0

        for indx in df.index:
            if df.loc[indx, "CaseIndex"] == "CasePreStart":
                if case_pre_start != 0:
                    raise Exception(
                        f"CasePreStart Config err at index: {indx + 1}"
                    )
                case_pre_start = indx
            elif df.loc[indx, "CaseIndex"] == "CaseStart":
                if case_pre_start == 0:
                    raise Exception(
                        f"CaseStart Config err at index: {indx + 1} not config CasePreStart"
                    )
                case_start = indx
            elif df.loc[indx, "CaseIndex"] == "CaseEnd":
                if case_pre_start == 0 or case_start == 0:
                    raise Exception(
                        f"CaseEnd Config err at index: {indx + 1} not config CasePreStart or CaseStart"
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

class TestExcel:
    dcs_config_sheet = "DCS_Config"
    func_mapping_sheet = "Function_Mapping"
    def __init__(self, excel=None):
        self.excel = excel







if __name__ == "__main__":
    excel = r"C:\Users\victor.yang\Desktop\Work\CHT_SYV_Geely_GEAA2_HX11_DCS_Test Specification.xlsm"
    sheet = "DCS_NormalStatus"
    testSpec = TestSpec(excel,sheet)
    testSpec.update_matrixs()
    print(testSpec.matrixs)
    test_excel = TestExcel(excel)

    # test_excel.get_func_mapping()

    # dcs_config = DCS_Config(excel,"DCS_Config")
    # dcs_config.refresh()

