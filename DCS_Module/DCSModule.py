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
Func_Dict = {
"PwOff":"PowerOff",
"PwOn":"PowerOn",
"TSlp":"Thread.Sleep",
"NmBSlp":"BussSleep",
"NmWkUp":"NmWakeUp",

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
    for ind in df.index:
        if df.loc[ind,"CaseIndex"] == "CaseStart":

            if case_start != 0:
                pass # 如果再找到caseStart的时候已经被赋值了，说明配置有问题，需要报错
            case_start = ind
        elif df.loc[ind,"CaseIndex"] == "CaseEnd":
            case_end = ind
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
    df_temp = df_case_list[0]

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

    test_object = "G_BBSD_DCS4"
    script_content = []
    script_content.append(script_header_1 + case_id +"\n" + script_header_2 + script_header_3 + test_begin)

    step = 0 # 用来定义步骤
    substep = 0
    deepth = 1 # 用来定义下面步骤换行的倍数
    for ind in df_temp.index:
        steps_flag = df_temp.loc[ind,"Steps_Flag"]
        support_flag = df_temp.loc[ind,"Support"]
        if support_flag == "No": # 如果改步骤不支持，则跳过
            continue
        # 否则便利col

        if steps_flag == "PreStep":
            step += 1
            substep = 0
            deepth = 1

            script_content.append(HC.return_start_Log(deepth,step,test_object,steps_flag))
            precondition = df_temp.loc[ind, "PreCondition"]
            script_content.append(HC.return_pre_post_action(deepth, precondition, Func_Dict))
            condition = df_temp.loc[ind, "DCSCondition"]
            script_content.append(HC.return_set_action(deepth,"BB_SetDCSCondition",test_object,condition))


            script_content.append("\n" * 2)


        elif steps_flag == "SwitchTimer":
            step += 1
            substep = 0
            deepth = 1



            script_content.append("\n" * 2)
        elif steps_flag == "InitTimer":
            step += 1
            substep = 0
            deepth = 1


            script_content.append("\n"*2)
        elif steps_flag == "Default":

            substep += 1
            deepth = 1
            script_content.append("\t"*deepth + "//" + str(step)  + "." + str(substep) + "#" * 15 + ";\n")
            action_comment = "\t" * deepth + "CommentSubStep(\"" + df_temp.loc[ind, "Comment"] + "\")" + ";\n"
            script_content.append(action_comment)

            script_content.append("\n" * 2)

    with open(Ts, 'w', encoding='UTF-8') as f:
        f.writelines(script_content)
        f.write("\n")

if __name__ == "__main__":
    pass
    ts = "DCS.ts"
    ExcelDir = r"C:\Users\victor.yang\Desktop\Work\CHT_SYV_Geely_GEAA2_HX11_DCS_Test Specification.xlsm"
    ObjectType = "DCS_NormalStatus"
    GetDCSModule(ExcelDir, ObjectType,ts)