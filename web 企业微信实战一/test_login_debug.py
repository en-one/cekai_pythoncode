from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestLogin:
    def test_debug_login(self):

        option = Options()
        # 指定调试地址 方便调试，debugger 方式
        option.debugger_address = "localhost:9222"
        # 打开页面
        driver = webdriver.Chrome(options=option)
        # https: // work.weixin.qq.com / wework_admin / loginpage_wx
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")

