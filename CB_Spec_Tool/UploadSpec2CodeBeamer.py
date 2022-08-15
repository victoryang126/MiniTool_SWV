from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


# 40804608
# 10574131

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
    print(1)
    print(CodeBeamer_Spec)

    browser.find_element(by=By.XPATH, value="//input[@type='file']").send_keys(CodeBeamer_Spec)
    time.sleep(10)
    # Next
    browser.find_element(by=By.ID, value="_eventId_next").click()
    # Next
    #选择ID Mapping
    print(1)
    id_slectorbutton= "//*[@id ='rawDataTable']/ tbody/tr[1]/th[2]/ button"
    browser.find_element(by=By.XPATH, value=id_slectorbutton).click()
    print(2)

    print(3)
    ul_slector = "/ html / body / div[12] / ul"
    parent_elemnt = browser.find_element(by=By.XPATH, value=ul_slector)
    slection_list = parent_elemnt.find_element(by=By.XPATH, value=ul_slector).text.split("\n")
    # time.sleep(10)
    print(slection_list)
    if "ID" in slection_list:
        print("find the ID selection")
        id_filter = "/ html / body / div[12] / div / div / input"
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
        print(1)
        # browser.execute_script(scroll_js_Top)
        time.sleep(10)
        while True:
            try:
                time.sleep(10)
                targetElement = browser.find_element(by=By.XPATH, value=CaseFolder_Filter)
                print(targetElement)
                time.sleep(10)
                Action.drag_and_drop(dragElement, targetElement).perform()
                print(33333)
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
    print(1)
    # print(CodeBeamer_Spec)

    # 定位到即将拖入的folder
    CaseFolder_Filter = '//li[@id=\"' + CaseFolderID + '\"]'
    targetElement = browser.find_element(by=By.XPATH, value=CaseFolder_Filter)
    print(targetElement)
    Action = ActionChains(browser)
    Action.key_down(Keys.SHIFT)  # 按住sheift
    for CaseName in InitCaseList:
        CaseName_Filter = '//li[@title=\"' + CaseName + '\"]'
        dragElement = browser.find_element(by=By.XPATH, value=CaseName_Filter)
        print(CaseName)
        Action.click(dragElement)
        time.sleep(2)
    time.sleep(10)
    print(1)
    Action.drag_and_drop(dragElement, targetElement).perform()
    print(2)
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
    print(11)

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


if __name__ == '__main__':
    pass
    CaseTrackerID = "22106033"
    CaseFolderID = "10367368"
    # # CaseFolderID = "11450597"
    CB_Spec_Folder = r"C:\Users\victor.yang\Desktop\Work\CB"
    CB_Spec_Generate = r"C:\Users\victor.yang\Desktop\Work\CB\CHT_SWV_GMW_D30_2S_DCS_Test_Result_CodeBeamer.xlsx"
    UploadSpec2CB(CaseTrackerID,CB_Spec_Generate,CaseFolderID,[])
    # CodeBeamer_Spec = "E:\Project_Test\Geely_Geea2_HX11\DCS\CHT_System_Validation_Chery_T26_CANC_Test Specification_CodeBeamer.xlsx"
    # InitCaseList = [
    #     "Test Case 1 - First Frame Transmitted Time and Init value",

    #     "Test Case 2 - Stop sending Msg  Time",
    #     "Test Case 3 - BUSOFF Strategy",
    #     "Test Case 4 - Transmit capability",
    #     "Test Case 5 - Signal of Message ABM1(0x31C)",
    #     "Test Case 7 - Receive Message Monitor",
    #     "Test Case 8 - High Priority Behavior",
    #     "Test Case 9 - ECU behavior during lost communication failure",
    #     "Test Case 10 - Low power supply",
    #     "Test Case 11 - High power supply",
    #     "Test Case 12 - Check ECU Receive Message",
    #     "Test Case 13 - ECU Sample Point Test"
    # ]
    # CodeBeamer_Spec_FromCB = ""
    # UploadSpec2CB(CaseTrackerID, CodeBeamer_Spec, CaseFolderID, InitCaseList)
    DownLoadSpecFromCB(CaseTrackerID, CB_Spec_Folder, CaseFolderID)
    # DragCaseItem2oFolder(CaseTrackerID, CaseFolderID, InitCaseList)