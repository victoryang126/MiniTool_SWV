import PyPDF2 #可从PDF文档提取信息
import os #用于获取需要合并的PDF文件所在路径
import pandas as pd




def get_pwd_dict(pwd_excel):
    """

    :param pwd_excel:
    :return:
    """
    # ID	姓名	Password
    # Excel 必须保证第一行有ID 和 Password 作为title的两列
    df = pd.read_excel(pwd_excel,"Sheet1") # "Sheet1 为Excel的sheet 名字
    df = df[["ID","Password"]]
    df.set_index("ID",inplace= True)
    pwd_dict = df.to_dict(orient = "index")
    print(pwd_dict)

    return pwd_dict

def encryp_pdf(pdf_path,pwd_dict):
    """
    遍历pdf_path 获取其中的pdf文件

    然后根据pwd_dict 中依据 ID 来匹配文件找到相关文件的密码定义，给PDF文件加密
    :param pdf_path:
    :param pwd_dict:
    :return:
    """
    files=[]
    for file in os.listdir(pdf_path):
        if file.endswith(".pdf"): #排除文件夹内的其它干扰文件，只获取PDF文件
            files.append(pdf_path + "/"+ file)

    for file in files:
        pdf_obj=open(file,'rb')# 以二进制读取，将保留PDF中的所有信息
        pdf_reader=PyPDF2.PdfFileReader(pdf_obj)
        pdf_writer=PyPDF2.PdfFileWriter()
        for page_num in range(pdf_reader.numPages):
            page_obj=pdf_reader.getPage(page_num)
            pdf_writer.addPage(page_obj)

        pwd = "12345" #默认密码
        #根据ID 是否在文件名字中来获取相对应文件的秘密
        for ID in pwd_dict:
            if ID in file:
                print(ID)
                pwd = pwd_dict[ID]["Password"]
                break;
        # 如果还是默认密码，则打印找不到相关文件的密码定义
        if pwd == "12345":
            print("can't find the pwd for %s" %file)

        pdf_writer.encrypt(pwd)# 加密,密码设为'pass'，可个性化调整
        #写入并保存PDF文件:
        pdf_output_file=open(file.split(".")[0]+"_sec.pdf",'wb') #以二进制写入，将保留源PDF中的所有信息
        pdf_writer.write(pdf_output_file)
        pdf_output_file.close()
if __name__ == '__main__':
    pwd_excel = r"/Users/monster/PycharmProjects/GitHub/MiniTool/DataSource/Original/Password_List.xlsx"
    pdf_path = r"/Users/monster/PycharmProjects/GitHub/MiniTool/DataSource/Original"
    pwd_dict = get_pwd_dict(pwd_excel)
    encryp_pdf(pdf_path,pwd_dict)