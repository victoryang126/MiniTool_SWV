import pandas as pd

from ErrorHandler.ImportModule import *
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)



class Func_Mapping:
    """
    一个用来生成函数mapping的类
    """
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


class Flt_Data:
    #用来获取snapshot和extended data 数据的函数
    def __init__(self,excel,sheet):
        self.excel = excel
        self.sheet = sheet
        self.df_snapshot = pd.DataFrame()

        self.snapshot_recordnumbers = []

        self.snapshot_did_config = {}
        self.snapshot_did_datarecord_config = {}
        self.snapshot_flag = True #是否支持的标志
        self.df_extend_data = pd.DataFrame()
        self.extend_data_recordnumbers = []
        self.extend_data_flag = True #是否支持的标志
        self.extend_data_config = {}

        self.snapshot_elements = {} #element->did字典
        self.extend_data_elements = []

    def refresh(self):
        df = pd.read_excel(self.excel,self.sheet)
        df.set_index("Config",inplace=True)

        #TODO 看这个数据是否支持去决定是否生成对应的数据
        self.snapshot_flag = regCompare.is_equal(df.loc["Snapshot","Number"],"Support")
        self.extend_data_flag = regCompare.is_equal(df.loc["ExtData","Number"],"Support")

        #处理snapshot的数据
        self.df_snapshot = df.loc["Snapshot_Start":"Snapshot_End", ["Number", "DataRecord", "Element","Length","StartBit","BitSize"]]
        self.df_snapshot.columns = self.df_snapshot.loc["Snapshot_Start"]
        self.df_snapshot.drop(["Snapshot_Start"], inplace = True)
        self.df_snapshot.fillna(method="ffill",inplace = True)
        self.df_snapshot["DID"] =  self.df_snapshot["DID"].apply(lambda x: re.sub("0x|\s", "", x))
        self.df_snapshot["SnaoshotRecordNumber"] =  self.df_snapshot["SnaoshotRecordNumber"].apply(lambda x: re.sub("0x|\s", "", x))


        #先获取snapshot 和did的关系
        # df_snapshot_confg = pd.pivot_table(self.df_snapshot,index=["SnaoshotRecordNumber"],values="DID",aggfunc=lambda x:",".join(x.values))
        df_temp = self.df_snapshot[["SnaoshotRecordNumber","DID"]]
        df_temp.drop_duplicates(inplace=True, keep="first")
        df_snapshot_confg = pd.pivot_table(df_temp, index=["SnaoshotRecordNumber"], values="DID",
                                           aggfunc=lambda x: list(x.values))
        df_snapshot_confg.reset_index()
        self.snapshot_did_config = df_snapshot_confg.to_dict(orient="index")
        self.snapshot_recordnumbers = list(self.snapshot_did_config.keys())
        print(self.snapshot_did_config)

        #获取did和数据长度的字典
        df_did_length =  self.df_snapshot[["DID", "Length"]]
        df_did_length.drop_duplicates(inplace=True, keep="first")
        df_did_length.set_index("DID", inplace=True, drop=True)
        self.snapshot_did_datarecord_config = df_did_length.to_dict(orient="index")
        #再获取did 里面的元素
        df_snapshot_group = self.df_snapshot.groupby("DID", as_index=False, sort=False)
        for did, group in df_snapshot_group:
            self.snapshot_did_datarecord_config[did]["Element"] = {}
            group.drop(["DID", 'Length','SnaoshotRecordNumber'], inplace=True, axis=1)
            group.set_index("Element", drop=True, inplace=True)
            self.snapshot_did_datarecord_config[did]["Element"] .update(group.to_dict(orient="index"))
        print(self.snapshot_did_datarecord_config)

        #处理extended data
        self.df_extend_data = df.loc["ExtData_Start":"ExtData_End", ["Number", "Element","Length","StartBit","BitSize"]]
        self.df_extend_data.columns = self.df_extend_data.loc["ExtData_Start"]
        self.df_extend_data.drop(["ExtData_Start"], inplace=True)
        self.df_extend_data.fillna(method="ffill", inplace=True)
        self.df_extend_data["ExtDataRecordNumber"] =  self.df_extend_data["ExtDataRecordNumber"].apply(lambda x: re.sub("0x|\s", "", x))

        df_length = self.df_extend_data[["ExtDataRecordNumber", "Length"]]
        df_length.drop_duplicates(inplace=True, keep="first")
        df_length.set_index("ExtDataRecordNumber", inplace=True, drop=True)
        self.extend_data_config = df_length.to_dict(orient="index")
        self.extend_data_recordnumbers = list(self.extend_data_config.keys())
        df_extend_data_group = self.df_extend_data.groupby("ExtDataRecordNumber", as_index=False, sort=False)
        for extDataRecordNumber, group in df_extend_data_group:
            self.extend_data_config[extDataRecordNumber]["Element"] = {}
            group.drop([ 'Length', 'ExtDataRecordNumber'], inplace=True, axis=1)
            group.set_index("Element", drop=True, inplace=True)
            self.extend_data_config[extDataRecordNumber]["Element"].update(group.to_dict(orient="index"))
        print(self.extend_data_config)

        #获取snapshot和ExtData里面所有的元素
        df_element_did = self.df_snapshot[["DID","Element"]].drop_duplicates(keep="first")
        self.snapshot_elements =  dict(zip(df_element_did["Element"].values,df_element_did["DID"].values))
        self.extend_data_elements = list(self.df_extend_data["Element"].drop_duplicates(keep="first").values)
        print(self.snapshot_elements)
        # print(self.df_snapshot["Element"].drop_duplicates(keep="first").values,self.df_extend_data["Element"].values)


    def generate_GBB_Snapshot_DID_Config(self,outdir,file):
        fileUtil.dumps_object_to_js_parameter(self.snapshot_did_config, "var GBB_Snapshot_DID_Config = ", outdir, file, "w")

    def generate_GBB_Snapshot_DID_DataRecord_Config(self,outdir,file):
        fileUtil.dumps_object_to_js_parameter(self.snapshot_did_datarecord_config, "var GBB_Snapshot_DID_DataRecord_Config = ", outdir, file, "w")

    def generate_GBB_ExtDataRecord_Config(self,outdir,file):
        fileUtil.dumps_object_to_js_parameter(self.extend_data_config,"var GBB_ExtDataRecord_Config = ",outdir,file,"w")


    def generate_BB_Create_DTC(self,outdir,file):
        scripts = []
        scripts.append(f"/**\n")
        scripts.append(f" * function used to create dtc obj, it contains the snapshot,extened data, dtc status\n")
        scripts.append(f" * @param DTCRecord\n")
        scripts.append(f" * @version V1.0 MinitoolGenerated\n")
        scripts.append(f" */\n")
        scripts.append(f"function BB_Create_DTC(DTCRecord)\n{'{'}\n")
        scripts.append(f"\tDTCRecord = DTCRecord.replace(/(0x|\s)/gi,"");\n")
        scripts.append(f"\tthis.Description = DTCRecord;\n")
        scripts.append(f"\tthis.DTCRecord = DTCRecord;\n")
        scripts.append(f"\tthis.DTCStatus = '00';\n")
        scripts.append(f"\tthis.SnapshotRecord_Flag = false;\n")
        scripts.append(f"\tthis.ExtDataRecord_Flag = false;\n")
        scripts.append(f"\tthis.SnapshotResp = '';\n")
        scripts.append(f"\tthis.Snapshot = {'{'} \n")
        snapshots = [f"\t\'{i}\': new BB_Create_SnapshotRecord(\'{i}\')" for i in self.snapshot_recordnumbers]
        scripts.append(",\n".join(snapshots) + "\n")
        scripts.append(f"\t{'}'}\n")

        scripts.append(f"\tthis.ExtData = {'{'} \n")
        extDatas = [f"\t\'{i}\': new BB_Create_ExtDataRecord(\'{i}\')" for i in self.extend_data_recordnumbers]
        scripts.append(",\n".join(extDatas) + "\n")
        scripts.append(f"\t{'}'}\n")

        scripts.append(f"{'}'}\n")
        # scripts.append(f"//prototype function\n")
        # scripts.append(f"BB_Create_DTC.prototype.Check_ExtDataRecord = BB_Check_ExtDataRecord\n")
        # scripts.append(f"BB_Create_DTC.prototype.Check_Snapshot = BB_Check_SnapshotRecord\n")
        # for value in self.extend_data_elements:
        #     scripts.append(f"BB_Create_DTC.prototype.Update_Ext_{value} = BB_Update_Ext_{value}\n")
        # for value in self.snapshot_elements:
        #     scripts.append(f"BB_Create_DTC.prototype.Update_Snap_{value} = BB_Update_Snap_{value}\n")


        fileUtil.generate_script("".join(scripts),outdir,file)

    def generate_snapshot_func(self,did,value):
        set_func = f"function BB_Set_Snap_{value}()\n{'{'}\n\t\n{'}'}\n\n"
        update_func = f"function BB_Update_Snap_{value}(DTC,SnapshotRecordNumber,Data)\n{'{'}\n" \
                      f"\tDTC.Snapshot[SnapshotRecordNumber].SnapshotDataRecord[\"{did}\"][\"{value}\"] = Data;\n"\
                      f"\tvar action = String.Format(\"SnapshotRecordNumber {'{0}'} Update_Snap_{value} to {'{1}'} \",SnapshotRecordNumber,Data);\n" \
                      f"\tRESULT.InterpretEqualResult(action,[\"0000\",\"AssignValue\"]);\n"\
                      f"{'}'}\n\n"
        scrtipts = [set_func,update_func]
        return scrtipts

    def generate_extend_data_func(self, value):
        set_func = f"function BB_Set_Ext_{value}()\n{'{'}\n\t\n{'}'}\n\n"
        update_func = f"function BB_Update_Ext_{value}(DTC,ExtDataRecordNumber,Data)\n{'{'}\n" \
                      f"\tDTC.ExtData[ExtDataRecordNumber].ExtDataRecord[\"{value}\"] = Data;\n" \
                      f"\tvar action = String.Format(\"ExtDataRecordNumber {'{0}'} Update_Ext_{value} to {'{1}'} \",ExtDataRecordNumber,Data);\n" \
                      f"\tRESULT.InterpretEqualResult(action,[\"0000\",\"AssignValue\"]);\n" \
                      f"{'}'}\n\n"
        scrtipts = [set_func, update_func]
        return scrtipts

    def generate_set_update_func(self,outdir,file):
        scripts = []
        for value in self.extend_data_elements:
            scripts.extend(self.generate_extend_data_func(value))
        for value in self.snapshot_elements:
            did = self.snapshot_elements[value]
            scripts.extend(self.generate_snapshot_func(did,value))
        fileUtil.generate_script("".join(scripts), outdir, file)


    def generate_all(self):
        pass



if __name__ == "__main__":
    excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\Errorandler\CHT_SWV_SAIC_ZP22_ErrorHandler_Test Specification.xlsm"
    sheet = "Snapshot_ExtendedData"
    outdir = r"C:\Users\victor.yang\Desktop\Work\Scripts\Temp"
    flt_data = Flt_Data(excel,sheet)
    flt_data.refresh()
    flt_data.generate_GBB_Snapshot_DID_Config(outdir,"GBB_Snapshot_DID_Config.ts")
    flt_data.generate_GBB_Snapshot_DID_DataRecord_Config(outdir, "GBB_Snapshot_DID_DataRecord_Config.ts")
    flt_data.generate_GBB_ExtDataRecord_Config(outdir,"GBB_ExtDataRecord_Config.ts")
    flt_data.generate_BB_Create_DTC(outdir,"DTC.ts")
    flt_data.generate_set_update_func(outdir,"Set_Update.ts")