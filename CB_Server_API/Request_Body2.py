
import json
import dataclasses
"""
获取response 里面的属性

根据需求生成Request Body

Field类型：
1
{
filedId
name
value = "" or[]
type = ""
}

2
{
"ID:
"Name"
"type"
}

3.
{
ID,
Name
type
referenceData = {}
}

"""
class Field_Type:
    ChoiceFieldValue = "ChoiceFieldValue"
    ChoiceOptionReference = "ChoiceOptionReference"
    TrackerItemReference = "TrackerItemReference"
    TextFieldValue = "TextFieldValue"
    Testcase = "Testcase"
    Testrun = "Testrun"
    TableFieldValue = "TableFieldValue"
    BoolFieldValue = "BoolFieldValue"
    TrackerReference = "TrackerReference"

class Value_Mapping:
    descriptionFormat = "Wiki"
    flase = False
    true = True


class SuspectPropagation:
    DO_NOT_PROPAGATE = "DO_NOT_PROPAGATE"
    null = None
    PROPAGATE = "PROPAGATE"
# @dataclasses
class Field:
    def __init__(self,fieldId=0,name="",value="",type = ""):
        self.fieldId = fieldId
        self.name = name
        self.value = value
        self.type = type

class Field_Values:
    def __init__(self, fieldId=0, name="", values=[], type=""):
        self.fieldId = fieldId
        self.name = name
        self.values = values
        self.type = type
    # def __getattr__(self, attr):
    #     return self[attr]

# @dataclasses
class Value_Id:
    def __init__(self,id=0,name="",type = ""):
        self.id = id
        self.name = name
        self.type = type
    # def __getattr__(self, attr):
    #     return self[attr]
# @dataclasses
class Value_Id_Refer_Data:
    def __init__(self, id=0, name="", type="",suspectPropagation = ""):
        self.id = id
        self.name = name
        self.type = type
        self.referenceData = {}
        self.referenceData["suspectPropagation"] = suspectPropagation
    # def __getattr__(self, attr):
    #     return self[attr]

class IncidentId:
    def __init__(self, id=0):
        self.id = id
        self.type = Field_Type.TrackerItemReference


class Verifies:
    def __init__(self, id=0):
        self.id = id
        self.type = Field_Type.TrackerItemReference
        self.referenceData = {}
        self.referenceData["suspectPropagation"] = SuspectPropagation.PROPAGATE

class TestMethod(Value_Id):
    """

    """
    def __init__(self,indx):
        if indx == 0:
            super().__init__(0,"Unset",Field_Type.ChoiceOptionReference)
        elif indx == 1:
            super().__init__(1, "Others", Field_Type.ChoiceOptionReference)
        elif indx == 2:
            super().__init__(2, "Fault Injection", Field_Type.ChoiceOptionReference)
        elif indx == 3:
            super().__init__(3, "Internal External Interfaces", Field_Type.ChoiceOptionReference)
        elif indx == 4:
            super().__init__(4, "Statement Coverage", Field_Type.ChoiceOptionReference)
        elif indx == 5:
            super().__init__(5, "Requirement Based", Field_Type.ChoiceOptionReference)
        elif indx == 6:
            super().__init__(6, "Analysis Of Functional Dependencies", Field_Type.ChoiceOptionReference)
        elif indx == 7:
            super().__init__(7, "Boundary Value Analysis", Field_Type.ChoiceOptionReference)
        elif indx == 8:
            super().__init__(8, "Environmental Conditions Or Use Case", Field_Type.ChoiceOptionReference)
        elif indx == 9:
            super().__init__(9, "Equivalence Classes", Field_Type.ChoiceOptionReference)
        elif indx == 10:
            super().__init__(10, "Error Guessing", Field_Type.ChoiceOptionReference)
        elif indx == 11:
            super().__init__(11, "Control Flow", Field_Type.ChoiceOptionReference)
        elif indx == 12:
            super().__init__(12, "Common Limit Conditions Or Sequences Or Sources Of Dependent Failures", Field_Type.ChoiceOptionReference)
        else:
            raise Exception("No test mothod defind for index " + str(indx))

class TestRun_Status(Value_Id):
    def __init__(self,indx):
        if indx == 1:
            super().__init__(indx, "In progress", Field_Type.ChoiceOptionReference)
        elif indx == 2:
            super().__init__(indx, "Suspended", Field_Type.ChoiceOptionReference)
        elif indx == 4:
            super().__init__(indx, "Finished", Field_Type.ChoiceOptionReference)
        elif indx == 5:
            super().__init__(indx, "Closed", Field_Type.ChoiceOptionReference)
        elif indx == 7:
            super().__init__(indx, "Ready for execution", Field_Type.ChoiceOptionReference)
        elif indx == 8:
            super().__init__(indx, "Rejected", Field_Type.ChoiceOptionReference)
        elif indx == 6:
            super().__init__(indx, "To be approved", Field_Type.ChoiceOptionReference)
        else:
            raise Exception("No TestRun_Status defind for index " + str(indx))

# @dataclasses
class TestCase_In_TestRun:
    '''
    用在Test Run里面case的元素，单独拉出来，仅仅只要定义ID ，namej即可
    '''
    def __init__(self,id = 0,name = ""):
        self.id = id
        self.name = name
        self.type = Field_Type.TrackerItemReference
        self.referenceData = {}
        self.referenceData["suspectPropagation"] = SuspectPropagation.DO_NOT_PROPAGATE
    # def __getattr__(self, attr):
    #     return self[attr]
# @dataclasses
class Post_TestCase_Body:
    """
    上传Test case的
    其中，修改Inciden ID, Test Method，Verifies的方式待定
    """
    testmethod_id = 1035
    def __init__(self,name):
        self.name = name
        self.descriptionFormat = Value_Mapping.descriptionFormat
        self.customFields = [  #Field_Values(1027,"Incident ID",[],Field_Type.ChoiceFieldValue).__dict__, # Incident Id
                             Field_Values(self.testmethod_id, "Test Method", [], Field_Type.ChoiceFieldValue).__dict__,  # Test Method
                             Field_Values(17, "Verifies", [], Field_Type.ChoiceFieldValue).__dict__ # Verifies

                             ]
        self.status = Value_Id(1, "Init", Field_Type.ChoiceOptionReference).__dict__
        self.versions = []
        self.typeName = Field_Type.Testcase

    @classmethod
    def update_testmethod_id(cls,testmethod_id):
        cls.testmethod_id = testmethod_id

    # def update_incidentid(self,incidentid_list):
    #     if len(incidentid_list)== 0:
    #         #不处理，继续为空
    #         pass
    #     else:
    #         incidentid_obj_list = [IncidentId(incidentid).__dict__ for incidentid in incidentid_list]
    #         self.customFields[0]["values"].extend(incidentid_obj_list)

    def update_testmethod(self,testmethodid_list):

        if len(testmethodid_list) == 0:
            pass
        else:
            testmethod_obj_list = [TestMethod(testmethodid).__dict__ for testmethodid in testmethodid_list]
            self.customFields[0]["values"].extend(testmethod_obj_list)




    def update_verifies(self,verifiesid_list):
        if len(verifiesid_list) == 0:
            pass
        else:
            verifies_obj_list = [Verifies(verifiesid).__dict__ for verifiesid in verifiesid_list]
            self.customFields[1]["values"].extend(verifies_obj_list)

    def update_versions(self,versions_dict):
        """

        Args:
            versions_dict:

        Returns:

        """
        self.versions.append(Value_Id(**versions_dict).__dict__)


    def delete_testcase(self):
        """
        customFields 设置为空，即不更新里面的数据，保持原来 数据
        Returns:
        None
        """
        self.status = Value_Id(6, "Obsolete", Field_Type.ChoiceOptionReference).__dict__
        self.customFields = []


# @dataclasses
class TestRunMoel:
    """
    暂时是上传Test run 里面的json的一个元素，拉到这里面单独定义

    Version待定
    """
    test_information_id = 10003
    def __init__(self,name,tracker,test_information):
        self.name = name
        self.descriptionFormat = Value_Mapping.descriptionFormat
        self.tracker = Value_Id(tracker,"",Field_Type.TrackerReference).__dict__ #Value_Id的对象
        self.customFields = [
            Field(self.test_information_id, "Test Information",test_information , Field_Type.TextFieldValue).__dict__, # Test Information
            Field_Values(1000000, "Test Cases", [[]], Field_Type.TableFieldValue).__dict__, #Test Cases
        ]
        self.status =TestRun_Status(7).__dict__
        self.formality = Value_Id(1, "Regular", Field_Type.ChoiceOptionReference).__dict__
        self.versions = []
        self.typeName = Field_Type.Testrun

    @classmethod
    def update_test_inforamtion_id(cls,test_inforamtion_id):
        cls.test_information_id = test_inforamtion_id

class Post_TestRun_Body:
    """
    暂定为上传test Run 需要用的元素
    """
    def __init__(self,testcases,name,tracker,test_information):
        self.testCaseIds = [testcase.__dict__ for testcase in testcases] # test case 必须是Value_Id_Refer_Data的对象数组
        self.testRunModel = TestRunMoel(name,tracker,test_information).__dict__


        for indx,testcase in enumerate(testcases): # 在Test Cass 里面添加 Test Case
            self.testRunModel['customFields'][2]['values'][0].append(Field_Values(1000001 + indx , "Test Case", [testcase.__dict__], Field_Type.ChoiceFieldValue).__dict__)
        # print(self.testRunModel['customFields'][1])


    def update_versions(self,versions_dict):
        """

        Args:
            versions_dict:

        Returns:

        """

        self.testRunModel["versions"].append(Value_Id(**versions_dict).__dict__)


class TestCaseReference:
    def __init__(self, testcase,result,incidentid_list):
        self.testCaseReference = testcase.__dict__
        self.result = result
        self.reportedBugReferences = []
        self.customFields = [Field_Values(1000000, "Test Cases", [[]], Field_Type.TableFieldValue).__dict__]
        self.customFields[0]['values'][0].append(Field_Values(1000001  , "Test Case", [testcase.__dict__], Field_Type.ChoiceFieldValue).__dict__)

        if len(incidentid_list) == 0:
            pass
        else:
            incidentid_obj_list = [IncidentId(incidentid).__dict__ for incidentid in incidentid_list]
            self.reportedBugReferences.extend(incidentid_obj_list)

class Put_TestRun_Body:

    def __init__(self,TestCaseReferences):
        self.updateRequestModels = [testcase_reference.__dict__ for testcase_reference in TestCaseReferences]
        self.parentResultPropagation = Value_Mapping.true


def obj_to_dict(obj):
    """
     将一个对象转换为字典，必须考虑对象里面的元素是对象的场景，这种情况下__dict__是无法转换的
    Args:
        obj:

    Returns:
        obj_dict
    """

    # if "__dict__" in dir(obj):  # 判定是否可以转换为字典。否则原值返回
    #     obj_dict = obj.__dict__
    #     # 如果__dict__的属性，则遍历相关数据
    #     for key in obj_dict:
    #         # print(key,obj_dict[key])
    #         if isinstance(obj_dict[key],dict): # 如果里面的元素是字典，则继续遍历
    #             # print("dict")
    #             for subkey in obj_dict[key]:
    #                 obj_dict[key][subkey] = obj_to_dict(obj_dict[key][subkey])
    #         elif isinstance(obj_dict[key],list) : # 如果是对象 且是对象的数组
    #             # print("list obj")
    #             for indx,element in enumerate(obj_dict[key]):
    #                 # print(obj_dict[key][indx].__dict__)
    #                 obj_dict[key][indx] = obj_to_dict(obj_dict[key][indx])
    #                 # pass
    #         elif isinstance(obj_dict[key],object): # 如果仅仅是一个对象
    #
    #             # print("obj")
    #             # print(obj_dict[key])
    #             obj_dict[key] = obj_to_dict(obj_dict[key])
    #         else: # 如果即不是字典，也不是 对象，也不是list，则是其他类型，继续遍历
    #             continue
    # elif isinstance(obj, list):  # 是否是数组，则判断数组里面元素是否是对象或者字典
    #     for indx, element in enumerate(obj):
    #         # print(obj_dict[key][indx].__dict__)
    #         obj = obj_to_dict(obj)
    #         # pass
    # else:
    #     return obj

    return  obj.__dict__




if __name__ == "__main__":
    status = Field()
    # a = Value_Id(0,2,3)
    a = Field_Values(1000000, "Test Cases", [[]], Field_Type.ChoiceFieldValue)
    a.values[0].append(Field_Values(1000000, "Test Case", [status], Field_Type.ChoiceFieldValue))
    # if "__dict__" in dir(a):
    #     print(a)

    # testcase = TestCase_In_TestRun(0,"A")
    testcases = [TestCase_In_TestRun(0,"A"),TestCase_In_TestRun(1,"B")]
    name = "Test Run"
    tracker = 10574133
    test_information = "ARiA4.11"
    testrun = TestRunMoel(name,tracker,test_information)
    TestRunMoel.update_test_inforamtion_id(1223)
    print(testrun.__dict__)
    Post_TestRun = Post_TestRun_Body(testcases,name,tracker,test_information)
    print(Post_TestRun.__dict__)
