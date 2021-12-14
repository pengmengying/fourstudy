# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : 111.py
@desc: 
@Created on: 2021/11/9 16:19
"""
nums=[2,7,11,15]
target=9
index=[]
for i in nums:
    for j in nums:
        if i+j==target:
            print(i,j)

