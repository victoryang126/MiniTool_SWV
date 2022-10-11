from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os
from CB_Tool_SC3 import HandleTestRun as HRun
import datetime



# 40804608
# 10574131

def LoginCodeBeamer(Url_Prefix,TrackerID,DownlaodPath):
    DownlaodPath = DownlaodPath.replace('/', '\\')
    options = webdriver.EdgeOptions()
    # print(CB_Spec_Folder)
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': DownlaodPath}
    options.add_experimental_option('prefs', prefs)
    url = Url_Prefix + TrackerID
    browser = webdriver.ChromiumEdge(options=options)
    browser.get(url)

    # 点击Login
    browser.find_element(by=By.NAME, value="saml").click()

    browser.implicitly_wait(30)
    time.sleep(1)
    return browser


def LoginCodeBeamer_WoPath(Url_Prefix,TrackerID):
    url = Url_Prefix + TrackerID
    browser = webdriver.ChromiumEdge()
    browser.get(url)
    # 点击Login
    browser.find_element(by=By.NAME, value="saml").click()
    browser.implicitly_wait(30)
    time.sleep(1)
    return browser

def LoginCodeBeamer_WorkingSet(Url_Prefix,TrackerID,WorkingSet,DownlaodPath):
    DownlaodPath = DownlaodPath.replace('/', '\\')
    options = webdriver.EdgeOptions()
    # print(CB_Spec_Folder)
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': DownlaodPath}
    options.add_experimental_option('prefs', prefs)
    url = Url_Prefix + TrackerID
    browser = webdriver.ChromiumEdge(options=options)
    browser.get(url)

    # 点击Login
    browser.find_element(by=By.NAME, value="saml").click()

    browser.implicitly_wait(30)

    # 选择workingset

    print("Click working set button")
    workingset_element = browser.find_element(by=By.XPATH,value="//button[@id='workingSetSelector_ms']")
    print(workingset_element)
    workingset_element.click()
    browser.implicitly_wait(10)
    try:
        target_workingset_element = browser.find_element(by=By.XPATH,value="//label[@title='" + WorkingSet + "']")
        target_workingset_element.click()
        print("Select working set finished")
    except Exception as err:
        raise Exception(WorkingSet + " not found")

    browser.implicitly_wait(30)
    return browser

def UploadSpec2CB(CaseTrackerID, CodeBeamer_Spec, CaseFolderID, InitCaseList):
    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)
    CodeBeamer_Upload_Url = "https://codebeamer.corp.int/cb/importIssue.spr?tracker_id=" + CaseTrackerID
    # CodeBeamer_Upload_Url = "https://codebeamer.corp.int/cb/tracker/10574131?view_id=-2"
    browser = webdriver.ChromiumEdge(options=options)
    browser.get(CodeBeamer_Upload_Url)
    browser.maximize_window()
    # 点击Login
    browser.find_element(by=By.NAME, value="saml").click()
    # browser.find_element(by=By.XPATH, value="//input[@title='SSL-Login']").click()
    # 等待进入页面以后拖拉需要上传的spec进去
    # time.sleep(10)
    # print(1)
    # print(CodeBeamer_Spec)

    browser.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(CodeBeamer_Spec)
    time.sleep(10)
    # Next
    browser.find_element(by=By.ID, value="_eventId_next").click()
    # Next
    #选择ID Mapping
    # print(1)
    id_slectorbutton= "//*[@id ='rawDataTable']/ tbody/tr[1]/th[2]/ button"
    browser.find_element(by=By.XPATH, value=id_slectorbutton).click()
    # print(2)

    # print(3)
    #查看下拉框菜单的内容
    ul_slector = "/ html / body / div[12] / ul"
    parent_elemnt = browser.find_element(by=By.XPATH, value=ul_slector)
    slection_list = parent_elemnt.find_element(by=By.XPATH, value=ul_slector).text.split("\n")
    # time.sleep(10)
    # print(slection_list)
    if "ID" in slection_list:
        print("find the ID selection")
        id_filter = "/ html / body / div[12] / div / div / input"
        #/html/body/div[12]/div/div/input
        #//input[@type='search']
        browser.find_element(by=By.XPATH, value=id_filter).send_keys("ID")
        id_slector = "//label/span[text()='ID']"
        parent_elemnt.find_element(by=By.XPATH, value=id_slector).click()
        # print(children_element)
    else:
        print("Can't find the ID")
        id_filter = "/ html / body / div[12] / div / div / input"
        browser.find_element(by=By.XPATH, value=id_filter).send_keys("ID")
        id_slector = "//label/span[text()='--']"
        parent_elemnt.find_element(by=By.XPATH, value=id_slector).click()

    # time.sleep(100)
    browser.find_element(by=By.NAME, value="_eventId_next").click()
    # Next
    browser.find_element(by=By.NAME, value="_eventId_next").click()
    # Finish
    time.sleep(10)
    browser.find_element(by=By.NAME, value="_eventId_next").click()
    # browser.implicitly_wait(10)
    time.sleep(10)
    # 判断是否有错误，如果错误，则停
    try:
        ErrorStatus = browser.find_element(by=By.CLASS_NAME, value="invalidfield").is_displayed()
        if ErrorStatus:
            print("Please check the error")
            # time.sleep(120)
            return False
    except Exception as err:
        print("Not exist Error")

    if len(InitCaseList) != 0:
        # 定位到即将拖入的folder
        print("Init Case will add to the case folder")
        CaseFolder_Filter = '//li[@id=\"' + CaseFolderID + '\"]'

        scroll_js_Top ="var q=document.documentElement.scrollTop=0"
        scroll_js_Down = "var q=document.documentElement.scrollTop=500"
        Action = ActionChains(browser)
        Action.key_down(Keys.SHIFT)  # 按住sheift
        for CaseName in InitCaseList:
            CaseName_Filter = '//li[@title=\"' + CaseName + '\"]'
            while True:
                try:
                    dragElement = browser.find_element(by=By.XPATH, value=CaseName_Filter)
                    print(CaseName)
                    Action.click(dragElement)
                    break;
                except Exception as err:
                    print(err)
                    browser.execute_script(scroll_js_Down)
                    continue;
                time.sleep(2)

        time.sleep(2)
        # print(1)
        # browser.execute_script(scroll_js_Top)
        time.sleep(10)
        while True:
            try:
                time.sleep(10)
                targetElement = browser.find_element(by=By.XPATH, value=CaseFolder_Filter)
                # print(targetElement)
                time.sleep(10)
                Action.drag_and_drop(dragElement, targetElement).perform()
                # print(33333)
                break;
            except Exception as err:
                print("Can't find folder")
                browser.execute_script(scroll_js_Down)
                time.sleep(2)
                continue;


        print(2)
    time.sleep(10)
    return True


def DragCaseItem2oFolder(CaseTrackerID, CaseFolderID, InitCaseList):
    CodeBeamer_Upload_Url = "https://codebeamer.corp.int/cb/tracker/" + CaseTrackerID
    # CodeBeamer_Upload_Url = "https://codebeamer.corp.int/cb/tracker/10574131?view_id=-2"
    browser = webdriver.ChromiumEdge()
    browser.get(CodeBeamer_Upload_Url)

    # 点击Login
    browser.find_element(by=By.NAME, value="saml").click()

    # 等待进入页面以后拖拉需要上传的spec进去
    # time.sleep(10)
    # print(1)
    # print(CodeBeamer_Spec)

    # 定位到即将拖入的folder
    CaseFolder_Filter = '//li[@id=\"' + CaseFolderID + '\"]'
    targetElement = browser.find_element(by=By.XPATH, value=CaseFolder_Filter)
    # print(targetElement)
    Action = ActionChains(browser)
    Action.key_down(Keys.SHIFT)  # 按住sheift
    for CaseName in InitCaseList:
        CaseName_Filter = '//li[@title=\"' + CaseName + '\"]'
        dragElement = browser.find_element(by=By.XPATH, value=CaseName_Filter)
        print(CaseName)
        Action.click(dragElement)
        time.sleep(2)
    time.sleep(10)
    # print(1)
    Action.drag_and_drop(dragElement, targetElement).perform()
    # print(2)
    time.sleep(10)


def DownLoadSpecFromCB(CaseTrackerID, CB_Spec_Folder, CaseFolderID):
    CB_Spec_Folder = CB_Spec_Folder.replace('/', '\\')
    options = webdriver.EdgeOptions()
    # print(CB_Spec_Folder)
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': CB_Spec_Folder}
    options.add_experimental_option('prefs', prefs)
    CodeBeamer_Upload_Url = "https://codebeamer.corp.int/cb/tracker/" + CaseTrackerID
    browser = webdriver.ChromiumEdge(options=options)
    browser.get(CodeBeamer_Upload_Url)

    # 点击Login
    browser.find_element(by=By.NAME, value="saml").click()

    browser.implicitly_wait(30)
    time.sleep(10)
    CaseFolder_Filter = '//li[@id=\"' + CaseFolderID + '\"]'
    # TargetElement = browser.find_element(by=By.XPATH, value=CaseFolder_Filter)
    print("Find Case Folder ID")
    browser.find_element(by=By.XPATH, value=CaseFolder_Filter).click()

    print("Click Case Folder ID")
    # MoreButton = browser.find_element(by=By.XPATH, value="//img[@data-tooltip='more']")
    # print(MoreButton)
    browser.implicitly_wait(30)
    # time.sleep(10)
    # browser.find_element(by=By.XPATH, value="//img[@data-tooltip='more']").click()
    # ele = browser.find_element(by=By.XPATH, value="/html/body/div[3]/div/form/div[2]/div[1]/div[1]/table/tbody/tr/td[1]/span/span/img")
    actionBarColumn = browser.find_element(by=By.XPATH,value="//td[@class='actionBarColumn']/span/span/img")#新版本是可以使用
    # ele = actionBarColumn.find_element(by=By.XPATH, value="//span[@class ='inlinemenuTrigger  initialized']")
    # ele = browser.find_element(by=By.XPATH, value="//img[@data-tooltip='more']"#老版本上可以使用的
    print(actionBarColumn)
    actionBarColumn.click()
    browser.implicitly_wait(5)
    print("Click data-tooltip='more")
    exportSelection =  browser.find_element(by=By.XPATH,value="//div[@class='yuimenu inlinemenu']/div/ul[2]/li[3]")
    # browser.find_element(by=By.ID, value="ui-id-6").click()
    exportSelection.click()
    print("exportSelection")
    browser.implicitly_wait(5)

    browser.switch_to.frame("inlinedPopupIframe")
    browser.find_element(by=By.ID, value="excelExportTabPane-tab").click()

    # browser.find_element(by=By.XPATH, value="//div[@id='excelExportTabPane-tab']").click()
    # print(11)

    browser.find_element(by=By.XPATH,value="//div[@id='excelExportTabPane']//label[@for='roundtripExcelExport']").click()

    # 下载数据
    browser.find_element(by=By.XPATH, value="//div[@id='excelExportTabPane']//input[@value='Export']").click()
    time.sleep(10)
    # FileName = browser.find_element(by=By.XPATH, value="//div[@class='information onlyOneMessage']//li[@target='_top']").text()
    # print(FileName)
    # time.sleep(3)

    browser.execute_script("window.open()")
    # switch to new tab
    browser.switch_to.window(browser.window_handles[-1])
    # navigate to edge downloads
    browser.get('edge://downloads')
    # define the endTime
    # //*[@id="open_file1"]
    # // *[ @ id = "downloads-item-1"] / div[1] / img
    # // *[ @ id = "downloads-item-1"] / div[1] / img
    # // *[ @ id = "downloads-item-1"]

    browser.implicitly_wait(5)
    # fileName = browser.find_element(by=By.XPATH, value="// *[ @ id = 'downloads-item-1'] / div[1] / img[1]").get_attribute("aria-label")
    # fileName = browser.find_element(by=By.XPATH, value="//*[@id='downloads-item-1'] / div[1] / img[1]").get_attribute(
    #     "aria-label")
    fileName = browser.find_element(by=By.XPATH, value="//img[@aria-label]").get_attribute("aria-label")
    print(fileName)
    return fileName

def Run_TestRun_InExcel(Browser,Test_Run_Folder,Df_Result):

    print("#################Run_TestRun_InExcel################################")
    #定位当前的TestRun ID
    test_run_id_element = Browser.find_element(by=By.XPATH,value="//div[@class='actionMenuBar large']//span[@class='breadcrumbs-summary  tail']//span")
    Test_Run_ID = test_run_id_element.text.replace("#","")
    # print(Test_Run_ID)

    print("Click run in  excel")
    ######################**************************************************
    #执行Run in excel,生成excel用于上传test result
    run_in_excel_element = Browser.find_element(by=By.XPATH,value="//a[@title='Run in Excel']")
    run_in_excel_element.click()
    #定位下载文件
    print("go to downlaod , select the file")
    Browser.execute_script("window.open()")
    # switch to new tab
    Browser.switch_to.window(Browser.window_handles[-1])
    # navigate to edge downloads
    Browser.get('edge://downloads')

    Browser.implicitly_wait(5)
    #     "aria-label")
    Test_Run_Report = Browser.find_element(by=By.XPATH, value="//img[@aria-label]").get_attribute("aria-label")

    Test_Run_Report_WithPath = os.path.join(Test_Run_Folder, Test_Run_Report)
    # print(Test_Run_Report_WithPath)
    """
    处理Test Run的数据,上传
    """
    HRun.Handle_TestRun_Report(Test_Run_Report_WithPath, Df_Result)
    # 返回之前的页面,上传文件
    print("swithc to the previos page, then upload the test run result")
    Browser.switch_to.window(Browser.window_handles[0])
    Browser.implicitly_wait(30)

    return Test_Run_Report_WithPath,Test_Run_ID

def UploadTestRun(Browser,Test_Run_Report_WithPath):

    print("#################UploadTestRun################################")

    upload_file_element = Browser.find_element(by=By.XPATH,value="//div[@class='qq-upload-button']//input[@type='file']")
    upload_file_element.send_keys(Test_Run_Report_WithPath)

    time.sleep(2)
    print("Confirm upload")
    # confirm_upload_element = browser.find_element(by=By.XPATH, value="//input[@value='Upload']")
    Browser.find_element(by=By.XPATH, value="//input[@value='Upload']").click()
    print("Confirm upload finished")
    time.sleep(10)

    """
    刷新页面，确定测试用例结果是否上传
    """
    print("fresh page")
    Browser.refresh()
    Browser.implicitly_wait(30)
    Status = Browser.find_element(by=By.XPATH,
                                  value="//table[@class='propertyTable inlineEditEnabled']//tr[2]//td[@class='tableItem']//span").text
    # print(Status)

    Result = Browser.find_element(by=By.XPATH, value="//td[@class='tableItem fieldColumn fieldId_15']").text
    print(Result)
    # time.sleep(10)
    return Status,Result

def Generate_TestRun(Browser, CaseFolderID, TestRun_TrackerName,Release):

    print("#################CreateTestRun################################")
    #
    CaseFolder_Filter = '//li[@id=\"' + CaseFolderID + '\"]'
    # TargetElement = browser.find_element(by=By.XPATH, value=CaseFolder_Filter)
    print("Find Case Folder ID")
    try:
        casefolder_element = Browser.find_element(by=By.XPATH, value=CaseFolder_Filter)
    except Exception as err:
        raise Exception("Can't find the case folder ID " + CaseFolderID)
    aau_name = casefolder_element.get_attribute('title')

    action = ActionChains(Browser)
    action.click(casefolder_element)
    action.context_click(casefolder_element).perform()

    print("right click finished")

    # generate_testrun_element = browser.find_element(by=By.XPATH, value="//ul//li//a[text()='Generate Test Run(s) from Selected']")
    # generate_testrun_element = browser.find_element(by=By.XPATH,value="/html/body/ul/li[16]")
    generate_testrun_element = Browser.find_element(by=By.XPATH,
                                                    value="//ul[@class='vakata-context jstree-contextmenu jstree-default-contextmenu']//a[@class='vakata-context-parent']")
    # print(generate_testrun_element)
    action.click(generate_testrun_element).perform()

    recursive_element = Browser.find_element(by=By.XPATH, value="//button[@class='ui-button ui-corner-all ui-widget']")
    print(recursive_element)
    action.click(recursive_element).perform()

    print("switch to another frame, then go to the search pattern")
    Browser.switch_to.frame("inlinedPopupIframe")  # 切换frame

    find_test_run_element = Browser.find_element(by=By.XPATH, value="//div[@id='searchTab-tab']")  # 点击FInd Test Run Trackers
    find_test_run_element.click()
    search_pattern_element = Browser.find_element(by=By.XPATH, value="//input[@id='searchPattern']")  # 定义搜索窗口

    # print(search_pattern_element)
    print("input the test run name")
    search_pattern_element.send_keys(TestRun_TrackerName)  # 输入test Run 名称

    print("click search")
    search_button_element = Browser.find_element(by=By.XPATH, value="//input[@id='searchButton']")  # 点击搜索按钮

    # print(search_button_element)
    search_button_element.click()
    Browser.implicitly_wait(30)
    # time.sleep(2)
    print("select the test run itme, then generate test run")
    test_run_select_element = Browser.find_element(by=By.XPATH,
                                                   value="//table[@id='searchList']//tbody//div[@class='wikiLinkContainer']")  # 选中搜索到的TestRun

    # print(test_run_select_element)
    test_run_select_element.click()

    test_run_submit_element = Browser.find_element(by=By.XPATH, value="//input[@type='submit']")  # 点击Generate
    # print(test_run_submit_element)
    test_run_submit_element.click()
    Browser.implicitly_wait(30)


    print("wait the page fresh, select all case don't need accepted, then save it to generate the test run")
    all_case_select_element = Browser.find_element(by=By.XPATH,
                                                   value="//input[@id='runOnlyAcceptedTestCases2']")  # 选择所有case
    all_case_select_element.click()

    # 需要考虑下滑到底部
    scroll_js_Down = "var q=document.documentElement.scrollTop=5000"
    Browser.execute_script(scroll_js_Down)

    # start_date_element = Browser.find_element(by=By.XPATH,value = "//input[@id='startDate']")
    #
    # end_date_element = Browser.find_element(by=By.XPATH, value="//input[@id='closeDate']")

    #对Test Run Name进行修改
    name_element = Browser.find_element(by=By.XPATH,value = "//input[@id='summary']")
    #根据CaseFolderID的名字抓取
    system_date = ""
    test_run_name = aau_name + "_" + str(datetime.date.today()).replace("-","_")
    name_element.clear()
    name_element.send_keys(test_run_name)

    release_select_element = Browser.find_element(by=By.XPATH,value="//select[@id='releaseId']")
    release_list = release_select_element.text.split("\n") # 单机release
    release_select_element.click()
    # print(release_list)
    release_list = [x.strip() for x in release_list]
    # option[text()='CHERY_T26&M1E_Release P10']
    #Release_P11_BYD_SG_Series
    #//select[@id='releaseId']//option[text()='" + Release + "']
    #//select[@id='releaseId']//option[text()='Release_P11_BYD_SG_Series']
    if Release in release_list:
        releasee_xpath = "//select[@id='releaseId']//option[text()='" + Release + "']"
        release_element = Browser.find_element(by=By.XPATH, value=releasee_xpath)
        release_element.click()
    else:
        raise  Exception(Release + " not exist")
    # 需要考虑上滑到底部
    time.sleep(1)

    save_element = Browser.find_element(by=By.XPATH, value="//input[@type='submit']")
    save_element.click()



    print("go to test run page")
    goto_test_run_element = Browser.find_element(by=By.XPATH,
                                                 value="//div[@class='overlayMessageBoxContainer animate-common-entry']//div[@class='overlayMessageBox notification']//a")
    goto_test_run_element.click()

    Browser.implicitly_wait(30)





def CreateTestRun_UpdateResult(CaseTrackerID,WokingSet, CaseFolderID, Test_Run_Folder, TestRun_TrackerName, Df_Result,Release):

    print("#########CreateTestRun_UpdateResult ########")
    # 生成browse
    if WokingSet == "":
        browser = LoginCodeBeamer("https://codebeamer.corp.int/cb/tracker/", CaseTrackerID, Test_Run_Folder)
    else:
        browser = LoginCodeBeamer_WorkingSet("https://codebeamer.corp.int/cb/tracker/", CaseTrackerID,WokingSet, Test_Run_Folder)

    # print(CaseFolderID)
    # 定位到CaseFolderID 里面根据Test_Run_Tracker名称去生成Test Run
    Generate_TestRun(browser, CaseFolderID, TestRun_TrackerName,Release)

    Test_Run_Report_WithPath,Test_Run_ID= Run_TestRun_InExcel(browser, Test_Run_Folder, Df_Result)

    Status,Result = UploadTestRun(browser, Test_Run_Report_WithPath)

    return Test_Run_Report_WithPath, Test_Run_ID,Status,Result


def ReUpload_TestRun(Test_Run_ID,Test_Run_Report_WithPath):
    # print(Test_Run_ID)
    browser = LoginCodeBeamer_WoPath("https://codebeamer.corp.int/cb/issue/", Test_Run_ID)

    upload_file_element = browser.find_element(by=By.XPATH,value="//div[@class='qq-upload-button']//input[@type='file']")
    upload_file_element.send_keys(Test_Run_Report_WithPath)

    Status,Result = UploadTestRun(browser, Test_Run_Report_WithPath)

    return Status,Result

def Restart_TestRun(Test_Run_ID,Test_Run_Folder,Df_Result):
    browser = LoginCodeBeamer("https://codebeamer.corp.int/cb/issue/",Test_Run_ID,Test_Run_Folder)

    print("Restart the test run to generate new Test Run ID")
    restart_test_run_element = browser.find_element(by=By.XPATH,value="//div[@class='item-transitions']//a")
    restart_test_run_element.click()
    browser.implicitly_wait(30)

    # reRunOpt_selected_but_in_same_run
    print("Select reRunOpt_selected_but_in_same_run")
    rerun_in_same_run_element = browser.find_element(by=By.XPATH,value="//input[@id='reRunOpt_selected_but_in_same_run']")
    rerun_in_same_run_element.click()
    browser.implicitly_wait(30)
    browser.switch_to.frame("inlinedPopupIframe")

    print("Select all case and then click select button")
    select_all_case_element = browser.find_element(by=By.XPATH,value="//input[@name='SELECT_ALL']")
    if not select_all_case_element.is_selected():
        select_all_case_element.click()

    submit_element = browser.find_element(by=By.XPATH,value = "//input[@onclick='saveSelection();']")
    submit_element.click()
    browser.implicitly_wait(30)

    print("Save to generate new Test Run")
    save_test_run_element = browser.find_element(by=By.XPATH,value="//input[@type='submit']")
    save_test_run_element.click()
    browser.implicitly_wait(30)
    time.sleep(1)

    # 定位当前的TestRun ID
    test_run_id_element = browser.find_element(by=By.XPATH,
                                               value="//div[@class='actionMenuBar large']//span[@class='breadcrumbs-summary  tail']//span")
    Test_Run_ID = test_run_id_element.text.replace("#", "")
    # print(Test_Run_ID)

    Test_Run_Report_WithPath,Test_Run_ID= Run_TestRun_InExcel(browser, Test_Run_Folder, Df_Result)

    Status,Result = UploadTestRun(browser, Test_Run_Report_WithPath)

    return Test_Run_Report_WithPath, Test_Run_ID,Status,Result


if __name__ == '__main__':
    pass
    CaseTrackerID = "10574220"
    CaseFolderID = "9645625"
    # # CaseFolderID = "11450597"
    TestRun_TrackerName = "TR_SHR_TestRuns"
    Test_Run_Folder = r"C:\Users\victor.yang\Desktop\Work\CB\TestRun"
    Test_Run_ID = "15666467"
    Test_Run_Report_WithPath = r"C:\Users\victor.yang\Desktop\Work\CB\TestRun\Quick Test Run for 11 Test Cases at Sep 21 2022 (2).xlsx"
    CB_Spec_Folder = r"C:\Users\victor.yang\Desktop\Work\CB"
    CB_Spec_Generate = r"C:\Users\victor.yang\Desktop\Work\CB\TestRun\EOLP31.xlsx"

    # CreateTestRun(CaseTrackerID, CaseFolderID,Test_Run,Test_Run_Folder)
    # UploadTestRun(Test_Run_ID, Test_Run_File)
    Result = r"C:\Users\victor.yang\Desktop\Work\CB\TestRun\EOLP31.xlsm"

    # Df_Result, CaseTrackerID, CB_Spec_Folder_ID, Release = HRun.ReadResult_TableOfContent(Result)
    CaseTrackerID = "1908975"
    CaseFolderID = "14494454"
    Release = "1908975"
    WorkingSet = "GEELY_GEEA2.0_SX21"#"-1"# "76695643"#"GEELY_GEEA2.0_SX21"
    Url_Prefix = "https://codebeamer.corp.int/cb/tracker/"
    LoginCodeBeamer_WorkingSet(Url_Prefix,CaseTrackerID,WorkingSet,Test_Run_Folder)
    # Generate_TestRun_WorkingSet(Browser, CaseFolderID, TestRun_TrackerName,Release,WorkingSet)
    # CreateTestRun_UpdateResult(CaseTrackerID, CaseFolderID, Test_Run_Folder, TestRun_TrackerName,Df_Result,Release)
    # ReUpload_TestRun(Test_Run_ID,Test_Run_Report_WithPath)
    # Restart_TestRun(Test_Run_ID, Test_Run_Folder, Df_Result)
