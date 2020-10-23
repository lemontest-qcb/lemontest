#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/10/21 13:54 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
第四次作业：
2. 完成任意整数序列的相加 -- range()- 生成一个整数序列，里面全是数字。求里面所有数字的和
3. 定义函数：判断一个对象（列表，字典，字符串）的长度是否大于5，如果大于5，输出True；否则输出False。-
'''
# def  add_fun(num):
#     sum = 0
#     # num = int(input("input正数："))   # 字符串
#     for i in range(num):
#         sum += i
#     print(sum)
# add_fun(100)
# def function_len(object):
#     # if type(object)==dict or type(object)==list or type(object)== str:
#     if isinstance(object,str) or isinstance(object,list) or isinstance(object,dict):  # True--False
#         leng = len(object)
#         if leng >= 5:
#             print("True")
#         else:
#             print("False")
#     else:
#         print("数据类型不能计算长度！")   # 容错性友好
# function_len((1,2,3,4))   # 函数的调用--- 传入参数
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://erp.lemfix.com")
driver.find_element_by_id("username").send_keys("test123")    # 找到了有username这个id的元素--点击,输入内容
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()