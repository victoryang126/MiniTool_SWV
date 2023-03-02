from CB_Server_API.Abstract import  *




@dataclass
class TestMethod(ChoiceOptionReference):
    id:int = 0
    def __post_init__(self):
        if self.id == 0:
            self.name = "Unset"
        elif self.id == 1:
            self.name = "Others"
        elif self.id == 2:
            self.name = "Fault Injection"
        elif self.id == 3:
            self.name = "Internal External Interfaces"
        elif self.id == 4:
            self.name = "Statement Coverage"
        elif self.id == 5:
            self.name = "Requirement Based"
        elif self.id == 6:
            self.name =  "Analysis Of Functional Dependencies"
        elif self.id == 7:
            self.name = "Boundary Value Analysis"
        elif self.id == 8:
            self.name = "Environmental Conditions Or Use Case"
        elif self.id == 9:
            self.name = "Equivalence Classes"
        elif self.id == 10:
            self.name = "Error Guessing"
        elif self.id == 11:
            self.name = "Control Flow"
        elif self.id == 12:
            self.name = "Common Limit Conditions Or Sequences Or Sources Of Dependent Failures"
        else:
            raise Exception("No test mothod defind for index " + str(self.id))

@dataclass
class TestCaseStatus(ChoiceOptionReference):
    id:int = 1
    def __post_init__(self):
        if self.id == 1:
            self.name = "Init"
        elif self.id == 6:
            self.name = "Obsolete"
        else:
            raise Exception("No test case status for id " + str(self.id))

@dataclass
class Post_TestCase_Body:

    name:str
    descriptionFormat:str = "Wiki"
    customFields: List[Any] = field(default_factory=list)
    # customFields:List[Field_Values] = field(default_factory=
    #    [ ChoiceFieldValue(fieldId=17, name= "Verifies", type= "ChoiceFieldValue"),
    #     ChoiceOptionReference(fieldId=1035,name= "Test Method",type= "ChoiceFieldValue")]
    # )
    status:TestCaseStatus = TestCaseStatus()
    versions:List[AbstractReference] = field(default_factory=list)
    typeName:str =  "Testcase"

    def update_verifies(self,ids:list):
        self.customFields.append(ChoiceFieldValue(fieldId=17, name= "Verifies"))
        if len(ids) == 0:
            pass
        else:
            verifies = [TrackerItemReference(id= id) for id in ids]
            self.customFields[len(self.customFields) -1].values.extend(verifies)

    def update_test_method(self,test_method_id,ids:list):
        if test_method_id == None or len(ids) == 0 :
            pass
        else:
            self.customFields.append(ChoiceFieldValue(fieldId=test_method_id, name="Test Method"))
            test_methods = [TestMethod(id) for id in ids]
            self.customFields[len(self.customFields) -1].values.extend(test_methods)

    def update_versions(self, versions_dict):
        """
        Args:
            versions_dict:
        Returns:
        """
        self.versions.append(TrackerItemReference(**versions_dict))

    def delete_testcase(self):
        """
        customFields 设置为空，即不更新里面的数据，保持原来 数据
        Returns:
        None
        """
        self.status = TestCaseStatus(6)

if __name__ == "__main__":
    test_case_body = Post_TestCase_Body("Test DD")
    test_case_body.update_verifies([5488309,5491869])
    test_case_body.update_test_method(1035,[2,5])
    versions_dict =  {
      "id": 5240610,
      "name": "CHERY_T26&M1E_Release P10",
      "type": "TrackerItemReference"
    }
    test_case_body.update_versions(versions_dict)
    # print(versions_dict)
    # a = TrackerItemReference(**versions_dict)
    # print(to_json(a))
    print(to_json(test_case_body))