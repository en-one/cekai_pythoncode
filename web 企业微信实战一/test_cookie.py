import time
import json

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestCookie:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")

    @pytest.mark.skip
    def test_get_cookie(self):
        time.sleep(15)
        cookies = self.driver.get_cookies()

        # 把cookie存放在文件里
        with open("cookie.json", "w") as f:
            json.dump(cookies, f)

    def test_cookie_login(self):
        cookies = json.load(open("cookie.json"))
        for cookie in cookies:
            # 吧cookie键值对一个一个添加到cookie里
            self.driver.add_cookie(cookie)

        # 刷新
        while True:
            self.driver.refresh()
            res = WebDriverWait(self.driver, 10). \
                until(expected_conditions.element_to_be_clickable((By.ID, "menu_index")))
            if res is not None:
                break


        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable)

        #点击导入通讯录
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable
                                             ((By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)")))
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()

        #导入通讯录
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "js_upload_file_input")))
        self.driver.find_element(By.ID,"js_upload_file_input").send_keys("E:\code\python\\test_developer\homework\pythoncode\web 企业微信实战一\data\workbook.xlsx")

        # #添加断言 上传成功后网页上显示文件名就是我们上传的文件名
        assert_ele = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, "upload_file_name"))).text
        print(assert_ele)
        assert assert_ele == "workbook.xlsx"


    def teardown(self):
        self.driver.quit()
