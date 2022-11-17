import pandas as pd
import numpy as np
import re
from string import Template
from DCS_Module import HandlerContent as HC



script_header_1 = """
// ******************************************************************************************
// **************************Veoneer Electronics document************************************
// ******************************************************************************************
// Result Test: 
// *******************************************************
               // Script Information
// *******************************************************
// Test case ID:"""

script_header_2 = """
// *******************************************************
// Full Automation: Yes
// *******************************************************

// *******************************************************
               // External Function
// *******************************************************
CALL(BB_DCS_Common_Define.ts);
// *******************************************************
               // Test Information
// *******************************************************
CommonInformation();

// *******************************************************
               // Test Log Variables Path Define
// *******************************************************
"""

script_header_3 ="""
// *******************************************************
               // Define/Re-Define parameters
// *******************************************************

// *******************************************************
               // Test Steps
// *******************************************************
"""
test_begin = "if(CheckTestEnvironment())\n{\n"

test_end = """
}
else 	
{
	RESULT.InterpretEqualResult("Check Test Bench condition: ",["0000","Not Normal"],"Normal");
}

// *******************************************************
                   // Re-Initialize
// *******************************************************
ReInitialize();

// *******************************************************
                   // Extract Result
// *******************************************************
var tst : TestStatus  = ExtractTestStatus(RESULT.ResultName);
RESULT.TestVerdict(tst);
"""

fault_loop_start = """
    for(var Fault in GBB_DCS_Fault)
    {
      
       
        RESULT.InsertComment("###########################################################################################################################")
        RESULT.InsertComment("Test the " + Fault + "  Fault of " + Sensor )
        G_StepNumber = 0
        RESULT.InsertComment("###########################################################################################################################")
        if(Sensor_Obj[Fault] != undefined && Sensor_Obj[Fault] != "undefined" && Fault != "CFG")
        {
"""

fault_loop_end = """
        }

    }
"""

Func_Dict = {
"PwOff":"PowerOff",
"PwOn":"PowerOn",
"TSlp":"Thread.Sleep",
"NmBSlp":"BussSleep",
"NmWkUp":"NmWakeUp",
"Periodic":"SendRequestPeriodic",
"Periodic19":"SendRequestPeriodic19",
"ClearDTC":"ClearDTC"

}

G_BBSD_DCS4 = {
    "ARiA_HW_Name": "SW_Channel_DCS_4",
    "FaultIndex": "3",
    "Normal": "100R",
    "Buckled": "OPEN",
    "UnBuckled": "100R",
    "CrossC": "undefined",
    "STB": "Yes",
    "GND": "undefined",
    "Open": "undefined",
    "TooHigh": "undefined",
    "TooLow": "undefined",
    "BadSensor": "undefined",
    "CFG": "Yes",
    "CurrentDID": "5B2F",
    "StatusDID": "5823",
    "CAN_StatusMsg": "SrsPassSafeCANFr01",
    "CAN_StatusSignal": "BltLockStAtDrvrBltLockSt1",
    "StatusMsg": "SrsBackBoneFr05",
    "StatusSignal": "BltLockStSafeAtDrvrBltLockSt1",
    "CAN_QFMsg": "SrsPassSafeCANFr01",
    "CAN_QFSignal": "BltLockStAtDrvrBltLockSts",
    "QFMsg": "SrsBackBoneFr05",
    "QFSignal": "BltLockStSafeAtDrvrBltLockStErrSts",
    "EquipMsg": "undefined",
    "EquipSignal": "undefined",
    "CrossCDTC": "undefined",
    "STBDTC": "805012",
    "GNDDTC": "undefined",
    "TooHighDTC": "undefined",
    "TooLowDTC": "undefined",
    "BadSensorDTC": "undefined",
    "OpenDTC": "undefined",
    "CFGDTC": "805064",
    "Status": [
        "Buckled",
        "UnBuckled"
    ]
}

def Check_Func_Flag(a):
    b = a.split("(")
    if re.search("\(",a):
        return "(" + b[1] +";\n"
    else:
        return "();\n"

def GetDCSModule(ExcelDir, ObjectType,Ts):
    # pd.set_option('display.max_columns', None)
    pd.set_option('max_colwidth', 8000)
    df = pd.read_excel(ExcelDir, ObjectType, dtype=str)
    # print(df)
    case_start = 0;
    case_end = 0
    df_case_list =[]
    for indx in df.index:
        if df.loc[indx,"CaseIndex"] == "CaseStart":

            if case_start != 0:
                pass # 如果再找到caseStart的时候已经被赋值了，说明配置有问题，需要报错
            case_start = indx
        elif df.loc[indx,"CaseIndex"] == "CaseEnd":
            case_end = indx
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
    # print(df_case_list.__len__())
    df_temp = df_case_list[0] # 后期循环处理数据

    # 后期获取caseID
    case_id = "1234567"
    # print(df_temp.columns)
    df_temp = df_temp.iloc[1:] # 从PreCondition 行开始计算
    # print(df_temp)
    # 先提出从PreCondition 单元格没内容的
    df_temp.columns = df_temp.iloc[1]
    df_temp = df_temp.loc[:,"Comment":"DTC"]  # 后期通过方式定位开始和截止位置
    df_temp = df_temp.iloc[2:]
    df_temp.fillna("undefined",inplace = True)
    print(df_temp)

    # 开始写入脚本

    action_list = ["PreCondition","Set_DCSCondition","PostCondition"]
    expect_behavior_list = ["Status_Signal", "QF_Signal", "Equib_Signal", "CustomerDID_Status", "InternalDID_Status",
                         "InternalDID_QF", "Timer", "DTC"]
    expect_dcs_data_list = ["Status_Signal", "QF_Signal", "Equib_Signal", "CustomerDID_Status", "InternalDID_Status",
                         "InternalDID_QF"]
    test_object = "G_BBSD_DCS4"
    script_content = []
    variables_define = "var Sensor = \"" + test_object + "\";\n"
    variables_define += "var Sensor_Obj = " + test_object + ";\n"
    script_content.append(script_header_1 + case_id +"\n" + script_header_2 + variables_define +  script_header_3 + test_begin)

    # print(df_temp["PostCondition"])
    step = 0 # 用来定义步骤
    substep = 0
    deepth = 1 # 用来定义下面步骤换行的倍数
    for indx in df_temp.index:
        steps_flag = df_temp.loc[indx,"Steps_Flag"]
        support_flag = df_temp.loc[indx,"Support"]
        if support_flag == "No": # 如果改步骤不支持，则跳过
            continue
        # 否则便利col

        if steps_flag == "PreStep":
            step += 1
            substep = 0
            deepth = 1
            script_content.append("\n" * 2)
            # 后期要用某种方式来处理列名的行为
            script_content.append(HC.return_start_Log(deepth,step,test_object,steps_flag))
            script_content.append(HC.return_step(deepth, step, substep))
            step_comment = df_temp.loc[indx, "Comment"]
            script_content.append(HC.return_step_comment(deepth, step_comment))

            script_temp = HC.handle_action(action_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
            script_temp = HC.handle_expect_result(expect_behavior_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)

            script_content.append(HC.return_stop_log(deepth))

        elif steps_flag == "SwitchTimer":
            step += 1
            substep = 0
            deepth = 1
            script_content.append("\n" * 2)
            script_content.append(HC.return_start_Log(deepth, step, test_object, steps_flag))
            script_content.append(HC.return_step(deepth, step, substep))
            step_comment = df_temp.loc[indx, "Comment"]
            script_content.append(HC.return_step_comment(deepth, step_comment))

            script_temp = HC.handle_action(action_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
            script_temp = HC.handle_expect_result(expect_behavior_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)

            script_content.append(HC.return_stop_log(deepth))

        elif steps_flag == "InitTimer":
            step += 1
            substep = 0
            deepth = 1
            script_content.append("\n" * 2)
            script_content.append(HC.return_start_Log(deepth, step, test_object, steps_flag))
            script_content.append(HC.return_step(deepth, step, substep))
            step_comment = df_temp.loc[indx, "Comment"]
            script_content.append(HC.return_step_comment(deepth, step_comment))

            script_temp = HC.handle_action(action_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
            script_temp = HC.handle_expect_result(expect_behavior_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)

            script_content.append(HC.return_stop_log(deepth))

        elif steps_flag == "Default":

            substep += 1
            deepth = 1

            script_content.append(HC.return_step(deepth, step, substep))
            step_comment = df_temp.loc[indx, "Comment"]
            script_content.append(HC.return_step_comment(deepth, step_comment))

            script_content.append(HC.handle_default_check(expect_dcs_data_list,df_temp,indx,deepth))




    script_content.append(test_end)
    with open(Ts, 'w', encoding='UTF-8') as f:
        f.writelines(script_content)
        f.write("\n")



def GetDCSModule_Fault(ExcelDir, ObjectType,Ts):
    # pd.set_option('display.max_columns', None)
    pd.set_option('max_colwidth', 8000)
    df = pd.read_excel(ExcelDir, ObjectType, dtype=str)
    # print(df)
    case_start = 0;
    case_end = 0
    df_case_list =[]
    for indx in df.index:
        if df.loc[indx,"CaseIndex"] == "CaseStart":

            if case_start != 0:
                pass # 如果再找到caseStart的时候已经被赋值了，说明配置有问题，需要报错
            case_start = indx
        elif df.loc[indx,"CaseIndex"] == "CaseEnd":
            case_end = indx
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
    # print(df_case_list.__len__())
    df_temp = df_case_list[0] # 后期循环处理数据

    # 后期获取caseID
    case_id = "1234567"
    # print(df_temp.columns)
    df_temp = df_temp.iloc[1:] # 从PreCondition 行开始计算
    # print(df_temp)
    # 先提出从PreCondition 单元格没内容的
    df_temp.columns = df_temp.iloc[1]
    df_temp = df_temp.loc[:,"Comment":"DTC"]  # 后期通过方式定位开始和截止位置
    df_temp = df_temp.iloc[2:]
    df_temp.fillna("undefined",inplace = True)
    print(df_temp)

    # 开始写入脚本

    action_list = ["PreCondition","Set_DCSCondition","PostCondition"]
    expect_behavior_list = ["Status_Signal", "QF_Signal", "Equib_Signal", "CustomerDID_Status", "InternalDID_Status",
                         "InternalDID_QF", "Timer", "DTC"]
    expect_dcs_data_list = ["Status_Signal", "QF_Signal", "Equib_Signal", "CustomerDID_Status", "InternalDID_Status",
                         "InternalDID_QF"]
    test_object = "G_BBSD_DCS4"
    script_content = []
    variables_define = "var Sensor = \"" + test_object + "\";\n"
    variables_define += "var Sensor_Obj = " + test_object + ";\n"

    # variables_define
    script_content.append(script_header_1 + case_id +"\n" + script_header_2 + variables_define +  script_header_3 + test_begin + fault_loop_start)

    # print(df_temp["PostCondition"])
    step = 0 # 用来定义步骤
    substep = 0
    deepth = 1 # 用来定义下面步骤换行的倍数
    for indx in df_temp.index:
        steps_flag = df_temp.loc[indx,"Steps_Flag"]
        support_flag = df_temp.loc[indx,"Support"]
        if support_flag == "No": # 如果改步骤不支持，则跳过
            continue
        # 否则便利col

        if steps_flag == "PreStep":
            step += 1
            substep = 0
            deepth = 1
            script_content.append("\n" * 2)
            # 后期要用某种方式来处理列名的行为
            script_content.append(HC.return_start_Log(deepth,step,test_object,steps_flag))
            script_content.append(HC.return_step(deepth, step, substep))
            step_comment = df_temp.loc[indx, "Comment"]
            script_content.append(HC.return_step_comment(deepth, step_comment))

            script_temp = HC.handle_action(action_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
            script_temp = HC.handle_expect_result(expect_behavior_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)

            script_content.append(HC.return_stop_log(deepth))

        elif steps_flag == "SwitchTimer":
            step += 1
            substep = 0
            deepth = 1
            script_content.append("\n" * 2)
            script_content.append(HC.return_start_Log(deepth, step, test_object, steps_flag))
            script_content.append(HC.return_step(deepth, step, substep))
            step_comment = df_temp.loc[indx, "Comment"]
            script_content.append(HC.return_step_comment(deepth, step_comment))

            script_temp = HC.handle_action(action_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
            script_temp = HC.handle_expect_result(expect_behavior_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)

            script_content.append(HC.return_stop_log(deepth))

        elif steps_flag == "InitTimer":
            step += 1
            substep = 0
            deepth = 1
            script_content.append("\n" * 2)
            script_content.append(HC.return_start_Log(deepth, step, test_object, steps_flag))
            script_content.append(HC.return_step(deepth, step, substep))
            step_comment = df_temp.loc[indx, "Comment"]
            script_content.append(HC.return_step_comment(deepth, step_comment))

            script_temp = HC.handle_action(action_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
            script_temp = HC.handle_expect_result(expect_behavior_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)

            script_content.append(HC.return_stop_log(deepth))

        elif steps_flag == "Default":

            substep += 1
            deepth = 1

            script_content.append(HC.return_step(deepth, step, substep))
            step_comment = df_temp.loc[indx, "Comment"]
            script_content.append(HC.return_step_comment(deepth, step_comment))

            script_content.append(HC.handle_default_check(expect_dcs_data_list,df_temp,indx,deepth))


        if steps_flag == "Fault_PreStep":
            step += 1
            substep = 0
            deepth = 3
            script_content.append("\n" * 2)
            # 后期要用某种方式来处理列名的行为
            script_content.append(HC.return_start_Log(deepth, step, test_object, steps_flag))
            script_content.append(HC.return_step(deepth, step, substep))
            step_comment = df_temp.loc[indx, "Comment"]
            script_content.append(HC.return_step_comment(deepth, step_comment))

            script_temp = HC.handle_action(action_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
            script_temp = HC.handle_expect_result(expect_behavior_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
            script_content.append(HC.return_stop_log(deepth))

        elif steps_flag == "Qualifing" or steps_flag == "Disqualifing":
            substep += 1
            deepth = 3
            script_content.append("\n" * 2)
            # 后期要用某种方式来处理列名的行为
            script_content.append(HC.return_start_Log(deepth, step, test_object, steps_flag))
            if steps_flag == "Qualifing":
                script_content.extend(HC.return_fault_timer(deepth,"Qualify"))
            if steps_flag == "Disqualifing":
                script_content.extend(HC.return_fault_timer(deepth, "Disqualify"))
            script_content.append(HC.return_step(deepth, step, substep))
            step_comment = df_temp.loc[indx, "Comment"]
            script_content.append(HC.return_step_comment(deepth, step_comment))

            script_temp = HC.handle_action(action_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
            script_temp = HC.handle_expect_result(expect_behavior_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
        elif steps_flag == "Faulty_Reboot" or steps_flag == "Disqualify_Clear":
            substep += 1
            deepth = 3
            script_content.append("\n" * 2)
            # 后期要用某种方式来处理列名的行为
            script_content.append(HC.return_step(deepth, step, substep))
            step_comment = df_temp.loc[indx, "Comment"]
            script_content.append(HC.return_step_comment(deepth, step_comment))

            script_temp = HC.handle_action(action_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
            script_temp = HC.handle_expect_result(expect_behavior_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
            script_content.append(HC.return_stop_log(deepth))
        else:
            substep += 1
            deepth = 3
            script_content.append("\n" * 2)
            # 后期要用某种方式来处理列名的行为
            script_content.append(HC.return_step(deepth, step, substep))
            step_comment = df_temp.loc[indx, "Comment"]
            script_content.append(HC.return_step_comment(deepth, step_comment))

            script_temp = HC.handle_action(action_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)
            script_temp = HC.handle_expect_result(expect_behavior_list, df_temp, indx, deepth, test_object, Func_Dict)
            script_content.extend(script_temp)



    script_content.append(fault_loop_end)
    script_content.append(test_end)

    with open(Ts, 'w', encoding='UTF-8') as f:
        f.writelines(script_content)
        f.write("\n")
if __name__ == "__main__":
    pass
    ts = "DCS_Fault.ts"
    ExcelDir = r"C:\Users\victor.yang\Desktop\Work\CHT_SYV_Geely_GEAA2_HX11_DCS_Test Specification.xlsm"
    ObjectType = "DCS_Fault"
    GetDCSModule_Fault(ExcelDir, ObjectType,ts)