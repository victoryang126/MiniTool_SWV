
from EDR.ImportModule import *

class Epprom_Translate:
    def __init__(self,excel):
        self.excel = excel
        self._block_ids = []
        self.sheet = "EEPROM Parameters"
        self.edr_block_params = None
        self.df_edr_block = pd.DataFrame()

    @property
    def block_ids(self):
        return self._block_ids

    @block_ids.setter
    def block_ids(self,ids):
        self._block_ids = ids

    @block_ids.getter
    def block_ids(self):
        return self._block_ids

    @func_monitor
    def get_edr_block(self):
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        df = pd.read_excel(self.excel, self.sheet)
        df = df[["PARAMETER NAME", "BLOCK SIGNATURE", "BLOCK ID", "READ VALUE"]]
        self.df_edr_block = df.loc[df["BLOCK ID"].isin(self.block_ids)]
        self.df_edr_block.columns = ["PARAMETER_NAME", "BLOCK_SIGNATURE", "BLOCK_ID", "READ_VALUE"]
        self.edr_block_params = list(self.df_edr_block["PARAMETER_NAME"].values)

    def generate_nvm_result(self,nvm_result):
        df_temp = self.df_edr_block[["PARAMETER_NAME","READ_VALUE"]]
        # df_temp.set_index("PARAMETER_NAME",inplace=True)
        temp_result = dict(zip(df_temp["PARAMETER_NAME"].values,df_temp["READ_VALUE"].values))
        with open(nvm_result, mode="w", encoding='UTF-8') as f:
            json.dump(temp_result, f, indent=4)
