# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : tset_case1028.py
@desc: 
@Created on: 2021/10/28 14:16
"""
import random

import pytest
import requests

from catmovie1028.common import readcsv, csvpath
from myredis1027.redis1027 import mymyredis




class Test_redis():
    def setup_class(self):
        self.re =mymyredis()

    # def test_startlogin(self): #登录网页的接口
    #     url = "http://www.wncinema.com/"
    #     headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0"}
    #     res = requests.get(url, headers=headers)
    #     return res
    @pytest.mark.parametrize("phonenum,verifycode,userPassword,userPassword2,except1",readcsv(csvpath+'/register.csv'),ids=["注册成功","验证码错误","验证码为空","用户名重复"])
    def test_login01(self,phonenum,verifycode,userPassword,userPassword2,except1): #注册成功
        url = f"http://api.wncinema.com/api/user/verifyCode?cellPhone={phonenum}"
        print(phonenum,verifycode,userPassword,userPassword2,except1)
        requests.get(url=url)
        if verifycode=="rediscode":
            verifycode=self.re.get_string(phonenum).split('"')[1]
        url1="http://api.wncinema.com/api/user/register"
        data={"userAccount":phonenum,"userPassword":userPassword,"userPhone":phonenum,"verifyCode":verifycode,"userPassword2":userPassword2}
        res1 = requests.post(url=url1,json=data)
        # if res1.json()["msg"] == except1:
        #     return "测试成功"
        # return "测试失败"
        assert res1.json()["msg"]==except1

    # @pytest.mark.parametrize("phonenum,userPassword,except1",
    #                          readcsv(r'D:\study\threestudy\fourstudy\catmovie1028\login.csv'), ids=["登录成功","用户名和密码不正确"])
    def loginning(self,username):
        url = "http://api.wncinema.com/api/auth/weblogin"
        data={"username":username,"password":"123"}
        header={'Content-Type':'application/json'}
        res = requests.post(url=url,json=data,headers=header)
        # assert "text/plain" in res.headers['Content-Type']
        return res.text

    @pytest.mark.skip(reason="跳过")
    def test_buycienma(self):  #选择中某影院购票
        url="http://www.wncinema.com/cinemadetail.html?cinemaId=4&movieId=166"
        header = {"Cookie":
                      "Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IntcInVzZXJJZFwiOjExMixcInVzZXJOYW1lXCI6bnVsbCxcInVzZXJBY2NvdW50XCI6XCIxOTkzOTk5MDE0MFwiLFwiZXhwaXJlVGltZVwiOjE2MzU5MzYzMzc3NjJ9In0.-NHBTEwPvJw6zU7gJXILjfCp8NjLhxM3uq3UpneDcLH7NwnhRsgR0TgUhNt-WW3cVNjoALhRkvP-2ufIOdrnaA"}
        res = requests.get(url=url, headers=header)
        return res

    @pytest.mark.skip(reason="跳过")
    def test_buyseat(self):  # 选择中某影院购票后选择座位
        url = "http://www.wncinema.com/chooseseat.html?hallId=1&hallMovieId=4&movieId=166"
        header = {"Cookie":
                      "Admin-Token=eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IntcInVzZXJJZFwiOjExMixcInVzZXJOYW1lXCI6bnVsbCxcInVzZXJBY2NvdW50XCI6XCIxOTkzOTk5MDE0MFwiLFwiZXhwaXJlVGltZVwiOjE2MzU5MzYzMzc3NjJ9In0.-NHBTEwPvJw6zU7gJXILjfCp8NjLhxM3uq3UpneDcLH7NwnhRsgR0TgUhNt-WW3cVNjoALhRkvP-2ufIOdrnaA"}
        res = requests.get(url=url, headers=header)
        return res


    def orderid(self,username):
        url = "http://api.wncinema.com/api/order/order/query/orderId"
        token = "Bearer " + self.loginning(username)
        header = {'Content-Type': 'application/json', 'Authorization': token}
        res = requests.get(url=url, headers=header)
        return res.json()["data"]


    def seatid(self,username):
        url = "http://api.wncinema.com/api/cinema/cinema/seat/list?pageNum=1&pageSize=1000&hallMovieId=4"
        token = "Bearer " + self.loginning(username)
        header = {'Content-Type': 'application/json', 'Authorization': token}
        res = requests.get(url=url, headers=header)
        rowslist=res.json()["rows"]
        #JsonPath.read(json, "$..seatId")
        seatIdlist=[]
        for i in rowslist:
            if i['seatStatus']==1:
                seatIdlist.append(i["seatId"])
        return random.choice(seatIdlist)
    #String json = "...";
    #List<String> authors = JsonPath.read(json, "$.store.book[*].author");  JsonPath的用法  ..：深层扫描
    def hallMovieId(self, username):
        url = "http://api.wncinema.com/api/cinema/cinema/hallmovierel/listByCinemaAndMovieAndPlaytime?cinemaId=4&moviePlayTime=2021-10-28%2014%3A39%3A08&movieId=166"
        token = "Bearer " + self.loginning(username)
        header = {'Content-Type': 'application/json', 'Authorization': token}
        res = requests.get(url=url, headers=header)
        halllist=res.json()["data"]
        hallMovieIdlist=[]
        for i in halllist:
            hallMovieIdlist.append(i["hallMovieId"])
        return random.choice(hallMovieIdlist)


    def myorderlist(self,username):  #提取我的订单里接口返回的数据，以便验证是否成功新增订单
        url = "http://api.wncinema.com/api/order/order/list?pageNum=1&pageSize=100"
        token = "Bearer " + self.loginning(username)   
        header = {'Content-Type': 'application/json', 'Authorization': token}
        res = requests.get(url=url, headers=header)
        orderlistrows=res.json()["rows"]
        orderlist=[]
        for i in orderlistrows:
            orderlist.append(i["orderId"])
        return orderlist

    @pytest.mark.parametrize("username",readcsv(csvpath+'/username.csv'),ids=["下订单成功"])
    def test_order(self,username): #确认选座接口
        hallMovieId=self.hallMovieId(username[0])
        seatid=self.seatid(username[0])
        orderId=self.orderid(username[0])
        url="http://api.wncinema.com/api/order/order/makeOrder"
        token="Bearer "+self.loginning(username[0])
        data={"selectedSeatIdList":[seatid],"hallMovieId":hallMovieId,"orderId":orderId} #[339],"hallMovieId":"3","orderId":1453299594069938202
        header={'Content-Type':'application/json','Autho rization':token}
        requests.post(url=url,json=data,headers=header)
        orderlist=self.myorderlist(username[0])
        # if orderId in orderlist:
        #     print("通过")
        # else:
        #     print("失败")
        assert orderId in orderlist


if __name__ == '__main__':
    red=Test_redis()
    # red.test_login01()
    # red.test_loginning("17839926247")
    # red.test_seatid('17839926247')
    # red.test_orderid("17839926247")
    # red.test_order('17839926250')
    red.myorderlist('17839926250')
    # red.test_hallMovieId("17839926247")
    # print(red.seatid('17839926250'))