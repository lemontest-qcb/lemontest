#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/10/22 11:48 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
from common import method# 导入第一个文件里封装好的函数
from test_data import test_data# 导入测试数据
import time
def execute_test(driver):
    method.open_url(test_data.url["url"],driver)
    method.login_page(test_data.login_data[0]["username"],test_data.login_data[1]["password"],driver)
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    id = driver.find_element_by_xpath('//div[@id="tabpanel"]//div[text()="零售出库"]/..').get_attribute("id")
    iframe_id = id+"-frame"  #  拼接成iframe ID
    driver.switch_to.frame(iframe_id)
    driver.find_element_by_id("searchNumber").send_keys("314")
    driver.find_element_by_id("searchBtn").click()
    time.sleep(5)
    result = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]').text
    if "314" in result:
        print("搜索结果正确！")
