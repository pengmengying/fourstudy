# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : duotaishouji.py
@desc: 
@Created on: 2021/11/4 14:36
"""
import os
# #用夜神里的模拟器打开网页
# # from appium import webdriver
# # import time
# # myapp={
# #   "platformName": "Android",
# #   "platformVersion": "5.1.1",
# #   "deviceName": "Appium",
# #   "appPackage": "com.android.browser",
# #   "appActivity": ".BrowserActivity",
# #   "udid": "127.0.0.1:62001"
# # }
# # dr=webdriver.Remote('http://127.0.0.1:4723/wd/hub', myapp)
# # dr.implicitly_wait(20)
# # dr.find_element_by_id("com.android.browser:id/url").send_keys("http://192.168.137.1:8080/WoniuSales_V1_3_bin/")
# # dr.find_element_by_id("com.android.browser:id/magnify").click()

##另外的课程1104
#通过命令获取设备号
result=os.popen("adb devices").read()
udids=[]
for udid in result.strip().split("\n")[1:]:
    udid=udid.split("\t")[0]
    udids.append(udid)
print(udids)
#获取手机系统版本号
print(os.popen("adb -s 127.0.0.1:62025 shell getprop ro.build.version.release").read())

#启动appium server
os.system('chcp 65001')
os.system("start appium -a 127.0.0.1 -p 4723 -bp 4724 -U 127.0.0.1:62025")