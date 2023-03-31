import re

from EDR.EDR_Signal import *
from EDR.EDR_General_Scripts import *

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

    def get_scripts_by_id(self,id,frame,signal,value):
        if re.search(".*_Signal_.*",id):
            #set signal value, and assign the value to the input parameter
            return f"\tBB_ArrSignalChange(\'{frame}\', \'{signal}\', {value});\n" \
                   f"\t{signal} = \'{value}\';\n"
        elif regCompare.is_equal("FUNC",id):
            values = value.split("\n")
            values = [f"\t{value};\n" for value in values]
            return "".join(values)
        elif re.search(".*DCS.*",id):
            #set the signal value
            return f"\tSetDCSConditions(\"{signal}\",\'{value}\');\n" \
                   f"\t{signal}[\"ExpectStatus\"] = \'{value}\';\n"
        elif regCompare.is_equal("Fault",id):
            if value != "NONE":
                values = value.split("\n")
                faults = [fault.split(",") for fault in values]
                validate_fault_format(signal,faults)
                print(faults)
                #conver to the format in js scripts, EDR + 'ACTIVE@'
                faults = [f"{fault[0]} + \'{fault[1]}\'" for fault in faults]
                # print(faults)
                _faults = ",\n\t\t\t".join(faults)
                _scripts_line = []
                _scripts_line.append(f"\tvar Ret = ActualResults();\n")
                _scripts_line.append(f"\tvar var Fault_Array = [{_faults}];\n")
                _scripts_line.append(f"\tvar Expect_Fault_Info = SetSuffixToFaultInfo(Fault_Array.toString());\n")
                _scripts_line.append(f"\tCompareResultsDefine(Ret,Expect_Fault_Info[1],Expect_Fault_Info[0]);\n")
            else:
                _scripts_line = []
                _scripts_line.append(f"\tvar Ret = ActualResults();\n")
                _scripts_line.append(f"\tvar Expect_Fault_Info = SetSuffixToFaultInfo(\"NONE\");")
                _scripts_line.append(f"\tCompareResultsDefine(Ret,Expect_Fault_Info[1],Expect_Fault_Info[0]);\n")
            return "".join(_scripts_line)
        else:
            raise Exception(f"get_scripts_by_id have not handler this id value: {id}")


    def generate_scripts(self,digital_cols,df_dict):
        # loop the variatn to get realted df
        for variant in df_dict:
            df:pd.DataFrame = df_dict[variant]
            #loop the digital_cols to generate scripts
            for digtal_col in digital_cols:
                script_file = f"{self.sheet}_{variant}_{digtal_col}.ts"
                result_name = f"{self.sheet}_{variant}_{digtal_col}"
                script_lines = []
                script_lines.append(SCRIPT_BEGIN)
                script_lines.append(f"\tResultname = \'{result_name}\';\n")
                #then loop the index to get the script_lines
                for indx in df.index:
                    id = df.loc[indx,"ID"]
                    frame = df.loc[indx,"Frame"]
                    signal = df.loc[indx,"Signal"]
                    value = df.loc[indx,digtal_col]
                    temp = self.get_scripts_by_id(id, frame, signal, value)
                    script_lines.append(temp)
                script_lines.append(SCRIPT_END)
                fileUtil.generate_script("".join(script_lines),self.outdir,script_file)
                break;









if __name__ == "__main__":
    excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\SAIC_ZP22_Signal_Record_Strategy_20230323.xlsx"
    fault = "Fault"
    edr_fault = EDR_Fault(excel, fault)
    edr_fault.refresh()
    sheet = "EDR_General_Element"
    edr_signal = EDR_Signal(excel, sheet)
    edr_signal.refresh(edr_fault.fault_dict)

    script_engine = EDR_Script_Engine(r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\tempscripts",sheet)
    script_engine.generate_scripts(edr_signal.digital_cols,edr_signal.df_dict)