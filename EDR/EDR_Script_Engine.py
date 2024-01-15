import re

from EDR.EDR_Signal import *
from EDR.EDR_General_Scripts import *

"""
function used to generate scripts
"""

def get_script_name(sheet,variant,digtal_col):
    return f"{sheet}_{variant}_{digtal_col}.ts"

def validate_fault_format(signal,faults):
    """
    function used to check if the fault format is correct or not
    Args:
        signal: the value in the sigla columns
        faults: the cell value,it shall be a list in parent scripts,
                and the element format shall be "EDRDTC,ACTIVE@"
    Returns:
    """
    for element in faults:
        if len(element) != 2:# length shall be two
            raise Exception(f"the faults{faults} in the signal {signal} is not correct, format shall as \'EDRDTC,ACTIVE@\'")
        else: # check if active and historic in it
            if (re.search("ACTIVE",element[1],re.I) == None) and (re.search("HISTORIC",element[1],re.I) == None):
                raise Exception(
                    f"the faults status of {faults} in the signal {signal} is not correct,the fault status shall contains ACTIVE or HISTORIC")


class EDR_Script_Engine:

    def __init__(self,outdir,sheet):
        self.outdir = outdir
        self.sheet = sheet


    def generate_start_Log(self,script_name):
        log_path = f"\tvar LogPath = LogFolder + \"{script_name}.log\";\n"
        log_action = f"\tStartToLog(LogPath);\n\n"
        return log_path + log_action



    def generate_stop_Log(self):
        stoplog_action = f"\n\n\tStopToLog();\n\n"
        return stoplog_action


    def get_scripts_by_id(self,id,frame,pdu,signal,value):
        pass_ids = ["Incident","Result"]
        # print(signal)
        # print(id,id=="au32EncodedActFlts[0]",regCompare.is_equal("au32EncodedActFlts[0]",id))
        if isinstance(value,str) == False:
            raise Exception(f"id:{id},frame: {frame},signal :{signal} have empty(NAN) value")
        value = value.strip()
        if re.search(".*_Signal_.*",id):
            frame = frame.strip()
            value = value.strip()
            hex_format_pattern = r"0x"
            if re.match(hex_format_pattern,value) == None:
                if value == "PDUDisabled":
                    return f"\tEnabledDisabledPDU(\'{frame}\', \'{pdu}\', false);\n" \
                           f"\t{signal} = \'PDUDisabled\';\n"
                else:
                    return f"\tBB_ArrSignalChange(\'{frame}\', \'{signal}\', '{value}');\n" \
                           f"\t{signal} = \'{value}\';\n"
            #set signal value, and assign the value to the input parameter
            else:
                return f"\tBB_ArrSignalChange(\'{frame}\', \'{signal}\', {value});\n" \
                   f"\t{signal} = \'{value}\';\n"
        elif regCompare.is_equal("FUNC",id):
            values = value.split("\n")
            # values = [f"\t{value};\n" for value in values]
            values = [f"\t{value[0:-1].strip()}\n" if value.endswith("#") else f"\t{value.strip()};\n" for value in values]
            values.insert(0,f"\tCommentStep(\"{signal}\");\n")
            values.insert(0, f"\n\t//-----------------------------TEST STEP------------------------------//;\n")
            return "".join(values)
        elif re.search(".*DCS.*",id):
            #set the signal value
            return f"\tSetDCSCondition(\"{signal}\",\'{value}\');\n" \
                   f"\t{signal}[\"ExpectStatus\"] = \'{value}\';\n"
        elif regCompare.is_equal("Fault",id):
            if value != "NONE":
                values = value.split("\n")
                faults = [fault.split(",") for fault in values]
                validate_fault_format(signal,faults)
                # print(faults)
                #conver to the format in js scripts, EDR + 'ACTIVE@'
                faults = [f"{fault[0]} + \'-{fault[1]}\'" for fault in faults]
                # print(faults)
                _faults = ",\n\t\t\t".join(faults)
                _scripts_line = []
                _scripts_line.append(f"\tvar Ret = ActualResults();\n")
                _scripts_line.append(f"\tvar Fault_Array = [{_faults}];\n")
                _scripts_line.append(f"\tvar Expect_Fault_Info = SetSuffixToFaultInfo(Fault_Array.toString());\n")
                _scripts_line.append(f"\tCompareResultsDefine(Ret,Expect_Fault_Info[1],Expect_Fault_Info[0]);\n")
            else:
                _scripts_line = []
                _scripts_line.append(f"\tvar Ret = ActualResults();\n")
                _scripts_line.append(f"\tvar Expect_Fault_Info = SetSuffixToFaultInfo(\"NONE\");")
                _scripts_line.append(f"\tCompareResultsDefine(Ret,Expect_Fault_Info[1],Expect_Fault_Info[0]);\n")
            _scripts_line.insert(0, f"\tCommentStep(\"Check Fault\");\n")
            _scripts_line.insert(0, f"\n\t//-----------------------------TEST STEP------------------------------//;\n")
            return "".join(_scripts_line)
        elif "au32EncodedActFlts[0]" == id:
            _scripts_line = []
            _scripts_line.append("\tvar Faults = new Array();\n")
            if value != "NONE":
                values = value.split("\n")
                faults = [fault.split(",") for fault in values]
                validate_fault_format(signal,faults)
                faults = [f"{fault[0]} + \'-{fault[1]}\'" for fault in faults]
                _faults = ",\n\t\t\t".join(faults)
                _scripts_line.append(f"\tFaults[0] = [{_faults}];\n")
            else:
                _scripts_line.append(f"\tFaults[0] = [];\n")
            _scripts_line.insert(0,f"\tCommentStep(\"{signal}\");\n")
            _scripts_line.insert(0, f"\n\t//-----------------------------TEST STEP------------------------------//;\n")
            return "".join(_scripts_line)
        elif "au32EncodedActFlts[1]" == id:
            _scripts_line = []
            if value != "NONE":
                values = value.split("\n")
                faults = [fault.split(",") for fault in values]
                validate_fault_format(signal,faults)
                faults = [f"{fault[0]} + \'-{fault[1]}\'" for fault in faults]
                _faults = ",\n\t\t\t".join(faults)
                _scripts_line.append(f"\tFaults[1] = [{_faults}];\n")
            else:
                _scripts_line.append(f"\tFaults[1] = [];\n")
            _scripts_line.insert(0,f"\tCommentStep(\"{signal}\");\n")
            _scripts_line.insert(0, f"\n\t//-----------------------------TEST STEP------------------------------//;\n")
            return "".join(_scripts_line)
        elif "au32EncodedActFlts[2]" == id:
            _scripts_line = []
            if value != "NONE":
                values = value.split("\n")
                faults = [fault.split(",") for fault in values]
                validate_fault_format(signal,faults)
                faults = [f"{fault[0]} + \'-{fault[1]}\'" for fault in faults]
                _faults = ",\n\t\t\t".join(faults)
                _scripts_line.append(f"\tFaults[2] = [{_faults}];\n")
            else:
                _scripts_line.append(f"\tFaults[2] = [];\n")
            _scripts_line.insert(0,f"\tCommentStep(\"{signal}\");\n")
            _scripts_line.insert(0, f"\n\t//-----------------------------TEST STEP------------------------------//;\n")
            return "".join(_scripts_line)
        elif id in pass_ids:
           return ""
        else:
            raise Exception(f"get_scripts_by_id have not handler this id value: {id}")


    def generate_scripts(self,digital_cols,df_dict):
        # loop the variatn to get realted df
        for variant in df_dict:
            df:pd.DataFrame = df_dict[variant]
            #loop the digital_cols to generate scripts
            for digtal_col in digital_cols:
                script_file = f"{self.sheet}_{variant}_{padded_number(digtal_col,3)}.ts"
                result_name = f"{self.sheet}_{variant}_{padded_number(digtal_col,3)}"
                case_info = f"EDR_{self.sheet}_{digtal_col}"
                script_lines = []
                script_lines.append(SCRIPT_BEGIN)
                script_lines.append(f"\tResultname = \'{result_name}\';\n")
                script_lines.append(f"\tCase_Info = \'{case_info}\';\n")
                script_lines.append(f"\tG_Variant = \'{variant}\';\n")
                script_lines.append(self.generate_start_Log(result_name))
                #then loop the index to get the script_lines
                for indx in df.index:
                    id = df.loc[indx,"ID"]
                    frame = df.loc[indx,"FRAME"]
                    pdu = df.loc[indx,"PDU"]
                    signal = df.loc[indx,"SIGNAL"]
                    value = df.loc[indx,digtal_col]
                    temp = self.get_scripts_by_id(id, frame, pdu,signal, value)
                    script_lines.append(temp)
                # script_lines.append(self.generate_start_Log(result_name))
                script_lines.append(SCRIPT_END)
                # print(script_lines)
                fileUtil.generate_script("".join(script_lines),self.outdir,script_file)
                # break









if __name__ == "__main__":
    # excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\SAIC_ZP22_Signal_Record_Strategy_20230323.xlsx"
    # fault = "Fault"
    # edr_fault = EDR_Fault(excel, fault)
    # edr_fault.refresh()
    # sheet = "EDR_General_Element"
    # edr_signal = EDR_Signal(excel, sheet)
    # edr_signal.refresh(edr_fault.fault_dict)
    excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\CHT_SAIC_ZP22_EDR_Script_Generator_Specification.xlsm"
    config_sheet = "EDR_Case_Config"

    edr_signal_config = EDR_Signal_Config(excel, config_sheet)
    edr_signal_config.refresh()

    sheets = ["EDR_General_Element","EDR_Dynamic_Value","EDR_Element_Abnormal","EDR_Config_C005","EDR_Config_C004","GB_EDR_Signal_16_isDircnIndLamp","GB_EDR_Signal_16_isVehHzrdMdSts"]
    # sheets = ["EDR_General_Element","EDR_Element_Abnormal"]
    # sheet = "EDR_General_Element"
    # sheet = "EDR_Config_C005"
    # sheet = "EDR_Config_C004"
    # sheet = "GB_EDR_Signal_16_isDircnIndLamp"
    # sheet = "GB_EDR_Signal_16_isVehHzrdMdSts"
    # sheet = "EDR_Element_Abnormal"
    for sheet in sheets:
        print(sheet)
        edr_signal = EDR_Signal(excel, sheet)
        edr_signal.refresh(edr_signal_config.signal_dict)
        script_engine = EDR_Script_Engine(r"C:\Users\victor.yang\Desktop\Work\Scripts\EDRScripts",sheet)
        script_engine.generate_scripts(edr_signal.digital_cols,edr_signal.df_dict)