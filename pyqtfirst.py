#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 @Author:qxl
 @Time:2019/12/21 0021 15:26
 @File:pyqtfirst.py
"""

from PyQt5.QtWidgets import *

import sys
class SigalSlotDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def onClick(self):
        self.btn.setText("sent signal")
        # self.btn.setStyleSheet()
    def initUI(self):
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('signal nad slot')
        self.btn = QPushButton("button")
        self.btn.clicked.connect(self.onClick)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = SigalSlotDemo()
    gui.show()
    sys.exit(app.exec_())