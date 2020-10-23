#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/10/22 11:42 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
import time
def open_url(driver,url):
    driver.get(url)
    driver.maximize_window()
def login_page(username,password,driver):
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
def execute_test(driver,url,username,password,ser_key):
    open_url(driver,url)
    login_page(username,password,driver)
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    id = driver.find_element_by_xpath('//div[@id="tabpanel"]//div[text()="零售出库"]/..').get_attribute("id")
    iframe_id = id+"-frame"  #  拼接成iframe ID
    driver.switch_to.frame(iframe_id)
    driver.find_element_by_id("searchNumber").send_keys(ser_key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(5)
    result = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]').text
    return result
