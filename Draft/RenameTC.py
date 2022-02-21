import os
import re

path = r"C:\Project\Geely_GEEA2_HX11\CANoe_Configuration\P30_01\Logs\UDS_Data_Test"


for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)) == True:
        if os.path.split(file)[1].split(".")[1] == 'blf':
            newname = file
            newname = newname.replace("TESTCASE", "TC")
            newname = newname + ".blf"
            # reg_Pattern = "TC_*"
            # re_match = re.match(reg_Pattern,newname).group()
            # if re_match:
            # newname = re_match + ".blf"
            # newname = newname.replace("TESTCASE", "TC")
            # print(newname)
            # caseID = os.path.split(file)[1].split(".")[0].split("_")[1]
            # print(file)
            # newname = "TC_" + caseID + ".blf"
            os.rename(os.path.join(path, file), os.path.join(path, newname))