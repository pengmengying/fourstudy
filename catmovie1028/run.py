# -*- coding: utf-8 -*-
"""
@author: ZJ
@email: 1576094876@qq.com
@File : run.py
@desc: 
@Created on: 2021/10/28 15:19
"""
import os
import pytest


pytest.main(["-vs"])
os.system("allure generate ./temp -o ./report --clean")
