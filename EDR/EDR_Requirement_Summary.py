import pandas as pd

from EDR.ImportModule import *

def merge_rows(row):
    return "\n".join(row.astype(str))

def process_result(row):
    # print(row)
    if row == ['OK']:
        return "OK"
    elif row == ['']:
        return "NA"
    else:
        return "NOK"

class EDR_Req_Summary:

    def __init__(self,excel,sheets):
        self.excel = excel
        self.sheets = sheets
        self.req_config = {}

    def get_req_config(self,sheet = "Requirement"):
        """
        funciton to get the requirement id config,
        in the test matrix, there some row may check many requirement
        Args:
            sheet:default value is Requirement
        Returns:
        """
        df = pd.read_excel(self.excel,sheet)
        for col in df.columns:
            df_cols = df[col]
            # print(col)
            df_cols.dropna(inplace=True)
            self.req_config[col] = "\n".join(df_cols.values.tolist())

    def get_req_ids_in_sheet(self,sheet,df):
        # df = pd.read_excel(self.excel,sheet)
        if "Requirement" not in df.columns:
            raise Exception(f"Requirement not defined in {sheet}")
        df_reqs = df["Requirement"].dropna()
        #check if the x is in the self.req_config, if yes, use the value in the req_config, or use the original
        df_reqs = df_reqs.apply(lambda x:x if x not in self.req_config else self.req_config[x])

        df_reqs = df_reqs.apply(lambda x:x.split("\n"))
        reqs = "\n".join(df_reqs.sum())
        return reqs

    def get_incidents_results_in_sheet(self,sheet,df,reqs):
        # df = pd.read_excel(self.excel,sheet,dtype="str")
        cols = ["ID"]
        digital_cols = df.filter(regex='^\d+$').columns.tolist()
        cols.extend(digital_cols)
        df = df[cols]
        df:pd.DataFrame = df.query("ID in ['Incident','Result']") #filter the Incident and Result in the col ID

        merge_df = pd.pivot_table(df,index="ID",aggfunc=lambda x:"\n".join(x.dropna()))
        # merge_df = df.pivot_table(index="ID",values = "Data",)

        merge_df.loc["Result"]  = merge_df.loc["Result"].apply(lambda x: list(set(x.split("\n"))))
        # print(merge_df)
        merge_df.loc["Result"] = merge_df.loc["Result"].apply(process_result)
        merge_df = merge_df.T
        # print(reqs)
        merge_df["Requirement"] = reqs
        # f"{self.sheet}_{variant}_{padded_number(digtal_col, 3)}
        # print()
        merge_df.set_index(pd.Index([ f"{sheet}_{padded_number(digtal_col,3)}" for digtal_col in digital_cols]),"ID",inplace=True)

        return merge_df

    def generate_summary_report(self,output_dir):
        df_summary = pd.DataFrame()
        self.get_req_config()
        for sheet in self.sheets:
            df = pd.read_excel(self.excel,sheet,dtype= str)
            reqs = self.get_req_ids_in_sheet(sheet,df)
            merge_df = self.get_incidents_results_in_sheet(sheet,df,reqs)
            df_summary = pd.concat([df_summary,merge_df])
        # print(df_summary)
        df_summary["Incident"] = df_summary["Incident"].apply(lambda x:"\n".join(set(x.split("\n"))))
        file_path = os.path.join(output_dir,"EDR_Summary_Report.xlsx")
        df_summary.to_excel(file_path)



if __name__ == "__main__":
    excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\SAIC_ZP22_Signal_Record_Strategy_20230526Victor.xlsx"
    sheets = ["EDR_General_Element", "EDR_Element_Abnormal", "EDR_Config_C005", "EDR_Config_C004",
              "GB_EDR_Signal_16_isDircnIndLamp", "GB_EDR_Signal_16_isVehHzrdMdSts"]
    outputdir = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR"
    edr_req_summary = EDR_Req_Summary(excel,sheets)
    edr_req_summary.generate_summary_report(outputdir)
    # edr_req_summary.get_req_config() # sheet name shall be requirement
    # edr_req_summary.get_req_ids_in_sheet("EDR_General_Element")
    # edr_req_summary.get_incidents_results_in_sheet("EDR_General_Element")
