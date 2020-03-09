# coding:utf-8

"""
Author      : converse
filename    : main.py
created Date: 2020/3/5 15:16
software    : PyCharm
version     : 3.7.2
"""
import sys
import time
from testui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import json


class MyWindow(QTableWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)     # 将窗体隐藏

    def update_item_data(self, data):
        """更新内容"""
        # self.setItem(3, 3, QTableWidgetItem(data))    # 设置表格内容(行， 列) 文字
        data_dict = data
        for coordinate, value in data_dict.items():
            x, y = coordinate.split(",")

            _translate = QtCore.QCoreApplication.translate  #
            item = self.tableWidget.item(int(x), int(y))  # 更新到坐标点
            item.setText(_translate("Form", value))  # 更新到Form中的语句
        print(data_dict)


class UpdateData(QThread):
    """更新数据类"""
    update_date = pyqtSignal(dict)  # pyqt5 支持python3的str, int, dict 等

    def run(self):
        cnt = 0
        while True:
            cnt += 1
            self.update_date.emit({"0,1": "嘉兴花园", "2,2": ""})  # 发射信号
            self.sleep(10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    # TODO 自适应的单元格，以及需要单元格自动调节大小。

    # 启动更新线程
    update_data_thread = UpdateData()
    update_data_thread.update_date.connect(myWin.update_item_data)  # 链接信号
    update_data_thread.start()

    # resize()方法调整窗口的大小。这离是800px宽440px高
    myWin.resize(804, 440)

    # move()方法移动窗口在屏幕上的位置到x = 0，y = 0坐标。
    myWin.move(20, 20)
    # 设置窗口的标题
    myWin.setWindowTitle('Simple')
    # 显示在屏幕上

    myWin.show()
    sys.exit(app.exec_())
