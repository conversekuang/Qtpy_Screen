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
import random
import time


class MyWindow(QTableWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 将窗体隐藏

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
            x = random.randint(0, 7)
            y = int(random.randint(0, 2)) * 3
            print(x, y)
            # 更新数据要进行全屏幕的单元格更新，才可以起到刷屏的作用
            sent_data = {}
            for row in range(8):
                for col in (0, 3, 6):
                    if row == x and col == y:
                        sent_data.update({
                            str(x) + "," + str(y): "辅79",
                            str(x) + "," + str(y + 1): "嘉兴花园-领秀智谷牙博士",
                            str(x) + "," + str(y + 2): time.strftime('%H:%M:%S', time.localtime(time.time())),
                        })
                    else:
                        sent_data.update({
                            str(row) + "," + str(col): "",
                            str(row) + "," + str(col + 1): "",
                            str(row) + "," + str(col + 2): "",
                        })
            print("----{}".format(sent_data))
            # 刷屏
            self.update_date.emit(sent_data)  # 发射信号
            self.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    # TODO 自适应的单元格，以及需要单元格自动调节大小。(67099395f34436152cf8127849f commit finished)
    # TODO 自己设定单元格的宽度。下一步需要做的

    # 启动更新线程
    update_data_thread = UpdateData()
    update_data_thread.update_date.connect(myWin.update_item_data)  # 链接信号
    update_data_thread.start()

    # resize()方法调整窗口的大小。这离是800px宽440px高
    myWin.resize(804, 450)

    # move()方法移动窗口在屏幕上的位置到x = 0，y = 0坐标。
    myWin.move(20, 20)
    # 设置窗口的标题
    myWin.setWindowTitle('Simple')
    # 显示在屏幕上

    myWin.show()
    sys.exit(app.exec_())
