from CB_Server_API.Abstract import *

# @dataclass
# class TestCase_In_TestRun(AbstractReference):
#     # referenceData:ReferenceData = ReferenceData("DO_NOT_PROPAGATE")
#     # type: str = AbstractReference_Type.TrackerItemReference

@dataclass
class TestCase_In_TestRun(TrackerItemReference):
    pass

@dataclass
class TestRun_Status(ChoiceOptionReference):
    id: int = 1
    def __post_init__(self):
        if self.id == 1:
            self.name = "In progress"
        elif self.id == 2:
            self.name = "Suspended"
        elif self.id == 4:
            self.name = "Finished"
        elif self.id == 5:
            self.name = "Closed"
        elif self.id == 6:
            self.name = "To be approved"
        elif self.id == 7:
            self.name = "Ready for execution"
        elif self.id == 8:
            self.name = "Rejected"
        else:
            raise Exception("No test mothod defind for index " + str(self.id))

@dataclass
class IncidentId(AbstractReference):
    type:str = "TrackerItemReference"

@dataclass
class TestRunModel:
    name:str = None
    descriptionFormat : str="Wiki"
    tracker:TrackerReference = TrackerReference(0)
    customFields: List[Any] = field(default_factory=list)
    status:TestRun_Status=TestRun_Status(7)
    versions :List[AbstractReference] = field(default_factory=list)
    formality = ChoiceOptionReference(1, "Regular")
    typeName:str = "Testrun"

    def update_test_case(self,testcases:list):
        self.customFields.append(TableFieldValue(1000000, "Test Cases", [[]]))
        test_cases_indx = len( self.customFields) - 1
        for indx,testcase in enumerate(testcases):
            self.customFields[test_cases_indx].values[0].append(ChoiceFieldValue(1000001 + indx,"Test Case",[testcase]))

    def update_test_information(self,test_information_id, test_information):
        if test_information_id == None:
            pass
        else:
            test_infomation_filed = TextFieldValue(test_information_id,"Test Information",test_information)
            self.customFields.append(test_infomation_filed)

    def update_working_set(self,working_set_id,working_set_dict):
        if working_set_id == None:
            pass
        else:
            working_set_field= ChoiceFieldValue(fieldId=working_set_id, name="Working Set",values=[ChoiceOptionReference(**working_set_dict)])
            self.customFields.append(working_set_field)

    def update_versions(self, versions_dict):
        """
        Args:
            versions_dict:
        Returns:
        """
        self.versions.append(AbstractReference(**versions_dict))

@dataclass
class Post_TestRun_Body:
    testCaseIds:list[TestCase_In_TestRun] = field(default_factory=list)
    testRunModel:TestRunModel = TestRunModel()

@dataclass
class Restart_TestRun_Body:
    name: str = None
    descriptionFormat: str = "Wiki"
    customFields: List[Any] = field(default_factory=list)
    status: TestRun_Status = TestRun_Status(1)
    versions: List[AbstractReference] = field(default_factory=list)
    formality = ChoiceOptionReference(1, "Regular")
    typeName: str = "Testrun"


    def update_test_information(self, test_information_id, test_information):
        if test_information_id == None:
            pass
        else:
            test_infomation_filed = TextFieldValue(test_information_id, "Test Information", test_information)
            self.customFields.append(test_infomation_filed)

    def update_working_set(self, working_set_id, working_set_dict):
        if working_set_id == None:
            pass
        else:
            working_set_field = ChoiceFieldValue(fieldId=working_set_id, name="Working Set",
                                                 values=[ChoiceOptionReference(**working_set_dict)])
            self.customFields.append(working_set_field)

    def update_versions(self, versions_dict):
        """
        Args:
            versions_dict:
        Returns:
        """
        self.versions.append(AbstractReference(**versions_dict))

@dataclass
class TestCaseReference:
    testCaseReference:TestCase_In_TestRun = TestCase_In_TestRun(0)
    result:str = None
    reportedBugReferences :List[Any] = field(default_factory=list)
    customFields: List[Any] = field(default_factory=list)

    def __post_init__(self):
        self.customFields.append(TableFieldValue(1000000, "Test Cases", [[]]))
        self.customFields[0].values[0].append(ChoiceFieldValue(1000001  , "Test Case", [self.testCaseReference]))
    def update_incidents(self,ids):
        if len(ids) == 0:
            pass
        else:
            incidents = [IncidentId(id) for id in ids]
            self.reportedBugReferences.extend(incidents)

@dataclass
class Put_TestRun_Body:
    updateRequestModels:List[TestCaseReference] = field(default_factory=list)
    parentResultPropagation:bool=True

if __name__ == "__main__":
    versions_dict =  {
      "id": 5240610,
      "name": "CHERY_T26&M1E_Release P10",
      "type": "TrackerItemReference"
    }
    testcase_ids = [21867362, 21867350]
    test_status = ["PASSED","PASSED"]
    incidents = [[25333086,26022438],[]]
    # testcases = [TestCase_In_TestRun(id) for id in testcase_ids]
    # testrun = TestRunModel(name = "TestRun for victor",tracker = TrackerReference(id =10574133))
    # testrun.update_test_case(testcases)
    # testrun.update_versions(versions_dict)
    # testrun.update_test_information(10003, "Test")
    # create_testrun_body = Post_TestRun_Body(testcases,testrun)

    testcaseRferences = []
    for indx,id in enumerate(testcase_ids):
        testcaseRference = TestCaseReference(testCaseReference = TestCase_In_TestRun(id),result = test_status[indx])
        testcaseRference.update_incidents(incidents[indx])
        testcaseRferences.append(testcaseRference)

    update_testrun_body = Put_TestRun_Body(updateRequestModels = testcaseRferences)
    print(to_json(update_testrun_body))