# pdf_2.py

# 导入库

# from pdfminer.pdfparser import PDFParser, PDFDocument,PDFPage
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import re
import pandas as pd
import os

def ReadPDF_GetTxt(Pdf_Path):
    # 提供初始密码
    # 没有密码可以初始密码
    # document.initialize()
    password = ''
    #打开pdf文件
    Pdf_Text = ""
    with open(Pdf_Path, 'rb') as fp:
        #从文件句柄创建一个pdf解析对象
        parser = PDFParser(fp)
        #创建pdf文档对象，存储文档结构
        document = PDFDocument(parser)
        #创建一个pdf资源管理对象，存储共享资源
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        #创建一个device对象
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        #创建一个解释对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        #处理包含在文档中的每一页
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                # 获取文本对象
                if isinstance(x, LTTextBox):
                    offer_text=x.get_text()
                    # print(offer_text)
                    Pdf_Text += offer_text
                # 获取图片对象
                # if isinstance(x,LTImage):
                #     print('这里获取到一张图片')
                # #获取 figure 对象
                # if isinstance(x,LTFigure):
                #     print('这里获取到一个 figure 对象')
    # print(Pdf_Text)
    Pdf_Name = os.path.basename(Pdf_Path)
    return Pdf_Text,Pdf_Name

def Get_PdfTxtKeyMesg(Pdf_Text, Pdf_Name):
    Name_Pattern = re.compile("(?<=尊敬的).*(?=先生|女士)")
    Company_Pattern = re.compile("(?<=欢迎加入)\S*")
    BaseSalary_Pattern = re.compile("(?<=基本工资是).*(?=元)")
    InternSalary_Pattern = re.compile("(?<=试用期月薪是).*(?=元)")

    Name_Group = re.search(Name_Pattern, Pdf_Text)
    if Name_Group:
        Name = Name_Group.group().strip()
    else:
        Name = Pdf_Name

    Comparny_Group = re.search(Company_Pattern, Pdf_Text)
    if Comparny_Group:
        Company = Comparny_Group.group().strip()
    else:
        Company = Pdf_Name

    BaseSalary_Group = re.search(BaseSalary_Pattern, Pdf_Text)

    if BaseSalary_Group:
        BaseSalary = BaseSalary_Group.group().strip()
    else:
        BaseSalary = Pdf_Name

    InternSalary_Group = re.search(InternSalary_Pattern, Pdf_Text)

    if InternSalary_Group:
        InternSalary = InternSalary_Group.group().strip()
    else:
        InternSalary = Pdf_Name

    return Name,Company,BaseSalary,InternSalary

def Generate_SalaryExcel_FromPdfOffer(Dict_Salary, ExcelName):
    df = pd.DataFrame.from_dict(Dict_Salary)
    df.to_excel(ExcelName,index = False)

def Summary_AllPdf_Data(PdfPath_List, ExcelName):
    Dict_Salary = {"Name":[],"Compary":[],"BaseSalary":[],"InternSalary":[]}
    for PdfPath in PdfPath_List:
        #获取单个pdf 里面的内容
        Pdf_Text,Pdf_Name = ReadPDF_GetTxt(PdfPath)
        #获取姓名，公司，基本工资实习工资等信息
        Key_Msg = Get_PdfTxtKeyMesg(Pdf_Text,Pdf_Name)
        #往字典里面放数据
        Dict_Salary["Name"].append(Key_Msg[0])
        Dict_Salary["Compary"].append(Key_Msg[1])
        Dict_Salary["BaseSalary"].append(Key_Msg[2])
        Dict_Salary["InternSalary"].append(Key_Msg[3])
    Generate_SalaryExcel_FromPdfOffer(Dict_Salary,ExcelName)  
# 获取特定文件夹下面的所有pdf文件
def Get_PdfFromFolder(Spefolder):
    PdfPath_List = []
    for root, dirs, files in os.walk(Spefolder):
        for file in files:
            if file.split(".")[-1] == 'pdf':
                PdfPath_List.append(root + "/"+file)
                # print(root + "/"+file)
                # print(os.path.isfile(root + "/"+file))
    print(PdfPath_List)
    return PdfPath_List
if __name__ == '__main__':
    pass
    # dict_Salary = {"Name":["章三","李四"],"Compary":["1","2"],"Base":[3000,4000],"Intern":[2000,3000]}
    # PdfPath_List = ['../DataSource/test.pdf','../DataSource/2.pdf','../DataSource/test.pdf']
    # pdfPath = '../DataSource/test.pdf'
    # Spefolder = "/Users/monster/PycharmProjects/GitHub/MiniTool/DataSource"
    # PdfPath_List = Get_PdfFromFolder(Spefolder)
    # ExcelName = '../DataSource/Salary.xlsx'
    # ReadPDF_GetTxt(pdfPath)
    # Generate_SalaryExcel_FromPdfOffer(dict_Salary,ExcelName)
    # Summary_AllPdf_Data(PdfPath_List, ExcelName)