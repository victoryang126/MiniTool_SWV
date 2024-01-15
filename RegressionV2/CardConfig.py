# from RegressionV2.ImportModule import *
# class CardRegression:

#
#     def __init__(self,excel,sheet):
#         self.excel = excel
#         self.sheet =

import pandas as pd

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
        # Debug_Logger.debug(col)
        if col.find("Qualify") >= 0:
            # df[col] = df[col].apply(lambda x: x.split(","))
            df[col] = df[col].str.split(",")
    return df

class CardRegression:
    def __init__(self,excel = None,sheet = None):
        self.excel = excel
        self.sheet = sheet

    @property
    def card_config(self):
        return self._card_config
    @card_config.setter
    def card_config(self,value):
        self._card_config = value
    @card_config.getter
    def card_config(self):
        return self._card_config

    @property
    def faults(self):
        return self._faults
    @faults.setter
    def faults(self, value):
        self._faults = value
    @faults.getter
    def faults(self):
        return self._faults

    @property
    def status(self):
        return self._status
    @status.setter
    def status(self,value):
        self._status = value
    @status.getter
    def status(self):
        return self._status

    # @func_monitor
    def get_df_card_config(self,outdir):
        self.card_config = {}
        df = pd.read_excel(self.excel,self.sheet,dtype='str')
        #获取Config
        df.set_index("Config", inplace=True, drop=True)
        # 1.********** 获取头部配置信息字典

        df_header_config = df.loc["ConfigStart":"ConfigEnd",]
        # 去除空白的区域 并获取头部信息的字典
        df_header_config = df_header_config[df_header_config["Abbreviation"].notnull()]
        df_header_config.set_index("Abbreviation",inplace=True)  # 将Abbreviation 设置为index
        df_header_config.fillna("undefined",inplace =True)  # 将空白区域填充为undefined

        df.set_index("Abbreviation", inplace=True, drop=False)
        # Debug_Logger.debug(df_header_config)
        # 获取头部区域文件的属性，主要是读取Sensor的开始行，Status 状态获取的列，Fault状态获取的列
        # print(HeaderDict)
        # 2.********** 根据Header字典的内容循环处理信息，每个sensor的相关属性
        # dcs_row_start	dcs_row_end	NormalCol	StatusColStart	StatusColEnd	FaultColStart	FaultColEnd
        # fileUtil.init_file(outdir, f"{self.sheet}.ts")
        for indx in df_header_config.index:
            # Debug_Logger.debug(indx)
            dcs_row_start = df_header_config.loc[indx, 'RowStart']
            dcs_row_end = df_header_config.loc[indx, 'RowEnd']
            df_temp = df.loc[dcs_row_start:dcs_row_end, ]
            df_temp.columns = df_temp.loc[dcs_row_start,:]

            fault_col_start = df_header_config.loc[indx,"FaultColStart"]
            fault_col_end =df_header_config.loc[indx,"FaultColEnd"]
            faults = df_temp.loc[dcs_row_start, fault_col_start:fault_col_end].to_list()
            # Debug_Logger.debug(f"faults:{faults}")
            fault_cycle = [500 for i in faults]
            self.faults = dict(zip(faults, fault_cycle))

            status_col_start = df_header_config.loc[indx,"StatusColStart"]
            status_col_end = df_header_config.loc[indx, "StatusColEnd"]
            if status_col_start != "undefined":
                self.status = df_temp.loc[dcs_row_start, status_col_start:status_col_end].to_list()
                # Debug_Logger.debug(f"status:{self.status}")

            # 5.******** 对dataframe进行数据处理，重新以 该df的0行为列索引，
            df_temp = df_temp[df_temp["Config"] == "Yes"]
            df_temp.drop(["Config"], inplace=True, axis=1)
            df_temp.drop([dcs_row_start], inplace=True, axis=1)
            df_temp.fillna("undefined", inplace=True)  # 填充空白区域 为undefined

            DealQualiyOrQualifyTime(df_temp)

            card_config = df_temp.to_dict(orient="index")
            self.card_config.update(card_config)

    def refresh(self):
        self.get_df_card_config()
        # Debug_Logger.debug(f"self.card_config {self.card_config}")
        # Debug_Logger.debug(f"self.faults {self._faults}")




if __name__ == "__main__":
    excel = r"C:\PyCharmProject\MiniTool_SWV\Data\RegressionImprove.xlsx"
    sheet = "DCS"
    pass