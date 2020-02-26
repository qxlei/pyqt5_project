#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 @Author:qxl
 @Time:2019/12/21 0021 16:19
 @File:可变参数与关键字参数.py
"""


#可变参数
#相对于是对list或者数组参数的扩展

def fact(*num):
    sum = 0
    for i in num:
        sum += i
    print("sum:", sum)

# 关键字参数, 增加扩展能力
def keypara(a, *b, **key):
    print("a:", a, "b:", b, "key:", key)
if __name__ == "__main__":
    num = [1, 2, 3, 4]
    fact(*num)

    a = 0
    b = [1, 2]
    key = {"num1":"L", "num2": "M"}
    keypara(a, *b, **key)


