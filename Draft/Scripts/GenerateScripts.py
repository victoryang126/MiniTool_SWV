from string import Template
import os
import pandas as pd

def GenerateScripts_BaseTemplate(ScriptTemplateContent,ReplaceDict,ScriptOutputPath,TestObject_Str,TestType):
    """

    :param ScriptTemplateContent: 模板脚本的内容
    :param ReplaceDict:需要替换模版里面到相关内容 字典格式 Key 为模版里面需要被替换到部分
                        ，Value为 对应替换到内容
    :param ScriptOutputPath:脚本保存的路径
    :param TestObject_Str: 测试对象的名称
    :param Test_Type: 测试类型
    :return:
    """
    ScriptName_W_Path = ScriptOutputPath + "/" + TestType + "_" +TestObject_Str + ".ts"
    TempleteTemp = Template(ScriptTemplateContent).safe_substitute(ReplaceDict)
    with open(ScriptName_W_Path, "w") as ScriptTemp:
        ScriptTemp.write(TempleteTemp)

def GetTempleteScript(ScriptTemplate):
    """
    获取模板文件的内容，和模板文件的名字
    Parameters:
      ScriptTemplate - 模板文件（路径加名字） 目前名字的规则是xxx_yyyy.ts
                       xxxx最终会被替换成测试对象的名字，例如G_BBSD_DCS4
                       yyyy 定义为测试类型 FaultCheck/NormalCheck等
    Returns:
        TempleteContent - 模板脚本里面的所有内容
        Test_Type - 测试类型  _yyyy.ts
    Raises:
        IOerror - 当模板脚本不能被发现的时候会抛出异常
    """
    with open(ScriptTemplate, "r",encoding='UTF-8') as TmpF:
        TempleteContent = TmpF.read()

    Test_Type ="_".join(os.path.split(ScriptTemplate)[1].split(".")[0].split("_")[:-1])
    print(Test_Type)
    return TempleteContent,Test_Type

def ReadSpec(excel):
    df = pd.read_excel(excel,sheet_name="Element")
    # print(df.index)
    df.fillna("0x00",inplace=True)
    # print(df["Element"].duplicated())
    df.set_index("Element",inplace=True)
    df = df.T
    # print(df.columns[0])
    # df.set_index(df.columns[0], inplace=True,drop= False)
    # print(df.index)
    # print(df.columns.duplicated())
    # print(df.columns)
    # print(df)
    TestObject_Dict = df.to_dict(orient="index")
    print(TestObject_Dict)
    return TestObject_Dict


if __name__ == '__main__':
    excel = r"C:\Users\victor.yang\Desktop\Work\EDR\EDR Spe.xlsx"
    template = r"C:\Project\Geely_GEEA_HX11\ARiA_Configuration\P30_03\Scripts\EDR\EDR_Element_Template.ts"
    TempleteContent, Test_Type = GetTempleteScript(template)
    ScriptPath = r"C:\Users\victor.yang\Desktop\Work"
    TestObject_Dict = ReadSpec(excel)
    for TestObject_Str in TestObject_Dict:

        ReplaceDict = TestObject_Dict[TestObject_Str]
        ReplaceDict["Index"] = TestObject_Str
        args = {"ScriptTemplateContent": TempleteContent,
                "ReplaceDict": ReplaceDict,
                "ScriptOutputPath": ScriptPath, "TestObject_Str": TestObject_Str, "TestType": Test_Type}
        # 生成测试脚本
        GenerateScripts_BaseTemplate(**args)