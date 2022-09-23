import re
from string import Template

def return_start_Log(deepth,step,test_object,flag):
    log_path = "\t" * deepth + "var StorePath = LogFolder + \"" + test_object \
           + "_" + flag + str(step) + ".log\"" + ";\n"
    log_action = "\t" * deepth + "StartToLog(StorePath)" + ";\n"
    return log_path + log_action

def return_stop_log(deepth):
    stoplog_action = "\t" * deepth + "StopToLog()" + ";\n"
    return stoplog_action

def return_step(deepth,step,substep):
    step = "\t" * deepth + "//" + str(step) + "." + str(substep) + "#" * 15 + ";\n"
    return step

def return_step_comment(deepth,comment):

    step_comment = "\t"*deepth + "CommentStep(\"" + comment + "\")" + ";\n"
    return step_comment

def check_func_flag(a):
    b = a.split("(")
    if re.search("\(",a):
        return "(" + b[1] +";\n"
    else:
        return "();\n"



def return_pre_post_action(deepth,p_condition,func_dict):
    pre_post_action =""
    if p_condition != "undefined":
        p_condition_funclist = p_condition.split(",")
        for func in p_condition_funclist:
            temp = "\t" * deepth + Template("${" + func.split("(")[0] + "}").safe_substitute(
                func_dict) + check_func_flag(func)
            pre_post_action += temp
    else:
        pre_post_action = ""
    return pre_post_action


def return_set_action(deepth,func_name,test_object,condition):
    set_action = "\t" * deepth + func_name + "(\"" + test_object + "\",\"" + condition  + "\");\n"
    return set_action

"""

"""
def return_check_action(deepth,func_name,test_object,status):
    check_action = "\t" * deepth + func_name + "(\"" + test_object + "\",\"" + status  + "\");\n"
    return check_action
