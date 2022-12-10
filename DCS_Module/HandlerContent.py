import re
from string import Template

def return_start_Log(deepth,step,test_object,flag):
    log_path = "\t" * deepth + "var LogPath = LogFolder + \"" + test_object \
           + "_" + flag + str(step) + ".log\"" + ";\n"
    log_action = "\t" * deepth + "StartToLog(StorePath)" + ";\n\n"
    return log_path + log_action

def return_stop_log(deepth):

    stoplog_action = "\n\n" + "\t"*deepth  + "StopToLog()" + ";\n"
    return stoplog_action

def return_step(deepth,step,substep):
    step = "\t" * deepth + "//" + str(step) + "." + str(substep)  + ";\n"
    step += "\t" * deepth + "//-----------------------------TEST STEP------------------------------//\n"
    return step

def return_step_comment(deepth,comment):

    step_comment = "\t"*deepth + "CommentStep(\"" + comment + "\")" + ";\n"
    return step_comment




def check_func_flag(a):
    #判断函数里面是否有参数
    b = a.split("(")
    if re.search("\(",a):
        return "(" + b[1] +";\n"
    else:
        return "();\n"



def return_pre_post_action(deepth,p_condition,func_dict):
    pre_post_action =""
    if p_condition != "undefined":

        p_condition_funclist = p_condition.split("->") # 获取function list
        # 然后遍历函数列表
        for func in p_condition_funclist:
            # print(func.split("("))
            # 通过（ 去区分函数和参数
            temp = "\t" * deepth + Template("${" + func.split("(")[0] + "}").safe_substitute(
                func_dict) + check_func_flag(func)
            pre_post_action += temp
    else:
        pre_post_action = ""
    return pre_post_action


def return_set_action(deepth,col_name,test_object,condition):
    func_name = "BB_" + col_name
    # print(func_name)
    set_action = "\t" * deepth + func_name + "(\"" + test_object + "\",\"" + condition + "\");\n"
    return set_action

def return_check_action(deepth,col_name,test_object,expect_result):
    func_name = "BB_Check_" + col_name
    check_action = "\t" * deepth + func_name + "(\"" + test_object + "\",\"" + expect_result + "\");\n"
    return check_action

def handle_action(action_list,df_temp,indx,deepth,test_object,Func_Dict):
    script = []
    for action in action_list:

        if df_temp.loc[indx, action] == "undefined":
            continue
        elif re.search("Set", action, re.I):  # 如果匹配到set 类函数
            condition = df_temp.loc[indx, action]
            script.append(return_set_action(deepth, action, test_object, condition))
        else:
            pre_post_condition = df_temp.loc[indx, action]
            script.append(return_pre_post_action(deepth, pre_post_condition, Func_Dict))
    return script

def return_check_switchtime(deepth,test_object,expect_status_list,expect_timer_range):
    func_name = "BB_Check_DCS_SwitchTime"
    check_action = "\t" * deepth + func_name + "(\"" + test_object + "\"," + str(expect_status_list) + "," + str(expect_timer_range) + ");\n"
    return check_action

def return_compareresultdefine(deepth, fault_info):
    compare_fault_action = []
    compare_fault_action.append("\n" + "\t"*deepth + "var Ret = ActualResults();\n")
    if re.search("NONE", fault_info, re.I):
        temp_list = fault_info.split(",")
        compare_fault_action.append("\t" * deepth + "CompareResultsDefine(Ret,\"" + ",".join(temp_list[1:]) + "\",\"" + temp_list[0] + "\");\n")
    elif re.search("DTC", fault_info, re.I): #表示有dtc
        temp_list = fault_info.split(",")
        compare_fault_action.append(
            "\t" * deepth + "var FaultInfo_Arr = GetFaultInfo_Arr(TestObject_Str,Fault,\""  +  ",".join(temp_list[1:]) +  "\",G_DCSCrossC_SelectObj))\n")
        compare_fault_action.append(
            "\t" * deepth + "var FaultInfo_Return = SetSuffixToFaultInfoSystem(FaultInfo_Arr.toString())\n")
        compare_fault_action.append(
            "\t" * deepth + "CompareResultsDefine(Ret,FaultInfo_Return[1],FaultInfo_Return[0])\n")
    return compare_fault_action

def handle_default_check(expect_dcs_data_list,df_temp,indx,deepth):
    expect_status_list = []
    for expect_behavior in expect_dcs_data_list:
        if df_temp.loc[indx, expect_behavior] == "undefined":
            continue
        else:
            expect_result = df_temp.loc[indx, expect_behavior]
            expect_status_list.append(expect_result)
    default_check = "\t" * deepth + "BB_Check_DCS_DefaultValue(Sensor," + str(expect_status_list) + ");\n"
    return default_check

def return_fault_timer(deepth,status):
    fault_timer = []
    fault_timer.append("\t" * deepth +"var DiagTime = int(Sensor_Obj[Fault + \"" +status + "\"][0]) *1.5;\n")
    fault_timer.append("\t" * deepth +"var HighRange = int(Sensor_Obj[Fault + \"" +status + "\"][0]) *1.5;\n")
    fault_timer.append("\t" * deepth +"var LowRange = int(Sensor_Obj[Fault + \"" +status + "\"][0]) *1.5;\n")
    return fault_timer

# def return_fault_check_timer(deepth,step_flag):
#     if step_flag == "Qualify":
#         fault_timer_check ="\t" * deepth +  "CheckDTCQualifyOrDisQualifyTime(StorePath[Fault][0],Sensor_Obj[Fault\+\"DTC\"] \+ \"-ACTIVE\",LowRange,HighRange);\n"
#     else:
#         fault_timer_check = "\t" * deepth + "CheckDTCQualifyOrDisQualifyTime(StorePath[Fault][0],Sensor_Obj[Fault\+\"DTC\"] \+ \"-HISTORIC\",LowRange,HighRange);\n"
#     return fault_timer_check

def handle_expect_result(expect_behavior_list,df_temp,indx,deepth,test_object,Func_Dict):
    scripts = []
    expect_status_list = []
    expect_timer_range = []
    step_flag = df_temp.loc[indx,"Steps_Flag"]
    for expect_behavior in expect_behavior_list:
        if df_temp.loc[indx, expect_behavior] == "undefined":
            continue
        elif re.search("Timer", expect_behavior, re.I):  # 如果匹配到Timer 类函数:
            expect_timer_range = df_temp.loc[indx, "Timer"].split("-")

            if step_flag == "SwitchTimer":
               timer_check_action =  return_check_switchtime(deepth,test_object,expect_status_list,expect_timer_range)
               scripts.append(timer_check_action)
            if step_flag == "InitTimer":
                timer_check_action = return_check_switchtime(deepth, test_object, expect_status_list,
                                                             expect_timer_range)
                scripts.append(timer_check_action)
            if step_flag == "Qualify":
                timer_check_action = "\t" * deepth + "CheckDTCQualifyOrDisQualifyTime(LogPath,Sensor_Obj[Fault+\"DTC\"] + \"-ACTIVE\",LowRange,HighRange);\n"
                scripts.append(timer_check_action)
            if step_flag == "Disqualify":
                timer_check_action = "\t" * deepth + "CheckDTCQualifyOrDisQualifyTime(LogPath,Sensor_Obj[Fault+\"DTC\"] + \"-HISTORIC\",LowRange,HighRange);\n"
                scripts.append(timer_check_action)

        elif re.search("DTC", expect_behavior, re.I):  # 如果匹配到预期结果为dtc
            fault_info = df_temp.loc[indx, expect_behavior]
            compare_fault_action =  return_compareresultdefine(deepth, fault_info)
            scripts.extend(compare_fault_action)
        elif re.search("DTC", expect_behavior, re.I):  # 如果匹配到预期结果为DID
            pass
        else:

            expect_result = df_temp.loc[indx, expect_behavior]
            # print(expect_result)
            if re.search("Status", expect_behavior, re.I):
                expect_status_list.append(expect_result)
            scripts.append(return_check_action(deepth, expect_behavior, test_object, expect_result))
    return scripts