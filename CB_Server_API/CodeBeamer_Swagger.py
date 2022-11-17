


"""
# 服务器
Server


方法
1. 通过Release字符串获取Release的字典对象，
2. 通过folder ID 获取下面所有的case 字典列表

工具属性


用户属性
User
Pwd

用户方法
get
post
put

工具
属性
Spec，
Result
TestCaseTrackerID
TestCaseFolderID
TestRunTrackerID


"""
import numpy as np

from CB_Server_API.Request_Body import *
import pandas as pd
import requests
import time
import datetime
from urllib3.exceptions import InsecureRequestWarning
from CB_Server_API.HandlePTCExcel import *
def get_check_resp(curl,resp):

    """
    根据status code 去判断除了啥问题，如果没问题，则返回json数据
    Args:
        curl: request的url
        resp: request

    Returns:
    """
    #####Note 后面考虑对异常的数据回复，根据curl和json数据dump 到本地作为时候分析的数据
    if resp.status_code != 200:
        if resp.status_code == 401:
            print(resp)
            raise Exception(f"Access denied code 401 when execute curl::{curl}")
        elif resp.status_code == 400:
            print(resp)
            raise Exception(f"Method not allowed code 400 when execute curl::{curl}")
        elif resp.status_code == 404:
            print(resp)
            raise Exception(f"Item not found code 404 when execute curl::{curl}")
        elif resp.status_code == 405:
            print(resp)
            raise Exception(f"Method not allowed code 405 when execute curl::{curl}")
        else:
            raise Exception(f"unknow error code {resp.status_code} when execute curl:{curl}" )
    # print(resp.status_code)

    return resp

def measure_execution_time(function):
    def wrapper(*args, **kwargs):
        return_value = None
        start = time.time()
        print(start)
        try:
            return_value = function(*args, **kwargs)
        except Exception as e:
            raise Exception(e)
        end = time.time()
        print(end)
        print("Execution time: ", end - start, "s")
        return return_value

    return wrapper

class User:
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    login = (0,0)
    # def __init__(self, login, rest):
    #     requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    #     self.login = login
    #     self.rest = rest

    @classmethod
    def get(cls, curl):
        resp = requests.get(curl, auth=cls.login, verify=False)

        return get_check_resp(curl,resp)

    @classmethod
    def put(cls, curl, json):
        resp = requests.put(curl, data=json, auth=cls.login, verify=False)
        return get_check_resp(curl, resp)

    @classmethod
    def post(cls, curl, json):
        resp = requests.post(curl, json=json, auth=cls.login, verify=False)
        return get_check_resp(curl, resp)


class CodeBeamer():


    def __init__(self,server,user,pwd ):
        self.server = server
        self.login = (user,pwd)

    def get(self, curl):
        resp = requests.get(curl, auth=self.login, verify=False)

        return get_check_resp(curl,resp)


    def put(self, curl, json):
        resp = requests.put(curl, auth=self.login, verify=False, json=json)
        return get_check_resp(curl, resp)


    def post(self, curl, json):
        resp = requests.post(curl, auth=self.login, verify=False, json=json)
        return get_check_resp(curl, resp)

    def update_codebeamer(self,server,user,pwd):
        self.server = server
        self.login = (user,pwd)


    def get_release(self,testcase_trackerid,release):
        """

        Args:
            testcase_trackerid:
            release: 如下的一个字典
             {
              "id": 5240610,
              "name": "CHERY_T26&M1E_Release P10",
              "type": "TrackerItemReference",
              "referenceData": {
                "suspectPropagation": null
              }
        Returns:

        """
        print("#####################get release dict")

        #先通过Tracker id获取project的id
        curl = self.server + f"/trackers/{testcase_trackerid}/"
        resp_json = self.get(curl).json()
        project_id = resp_json["project"]["id"]

        #然后通过上面获取的projectid 获取release的id
        curl = self.server + f"/projects/{project_id}/trackers"
        resp_list = self.get(curl).json() # 返回的书一个数组

        release_trackerid = 0
        for child in resp_list:
            if child["name"] == "Releases":
                release_trackerid = child["id"]
        if release_trackerid ==0:
            raise Exception("Can't find Tracker Release in curl" + curl)

        # 再通过release_trackerid 获取对应的release
        curl = self.server + f"/trackers/{release_trackerid}/children?page=1&pageSize=500"
        resp_json = self.get(curl).json()

        if release in [child["name"] for child in resp_json["itemRefs"]]:
            for child in resp_json["itemRefs"]:
                if child["name"] == release:
                    print(child)
                    return child
        else:
            raise  Exception("Release name is not correct")

    def get_testcase_infolder(self,testcase_folderid):
        print("#####################get_testcase_infolder")
        """

        Returns:
            下列格式字典的数组
         {
              "id": 19997581,
              "name": "Test Case  - Latest Body Modify",
              "type": "TrackerItemReference"
            },
        """
        # 'https://codebeamer.corp.int/cb/api/v3/items/19993113/children?page=1&pageSize=25'
        curl = self.server + f"/items/{testcase_folderid}/children?page=1&pageSize=500"
        resp_json = self.get(curl).json()
        print(resp_json["itemRefs"])

        # df = pd.DataFrame(np.array(resp_json["itemRefs"]),columns=['id','name','type'])
        # print(df)
        return resp_json["itemRefs"]


    """
    对case的内容分成三个函数处理，
    当没有id的时候，create
    当有id，status不为Obsolete的时候，为update
    当有id，但是status为Obsolte的，为delete
    """

    def create_newcase_tocb(self,testcase_trackerid,testcase_folderid,release_dict,pandas_series):
        """
        根据testcase 是否有id 去判断调用对应的函数，当没有id的时候表示是新的case
        Args:
            testcase_trackerid:
            testcase_folderid:
            release_dict: get_release(self,testcase_trackerid,release)
            pandas_series: 从HandlerPTCExcel 里面的generate_cb_case 函数获取的df
                 index为   ["id", "name", "status", "Verifies", "Incident ID", "Test Method"]

        Returns:

        """
        # 'https://codebeamer.corp.int/cb/api/v3/trackers/10574131/items?parentItemId=19993113'

        curl = self.server + f"/trackers/{testcase_trackerid}/items?parentItemId={testcase_folderid}"
        print("##############create_newcase_tocb " + pandas_series["name"])
        testcase_obj = Post_TestCase_Body(pandas_series["name"])
        # testcase_obj.update_incidentid(pandas_series["Incident ID"])
        # print()
        testcase_obj.update_verifies(pandas_series["Verifies"])
        # print(pandas_series["Test Method"])
        testcase_obj.update_testmethod(pandas_series["Test Method"])
        testcase_obj.update_versions(release_dict)
        request_body = obj_to_dict(testcase_obj)
        print(request_body)
        resp = self.post(curl,request_body)
        print(resp.json())
        return resp

    def update_cb_testcase(self, release_dict, pandas_series):
        """

        Args:
            release_dict: get_release(self,testcase_trackerid,release)
            pandas_series: 从HandlerPTCExcel 里面的generate_cb_case 函数获取的df
                 index为   ["id", "name", "status", "Verifies", "Incident ID", "Test Method"]

        Returns:

        """
        # put 'https://codebeamer.corp.int/cb/api/v3/items/19758493'
        print("##############update_cb_testcase " + pandas_series["name"])
        itemid = pandas_series['id']
        curl = self.server + f"/items/{itemid}"
        testcase_obj = Post_TestCase_Body(pandas_series["name"])
        # testcase_obj.update_incidentid(pandas_series["Incident ID"])
        testcase_obj.update_verifies(pandas_series["Verifies"])
        testcase_obj.update_testmethod(pandas_series["Test Method"])
        testcase_obj.update_versions(release_dict)
        request_body = obj_to_dict(testcase_obj)

        print(request_body)
        resp = self.put(curl, request_body)
        return resp

    def delete_cb_testcase(self,release_dict,pandas_series):
        """
        将status 更新为obsolte，但是这种情况下，其他属性也会被删除
        Args:
            release_dict: get_release(self,testcase_trackerid,release)
            pandas_series: 从HandlerPTCExcel 里面的generate_cb_case 函数获取的df
                 index为   ["id", "name", "status", "Verifies", "Incident ID", "Test Method"]

        Returns:

        """
        # put 'https://codebeamer.corp.int/cb/api/v3/items/19758493'
        print("##############delete_cb_testcase " + pandas_series["name"])
        itemid = pandas_series['id']
        curl = self.server + f"/items/{itemid}"
        testcase_obj = Post_TestCase_Body(pandas_series["name"])
        testcase_obj.update_versions(release_dict)
        testcase_obj.delete_testcase()
        request_body = obj_to_dict(testcase_obj)
        # request_body.pop("customFields")
        print(request_body)
        resp = self.put(curl,request_body)
        return resp

    def upload_testcases(self,df_cbcase,testcase_trackerid,testcase_folderid,release_dict):
        # Spec = r"C:\Users\victor.yang\Desktop\Work\CB\SpecTemplate\CHT_SWV_Project_FunctionName_Test Specification_Template_SC3.xlsm"
        #
        # df_ptc, excel_info = read_table_of_content(Spec)
        # testcase_dict_list = Cb.get_testcase_infolder(excel_info["TestCaseFolderID"])
        # df_ptc = generate_cb_case(df_ptc, testcase_dict_list)
        # # excel_info["Result_Summary"]= df_ptc.iloc[0, 4]
        # # excel_info["TestRunTrackerID"] = df_ptc.iloc[1, 4]
        # # excel_info["TestCaseTrackerID"] = df_ptc.iloc[2, 4]
        # # excel_info["TestCaseFolderID"] = df_ptc.iloc[3, 4]
        # # excel_info["Release"] = df_ptc.iloc[4, 4]
        # release_dict = Cb.get_release(excel_info["TestCaseTrackerID"], excel_info["Release"])
        for indx in df_cbcase.index:
            if df_cbcase.loc[indx, "id"] == "":
                self.create_newcase_tocb(testcase_trackerid, testcase_folderid, release_dict,
                                       df_cbcase.loc[indx])
            elif df_cbcase.loc[indx, "id"] != "" and df_cbcase.loc[indx, "status"] == "Obsolete":
                self.delete_cb_testcase(release_dict, df_cbcase.loc[indx])
            else:
                self.update_cb_testcase(release_dict, df_cbcase.loc[indx])
    def create_test_run_baseon_testcases(self,df_cbcase,testrun_trackerid,name,test_information,release_dict):
        """

        Args:
            df_cbcase:
            testrun_trackerid:
            name:
            test_information:
            release_dict:

        Returns:
            AAU的TestRun ID
        """
        #
        print("##########create_test_run_baseon_testcases")
        if True in df_cbcase["id"].isin([""]).values:
            raise Exception("create_test_run_baseon_testcases found new case which not been update to test cases tracker")


        #抓取结果为pass和failed 的case。仅仅用这个部分上传testcase
        df_result = df_cbcase.loc[df_cbcase["status"].isin(["PASSED","FAILED"]) , ['id', 'name']]
        print(df_result)
        result_list = [list(df_result.loc[x].values) for x in df_result.index]
        testcases_in_testrun = [TestCase_In_TestRun(*x) for x in result_list]

        curl = self.server + f"/trackers/{testrun_trackerid}/testruns"
        # testcases, name, tracker, test_information
        current_time = str(datetime.date.today()).replace("-","_")
        name = f"{name}_{current_time}"
        testrun_obj = Post_TestRun_Body(testcases_in_testrun,name, testrun_trackerid, test_information)
        testrun_obj.update_versions(release_dict)

        request_body = obj_to_dict(testrun_obj)
        # print(testrun_obj.testRunModel.customFields[2].values)
        print(request_body)
        resp = self.post(curl, request_body)
        print(resp.json())
        return resp.json()["id"]



    def update_test_run_result(self,df_cbcase,testrun_id):
        print("##########update_test_run_result")
        if True in df_cbcase["id"].isin([""]).values:
            raise Exception("update_test_run_result testcases found new case which not been update to test cases tracker")

        # 抓取结果为pass和failed 的case。仅仅用这个部分上传testcase
        # ["id", "name", "status", "Verifies", "Incident ID", "Test Method"]
        df_result = df_cbcase.loc[df_cbcase["status"].isin(["PASSED", "FAILED"]), ['id', 'name','status',"Incident ID"]]

        testCase_references = []
        # TestCaseReference testcase,result,incidentid_list
        # Put_TestRun_Body TestCaseReferences
        for indx in df_result.index:
            testCase_references.append(TestCaseReference(TestCase_In_TestRun(df_result.loc[indx,'id'],df_result.loc[indx,'name']),
                                        df_result.loc[indx, 'status'],df_result.loc[indx, 'Incident ID']
                                       ))
        put_test_run = Put_TestRun_Body(testCase_references)
        request_body = obj_to_dict(put_test_run)
        print(request_body)
        # print(put_test_run)
        # curl - X
        # 'PUT' \
        # 'https://codebeamer.corp.int/cb/api/v3/testruns/20165626' \
        curl = self.server + f"/testruns/{testrun_id}"
        resp = self.put(curl,request_body)
        print(resp.json())



if __name__ == "__main__":
    pass
    # User.login = ("victor.yang","Mate40@VY20082021")
    # Cb = CodeBeamer("https://codebeamer.corp.int/cb/api/v3","victor.yang","Mate40@VY20082021")
    # # Cb = CodeBeamer("https://codebeamer.corp.int/cb/api/v3", 10574131, 20108756, 10574133)
    # testcase_folderid = 19993113
    # testcase_trackerid = 10574131
    # testrun_trackerid = 10574133
    # # Cb.get_release_id("CHERY_T26&M1E_Release P10")
    # # Cb.get_release_id("CHERY_T26&M1E_Release P10")
    #
    #
    # Spec = r"C:\Users\victor.yang\Desktop\Work\CB\SpecTemplate\CHT_SWV_Project_FunctionName_Test Specification_Template_SC3.xlsm"
    #
    # df_ptc, excel_info = read_table_of_content(Spec)
    # testcase_dict_list = Cb.get_testcase_infolder(excel_info["testcase_folderid"])
    # df_cbcase = generate_cb_case(df_ptc,testcase_dict_list)
    # # excel_info["Result_Summary"]= df_ptc.iloc[0, 4]
    # # excel_info["TestRunTrackerID"] = df_ptc.iloc[1, 4]
    # # excel_info["TestCaseTrackerID"] = df_ptc.iloc[2, 4]
    # # excel_info["TestCaseFolderID"] = df_ptc.iloc[3, 4]
    # # excel_info["Release"] = df_ptc.iloc[4, 4]
    # #excel_info["AAU"]
    # release_dict =  Cb.get_release(excel_info["testcase_trackerid"],excel_info["release"])
    # # df_cbcase, testrun_trackerid, name, test_information, release_dict
    # name = excel_info["AAU"]
    # test_information = excel_info["test_information"]
    # # testrun_id = Cb.create_test_run_baseon_testcases(df_cbcase, testrun_trackerid, name, test_information, release_dict)
    # testrun_id = 20173215
    # Cb.update_test_run_result(df_cbcase, testrun_id)
    # for indx in df_ptc.index:
    #     if df_ptc.loc[indx,"id"] == "":
    #         Cb.create_newcase_tocb(excel_info["TestCaseTrackerID"],excel_info["TestCaseFolderID"],release_dict,df_ptc.loc[indx])
    #     elif df_ptc.loc[indx,"id"] != "" and df_ptc.loc[indx,"status"] == "Obsolete":
    #         print("del")
    #         Cb.delete_cb_testcase(release_dict,df_ptc.loc[indx])
    #     else:
    #         print(time.time())
    #         Cb.update_cb_testcase(release_dict, df_ptc.loc[indx])
    #         print(time.time())
            # print(3)
            # print(df_ptc.loc[indx])

