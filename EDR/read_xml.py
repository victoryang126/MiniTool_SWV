
import os
import sys
import pandas as pd
from bs4 import BeautifulSoup as Bs



class Xml_Result:

    def __init__(self,xml_file):
        self.xml_file = xml_file

    def generate_fail_report(self):
        outdir,file_name = os.path.split(self.xml_file)
        file_name = file_name.split(".")[0]

        with open(self.xml_file, "r", encoding='utf-8') as file:
            xmldata = file.read()

        soup = Bs(xmldata, "xml")

        fail_dict = {"Action":[],"Type":[],"Parameter":[],"Expected":[],"Obtained":[],"Result":[]}
        action_items = soup.find_all("Action")
        for item in action_items:
            if item.Result.text == "Failed":
                action = item.attrs["Name"].split(" ")
                fail_dict["Action"].append(item.attrs["Name"])
                if len(action)>3:
                    fail_dict["Type"].append(action[1])
                    fail_dict["Parameter"].append(action[3])
                else:
                    fail_dict["Type"].append("None")
                    fail_dict["Parameter"].append("None")
                fail_dict["Expected"].append(item.Expected.text)
                fail_dict["Obtained"].append(item.Obtained.text)
                fail_dict["Result"].append(item.Result.text)

        df_fail = pd.DataFrame.from_dict(fail_dict)
        report = os.path.join(outdir,file_name +".xlsx")
        df_fail.to_excel(report,sheet_name="Failed",index=False)


if __name__ == '__main__':
    result  = r"C:\Project\SAIC_ZP22\Test_Results\P10_02\HEV\EDR\LastOutput\Signal_Record_13.xml"
    xml_result = Xml_Result(result)
    xml_result.generate_fail_report()