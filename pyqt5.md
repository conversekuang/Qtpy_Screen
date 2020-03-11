## 								PyQt

​	需要在单机上显示界面上动态显示数据。

> 介绍与安装

PyQt官方数据手册

 https://www.riverbankcomputing.com/static/Docs/PyQt5/ 



5.13.0版本需要统一

pyqt5的安装和pyqt5-tools

​	 https://www.cnblogs.com/yclizq/p/11192128.html 

​	 https://blog.csdn.net/Cc_Sonia/article/details/83625298 



在pyqt5-tools中，有一个Py designer，可以对空间进行画图生成ui文件，再转成py文件。方便布局。后面再根据需求，自行调整即可。

Py designer的使用流程

 https://www.jianshu.com/p/5b063c5745d0 



Pyqt的介绍

 https://fishc.com.cn/forum.php?mod=viewthread&tid=59816&extra=page%3D1&page=1 



> 实现动态数据的方法

signal的用法

 https://www.cnblogs.com/XJT2018/p/10222981.html 



> 表格布局设置

表格头的设置

 https://blog.csdn.net/LaoYuanPython/article/details/103656856 



表格布局

 https://blog.csdn.net/yl_best/article/details/84070231 



tableview

 https://blog.csdn.net/qq_26093511/article/details/82861767 



表格样式的改变

```
self.tableWidget.horizontalHeader().setStyleSheet()
```



> 关于tableWidget 表头宽度的设置



PyQt（Python+Qt）学习随笔：QHeaderView.ResizeMode取值及含义

 https://blog.csdn.net/LaoYuanPython/article/details/104599978 



PyQt（Python+Qt）学习随笔：QTableWidget表格部件中行高和列宽的计算方式

 https://blog.csdn.net/LaoYuanPython/article/details/104600195 





Pyqt5之QTableWidget设置列宽行高大小的几种方式

 https://www.jianshu.com/p/ad125c7b2f8e 

```python
self.tableWidget.horizontalHeader().setSectionResizeMode(True)  
self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
# 以上两句，都可以实现列宽自动分配 

self.tableWidget.horizontalHeader().setSectionResizeMode( QtWidgets.QHeaderView.ResizeToContents)
# 列宽根据显示在一行的内容自适应

self.tableWidget.horizontalHeader().setSectionResizeMode(number, QtWidgets.QHeaderView.Interactive)
# 实现手动调整列宽
```



QTableView表格视图的宽设置（**自己设定宽度**）

 https://www.cnblogs.com/csuftzzk/p/QTableView.html 

```python
self.tableWidget.setColumnWidth(col, width)
# 输入列和对应的宽度即可，自动设置表格的每一列的宽度。
# 需要再设置完所有的之后头文件之后，再设置这个方法。
# 否则定制化的设置无效
```



 老猿Python 这个博主的PyQt文章比较多

 https://me.csdn.net/LaoYuanPython 



C++中的Qt包就是

python中的QtCore.Qt包



```python
from PyQt5.QtWidgets import QTableView, QHeaderView, QFormLayout,   QVBoxLayout,QWidget,QApplication ,QHBoxLayout, QPushButton,QMainWindow,QGridLayout,QLabel
```



![image.png](https://i.loli.net/2020/03/11/otYuQ9K1mfMXyD7.png)