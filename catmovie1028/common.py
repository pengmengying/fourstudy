# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : common.py
@desc: 
@Created on: 2021/10/28 16:31
"""
import csv
import os


file_path=os.path.abspath(__file__)
csvpath=os.path.dirname(file_path)


def  readcsv(csvfilepath):
    csvdata=[]
    with open(csvfilepath,"r",encoding="utf-8") as f:
        lines=csv.reader(f)
        for line in lines:
            csvdata.append(line)
    print(csvdata[1:])
    return csvdata[1:]  # [  [] ]

if __name__ == '__main__':
    print(readcsv(r'D:\study\threestudy\fourstudy\catmovie1028\username.csv'))