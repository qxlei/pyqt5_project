#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 @Author:qxl
 @Time:2019/12/21 0021 16:05
 @File:loggingprac.py
"""

import logging
#---------logging只能在stream和file中二选一显示log信息----
# logging.basicConfig(level=logging.DEBUG, filename="logging.log", format="%(asctime)s [%(lineno)d] %(message)s")#采用追加的模式
# logging.debug("debug message")
# logging.info("info")
# logging.warning("warning")
# logging.warning("error message")

#----------创建对象同时在stream和file中显示log信息----
# logger = logging.getLogger()
# logger.setLevel(level="DEBUG")
# fh = logging.FileHandler("test log")#写入文件所以需要文件名
# ch = logging.StreamHandler()
#
# fm = logging.Formatter("%(asctime)s %(message)s")
# fh.setFormatter(fm)
# ch.setFormatter(fm)
# logger.addHandler(fh)
# logger.addHandler(ch)
#
# logger.debug("debug")
# logger.info("info")
# logger.warning("warning")
# logger.error("error")



