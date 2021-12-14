# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : testappium1104.py
@desc: 
@Created on: 2021/11/4 16:43
"""
import os
import time

from phone_appium.jisuanqi1104 import test_calculator


class Test_phone():
    def __init__(self):
        pass
    def get_device(self):
        """
              获取设备id，版本号，端口
              :return: 列表嵌套字典
              """
        # 获取udid
        result = os.popen("adb devices").read()
        port = 4723
        bport = 5723
        udids = []
        for udid in result.strip().split("\n")[1:]:
            udid_dict = {}
            udid = udid.split('\t')[0]
            # 获取系统版本
            version = os.popen(f'adb -s {udid} shell getprop ro.build.version.release').read().strip()
            udid_dict['udid'] = udid
            udid_dict['platformVersion'] = version
            udid_dict['port'] = port
            udid_dict['bport'] = bport
            udids.append(udid_dict)
            port += 1
            bport += 1
        return udids
    def start_appium(self,port,bport,udid):
        os.system(f"start appium -a 127.0.0.1 -p {port} -bp {bport} -U {udid}")
    def start_test(self):
        udids=self.get_device()
        for device in udids:
            version=device["platformVersion"]
            bport=device["port"]
            port=device["port"]
            udid = device["udid"]
            self.start_appium(port,bport,udid)
            time.sleep(5)
            test=test_calculator(version, udid, port)
            test.test_add()
if __name__ == '__main__':
    c=Test_phone()
    c.start_test()