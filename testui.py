# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # Form.resize(800, 440)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(2, 0, 800, 50))
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        # self.textBrowser.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(2, 50, 800, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())

        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(800, 400))
        self.tableWidget.setMaximumSize(QtCore.QSize(800, 400))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 单元格不可编辑
        # self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setRowCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)

        # 设置全局数据
        rows_number = 8
        columns_number = 9
        header_columns = ["线路", "终点站", "发车时间"]

        # 设置每行的头
        for row_order in range(rows_number):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(row_order, item)

        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(2, item)

        # 设置每一列的表头
        for head_order in range(columns_number):
            if head_order % 3 == 0:
                headname = header_columns[0]
            elif head_order % 3 == 1:
                headname = header_columns[1]
            else:
                headname = header_columns[2]

            item = QtWidgets.QTableWidgetItem(headname)
            print(head_order, type(item))

            # 设置名称

            # 表头字体
            font = QtGui.QFont()
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)

            # 设置颜色
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            item.setBackground(brush)

            brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            item.setForeground(brush)

            self.tableWidget.setHorizontalHeaderItem(head_order, item)

        # 表头的字段设置
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(6, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(7, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(8, item)

        # 表中0行0列的属性
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # font.setBold(True)
        # font.setWeight(75)
        # item.setFont(font)
        # brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # item.setBackground(brush)
        # brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        # brush.setStyle(QtCore.Qt.SolidPattern)
        # item.setForeground(brush)
        # self.tableWidget.setItem(0, 0, item)

        # 表中单元格的属性【坐标是row，col】
        for row in range(rows_number):
            for col in range(columns_number):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # 字体居中
                font = QtGui.QFont()
                font.setPointSize(10)  # 字体大小
                font.setBold(True)  # 加粗
                font.setWeight(75)
                item.setFont(font)
                brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))  # 设置单元格的背景颜色
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setBackground(brush)
                brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))  # 设置单元格字体颜色
                brush.setStyle(QtCore.Qt.SolidPattern)
                item.setForeground(brush)
                item.setFlags(QtCore.Qt.NoItemFlags)  # 不可选中单元格
                self.tableWidget.setItem(row, col, item)

                # item = QtWidgets.QTableWidgetItem()
                # item.setTextAlignment(QtCore.Qt.AlignCenter)
                # self.tableWidget.setItem(0, 2, item)
                #
                # item = QtWidgets.QTableWidgetItem()
                # self.tableWidget.setItem(3, 3, item)
                #
                # item = QtWidgets.QTableWidgetItem()
                # self.tableWidget.setItem(1, 0, item)
                # item = QtWidgets.QTableWidgetItem()
                # self.tableWidget.setItem(2, 0, item)
                # item = QtWidgets.QTableWidgetItem()
                # self.tableWidget.setItem(2, 6, item)
                # item = QtWidgets.QTableWidgetItem()
                # self.tableWidget.setItem(2, 7, item)
                # item = QtWidgets.QTableWidgetItem()
                # self.tableWidget.setItem(2, 8, item)

        # 设置表头属性
        self.tableWidget.horizontalHeader().setVisible(True)
        # self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(20)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section {background-color: #000;color:red; border:1px solid white;margin: 0 0 0 -1px;}")
        # border-left:1px solid #000;"
        #             "border-right:1px solid white;border-top:1px solid #000;border-bottom:1px solid #000;

        # self.tableWidget.resizeColumnToContents(1)  # 表格适应内容指定列

        # self.tableWidget.horizontalHeader().setSectionResizeMode(True)  # 列宽自动分配
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)        # 随内容分配列宽
        # 1.判断项是否设置了sizeHint，如果没有设置则按项的内容计算列宽，确保所有项的内容在一行上完整展示
        # 2.如果项设置了sizeHint，则取sizeHint的宽和水平表头horizontalHeader().minimumSectionSize()两者之间最大值作为项的列宽
        for number in range(columns_number):
            self.tableWidget.horizontalHeader().setSectionResizeMode(number, QtWidgets.QHeaderView.ResizeToContents)

        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setSectionResizeMode(True)      # 列宽自动分配
        # self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(26)
        self.tableWidget.verticalHeader().setMinimumSectionSize(10)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        # 重新填写数据
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;background-color:#000000;border-top:1px solid white;\">"
                                            "<p align=\"center\" dir=\'rtl\' style=\" margin:0 0 0 0 ; -qt-block-indent:0; text-indent:0px; \"><span style=\" font-size:20pt; font-weight:600; color:#e60000;border:1px solid white;\">火车站</span></p></body></html>"))
        self.tableWidget.setSortingEnabled(False)

        # tableWidget.verticalHeaderItem 表头行名 row
        for i in range(3):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("Form", str(i)))

        # item = self.tableWidget.verticalHeaderItem(0)
        # item.setText(_translate("Form", "0"))
        # item = self.tableWidget.verticalHeaderItem(1)
        # item.setText(_translate("Form", "1"))
        # item = self.tableWidget.verticalHeaderItem(2)
        # item.setText(_translate("Form", "2"))

        # item = self.tableWidget.horizontalHeaderItem(1)
        # item.setText(_translate("Form", "终点站"))
        # item = self.tableWidget.horizontalHeaderItem(2)
        # item.setText(_translate("Form", "待发车时间"))
        # item = self.tableWidget.horizontalHeaderItem(3)
        #
        # item.setText(_translate("Form", "线路"))
        # item = self.tableWidget.horizontalHeaderItem(4)
        # item.setText(_translate("Form", "终点站"))
        # item = self.tableWidget.horizontalHeaderItem(5)
        # item.setText(_translate("Form", "待发车时间"))
        #
        # item = self.tableWidget.horizontalHeaderItem(6)
        # item.setText(_translate("Form", "线路"))
        # item = self.tableWidget.horizontalHeaderItem(7)
        # item.setText(_translate("Form", "终点站"))
        # item = self.tableWidget.horizontalHeaderItem(8)
        # item.setText(_translate("Form", "待发车时间"))

        # __sortingEnabled = self.tableWidget.isSortingEnabled()
        # self.tableWidget.setSortingEnabled(False)
        #
        # item = self.tableWidget.item(0, 0)
        # item.setText(_translate("Form", "SHE路"))
        #
        # item = self.tableWidget.item(3, 3)
        # item.setText(_translate("Form", ""))
        #
        # item = self.tableWidget.item(0, 1)
        # item.setText(_translate("Form", "嘉兴花园"))
        # item = self.tableWidget.item(0, 2)
        # item.setText(_translate("Form", "07:00:00"))
        # item = self.tableWidget.item(2, 6)
        # item.setText(_translate("Form", "辅100"))
        # item = self.tableWidget.item(2, 7)
        # item.setText(_translate("Form", "重点科技"))
        # item = self.tableWidget.item(2, 8)
        # item.setText(_translate("Form", "08:00:00"))

        # self.tableWidget.setSortingEnabled(__sortingEnabled)
