# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : jisuanqi1104.py
@desc: 
@Created on: 2021/11/4 17:05
"""
from selenium import webdriver


class test_calculator:

    def __init__(self, version, udid, port):
        self.desired_caps = {
            "platformName": "Android",  # 平台的名称：iOS, Android, or FirefoxOS
            "platformVersion": version,  # 移动设备的系统版本号
            "deviceName": "Appium",  # Android不做严格识别，注：IOS：instruments -s devices
            "appPackage": "com.miui.calculator",  # 应用包名
            "appActivity": ".cal.CalculatorActivity",  # 应用主类名
            "udid": udid  # 设备ID
        }
        self.dr = webdriver.Remote(f'http://127.0.0.1:{port}/wd/hub', self.desired_caps)
        self.dr.implicitly_wait(10)

    def test_add(self):
        self.dr.find_element_by_id('android:id/button1').click()
        son = 'text("1").fromParent(text("4"))'
        son1 = 'new UiSelector().text("1")'
        element1 = 'new UiSelector().resourceId("com.miui.calculator:id/btn_1_s")'
        element2 = 'resourceId("com.miui.calculator:id/btn_1_s")'
        self.dr.find_element_by_id('com.miui.calculator:id/btn_mul_s').click()
        self.dr.find_element_by_id('com.miui.calculator:id/btn_1_s').click()