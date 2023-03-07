import re

import pandas as pd

from ImportModule import *
from Read_Excel_Config import *
from TestCaseHeader import *


@dataclass
class TSStep_Flag:
    start_log:bool=True
    stop_log:bool = True
    step:bool = True
    flag:str = None

@dataclass
class TSStep:
    step:int = 1
    sub_step:int = 0
    deepth:int = 1

    def tabs(self):
        return "\t"*self.deepth

class Func_Policy:
    FUNC = "FUNC"
    NORMAL = "NORMAL"
    TIMER = "TIMER"
    DTC = "DTC"



class Policy:
    def __init__(self):
        pass

    def generate_script_name(self,matrix:TSMatrix,sensor):
        if matrix.case_policy == "SensorName":
            pattern = "(?<=_)Sensor(?=_)"
            return re.sub(pattern,sensor,matrix.case_name) + ".ts"

    def generate_step_flag(self,step_flag):
        templist = step_flag.split("_")
        if len(templist) < 4:
            raise Exception("Step Flag not correct,shall be (StartLog)_(StopLog)_(Step)__(Flag)")
        step_flag = TSStep_Flag(templist[0] == "STLog",
                              templist[1] == "STPLog",
                              templist[2] == "ST",
                              templist[3]
                              )
        return step_flag
    @func_monitor
    def generate_col_name_to_func_policy(self,col):
        """
        Args:
            col:

        Returns:
        func_policy:
        func:
        """
        pattern = r"FUNC_(.+)"
        m = re.match(pattern,col,re.I)
        if m:
            return "FUNC",m.group(1)
        else:
            if re.match("TIMER",col,re.I):
                return "TIMER",""
            elif re.match("DTC",col,re.I):
                return "DTC",""
            else:
                return "NORMAL",""

    def convert_args_value(self,value):
        args = value.split(",")
        for indx,arg in enumerate(args):

            if re.match("^\d+$",arg):
                pass
                # args[indx] = int(arg) #如果是数字字符串 不处理
            elif re.match("^SENSOR。*?",arg,re.I): #如果改参数的对象名称为Sensor,则也不处理
                pass
            elif re.search("\.",arg,re.I):  # 如果是带.号
                pass
            elif re.match("^LogPath$", arg, re.I):  # 如果改参数的对象名称为Sensor,则也不处理
                pass
            else:
                args[indx] = "\"" + arg + "\""
        return ",".join(args)

    def get_args_from_func_call(self,text):
        pattern = r"\((.*?)\)"
        result = re.search(pattern, text)
        if result:
            # print(result.group(1))
            return True, self.convert_args_value(result.group(1))
        else:
            # print("TT")
            return False, ""



    def add_func_call_suffix(self,func_call):
        args_flag,args =  self.get_args_from_func_call(func_call)
        if args_flag:
            return "(" + args + ");\n"
        else:
            return "();\n"




class ScriptEngine:
    def __init__(self,policy:Policy = Policy(),ts_matrix:TSMatrix = TSMatrix(),ts_step:TSStep = TSStep(),script_content = []):
        self.policy = policy
        self.matrix = ts_matrix
        self.ts_step = ts_step
        self.script_content = script_content


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
    def ts_step_flag(self):
        return self._ts_step_flag

    @ts_step_flag.setter
    def ts_step_flag(self,value:TSStep_Flag):
        self._ts_step_flag = value

    @ts_step_flag.getter
    def ts_step_flag(self):
        return self._ts_step_flag


    # @property
    # def script_content(self):
    #     return self.script_content
    #
    # @script_content.setter
    # def script_content(self,value:TSStep_Flag):
    #     self.script_content = value
    #
    # @script_content.getter
    # def script_content(self):
    #     return self.script_content


    @func_monitor
    def generate_step(self):
        step = f"{self.ts_step.tabs()}//{self.ts_step.step}.{self.ts_step.sub_step};\n"
        step += f"{self.ts_step.tabs()}//-----------------------------TEST STEP------------------------------//\n"
        if self.ts_step_flag.step:
            self.ts_step.step +=1
            self.ts_step.sub_step = 0
        else:
            self.ts_step.sub_step += 1
        self.script_content.append(step)
        return step

    @func_monitor
    def generate_comment(self,value):
        if self.ts_step_flag.step:
            step_comment = f"{self.ts_step.tabs()}CommentStep(\"{value} \");\n"

        else:
            step_comment = f"{self.ts_step.tabs()}CommentSubStep(\"{value} \");\n"

        self.script_content.append(step_comment)
        return step_comment

    @func_monitor
    def generate_start_Log(self,script_name):
        if self.ts_step_flag.start_log:
            log_path = f"{self.ts_step.tabs()}var LogPath = LogFolder + \"" \
                       f"_{script_name}_{self.ts_step.step}_{self.ts_step.sub_step}.log\";\n"
            log_action = f"{self.ts_step.tabs()}StartToLog(LogPath);\n\n"
            self.script_content.append(f"{log_path}{log_action}")
            return log_path + log_action
        else:
            return ""

    @func_monitor
    def generate_stop_Log(self):
        if self.ts_step_flag.stop_log:
            stoplog_action = f"\n\n{self.ts_step.tabs()}StopLog();\n\n"
            self.script_content.append(stoplog_action)
            return stoplog_action
        else:
            return ""

    @func_monitor
    def generate_action_cell(self,value):
        scripts = []
        if value != "undefined":
            func_list = value.split("->")  # 获取function list
            # 然后遍历函数列表
            for func in func_list:
                # 通过（ 去区分函数和参数
                script_line = self.ts_step.tabs() + Template("${" + func.split("(")[0] + "}").safe_substitute(
                    self.func_mapping) + self.policy.add_func_call_suffix(func)
                scripts.append(script_line)
        else:
            pass
        self.script_content.extend(scripts)
        return "".join(scripts)

    @func_monitor
    def generate_func_cell(self,func,value):
        scripts = []
        if value != "undefined":
            # Monitor_Logger.info(f"{func} {self.func_mapping}")
            # script_line = Template("${" + func +"}").safe_substitute(self.func_mapping)
            script_line = self.ts_step.tabs() + Template("${" + func +"}").safe_substitute(
                    self.func_mapping)  + "(Sensor," + self.policy.convert_args_value(value)  + ");\n"
            scripts.append(script_line)
        else:
            pass
        self.script_content.extend(scripts)
        return "".join(scripts)

    @func_monitor
    def generate_fault_timer_cell(self):
        # SwitchTimer InitTimer,Qualify,Disqualify
        if re.match("^QualifyTimer$",self.ts_step_flag.flag,re.I):
            timer_check_action =f"{self.ts_step.tabs() }CheckDTCQualifyOrDisQualifyTime(LogPath,Sensor[Fault+\"DTC\"] + \"-ACTIVE\",LowRange,HighRange);\n"
            # return timer_check_action
        elif re.match("^DisqualifyTimer$",self.ts_step_flag.flag,re.I):
            timer_check_action = f"{self.ts_step.tabs()}CheckDTCQualifyOrDisQualifyTime(LogPath,Sensor[Fault+\"DTC\"] + \"-HISTORIC\",LowRange,HighRange);\n"
            # return timer_check_action
        else:
            timer_check_action = ""
        self.script_content.extend(timer_check_action)
        return timer_check_action

    @func_monitor
    def generate_dtc_cell(self,value):
        scripts = []
        if re.match("^NONE$", value, re.I):
            scripts.append(f"\n{self.ts_step.tabs()}var Ret = ActualResults();\n{self.ts_step.tabs()}Thread.Sleep(8000);")
            scripts.append(f"\n{self.ts_step.tabs()}var Expect_Fault_Info = SetSuffixToFaultInfo(\"NONE\");")
            scripts.append(f"\n{self.ts_step.tabs()}CompareResultsDefine(Ret,Expect_Fault_Info[1],Expect_Fault_Info[0])")
        else:
            if regCompare.is_equal("DTC",value):
                scripts.append(
                    f"\n{self.ts_step.tabs()}var Ret = ActualResults();")
                scripts.append(f"\n{self.ts_step.tabs()}var FaultInfo_Array = BB_Get_FaultInfo_Array(SensorFaults);")
                scripts.append(f"\n{self.ts_step.tabs()}var Expect_Fault_Info = SetSuffixToFaultInfo(FaultInfo_Array.toString()) ;")
                scripts.append(
                    f"\n{self.ts_step.tabs()}CompareResultsDefine(Ret,Expect_Fault_Info[1],Expect_Fault_Info[0])")
            else:#先调用里面的函数，然后再调用其他代码
                self.generate_action_cell(value)
                scripts.append(
                    f"\n{self.ts_step.tabs()}var Ret = ActualResults();")
                scripts.append(
                    f"\n{self.ts_step.tabs()}var FaultInfo_Array = BB_Get_FaultInfo_Array(SensorFaults);")
                scripts.append(
                    f"\n{self.ts_step.tabs()}var Expect_Fault_Info = SetSuffixToFaultInfo(FaultInfo_Array.toString()) ;")
                scripts.append(
                    f"\n{self.ts_step.tabs()}CompareResultsDefine(Ret,Expect_Fault_Info[1],Expect_Fault_Info[0])")

        self.script_content.extend(scripts)
        return "".join(scripts)

    @func_monitor
    def generate_fault_timer_deinition(self):
        if re.match("^Fault$", self.matrix.case_type) and (regCompare.is_equal(self.ts_step_flag.flag, "Qualify") or regCompare.is_equal(self.ts_step_flag.flag, "DisQualify")):
            fault_timer = []
            fault_timer.append(f"{self.ts_step.tabs()}var DiagTime = int(Sensor[Fault + \"{self.ts_step_flag.flag}\"][0]) *1.5;\n")
            fault_timer.append(f"{self.ts_step.tabs()}var HighRange = int(Sensor[Fault + \"{self.ts_step_flag.flag}\"][0]) *1.5;\n")
            fault_timer.append(f"{self.ts_step.tabs()}var LowRange = int(Sensor[Fault + \"{self.ts_step_flag.flag}\"][0]) *1.5;\n")
            self.script_content.extend(fault_timer)
            return "".join(fault_timer)
        else:
            return ""

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
            if regCompare.is_equal(func_policy, Func_Policy.TIMER):
                if re.match("^Fault$", self.matrix.case_type): # 如果测试类型是Fault的话，则Timer为检查Qualify和disqualify
                    self.generate_fault_timer_cell()
                else:   #否则用函数方式去检查
                    self.generate_action_cell(df.loc[index, action_result])
            if regCompare.is_equal(func_policy, Func_Policy.NORMAL):
                self.generate_action_cell(df.loc[index,action_result])
            if regCompare.is_equal(func_policy, Func_Policy.DTC):
                self.generate_dtc_cell(df.loc[index,action_result])


    def generate_scripts(self,outputDir):
        actions = self.matrix.case_col_config.action_list
        results = self.matrix.case_col_config.result_list

        if regCompare.is_equal(self.matrix.case_type,"Normal") or regCompare.is_equal(self.matrix.case_type,"Fault"):
            for sensor in self.matrix.sensor_list:
                self.ts_step = TSStep()
                self.ts_step_flag = TSStep_Flag()
                variables_define = f"var Sensor = {sensor};\nvar SensorFaults = new Array()"
                self.script_content = []
                self.script_content.append(
                    SCRIPT_HEADER_1  + "\n" + SCRIPT_HEADER_2 + variables_define + SCRIPT_HEADER_3 + TEST_BEGIN)

                if regCompare.is_equal(self.matrix.case_type, "Fault"): #如果测试类型是Fault
                    self.script_content.append(FAULT_LOOP_START)
                    self.ts_step.deepth = 3

                script_name = self.policy.generate_script_name(self.matrix, sensor)
                Monitor_Logger.info(f"generate scripts{script_name}")
                df = self.matrix.df_matrix
                for index in df.index:
                    self.ts_step_flag = self.policy.generate_step_flag(df.loc[index,"Steps_Flag"])
                    support = df.loc[index,"Support"]
                    if regCompare.is_equal(support,"No"):
                        continue # 如果改步骤不支持，则跳过继续
                    self.script_content.append("\n" * 2)
                    self.generate_start_Log(script_name)

                    self.generate_fault_timer_deinition()
                    self.generate_step()
                    self.generate_comment(df.loc[index,"Comment"])
                    self.generate_actions_results(actions,df,index)
                    self.generate_actions_results(results, df, index)
                    self.generate_stop_Log()

                if regCompare.is_equal(self.matrix.case_type, "Fault"):  # 如果测试类型是Fault
                    self.script_content.append(FAULT_LOOP_END)
                self.script_content.append(TEST_END)
                fileUtil.generate_script("".join(self.script_content), outputDir, script_name)





if __name__ == "__main__":
    excel = r"C:\Users\victor.yang\Desktop\Work\CHT_SWV_SAIC_ZP22_DCS_Test Specification.xlsm"
    sheet = "DCS_Fault"
    testSpec = TestSpec(excel, sheet)
    testSpec.update_matrixs()
    scritp_enginer = ScriptEngine(ts_matrix=testSpec.matrixs[0])
    func_mapping =  Func_Mapping(excel,"Function_Mapping")
    scritp_enginer.func_mapping = func_mapping.get_func_mapping()
    # scritp_enginer.generate_func_cell("Set","HighRange")
    scritp_enginer.generate_scripts(r"C:\Users\victor.yang\Desktop\Work")