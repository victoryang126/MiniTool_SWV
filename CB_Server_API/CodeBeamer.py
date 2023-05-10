


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
from Util.LogCFG import *
from CB_Server_API.TestRun import *
from CB_Server_API.TestCase import *
import pandas as pd
import requests
import time
import datetime
from urllib3.exceptions import InsecureRequestWarning
from CB_Server_API.HandlePTCExcel import *

def get_check_resp(resp):

    """
    根据status code 去判断出了啥问题，如果没问题，则返回json数据
    Args:
        resp: request的回复

    Returns:
    """
    #####Note 后面考虑对异常的数据回复，根据curl和json数据dump 到本地作为时候分析的数据
    if resp.status_code != 200:
        if resp.status_code == 401:
            raise Exception(f"Access denied code 401 when execute url::{resp.url} ::{resp.text}")
        elif resp.status_code == 400:
            raise Exception(f"Method not allowed code 400 when execute url::{resp.url}::{resp.text}")
        elif resp.status_code == 404:
            raise Exception(f"Item not found code 404 when execute url::{resp.url}::{resp.text}")
        elif resp.status_code == 405:
            raise Exception(f"Method not allowed code 405 when execute url::{resp.url}::{resp.text}")
        else:
            raise Exception(f"unknow error code {resp.status_code} when execute url:{resp.url}::{resp.text}")
    return resp

def is_nan(value):
    if isinstance(value,float):
        if np.isnan(value):
            return True
        else:
            return False
    else:
        return False

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



class CodeBeamer():
    def __init__(self,server,user,pwd ):
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        self.server = server
        self.login = (user,pwd)

    def get(self, url):
        Debug_Logger.debug(f'get url:{url}')
        resp = requests.get(url, auth=self.login, verify=False)
        return get_check_resp(resp)

    def put(self, url, json):
        Debug_Logger.debug(f'put url:{url}  \njson\n:{json}')
        resp = requests.put(url, auth=self.login, verify=False, json=json)
        return get_check_resp(resp)

    def post(self, url, json):
        Debug_Logger.debug(f'post url:{url}  \njson\n:{json}')
        resp = requests.post(url, auth=self.login, verify=False, json=json)
        return get_check_resp(resp)

    def update_codebeamer(self,server,user,pwd):
        self.server = server
        self.login = (user,pwd)

    @func_monitor
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


        #先通过Tracker id获取project的id
        url = self.server + f"/trackers/{testcase_trackerid}/"
        resp_json = self.get(url).json()
        project_id = resp_json["project"]["id"]

        #然后通过上面获取的projectid 获取release的id
        url = self.server + f"/projects/{project_id}/trackers"
        resp_list = self.get(url).json() # 返回的书一个数组

        release_trackerid = 0
        for child in resp_list:
            if child["name"] == "Releases":
                release_trackerid = child["id"]
        if release_trackerid ==0:
            raise Exception("Can't find Tracker Release in url" + url)

        # 再通过release_trackerid 获取对应的release
        url = self.server + f"/trackers/{release_trackerid}/children?page=1&pageSize=500"
        resp_json = self.get(url).json()

        if release in [child["name"] for child in resp_json["itemRefs"]]:
            for child in resp_json["itemRefs"]:
                if child["name"] == release:
                    return child
        else:
            raise  Exception("Release name is not correct")

    @func_monitor
    def get_testcase_infolder(self,testcase_folderid):
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
        url = self.server + f"/items/{testcase_folderid}/children?page=1&pageSize=500"
        resp_json = self.get(url).json()
        return resp_json["itemRefs"]

    @func_monitor
    def get_data_from_item(self,itemid):
        #https://codebeamer.corp.int/cb/api/v3/items/20451445
        url = self.server + f"/items/{itemid}"
        resp = self.get(url)
        return resp

    @func_monitor
    def get_verfies_testmethod(self,itemid,test_method_id):
        resp = self.get_data_from_item(itemid)
        testmethod_dict = {}
        customFileds = resp.json()["customFields"]

        for fields in customFileds:
            if fields["fieldId"] == test_method_id:
                testmethod_dict = fields
                # {'fieldId': 1035, 'name': 'Test Method',
                #  'values': [{'id': 1, 'name': 'Others', 'type': 'ChoiceOptionReference'}], 'type': 'ChoiceFieldValue'}
                # print(testmethod_dict)

        if len(resp.json()["subjects"]) == 0: # 如果原来的case 里面就是为空的，则返回空数组
            verifies = []
        else:
            verifies = [verify["id"] for verify in resp.json()["subjects"] ]

        if len(testmethod_dict.keys()) == 0: # 如果没有testmethod的属性返回，说明为空
            testmethods = []
        else:
            testmethods = [testmethod['id'] for testmethod in testmethod_dict["values"]]
        #统一规则，返回Test Method的ID数组和Verifies的数组

        return testmethods,verifies

    @func_monitor
    def get_test_case_status(self,itemid):
        resp = self.get_data_from_item(itemid)
        return resp.json()["status"]['id']

    @func_monitor
    def get_tracker_fileds(self,trackerid):
        """
        用于获取Tracker 下面的filed等相关属性。类似下面元素的列表
         {
        "id": 1000000,
        "name": "Test Steps",
        "type": "FieldReference",
        "trackerId": 14937781
      }
        Args:
            trackerid:

        Returns:

        """
        # 'https://codebeamer.corp.int/cb/api/v3/trackers/14937781/fields'
        url = self.server + f"/trackers/{trackerid}/fields"
        resp = self.get(url)
        return resp.json()

    @func_monitor
    def check_get_field_id(self,trackerid,field_name):
        """
        获取Tracker 下面的field，并判断是否存在相关field,主要用于检查Test Method和Test Information等相关信息
        因为这个部分存在与customefileds 里面，因为Tracker模板配置的问题，可能缺少相关属性，或者相关属性id和默认配置不一样
        Args:
            trackerid:
            field_name:
        Returns:
        """
        tracker_fields = self.get_tracker_fileds(trackerid)

        field_id_list = [field["id"] for field in tracker_fields if field["name"] == field_name]
        Debug_Logger.debug(f"field_name {field_name} fieldId: {str(field_id_list)}" )
        if len(field_id_list) == 0:
            return None # 如果没有Test Method的filed则返回None
            # raise Exception(f"{field_name} not exist in related tracker, please contact Milly du to ask system engineer update config")
        elif len(field_id_list) == 1:
            return field_id_list[0]
        else:
            raise Exception(
                f"{len(field_id_list)}  {field_name} exist in related tracker, please contact Milly du to ask system engineer update config")

    @func_monitor
    def get_tracker_field_options(self,trackerId,fieldId):
        if fieldId == None:
            return None
        else:
            url = self.server + f"/trackers/{trackerId}/fields/{fieldId}"
            resp = self.get(url)
            options = resp.json()["options"]
            return options

    @func_monitor
    def validate_and_return_field_option(self,defined_options,user_provide_option):
        option_list = [option for option in defined_options if option["name"] == user_provide_option]
        if len(option_list) == 0:
            raise Exception(
            f" {user_provide_option} not defiend the the CodeBeamer, please check the options in the tracker field ") # 如果没有Test Method的filed则返回None
                # raise Exception(f"{field_name} not exist in related tracker, please contact Milly du to ask system engineer update config")
        elif len(option_list) == 1:
            return option_list[0]
        else:
            raise Exception(
                f"{len(option_list)}  {user_provide_option} exist in related tracker, please contact Milly du to ask system engineer update config")


    """
    对case的内容分成三个函数处理，
    当没有id的时候，create
    当有id，status不为Obsolete的时候，为update
    当有id，但是status为Obsolte的，为delete
    """

    @func_monitor
    def create_newcase_tocb(self,testcase_trackerid,testcase_folderid,release_dict,pandas_series,test_method_id):
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

        url = self.server + f"/trackers/{testcase_trackerid}/items?parentItemId={testcase_folderid}"



        test_case_body = Post_TestCase_Body(pandas_series["name"])
        test_case_body.update_verifies(pandas_series["Verifies"])
        test_case_body.update_test_method(test_method_id,pandas_series["Test Method"])
        test_case_body.update_versions(release_dict)
        request_body = to_json(test_case_body)
        Debug_Logger.debug(request_body)
        resp = self.post(url,request_body)
        return resp

    @func_monitor
    def update_cb_testcase(self, release_dict, pandas_series,test_method_id):
        """

        Args:
            release_dict: get_release(self,testcase_trackerid,release)
            pandas_series: 从HandlerPTCExcel 里面的generate_cb_case 函数获取的df
                 index为   ["id", "name", "status", "Verifies", "Incident ID", "Test Method"]

        Returns:

        """
        # put 'https://codebeamer.corp.int/cb/api/v3/items/19758493'
        itemid = pandas_series['id']
        test_case_body = Post_TestCase_Body(pandas_series["name"])
        test_case_body.update_verifies(pandas_series["Verifies"])
        test_case_body.update_test_method(test_method_id,pandas_series["Test Method"])
        test_case_body.update_versions(release_dict)


        #2023/05/09
        #将test case的状态从服务器取出来，然后根据服务器里面的状态去更新case状态
        #当case状态再服务器是Obsolete的时候，不用更新2，需要用默认的状态init重置testcase
        #方便后续Run完testRun 以后更新test case status
        test_case_status_id = self.get_test_case_status(itemid)
        if test_case_status_id != 6:
            test_case_body.update_testcase_status_by_id(test_case_status_id)

        request_body = to_json(test_case_body)

        Debug_Logger.debug(request_body)
        url = self.server + f"/items/{itemid}"
        resp = self.put(url, request_body)
        return resp

    @func_monitor
    def update_cb_testcase_status(self, release_dict, pandas_series,test_method_id):
        """
        funtion used to update the status of test case
        2023/05/09 added
        Args:
            release_dict: get_release(self,testcase_trackerid,release)
            pandas_series: 从HandlerPTCExcel 里面的generate_cb_case 函数获取的df
                 index为   ["id", "name", "status", "Verifies", "Incident ID", "Test Method"]

        Returns:

        """
        # put 'https://codebeamer.corp.int/cb/api/v3/items/19758493'
        itemid = pandas_series['id']
        test_case_body = Post_TestCase_Body(pandas_series["name"])
        test_case_body.update_verifies(pandas_series["Verifies"])
        test_case_body.update_test_method(test_method_id,pandas_series["Test Method"])
        test_case_body.update_versions(release_dict)
        test_case_body.update_testcase_status(pandas_series["status"])
        request_body = to_json(test_case_body)

        Debug_Logger.debug(request_body)
        url = self.server + f"/items/{itemid}"
        resp = self.put(url, request_body)
        return resp

    @func_monitor
    def delete_cb_testcase(self,release_dict,pandas_series,test_method_id):
        """
        将status 更新为obsolte，但是这种情况下，其他属性也会被删除
        Args:
            release_dict: get_release(self,testcase_trackerid,release)
            pandas_series: 从HandlerPTCExcel 里面的generate_cb_case 函数获取的df
                 index为   ["id", "name", "status", "Verifies", "Incident ID", "Test Method"]

        Returns:

        """
        # put 'https://codebeamer.corp.int/cb/api/v3/items/19758493'
        itemid = pandas_series['id']
        url = self.server + f"/items/{itemid}"
        test_case_body = Post_TestCase_Body(pandas_series["name"])

        ######  2022/11/21新增加逻辑，当status为obsolete的时候，从服务器拉数据填充，否则会因为设置obsolete导致属性丢失
        testmethods, verifies = self.get_verfies_testmethod(itemid,test_method_id)
        test_case_body.update_verifies(verifies)
        test_case_body.update_test_method(test_method_id,testmethods)
        #######
        test_case_body.update_versions(release_dict)
        test_case_body.delete_testcase()
        request_body = to_json(test_case_body)
        # request_body.pop("customFields")
        Debug_Logger.debug(request_body)
        resp = self.put(url,request_body)
        return resp

    @func_monitor
    def upload_testcases(self,df_cbcase,testcase_trackerid,testcase_folderid,release_dict):

        test_method_id = self.check_get_field_id(testcase_trackerid, "Test Method")
        for indx in df_cbcase.index:
            if df_cbcase.loc[indx, "id"] == "":
                self.create_newcase_tocb(testcase_trackerid, testcase_folderid, release_dict,
                                       df_cbcase.loc[indx],test_method_id)
            elif df_cbcase.loc[indx, "id"] != "" and df_cbcase.loc[indx, "status"] == "Obsolete":
                self.delete_cb_testcase(release_dict, df_cbcase.loc[indx],test_method_id)
            else:
                self.update_cb_testcase(release_dict, df_cbcase.loc[indx],test_method_id)

    @func_monitor
    def upload_testcases_status(self,df_cbcase,testcase_trackerid,testcase_folderid,release_dict):


        test_method_id = self.check_get_field_id(testcase_trackerid, "Test Method")
        # 抓取结果为pass和failed 的case。仅仅用这个部分上传testcase
        df_result = df_cbcase.loc[df_cbcase["status"].isin(["PASSED", "FAILED"])]
        # Monitor_Logger.info(df_result)
        for indx in df_result.index:
            # if df_cbcase.loc[indx, "id"] == "":
            #     pass
            # elif df_cbcase.loc[indx, "id"] != "" and df_cbcase.loc[indx, "status"] == "Obsolete":
            #     pass
            #     # self.delete_cb_testcase(release_dict, df_cbcase.loc[indx],test_method_id)
            # else: #仅当有测试结果的case才去更新
            self.update_cb_testcase_status(release_dict, df_result.loc[indx],test_method_id)

    @func_monitor
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
        # working_set_id = self.check_get_field_id(testrun_trackerid, "Working Set")

        if True in df_cbcase["id"].isin([""]).values:
            Monitor_Logger.info(df_cbcase[["name","id"]])
            Debug_Logger.debug("Case Not been updated in to CB")
            Debug_Logger.debug(df_cbcase[["name","id"]])
            raise Exception("create_test_run_baseon_testcases found new case which not been update to test cases tracker")


        #抓取结果为pass和failed 的case。仅仅用这个部分上传testcase
        df_result = df_cbcase.loc[df_cbcase["status"].isin(["PASSED","FAILED"]) , ['id', 'name']]
        Debug_Logger.debug(f"df_result {df_result}")
        result_list = [list(df_result.loc[x].values) for x in df_result.index]


        Debug_Logger.debug(f"result_list {result_list}")
        url = self.server + f"/trackers/{testrun_trackerid}/testruns"
        current_time = str(datetime.date.today()).replace("-","_")
        name = f"{name}_{current_time}"



        #判断Test Information 是否存在，并赋值新的id
        testcases_in_testrun = [TestCase_In_TestRun(*x) for x in result_list]
        # testrun_model = TestRunModel(name = name,tracker = TrackerReference(id =testrun_trackerid))
        testrun_model = TestRunModel(tracker=TrackerReference(id=testrun_trackerid))
        test_information_id = self.check_get_field_id(testrun_trackerid, "Test Information")
        testrun_model.update_test_case(testcases_in_testrun)
        testrun_model.update_versions(release_dict)
        testrun_model.update_test_information(test_information_id, test_information)
        create_testrun_body = Post_TestRun_Body(testcases_in_testrun,testrun_model)



        request_body = to_json(create_testrun_body)
        Debug_Logger.debug(request_body)
        resp = self.post(url, request_body)
        return resp.json()["id"]

    @func_monitor
    def create_test_run_baseon_testcases_workingset(self,df_cbcase,testrun_trackerid,name,test_information,release_dict,working_set_name):
        """
        2023/3/3 added
        Args:
            df_cbcase:
            testrun_trackerid:
            name:
            test_information:
            release_dict:
            working_set: the working set name,add for smart project

        Returns:
            AAU的TestRun ID
        """
        #

        if True in df_cbcase["id"].isin([""]).values:
            Monitor_Logger.info(df_cbcase[["name", "id"]])
            Debug_Logger.debug("Case Not been updated in to CB")
            Debug_Logger.debug(df_cbcase[["name", "id"]])
            raise Exception("create_test_run_baseon_testcases found new case which not been update to test cases tracker")


        #抓取结果为pass和failed 的case。仅仅用这个部分上传testcase
        Monitor_Logger.info("get the case which have filled the test result pass or filled")
        Debug_Logger.debug("get the case which have filled the test result pass or filled")
        df_result = df_cbcase.loc[df_cbcase["status"].isin(["PASSED","FAILED"]) , ['id', 'name']]
        Debug_Logger.debug(f"df_result {df_result}")
        result_list = [list(df_result.loc[x].values) for x in df_result.index]
        Debug_Logger.debug(f"result_list {result_list}")




        url = self.server + f"/trackers/{testrun_trackerid}/testruns"
        # testcases, name, tracker, test_information
        current_time = str(datetime.date.today()).replace("-","_")
        name = f"{name}_{current_time}"


        #判断Test Information 是否存在，并赋值新的id
        testcases_in_testrun = [TestCase_In_TestRun(*x) for x in result_list]
        testrun_model = TestRunModel(name = name,tracker = TrackerReference(id =testrun_trackerid))
        # testrun_model = TestRunModel(tracker=TrackerReference(id=testrun_trackerid))
        test_information_id = self.check_get_field_id(testrun_trackerid, "Test Information")
        testrun_model.update_test_case(testcases_in_testrun)
        testrun_model.update_versions(release_dict)
        testrun_model.update_test_information(test_information_id, test_information)
        #2023/3/3 added
        if is_nan(working_set_name):
            pass
        else:
            working_set_id = self.check_get_field_id(testrun_trackerid, "Working Set")
            working_set_config_options = self.get_tracker_field_options(testrun_trackerid,working_set_id)
            working_set_option = self.validate_and_return_field_option(working_set_config_options,working_set_name)
            testrun_model.update_working_set(working_set_id,working_set_option)
        create_testrun_body = Post_TestRun_Body(testcases_in_testrun,testrun_model)



        request_body = to_json(create_testrun_body)
        Debug_Logger.debug(request_body)
        resp = self.post(url, request_body)
        return resp.json()["id"]


    @func_monitor
    def restart_test_run(self, testrun_trackerid, testrun_item_id, name, test_information, release_dict, working_set_name):
        """
        2023/3/3 added
        Args:
            df_cbcase:
            testrun_item_id:
            name:
            test_information:
            release_dict:
            working_set: the working set name,add for smart project

        Returns:
            AAU的TestRun ID
        """
        #





        url = self.server + f"/items/{testrun_item_id}"
        # testcases, name, tracker, test_information
        current_time = str(datetime.date.today()).replace("-","_")
        name = f"{name}_{current_time}"


        #判断Test Information 是否存在，并赋值新的id

        restart_testRun = Restart_TestRun_Body(name = name)
        test_information_id = self.check_get_field_id(testrun_trackerid, "Test Information")
        restart_testRun.update_versions(release_dict)
        restart_testRun.update_test_information(test_information_id, test_information)
        #2023/3/3 added
        if is_nan(working_set_name):
            pass
        else:
            working_set_id = self.check_get_field_id(testrun_trackerid, "Working Set")
            working_set_config_options = self.get_tracker_field_options(testrun_trackerid,working_set_id)
            working_set_option = self.validate_and_return_field_option(working_set_config_options,working_set_name)
            restart_testRun.update_working_set(working_set_id,working_set_option)

        request_body = to_json(restart_testRun)
        Debug_Logger.debug(request_body)
        resp = self.put(url, request_body)
        return resp.json()["id"]

    @func_monitor
    def update_test_run_result(self,df_cbcase,testrun_id):
        if True in df_cbcase["id"].isin([""]).values:
            raise Exception("update_test_run_result testcases found new case which not been update to test cases tracker")

        # 抓取结果为pass和failed 的case。仅仅用这个部分上传testcase
        # ["id", "name", "status", "Verifies", "Incident ID", "Test Method"]
        df_result = df_cbcase.loc[df_cbcase["status"].isin(["PASSED", "FAILED"]), ['id', 'name','status',"Incident ID"]]

        testcaseRferences = []
        for indx in df_result.index:
            testcaseRference = TestCaseReference(testCaseReference=TestCase_In_TestRun(df_result.loc[indx,'id'],df_result.loc[indx,'name']),
                                                 result=df_result.loc[indx, 'status'])
            testcaseRference.update_incidents(df_result.loc[indx, 'Incident ID'])
            testcaseRferences.append(testcaseRference)

        update_testrun_body = Put_TestRun_Body(updateRequestModels=testcaseRferences)


        request_body = to_json(update_testrun_body)
        Debug_Logger.debug(request_body)
        # url - X
        # 'PUT' \
        # 'https://codebeamer.corp.int/cb/api/v3/testruns/20165626' \
        url = self.server + f"/testruns/{testrun_id}"
        resp = self.put(url,request_body)






if __name__ == "__main__":
    pass

    Cb = CodeBeamer("https://codebeamer.corp.int/cb/api/v3","victor.yang","TTT")
    url = 'https://codebeamer.corp.int/cb/api/v3/items/26932821'

    # options = Cb.get_tracker_field_options(1908978,1000)
    json = {
"name":"TTA",
  "status": {
    "id": 7,
    "name": "In progress",
    "type": "ChoiceOptionReference"
  },
  "customFields": [
    {
      "fieldId": 1000,
      "name": "Working Set",
      "values": [
        {
          "id": 4,
          "name": "GEELY_GEEA2.0_G733P_FS11-A2",
          "type": "ChoiceOptionReference"
        }
      ],
      "type": "ChoiceFieldValue"
    },
    {
      "fieldId": 10003,
      "name": "Test Information",
      "value": "ARIA4.11",
      "type": "TextFieldValue"
    }
  ],
  "versions": [
    {
      "id": 21468139,
      "name": "Release_P31.11_Geely_HC11",
      "type": "TrackerItemReference"
    }
  ]
}
    Cb.put(url,json)
    # Cb.get_tracker_fileds(14937781)
    # Cb.get_verfies_testmethod(20451445)
    # Cb.get_verfies_testmethod(20108756)
