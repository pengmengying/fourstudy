# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : test1027.py
@desc: 
@Created on: 2021/10/27 10:54
"""
import redis
class mymyredis():
    def __init__(self):
        pool = redis.ConnectionPool(host='192.168.9.62', port=6379)
        self.connect=redis.Redis(connection_pool=pool)
    def set_string(self,name,valuse):
         return self.connect.set(name,valuse)
    def get_string(self,name):
         return self.connect.get(name).decode()
    # def hset_hash(self,name,key,value):
    #     #      if key is None:
    #     #          return self.connect.hmset fle2 k1 3 k2 4 k3 5
    #     #      return self.connect.hget(name,key)
    def hget_hash(self,name,key=None):
         if key is None:
             return self.connect.hgetall(name)
         return self.connect.hget(name,key)

if __name__ == '__main__':
    my=myredis()
    # my.set_string("name","zz")
    print(my.get_string("name"))