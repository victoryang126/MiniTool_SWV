

from ImportModule import *
from Errorhandler_Spec import *
from TestCaseHeader import *
from ErrorHandler_Scripts_Object import  *
from ErrorHandler_Config import *

class Func_Policy:
    FUNC = "FUNC"
    NORMAL = "NORMAL"
    TIMER = "TIMER"
    DTC = "DTC"



class Policy:
    def __init__(self):
        pass

    def generate_script_case_name(self, matrix:TSMatrix, test_obj):
        """
        返回脚本名字和case名字
        Args:
            matrix:
            test_obj:

        Returns:
            scriptsname, casename
        """
        # 如果case policy 为ObjectName,则表示脚本需要循环遍历
        if regCompare.is_equal(matrix.case_policy,"ObjectName"):
            pattern = "(?<=_)Object(?=_)"
            return re.sub(pattern,test_obj,matrix.case_name) + ".ts",re.sub(pattern,test_obj,matrix.case_name)
        #如果case policy 为Normal，则直接拿原来的名字
        elif regCompare.is_equal(matrix.case_policy,"Normal"):
            return matrix.case_name + ".ts", matrix.case_name
        else:
            raise Exception(f"have not hanlder case policy: {matrix.case_policy}")


    @func_monitor
    def generate_col_name_to_func_policy(self,col):
        """
        根据Col的名字，转化相关的策略，同时返回可能的函数缩写
        Args:
            col:

        Returns:
        func_policy:
        func:
        """
        pattern = r"FUNC_(.+)"
        m = re.match(pattern,col,re.I)
        if m:
            return "FUNC",m.group(1) #返回FUNC_后面的数据，
        else:
            # return "NORMAL", ""
            if re.match("DTC",col,re.I):
                return "DTC",""
            else:
                return "NORMAL",""



    def get_func_abbreviation(self,text):
        """
        从数据里面获取函数缩写字段
        Args:
            text:

        Returns:

        """
        pattern = r"(\w+)(?=\()"
        #  "th()" "Flt.Update('0x12')"
        result = re.search(pattern, text)
        if result:
            # print(result.group(1))
            return True, result.group()
        else:
            return False, ""








class ScriptEngine:
    def __init__(self,policy:Policy = Policy(),ts_matrix:TSMatrix = TSMatrix(),ts_step:TSStep = TSStep()):
        self.policy = policy
        self._matrix = ts_matrix
        self.ts_step = ts_step
        self.script_content = []


    @property
    def func_mapping(self):
        return self._func_mapping
    @func_mapping.setter
    def func_mapping(self,value:Dict):
        self._func_mapping = value
    @func_mapping.getter
    def func_mapping(self):
        return self._func_mapping


    @property
    def matrix(self):
        return self._matrix
    @matrix.setter
    def matrix(self,value:TSMatrix):
        self._matrix = value
    @matrix.getter
    def matrix(self):
        return self._matrix

    @property
    def ts_step_flag(self):
        return self._ts_step_flag
    @ts_step_flag.setter
    def ts_step_flag(self,value:TSStep_Flag):
        self._ts_step_flag = value
    @ts_step_flag.getter
    def ts_step_flag(self):
        return self._ts_step_flag

    def generate_args(self,case_name):
        value = self.matrix.case_args
        if self.matrix.case_args != "undefined":
            values = value.split("\n")
            scripts = [f"{i};\n" for i in values]
            scripts.insert(0,f"var CaseName = '{case_name}';\n")
        else:
            scripts =[f"var CaseName = {case_name};\n"]
        self.script_content.extend(scripts)

    @func_monitor
    def generate_step(self):
        if self.ts_step_flag.step:
            self.ts_step.step +=1
            self.ts_step.sub_step = 0
        else:
            self.ts_step.sub_step += 1
        step = f"{self.ts_step.tabs()}//{self.ts_step.step}.{self.ts_step.sub_step};\n"
        step += f"{self.ts_step.tabs()}//-----------------------------TEST STEP------------------------------//\n"
        self.script_content.append(step)
        return step

    @func_monitor
    def generate_comment(self,value):
        value = value.replace("\n", " ")
        if self.ts_step_flag.step:
            step_comment = f"{self.ts_step.tabs()}CommentStep(\"{value} \");\n"

        else:
            step_comment = f"{self.ts_step.tabs()}CommentSubStep(\"{value} \");\n"

        self.script_content.append(step_comment)
        return step_comment

    @func_monitor
    def generate_start_Log(self):
        if self.ts_step_flag.start_log:
            log_path = f"{self.ts_step.tabs()}var LogPath = LogFolder + " \
                       f"CaseName + \" _{self.ts_step.step}_{self.ts_step.sub_step}.log\";\n"
            log_action = f"{self.ts_step.tabs()}StartToLog(LogPath);\n\n"
            self.script_content.append(f"{log_path}{log_action}")
            return log_path + log_action
        else:
            return ""

    @func_monitor
    def generate_stop_Log(self):
        if self.ts_step_flag.stop_log:
            stoplog_action = f"\n\n{self.ts_step.tabs()}StopToLog();\n\n"
            self.script_content.append(stoplog_action)
            return stoplog_action
        else:
            return ""

    @func_monitor
    def generate_action_cell(self,value):
        scripts = []
        if value != "undefined":
            func_list = value.split("\n")  # 获取function list
            # 然后遍历函数列表
            for func in func_list:
                # 通过（ 去区分函数和参数
                abbreviation,fun_abbreviation = self.policy.get_func_abbreviation(func)
                if abbreviation: #如果抓到了函数缩写的可能行
                    if fun_abbreviation in self.func_mapping:#如果在缩写定义里面
                        pattern = r"(\w+)(?=\()"
                        script_line = self.ts_step.tabs() + re.sub(pattern, self.func_mapping[fun_abbreviation], func) + ";\n"
                    else:
                        script_line = f"{self.ts_step.tabs()}{func};\n"
                else:
                    script_line =  f"{self.ts_step.tabs()}{func};\n"
                scripts.append(script_line)
        else:
            pass
        self.script_content.extend(scripts)
        return "".join(scripts)

    @func_monitor
    def generate_func_cell(self,func,value):
        scripts = []
        if value != "undefined":
            values = value.strip().split("\n")
            if True:  # 如果抓到了函数缩写的可能行
                if func in self.func_mapping:  # 如果在缩写定义里面
                    scripts =[ self.ts_step.tabs() + \
                                  Template("${" + func + "}").safe_substitute(self.func_mapping)\
                                  + f"({value1});\n" for value1 in values]
                else:
                    scripts = [f"{self.ts_step.tabs()}{func}({value1});\n " for value1 in values ]
            else:
                scripts = [f"{self.ts_step.tabs()}{func}({value1});\n" for value1 in values]
            # if True:  # 如果抓到了函数缩写的可能行
            #     if func in self.func_mapping:  # 如果在缩写定义里面
            #         script_line = self.ts_step.tabs() + \
            #                       Template("${" + func + "}").safe_substitute(self.func_mapping)\
            #                       + f"({value});\n"
            #     else:
            #         script_line = f"{self.ts_step.tabs()}{func}({value});\n "
            # else:
            #     script_line = f"{self.ts_step.tabs()}{func}({value});\n"
            # scripts.append(script_line)
        else:
            pass
        self.script_content.extend(scripts)
        return "".join(scripts)


    @func_monitor
    def generate_dtc_cell(self,value):
        scripts = []
        if re.match("^NONE$", value, re.I):
            scripts.append(f"\n{self.ts_step.tabs()}Thread.Sleep(8000);\n{self.ts_step.tabs()}var Ret = ActualResults();")
            scripts.append(f"\n{self.ts_step.tabs()}var Expect_WL = BB_Update_Flts_External_Symbol(\'NONE\').WL;")
            scripts.append(f"\n{self.ts_step.tabs()}BB_CompareResultsDefine(Ret,Expect_WL,\'NONE\')\n")
        else:
            if regCompare.is_equal("DTC",value):
                scripts.append(
                    f"\n{self.ts_step.tabs()}var Ret = ActualResults();")
                scripts.append(f"\n{self.ts_step.tabs()}var Expect_WL = BB_Update_Flts_External_Symbol(Flt_Array).WL;")
                scripts.append(
                    f"\n{self.ts_step.tabs()}BB_CompareResultsDefine(Ret,Expect_WL,Flt_Array);\n")
            else:#先调用里面的函数，然后再调用其他代码
                self.generate_action_cell(value)
                scripts.append(
                    f"\n{self.ts_step.tabs()}var Ret = ActualResults();")
                scripts.append(f"\n{self.ts_step.tabs()}var Expect_WL = BB_Update_Flts_External_Symbol(Flt_Array).WL;")
                scripts.append(
                    f"\n{self.ts_step.tabs()}BB_CompareResultsDefine(Ret,Expect_WL,Flt_Array);\n")

        self.script_content.extend(scripts)
        return "".join(scripts)

    @func_monitor
    def generate_actions_results(self,actions_results:List,df:pd.DataFrame,index:pd.Index):

        for action_result in actions_results:
            Monitor_Logger.info(f"generate_actions_results at col:{action_result} index:{index + 2} ")
            df.loc[index, action_result]
            if df.loc[index,action_result] == "undefined":
                continue
            func_policy,func_name = self.policy.generate_col_name_to_func_policy(action_result)

            if regCompare.is_equal(func_policy,Func_Policy.FUNC):
                self.generate_func_cell(func_name,df.loc[index,action_result])
            if regCompare.is_equal(func_policy, Func_Policy.NORMAL):
                self.generate_action_cell(df.loc[index,action_result])
            if regCompare.is_equal(func_policy, Func_Policy.DTC):
                self.generate_dtc_cell(df.loc[index,action_result])


    def generate_scripts(self,outputDir):
        actions = self.matrix.case_col_config.action_list
        results = self.matrix.case_col_config.result_list

        #如果case是正常的case，不用循环处理数据，且这个矩阵图是支持的
        if regCompare.is_equal(self.matrix.case_type,"Normal") and self.matrix.ts_matrix_support :
            self.ts_step = TSStep()
            self.ts_step_flag = TSStep_Flag()
            # 获取脚本名字和case名字
            script_name, case_name = self.policy.generate_script_case_name(self.matrix, "")
            Monitor_Logger.info(f"generate scripts{script_name}")
            self.script_content = []
            #生成脚本开头的字段
            self.script_content.append(
                SCRIPT_HEADER_1  + "\n" + SCRIPT_HEADER_2  + SCRIPT_HEADER_3)
            # 生成参数定义部分和脚本开始部分
            self.generate_args(case_name)
            self.script_content.append(TEST_BEGIN)

            #然后循环遍历处理测试用例的矩阵图
            df = self.matrix.df_matrix
            for index in df.index:
                #首先获取每行测试的步骤flag，是否开启截取log,停止截取log，Step还是SubStep,以及步骤的flag
                self.ts_step_flag = TSStep_Flag( regCompare.is_equal(df.loc[index,"LogStart"], "START"),
                                                 regCompare.is_equal(df.loc[index, "LogStop"], "STOP"),
                                                regCompare.is_equal(df.loc[index, "Step"], "ST"),
                                                             df.loc[index, "Steps_Flag"]
                          )
                support = df.loc[index,"Support"]
                if regCompare.is_equal(support,"No"):
                    continue # 如果改步骤不支持，则跳过继续
                #打印Comment
                self.script_content.append("\n" * 2)
                self.generate_step()
                self.generate_start_Log()
                self.generate_comment(df.loc[index,"Comment"])
                self.generate_actions_results(actions,df,index)
                self.generate_actions_results(results, df, index)
                self.generate_stop_Log()
            self.script_content.append(TEST_END)
            fileUtil.generate_script("".join(self.script_content), outputDir, script_name)





if __name__ == "__main__":
    # excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\Errorandler\CHT_SWV_SAIC_ZP22_ErrorHandler_Test Specification.xlsm"
    # # config = r"C:\Users\victor.yang\Desktop\Work\DCS_Config.xlsx"
    # # sheet = "DTCStatus2"
    # # sheet = "UnderVoltage_Suspend"
    # # sheet = "Suspend_Strategy_2"
    # # sheet = "DemBuffer_Value2"
    # # sheet = "OverVoltage_Suspend"
    # # sheet = "En12VoltStrMotCmddOn_Suspend"
    # # sheet = "EPTStCmdOn_Suspend"
    # # sheet = "ECUPowerMode_Suspend"
    # # sheet = "Suspend_Strategy"
    # sheets = ["DTCStatus","Suspend_Strategy","OverVoltage_Suspend","UnderVoltage_Suspend","En12VoltStrMotCmddOn_Suspend","EPTStCmdOn_Suspend",
    #           "ECUPowerMode_Suspend","ExtendedData","DemBuffer_RecordLogic","DemBuffer_Value2","DemBuffer_Value"]
    # sheets = ["DemBuffer_RecordLogic"]
    # outdir = r"C:\Users\victor.yang\Desktop\Work\Scripts\Temp"
    excel = r"C:\Users\victor.yang\Desktop\Work\G08\CHT_SWV_HYCAN_G08_ErrorHandler_Test Specification_Linb.xlsm"
    sheet = "Snapshot_ExtendedData"
    outdir = r"C:\Users\victor.yang\Desktop\Work\G08"
    sheets = ["DTCStatus","OverVoltage_Suspend","UnderVoltage_Suspend","ExtendedData",
         "DemBuffer_RecordLogic","DemBuffer_Value2","DemBuffer_Value"]
    scritp_enginer = ScriptEngine()
    func_mapping = Func_Mapping(excel, "Function_Mapping")
    scritp_enginer.func_mapping = func_mapping.get_func_mapping()

    for sheet in sheets:
        spec_sheet = SpecSheet(excel, sheet)
        spec_sheet.update_matrixs()
        for matrix in spec_sheet.matrixs:
            scritp_enginer.matrix = matrix
            scritp_enginer.generate_scripts(outdir)
