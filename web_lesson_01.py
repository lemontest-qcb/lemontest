#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/9/7 14:22 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
from selenium import webdriver
from python_package1 import test_data
import time
driver = webdriver.Chrome()
driver.implicitly_wait(10)
# 打开页面
def open_url(url):
    driver.get(url)
    driver.maximize_window()

#登录
def login_page(username,password):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
open_url(test_data.url["url"])
login_page(test_data.login_data[0]["username"],test_data.login_data[1]["password"])
# 获取页面标题
title1 = driver.title
if title1 == "柠檬ERP":
    print("页面打开正确")
else:
    print("页面没有打开")
"""
等待：
1、强制等待
2、隐形等待
"""
# time.sleep(5)


# 检查登录用户名
user = driver.find_element_by_xpath("//p").text
if user == "测试用户":
    print("用户登录成功")
else:
    print("用户登录失败")

# 搜索零售出库单号
driver.find_element_by_xpath('//span[text()="零售出库"]').click()

"""
iframe 切换：
1、识别iframe
2、切换iframe
2.1 通过id切换：
"""

id = driver.find_element_by_xpath('//div[@id="tabpanel"]//div[text()="零售出库"]/..').get_attribute("id")
iframe_id = id+"-frame"  #  拼接成iframe ID
driver.switch_to.frame(iframe_id)
driver.find_element_by_id("searchNumber").send_keys("314")
driver.find_element_by_id("searchBtn").click()
time.sleep(5)
result = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]').text
if "314" in result:
    print("搜索结果正确！")
# element = driver.find_elements_by_xpath('//table[@class="datagrid-btable"]//tr')
# if len(element) == 1:
#     print("搜索正确！")

















