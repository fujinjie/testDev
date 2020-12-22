#!/usr/bin/python
# -*- coding: utf-8 -*-

import pytest
import allure
from selenium import webdriver
import time

@allure.feature("百度搜索")
class TestDemo:

    @classmethod
    def setup_class(cls):
        with allure.step("初始化safari浏览器"):
            cls.driver = webdriver.Safari()

    @classmethod
    def teardown_class(cls):
        with allure.step("关闭safari浏览器"):
            cls.driver.quit()


    @pytest.mark.parametrize("testdata",["pytest","unittest","Junit"])
    def testBaiduSearch(self,testdata):

        with allure.step("用safari打开百度首页"):
            self.driver.get("https://www.baidu.com")
            self.driver.maximize_window()

        with allure.step(f"在百度搜索中输入{testdata}"):
            self.driver.find_element_by_id("kw").send_keys(testdata)
            time.sleep(2)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.driver.find_element_by_id("kw").clear()
            time.sleep(2)

        with allure.step("保存截图"):
            self.driver.save_screenshot("./screenshot/a.png")
            allure.attach.file("./screenshot/a.png", attachment_type=allure.attachment_type.PNG)
            time.sleep(2)



