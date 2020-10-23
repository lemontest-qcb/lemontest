#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/10/12 20:42 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
自己取的名字= 标识符：project 名字，包名，python file 名字 === 命名规则 --- 变量  函数名
1、只能包含数字、字母、下划线
2、不能以数字开头
3、不能用关键字 --- keyword  == 不需要记==用了会报错
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
4、不同数字和字母之间，下划线隔开--建议 --- 美观，易于阅读  Python_Lesson_Qcb_01 --驼峰命名 --类

Python的注释：
1、为什么需要注释？
1）注释--解释代码，方便阅读 ： 自己，别人
2）功能被删除-修改  == 注释掉 ==不会影响运行 ，保留备份
2、注释方式：
1）单行注释： # 后面的内容 会被注释掉
2）多行注释： 成对的三引号 包裹的内容 --注释掉
3）快捷键：ctrl + /  ---选中多行，多行注释，再次执行--反注释

Python基础语法：
1） Python对缩进非常敏感：父子关系--缩进 === 顶格编写 : 循环  函数
2）Python 没有分号
3）Python区分大小写
'''

# print("全程班小丑是最帅的！") # 打印内容
# print("全程班竹心是最美的！")

# print() -- 内置函数：Python定义好的，可以直接用的功能 === 打印内容到控制台

"""
python常用的数据类型：整型 （int）,浮点型（float）,布尔型（bool）：True（1）  False（0）
字符串（str）， 列表  元组  字典  集合
确定数据类型-：
1）type()--内置函数：判断数据类型
2）isinstance()：--- 结果是bool：True--类型对的， False—类型错误

字符串（str）：被成对的引号包裹的任何内容字符串-- '',"",""" """  
1) 引号嵌套 :单 双 三  
2) 三引号: 可以保持格式-- 所见即所得 =换行
"""
# print(type(3.1415926535))
# print(type(12))
# print(isinstance(12.1,int))
print("全程班'阿dflkjdf刁'"
      "是最漂亮的！")
print('''----竹心-----
name:竹心
     age: 24
         hobby: 百家讲坛
'''
      )
# print(type("""123abc！"""))
