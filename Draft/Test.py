import win32com
from win32com.client import Dispatch
ExcelAPP = win32com.client.DispatchEx('Excel.Application')
# ExcelAPP.Visible = 0
# ExcelAPP.DisplayAlerts = 0
# RepaceDoorsID_SaveMacroEcel(ExcelAPP,Spec,Df_PTC_Spec,LastSheet_Name,RowSize)
ExcelAPP.Quit()  # 退出