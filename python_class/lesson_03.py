#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/10/16 19:23 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
2、现在有字符串：str1 = 'python hello aaa 123123aabb'
1）请取出并打印字符串中的'python'。
2）请分别判断 'o a' 'he' 'ab' 是否是该字符串中的成员？
3）替换python为 “lemon”.
4) 找到aaa的起始位置
'''
# name = input("请输入姓名：")
# gender = input("请输入性别：")
# age = input("请输入年龄：")
# print("*" * 20)
# print('''name:{}
# gender:{}
# age:{}'''.format(name,gender,age))
# print("*" * 20)
# str1 = 'python hello aaa 123123aabb'
# print(str1[:6:])
# print('he' not in str1)
# print(str1.replace("python","lemon"))
# print(str1.find("aaa"))
# print(str1.index("aaa"))
'''
常用数据类型续：列表（list）  元组  字典  集合
列表（list） ： [],元素之间用英文的逗号 
1、元素可以是任意的是数据类型：int  float  bool  str  list tuple...
2、取值：索引取值--类比字符串 
取多个值：切片
扩展：列表的嵌套取值
3、列表的元素是可以被改变的！--增加，修改，删除 --重点
4、列表的元素是可以重复的---统计个数--count
5、len（）---- 统计元素个数
'''
# list1 = [20,3.14,True,"七木","荷花鱼",[1,2,3,4]]  # 空列表
# print(list1[3:5])
# print(list1[5][1])
# # 增加
# list1.append("焕蓝")  # 默认追加元素到列表的末尾  -P1
# list1.insert(5,"kingo") # 指定位置进行元素插入   --P2
# list1.extend(["十又","bingo","陌上寸草","大丑"])  # 两个列表合并   --P3
# print(list1)
# # 删除
# list1.pop(0)  # 默认删除最后一个元素，也可以指定位置（索引）进行删除
# list1.remove(3.14) # 指定元素本身进行删除
# # list1.clear()  # 清楚所有元素
# print(list1)
# # 修改  --  取值-重新赋值
# list1[4] = "Amiee"
# list1[0] = "方方土"
# print(list1)
# list1.append("方方土")
# print(list1)
# print(list1.count("方方土"))
# print(len(list1))
'''
元组：tuple , ()
1、元素可以是任意的是数据类型：int  float  bool  str  list tuple...
2、取值：索引取值--类比字符串 
取多个值：切片
扩展：列表的嵌套取值
3、元组的元素是不可以被改变的！
4、元组的元素是可以重复的---统计个数--count
5、len（）---- 统计元素个数
6、list（）  tuple（）  --- 扩展：数据类型转化 
'''
# tuple1 = ('方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝', '十又', 'bingo', '陌上寸草','大丑')
# # tuple1[-1] = "小丑"  ---不可以
# print(tuple1.count('大丑'))
# list1 = list(tuple1)  # 把元组转化为列表
# list1[-1] = "小丑"
# print(list1)
# tuple2 = tuple(list1)
# print(tuple2)
'''
字典：dict  {}
1、元素：key：value （键值对）--excel 表头  值
2、场景：存储数据属性 ：人--名字 身高 体重 
key: 1）不能是可以改变的数据类型（list，dict）--- 最常用的是字符串；
     2）不能重复的，唯一的
value: 可以是任意数据类型 --可以被改变== 增删改
3、字典是没有顺序的！！-- 不能用索引取值-  取值：通过key 取value
4、len() --- 长度
'''
# dict1 = {"name":"tan","height":"173","weight":"160"} # 空字典
# print(dict1["height"])  # key--value 1
# print(dict1.get("weight"))  # key  -- value  2
# # 修改
# dict1["weight"] = "150"   # key存在，修改对应key的value
# print(dict1)
# # 增加
# dict1["age"] = 18  # key不存在，新增加键值对
# print(dict1)
# dict1.update({"city":"北京","hobby":"学习Python","name":"male"})  # 字典的合并
# # 删除
# # dict1.pop("weight")  # 指定key删除 对应的键值对
# print(dict1)
# del dict1  # 变量存储 删除--对象不存在了
# print(dict1)
'''
集合；set  {}，元素单个    --了解
1、无序
2、元素不可以重复 —使用场景：去重
'''
# list2 = [11,22,11,33,11,11]  # 去重
# set1 = set(list2)   # set() --list2 转化为集合
# print(set1)
# list3 = list(set1)  # list() --set1 转化为列表
# print(list3)

'''
控制流：代码的执行顺序 --从上至下一次执行： 判断  循环
判断：if 语法
if 条件： --- 成立（bool值 True） ---冒号：缩进（4个空格=tab键）
    子代码（执行语言）
elif 条件：---成立
    执行语句（子代码）
... (elif可以没有，可以有多个)
else：（后面没有条件--兜底） --可以没有
    执行语句
'''
# money = int(input("请输入你的余额："))  # input（）控制台输入--数据类型--字符串
# if money >= 500:   #  False
#     print("买别墅！")
# elif money >= 200:  # True
#     print("买一栋楼！")
# elif money >= 50:
#     print("买车！")
# else:
#     print("滚去工作赚钱！")


dict1 = {"name":"Tricy","age":18}
dict2 = dict(name="Tricy",age="18")
print(dict2)


