#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/10/14 19:45 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司
'''
1、find  --- 可以
2、 _num --- 可以
3、7val ---  不可：数字开头
4、add. ---  不可 .
5、def --- 不可--关键字
6、pan --- 可以
7、-print  --- No
8、open_file --- YES
9、FileName --- YES
10、print --  可以：但是不建议，内置函数的名字 -- 因为一旦使用了，这个函数不能用了
11、INPUT  --- 可以 input
12、ls -- 可以
13、user^name --- 不可以
14、list1 --可以
15、str_ --- 可以
'''
'''
变量：存储数据的  ==  保险柜：钱，金条，户口本，珠宝，古董，砖头，纸，衣服，鞋子 --存储东西
数据类型：int  float bool str 
变量名：标识符 --1,2,3,4
5、见名知意：
6、 变量名一定要先申明（定义并赋值），再调用，否则报错

字符串的操作：
1、取值：元素 位置--索引，从0开始，依次加1 
2、取多个值： 切片-- [开始:结束:步长] === 取头不取尾
开始头--省略 == 默认从0开始
结束 -- 省略 == 默认末尾结束
步长 --省略  == 默认为1
3、负数:从右边开始取  -1--最后一个
4、元素个数 ：len()--内置函数：统计元素个数（长度）
5、替换字符串里的元素 ：replace（）
6、
'''
info = "全程班小丑是最帅的！"  # 定义了一个 变量，赋值  === 初始化，申明
# name = "彩虹"
str1 = "hello world!"
#       01234567891011
# print(str1[9])
# print(str1[0:len(str1):5])
# print(str1[-2])
# print(len(str1))
# # str1 = str1.replace("world","Tricy")
# print(str1)
# # print(str1.index("G"))  # 如果元素没有找到--会报错，代码终止运行
# print(str1.find("l"))  # 如果元素没有找到- 不会报错，返回-1
# print(str1.count("l"))
'''
格式化输出：
第一种：.format()
1、 占位符： {} --传 变量的地方   .format（）
2、.format() 可以默认按顺序传入变量；  也可以指定位置传入变量 === 注意：不能混合使用
第二种：%s--字符串 ==匹配所有  %d--整数  %f--小数  --了解
'''
# name = "一叶"
# age = 19
# hobby = "学习"
# print('''----{1}-----
# name:{1}
# age: {0}
# hobby: {3}
# '''.format(age,name,age,hobby))

# name = "一叶"
# age = 19
# hobby = "学习"
# print('''----%s-----
# name:%s
# age: %s
# hobby: %s
# '''%(age,name,age,hobby))

'''
Python运算符：
1、算术运算符：+ - * / % **
2、赋值运算符： = += -=  : 方向性-- 右边赋值左边
3、比较运算符： < <= > >=  == !=    ---- 运算结果是布尔值True False
4、逻辑运算符: 与-and== 真真为真  或--or==假假为假   非-not  ---运算结果是布尔值True False
5、成员运算符：in, not in----运算结果是布尔值True False
if 判断 
'''
# print(10 + 20)  # 两个数字的相加
# print("love"+"Tricy")  # 两个字符串的拼接
# print(str(123) + "abc")
# # int --》 str ：str()--强制字符串的转化, int()--整型 float() bool()
# print(30 - 10) # 两个数字的相减
# print(2 * 3)  # 两个数字的相乘
# print("I love you" * 3000)  # 字符串重复输出 * 次数
# print(10 / 3)  # 结果浮点型
# a = 10
# a += 10 # == a = a + 10
# a -= 5 # a = a - 5
# print(a)
# print(2 > 3)
# print("登录成功" != "登录成功") # 判断字符串是否相同 === 执行结果  vs  预期结果
# print(not 2 > 3)
# str2 = "python"
# print("Y" not in str2)

num = input("请输入你的数字：") # input() ---内置函数：在控制台输入数据--赋值给num这个变量
print(num)