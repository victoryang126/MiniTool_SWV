
from selenium import webdriver
from selenium.webdriver.common.by import By

CodeBeamer_Upload_Url = "https://codebeamer.corp.int/cb/importIssue.spr?tracker_id=40804608"

browser = webdriver.ChromiumEdge()
browser.get(CodeBeamer_Upload_Url)
print("1")
browser.find_element(by=By.NAME, value= "saml" )
browser.find_element_by_class_name()
# <button class="login_button" type="submit" name="saml" id="saml">
# 							Login with<br>Single Sign On
# 					</button>
# <div class="yuimenu inlinemenu __web-inspector-hide-shortcut__" id="login_ToolBarItempopup" style="display: none;"><div class="bd"></div></div>
# <div class="yuimenu inlinemenu" id="project_browser_ToolBarItempopup" style="display: none;"><div class="bd"></div></div>
# browser.get(CodeBeamer_Upload_Url)
# uploadConversationId_dropZone > div > div.qq-upload-button
# <div class="qq-upload-button" style="position: relative; overflow: hidden; direction: ltr;"><div class="qq-upload-icon"></div><div class="qq-upload-text">Attach a file…</div><input data-qq-xhr-supported="1" title="You can also drag and drop files here" type="file" name="file" style="font-size: 118px; position: absolute; left: 0px; top: 0px; font-family: Arial; margin: 0px; padding: 0px; cursor: pointer; opacity: 0; width: 100%;"></div>
# browser.get(CodeBeamer_Upload_Url)
browser.quit()