#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/10/19 15:13 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
1、a=[1,2,'6','summer'] 请用成员运算符判断 i是否在这个列表里面 -- in， not in
2：dict_1={"class_id":45,'num':20} 请判断班级上课人数是否大于5
注：num表示课堂人数。如果大于5，输出人数。
3、list3 = ['囧囧','唐僧', '旧模样', 'ouyang', 'Nacy, '土豆江'] ，扩充列表当中的每一个值包含：姓名、性别、年龄、城市。
以字典的形式表达，并且把字典都存在新的 list中，最后打印最终的列表。
提示： 手动扩充成字典，然后存放到列表里；存放在列表里面
'''
# a=[1,2,'6','summer']
# print("i" in a)
# a=[1,2,'6','summer']
# if "i" in a:
#     print("i是成员")
# else:
#     print("不是")

# dict_1={"class_id":45,'num':20}
# num = dict_1.get("num")
# if num >= 5:
#     print('班上的人数是：{}'.format(num))
# else:
#     print("班上人数不足5人！")

#手动
# list3 = ['囧囧','唐僧', '旧模样', 'ouyang', 'Nacy', '土豆江']
# dict1 = {"name":"囧囧","age":"18","city":"北京","gender":"Male"}
# dict2 = {"name":"唐僧","age":"18","city":"北京","gender":"female"}
# dict3 = {"name":"旧模样","age":"18","city":"北京","gender":"female"}
# dict4 = {"name":"ouyang","age":"18","city":"北京","gender":"female"}
# dict5 = {"name":"Nacy","age":"18","city":"北京","gender":"female"}
# dict6 = {"name":"土豆江","age":"18","city":"北京","gender":"female"}
# list4 = [dict1,dict2,dict3,dict4,dict5,dict6]
# print(list4)
#自动：
# list3 = ['囧囧','唐僧', '旧模样', 'ouyang', 'Nacy',"土豆江"]  # list[3]
# list4 = []  # 空列表 ---存新字典---列表里追加元素：append
# list2 = [18,19,20,21,22,23]
# list1 = ['Female','Man','Female','man','female','man']
# list5 = ['北京','深圳','北京','北京','长沙','武汉']
# for i in range(6):  # 0 1 2 3 4 5
#     dict1 = dict(name=list3[i],age=list2[i],sex=list1[i],city=list5[i])  # 生成一个字典 dict1
#     list4.append(dict1)
# print(list4)

# import selenium   # 工具里的所有的内容都导入
from selenium import webdriver  # 从selenium工具里导入webdriver库
import time   # 导入time这个模块  --- Python自带的
driver = webdriver.Chrome()  # 选择chrome这个浏览器，初始化driver=== 可以浏览器进行沟通  建立会话 = session
driver.implicitly_wait(10)  # 隐式等待，默认等待10s  == 最多等到10s，提前出现了，不继续等待了。

# 1、打开一个网址
driver.get("http://erp.lemfix.com")
# 2、浏览器窗口最大化
driver.maximize_window()
# # 3、打开新页面
# time.sleep(2)   # 等待，默认秒
# driver.get("http://erp.lemfix.com")
# # 4、向前 退后   刷新
# time.sleep(2)
# driver.back()   # 退回上一个页面
# time.sleep(2)
# driver.forward()  # 前进道下一个页面
# time.sleep(2)
# driver.refresh()   # 刷新页面
# # 5、退出
# driver.quit()  # 关闭驱动  session关闭
# driver.close()  # 关闭当前的窗口，不会退出会话

# 以上浏览器的常规操作,非常规的操作--要怎么实现呢？  === 元素定位--了解 前端页面


'''
web自动化：
代码           翻译（中间人）         浏览器 
Python  ----->  浏览器驱动(准备)  ----->   Chrome
selenium： Python的工具，三个部分  --了解
1）ide：录制脚本--用的少
2）webdriver:库--提供对网页的各种操作 + 结合语言使用 -- Python java   --重点
3)grid:分布式  --用的少

基础知识：web页面= HTML+CSS+Javascript   -- 扩展 了解
html: 标签语言 <标签名>值</标签名> == 呈现页面内容
CSS：页面布局设置，字体颜色，字体大小样式
JS：依据不同效果

元素的特征：根据页面设计规则，有些特征是唯一 ==开发遵循了这个规则
id ： 类比身份证号  ==仅限于当前页面   username   username
注意： 如果id 不是固定的话，就不能使用来定位！ 

xpath:
1、绝对路径：/html/body/div/div/div[1]/a/b   ---根节点，顺序性、继承关系--失效
== 面试不说，工作里不用；
2、相对路径：只靠自己的特征定位   // 开头 --加上我关心节点

对页面进行对应的操作：
1、点击：click
2、传值：send_keys
3、获取页面文本 ： text

但凡是切换了页面，页面没有加载完，元素不显示 === 最好加个等待；
三种等待方式：
1、强制等待： time.sleep(5)  == 没有完成等待时间  不往下执行；
2、智能等待：
  隐式等待： 可以设置等待时间，再这个等待时间还没有结束之前元素找到了，不继续等待，继续执行下面的代码；--灵活
  注意：一个session 里只执行一次。 
  显示等待：expected_condition  ==Python班级
  
八大元素定位方式
三大等待
四大操作 
'''
driver.find_element_by_id("username").send_keys("test123")    # 找到了有username这个id的元素--点击,输入内容
driver.find_element_by_id("password").send_keys("123456")
driver.find_element_by_id("btnSubmit").click()

# driver.find_element_by_xpath("//input[@id='username']").send_keys("test123")
page_text = driver.find_element_by_xpath('//div[@class="login-logo"]//b').text  # 找到这个元素的位置之后获取文本 ，赋值给变量
page_tile = driver.title  # 获取页面的标题
print("这个页面的标题是：{}".format(page_tile))
if page_text == "柠檬ERP":
    print("这个页面的标题是：{}".format(page_text))
else:
    print("这个条件测试用例不通过！")
# 第五条用例
# time.sleep(5)   # 强制等待5s
login_user = driver.find_element_by_xpath("//p[text()='测试用户']").text  # 获取到登录用例名
if login_user == "测试用户":
    print("这个登录的用户是：{}".format(login_user))
else:
    print("这个条件测试用例不通过！")
# 点击零售出库
driver.find_element_by_xpath("//span[text()='零售出库']").click()
# 点击搜索
# driver.find_element_by_id("searchNumber").send_keys("314")

'''
1、识别是否有子页面的方式：页面层级路径里出现iframe：就需要去切换iframe 才可以进行元素的定位。
2、怎么去切换：
1）找到这个iframe元素，切换 
'''
# id = driver.find_element_by_xpath("//iframe[@id='tabpanel-bafba10ab5-frame']")
# driver.switch_to.frame('tabpanel-bafba10ab5-frame')

P_id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")
F_id = P_id+"-frame"
# driver.switch_to.frame(F_id)
# driver.find_element_by_id("searchNumber").send_keys("314")
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(F_id)))
# driver.find_element_by_id("searchNumber").send_keys("314")
driver.switch_to.frame(1)
driver.find_element_by_id("searchNumber").send_keys("314")
driver.find_element_by_id("searchBtn").click()
time.sleep(0.5)
num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]').text

