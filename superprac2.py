#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 @Author:qxl
 @Time:2019/12/21 0021 19:14
 @File:superprac2.py
"""

class FatFather(object):
    def __init__(self, name, *args, **kwargs):
        print()
        print("======start call FatFather==========")
        self.name = name
        print("The FatFather class's name is %s" % self.name)
        print("FatFather init end")
        print()
        print("=======call FatFather end")


class FatBoss(FatFather):
    def __init__(self, name, hobby, *args, **kwargs):
        print()
        print("========start call FatBoos=====")
        super().__init__(name, *args, **kwargs)
        print("%s hobby is %s" % (name, hobby))
        print(" call FatBoos end")

class FatBossWife(FatFather):
    def __init__(self, name, housework, *args, **kwargs):
        print()
        print("========start call FatBoosWife=====")
        super().__init__(name, *args, **kwargs)
        print("%s housework is %s" % (name, housework))
        print(" call FatBoosWife end")

class FatBossGirl(FatBoss, FatBossWife):
    def __init__(self, name, hobby, housework, *args, **kwargs):
        print()
        print("========start call FatBoosGirl=====")
        super().__init__(name, hobby, housework, *args, **kwargs)

def main():
    print("print FatBossGirl class MRO")
    print(FatBossGirl.__mro__)
    print()

    print("the call order")
    girl = FatBossGirl("FatBoss", "LandLord", "sweep")
if __name__ == "__main__":
    main()