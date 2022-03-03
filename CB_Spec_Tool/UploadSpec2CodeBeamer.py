
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
import time
# 40804608
# 10574131

def UploadSpec2CB(CaseTrackerID,CodeBeamer_Spec,CaseFolderID,InitCaseList):
    CodeBeamer_Upload_Url = "https://codebeamer.corp.int/cb/importIssue.spr?tracker_id=" + CaseTrackerID
    # CodeBeamer_Upload_Url = "https://codebeamer.corp.int/cb/tracker/10574131?view_id=-2"
    browser = webdriver.ChromiumEdge()
    browser.get(CodeBeamer_Upload_Url)

    # 点击Login
    browser.find_element(by=By.NAME, value= "saml" ).click()

    # 等待进入页面以后拖拉需要上传的spec进去
    # time.sleep(10)
    print(1)
    print(CodeBeamer_Spec)

    browser.find_element(by=By.XPATH, value= "//input[@type='file']").send_keys(CodeBeamer_Spec)
    time.sleep(10)
    #Next
    browser.find_element(by=By.ID, value= "_eventId_next" ).click()
    # Next
    print(2)
    browser.find_element(by=By.NAME, value= "_eventId_next" ).click()
    # Next
    browser.find_element(by=By.NAME, value= "_eventId_next" ).click()
    # Finish
    browser.find_element(by=By.NAME, value= "_eventId_next" ).click()
    time.sleep(10)
    #判断是否有错误，如果错误，则停
    try:
        ErrorStatus = browser.find_element(by=By.CLASS_NAME, value= "invalidfield").is_displayed()
        if ErrorStatus:
            print("Please check the error")
            time.sleep(120)
            return False
    except Exception as err:
        print("Not exist Error")
        time.sleep(120)
        return True


    # 定位到即将拖入的folder
    # CaseFolder_Filter = '//li[@id=\"' +CaseFolderID + '\"]'
    # targetElement = browser.find_element(by=By.XPATH, value=CaseFolder_Filter)
    # Action = ActionChains(browser)
    # for CaseName in InitCaseList:
    #     CaseName_Filter = '//li[@title=\"' + CaseName + '\"]'
    #     dragElement = browser.find_element(by=By.XPATH, value=CaseName_Filter)
    #     sheft_key = browser.find_element(by=By.ID, value="Shift")
    #     Action.click_and_hold(sheft_key)
    #     Action.click(dragElement)
    # for CaseName in InitCaseList:
    #     targetElement = browser.find_element(by=By.XPATH, value=CaseFolder_Filter)
    #     print(targetElement)
    #     CaseName_Filter = '//li[@title=\"' + CaseName + '\"]'
    #     dragElement = browser.find_element(by=By.XPATH, value=CaseName_Filter)
    #     browser.find_elements()
    #     Action.drag_and_drop(dragElement,targetElement).perform()
    #     time.sleep(10)

    #     Action.move_to_element(targetElement).release().perform()
if __name__ == '__main__':
    CaseTrackerID = "10574131"
    CaseFolderID = "11862154"
    CodeBeamer_Spec = "E:\Project_Test\Geely_Geea2_HX11\DCS\CHT_System_Validation_Chery_T26_CANC_Test Specification_CodeBeamer.xlsx"
    InitCaseList = [
        "Test Case 1 - First Frame Transmitted Time and Init value",
        "Test Case 2 - Stop sending Msg  Time",
        "Test Case 3 - BUSOFF Strategy",
        "Test Case 4 - Transmit capability",
        "Test Case 5 - Signal of Message ABM1(0x31C)",
        "Test Case 7 - Receive Message Monitor",
        "Test Case 8 - High Priority Behavior",
        "Test Case 9 - ECU behavior during lost communication failure",
        "Test Case 10 - Low power supply",
        "Test Case 11 - High power supply",
        "Test Case 12 - Check ECU Receive Message",
        "Test Case 13 - ECU Sample Point Test"
    ]
    UploadSpec2CB(CaseTrackerID, CodeBeamer_Spec, CaseFolderID, InitCaseList)
