"""
二、系统的兼容性：新的手机系统能否正常的安装市面上比较流行的app并且正常运行
1、下载市面上流行的app
2、依次执行安装，monkey测试，卸载
"""
import os
import requests
import re

class Comp:
    def __init__(self):
        pass

    def download_apk(self):
        url = 'https://sj.qq.com/myapp/category.htm?orgame=1'
        resp = requests.get(url)
        # print(resp.text)
        download_url = re.findall('<a href="detail.htm(.+?)"',resp.text)
        # print(download_url)
        urls = []
        for u in download_url:
            u = 'https://sj.qq.com/myapp/detail.htm' + u
            urls.append(u)
        urls = list(set(urls))

        for au in urls[:1]:
            resp = requests.get(au)
            apkurl = re.findall('data-apkUrl="(.+?)"',resp.text)
            url = apkurl[0]
            # print(apkurl)
            print(url)
            res = requests.get(url)
            with open('./apk/test1.apk','wb') as f:
                f.write(res.content)



        # print(urls)
    def install_apk(self, apk):
        """
        获取apk的主包名
        aapt dump badging G:\workspace\SHClass45\app\com.miui.calculator.apk|findstr package
        # 安装
        1、adb install {apk}
        2、断言：判断主包名是否在pm list命令的结果中
        adb shell pm list package -3
        :return:
        """

    def start_app(self, apk):
        """
        获取主类名
        aapt dump badging G:\workspace\SHClass45\app\com.miui.calculator.apk|findstr activity
        1、启动app
        adb shell am start -n 主包名/主类名
        2、断言：判断主包名是否在下命令的结果中
        adb shell ps | finstr 主包名

        :return:
        """
        pass

    def monkey_test(self, apk):
        """
        adb shell monkey -p com.xy.android.junit -s 500 -v 10000
        断言：分析monkey日志，看日志中是否有crash
        :return:
        """
        pass

    def uninstall_apk(self, apk):
        """
        1、执行卸载
        adb uninstall apk主包名
        2、判断主包名是否在pm list命令的结果中
        adb shell pm list package -3

         :return:
        """
        pass


if __name__ == '__main__':
    c = Comp()
    c.download_apk()
    # apks = os.listdir('./apk')[:-1]
    # print(apks)
    # for apk in apks:
    #     c.install_apk(apk)
    #     c.start_app(apk)
    #     c.monkey_test(apk)
    #     c.uninstall_apk(apk)
