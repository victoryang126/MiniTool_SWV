from EDR.ImportModule import *


def process_signal(s):
    """
    function used to conver the value in the signal columsn
    as the sw cauptre from dbc or axrml, the value in the signal columns maybe
    isVehSpdAvgDrvn(15) or VehSpdAvgDrvn(15)
    so to get the actual signal name in ARIA, we need call this function to convert it
    Args:
        s:the cell value in the columns
    Returns:
    """
    is_signal_pattern = r'is([A-Za-z]+)\(\d+\)'
    signal_pattern = r'([A-Za-z]+)\(\d+\)'
    is_signal_match = re.match(is_signal_pattern,s)
    signal_match = re.match(signal_pattern,s)
    if is_signal_match:
        return is_signal_match.group(1)
    elif signal_match:
        return signal_match.group(1)
    else:
        return s


def process_fault(fault_series, digital_cols, df_map):
    """
    this function is used  map the value of fault from fault sheet to test case sheet
    Args:
        fault_series: signal series
        digital_cols: the columns that is digital
        df_map: the dataframe get from Fault sheet
    Returns:
    """
    id = fault_series.loc["ID"]
    variant = fault_series.loc["Variant"]
    # find the fault and variant in the fault sheet data frame, and then assigna related data to it
    if id in df_map["ID"].values and variant in df_map["Variant"].values:
        df_match = df_map.query("ID==@id and Variant==@variant")
        series_match = df_match.iloc[0]  # shall use series
        fault_series.loc[digital_cols] = series_match.loc[digital_cols]
    return fault_series

class EDR_Fault:
    def __init__(self,excel,sheet):
        self.excel = excel
        self.sheet = sheet
        self.fault_dict = {}
    def refresh(self):
        df = pd.read_excel(self.excel, self.sheet, dtype='str')
        df.fillna(method='ffill', axis=1, inplace=True)
        self.fault_dict = {}
        df_group = df.groupby("Sheet")
        for sheet, group in df_group:
            group.drop(columns=['Sheet'], inplace=True)
            self.fault_dict[sheet] = group

class EDR_Signal:

    def __init__(self,excel,sheet):
        self.excel = excel
        self.sheet = sheet
        self.df_dict = {}
        self.digital_cols = []

    def refresh(self,fault_dict):
        df = pd.read_excel(self.excel, self.sheet, dtype='str')
        #filger the columns, ID,Frame,Signal,Variant, and digital columns
        filter = '^(?i)(Signal|Variant|Frame|ID|\d+)$'
        df = df.filter(regex=filter)
        # need check if id frame,signal variant, is in the
        # strip the space in this columns
        df["ID"] = df["ID"].fillna(method='ffill')
        df["Frame"] = df["Frame"].fillna(method='ffill')
        df = df.query('Variant.notnull()')
        df["Signal"] = df["Signal"].apply(process_signal)


        # get the columns which is use to set the case
        self.digital_cols = df.filter(regex='^\d+$').columns.tolist()
        df_cols_is_digital = df[ self.digital_cols]
        df_cols_is_digital.fillna(method='ffill', axis=1, inplace=True)

        # get the colums which is not digital, then join the df_cols_is_digital
        df = df.filter(regex="^\D+$")
        df = df.join(df_cols_is_digital)
        # get the fault from fault sheet
        if self.sheet in fault_dict:
            df = df.apply(process_fault,digital_cols = self.digital_cols,df_map = fault_dict[self.sheet],axis= 1)
        # group based on Variant, using explode to tranform each variant to row
        #  such as [HEV,EP] will convert to two rows, other columns value will not changed
        df["Variant"] = df["Variant"].str.split(",")
        df = df.explode("Variant")
        # get how many variant is support
        series_variants = df["Variant"]
        variants = set(series_variants.tolist())
        Monitor_Logger.info(f"Variants {variants}")
        df = df.explode("Variant")
        for variant in variants:
            df_temp = df.query('Variant == @variant')
            Debug_Logger.debug(df_temp.tail(5))
            self.df_dict[variant] = df_temp


if __name__ == '__main__':
    excel = r"C:\Users\victor.yang\Desktop\Work\SAIC\EDR\SAIC_ZP22_Signal_Record_Strategy_20230323.xlsx"
    fault = "Fault"
    edr_fault = EDR_Fault(excel,fault)
    edr_fault.refresh()
    sheet = "EDR_General_Element"
    edr_signal = EDR_Signal(excel,sheet)
    edr_signal.refresh(edr_fault.fault_dict)

