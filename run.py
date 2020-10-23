#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/10/22 11:53 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
from common import method
from selenium import webdriver
from test_data import test_data# 导入测试数据
driver = webdriver.Chrome()
driver.implicitly_wait(10)
url = test_data.url["url"]
pwd = test_data.login_data[1]["password"]
user = test_data.login_data[0]["username"]
s_key = test_data.search_data["searchkey"]
result = method.execute_test(driver,url,user,pwd,s_key)
if s_key in result:
    print("搜索结果pass")