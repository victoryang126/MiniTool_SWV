
# from selenium im
#pip install urllib3==1.26.7 需要安装特定的版本
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service as ChromeService
# 设置 ChromeDriver 的路径（根据你的实际路径进行设置）
chromedriver_path = "/Users/monster/Downloads/chromedriver_mac64/chromedriver"
chromedriver_path = "/Users/monster/Downloads/chromedriver-mac-x64/chromedriver"
# 启动已经打开的 Chrome 浏览器

# 创建 ChromeOptions 对象
chrome_options = Options()

# 指定 ChromeDriver 的路径
chrome_options.add_argument(f"webdriver.chrome.driver={chromedriver_path}")

# 创建 Chrome 浏览器实例
driver = webdriver.Chrome(options=chrome_options)


chrome_service = ChromeService(executable_path=chromedriver_path)
# chrome_service.start()
capabilities = {
    "browserName": "chrome",  # 浏览器类型
    "version": "120.0.6099.109",            # 浏览器版本
}
# driver = webdriver.Remote(chrome_service.service_url,desired_capabilities =capabilities )
# driver = webdriver.Chrome(service=chrome_service)

# 打开网页
url = "https://wflow.yitutech.com/#/inbox/list"
driver.get(url)


# driver.execute_script(f'window.open("{url}","_blank");')

# 在这里可以执行其他 Selenium 操作
time.sleep(80)
# 关闭浏览器
driver.quit()
