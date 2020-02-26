#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 @Author:qxl
 @Time:2019/12/21 0021 18:53
 @File:superprac.py
"""

class FatFather(object):
    def __init__(self, name):
        print("FatFather init start...")
        self.name = name
        print("FatFather name is %s" % self.name)
        print("FatFather init end")
#胖子老板类继承FatFather类
class FatBoss(FatFather):
    def __init__(self, name, hobby):
        print("FatFather class is called")
        self.hobby = hobby
        # FatFather.__init__(self, name) #调用父类方法的构造方法
        #modified
        super().__init__(name)
        print("%s hobby is  %s" % (name, self.hobby))
def main():
    # ff = FatFather("FatBoss Father")
    print("print FatBoss class's MRO")
    print(FatBoss.__mro__)

    print()
    print("=========下面按照MRO 顺序执行super方法===========")
    fatboss = FatBoss("FatBoss", "LandLord")

#super方法的基本概念
# 那么除了直接使用 FatFather.__init__(self,name) 的方法，还可以使用super()方法来调用
# Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :


if __name__ == "__main__":
    main()

