# coding:utf-8

"""
Author      : converse
filename    : update.py
created Date: 2020/3/5 15:52
software    : PyCharm
version     : 3.7.2
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import time


class UpdateData(QThread):
    """更新数据类"""
    update_date = pyqtSignal(str)  # pyqt5 支持python3的str，没有Qstring

    def run(self):
        cnt = 0
        while True:
            cnt += 1
            self.update_date.emit(str(cnt))  # 发射信号
            time.sleep(1)
