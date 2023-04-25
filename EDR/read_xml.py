
import os
import sys
import pandas as pd
from bs4 import BeautifulSoup as Bs
import re



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



class Xml_Result_TTF:

    G_Loop_Config = ['DrAB1', 'PaAB1', 'DrPT1', 'PaPT1',
                     'LtThoraxRow1', 'RtThoraxRow1', 'LtCurtain1',
                     'RtCurtain1', 'LtPT1Row2', 'RtPT1Row2',
                     'DrPT2', 'PaPT2']

    def __init__(self,root):
        self.root = root
        self.xml_files = []
        self.ttf_maps = {}



    def read_all_xml(self):
        for main_folder, sub_folder, files in os.walk(self.root):
            self.xml_files = [os.path.join(main_folder,file) for file in files]
        for xml_file in self.xml_files:
            outdir,file_name = os.path.split(xml_file)
            file_name = file_name.split(".")[0]

            with open(xml_file, "r") as file:
                print(xml_file)
                xmldata = file.read()

            soup = Bs(xmldata, "xml")

            fail_dict = {"Action":[],"Type":[],"Parameter":[],"Expected":[],"Obtained":[],"Result":[]}
            action_items = soup.find_all("Action")
            # get_ttf_flag = False
            for item in action_items:
                if item.attrs["Name"] == "All TTF":
                    get_ttf_flag = True
                    ttf = item.Obtained.text
                    ttf = re.sub(r"\(|\)","",ttf)
                    ttf = ttf.split(",")
                    loop_ttf = dict(zip(self.G_Loop_Config,ttf))
                    self.ttf_maps[file_name] = loop_ttf
                #找ttf 下面的fault
                # if get_ttf_flag == True:
                #     pass

    def generate_ttf_report(self,outdir,file_name):

        df_ttf = pd.DataFrame.from_dict(self.ttf_maps)
        df_ttf = df_ttf.T
        # print(df_fail.T)
        report = os.path.join(outdir,file_name +".xlsx")
        df_ttf.to_excel(report,sheet_name="Failed",index=True)


if __name__ == '__main__':
    root = r"C:\Project\SAIC_ZP22\Test_Results\P20_02\HEV\EDR\LastOutput"

    for main_folder, sub_folder, files in os.walk(root):
        xml_files = [os.path.join(main_folder, file) for file in files if file.split(".")[1] == 'xml']

    for result in xml_files:
        xml_reult  =  Xml_Result(result)
        xml_reult.generate_fail_report()

    # root = r"C:\Users\victor.yang\Downloads\ARB_Backup_Auto"
    # outdir = r"C:\Project\SAIC_ZP22"
    # file_name = "SAIC_ZP22_TTF_Backup.xlsx"
    # xml_result = Xml_Result_TTF(root)
    # xml_result.read_all_xml()
    # xml_result.generate_ttf_report(root,file_name)