"""
app兼容性测试：
一、app的兼容性：app在不同型号的手机上能否正常运行
1、业务测试脚本
2、启动多个appium server
3、多台手机同时执行业务脚本


二、系统的兼容性：新的手机系统能否正常的安装市面上比较流行的app并且正常运行
1、下载市面上流行的app
2、依次执行安装，monkey测试，卸载

"""
import os
import time

import threading

from phone_appium.jisuanqi1104 import test_calculator


class Compatibility:
    def __init__(self):
        pass

    def get_version(self):
        pass

    def get_udid(self):
        pass

    def get_device(self):
        """
        获取设备id，版本号，端口
        :return: 列表嵌套字典
        """
        # 获取udid
        result = os.popen('adb devices').read()
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

    def start_appium(self, port, bport, udid):
        """
        启动appium server
        :param port:
        :param bport:
        :param udid:
        :return:
        """
        os.system(f'start appium -a 127.0.0.1 -p {port} -bp {bport} -U {udid}')

    def start_test(self):
        """
        执行测试：
        1、先启动appium server
        2、再执行业务测试代码
        :return:
        """
        udids = self.get_device()
        for device in udids:
            version = device['platformVersion']
            port = device['port']
            bport = device['bport']
            udid = device['udid']
            self.start_appium(port, bport, udid)
            time.sleep(5)
            test = test_calculator(version, port, udid)
            test.test_add()

    def start_thread(self,version,port,bport,udid):
        self.start_appium(port, bport, udid)
        time.sleep(5)
        test = test_calculator(version, udid, port)
        test.test_add()


if __name__ == '__main__':
    c = Compatibility()
    udids = c.get_device()
    thread_list =[]
    for device in udids:
        version = device['platformVersion']
        port = device['port']
        bport = device['bport']
        udid = device['udid']
        t = threading.Thread(target=c.start_thread,args=(version,port,bport,udid))
        thread_list.append(t)

    for t in thread_list:
        t.start()

    for t in thread_list:
        t.join()
    os.system('chcp 65001')
    os.system('taskkill /F /IM node.exe')
    os.system('taskkill /F /IM cmd.exe')