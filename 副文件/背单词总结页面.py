# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '背单词总结页面.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QCursor
from 六七 import Homepages
from 六七 import MyQLabel
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time


class Ui_Beidanci_Finally(QMainWindow):
    def setupUi(self, Beidanci_Finally):
        Beidanci_Finally.setObjectName("Beidanci_Finally")
        Beidanci_Finally.setWindowModality(QtCore.Qt.WindowModal)
        Beidanci_Finally.resize(400, 322)
        font = QtGui.QFont()
        font.setFamily("楷体")
        Beidanci_Finally.setFont(font)
        Beidanci_Finally.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/小窗口图标/图片文件夹/成绩单.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Beidanci_Finally.setWindowIcon(icon)
        Beidanci_Finally.setStyleSheet("#Beidanci_Finally{border-image: url(:/小窗口图标/图片文件夹/背单词总结页面背景图.webp);}")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Beidanci_Finally)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 60, 401, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.zhengquelv = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.zhengquelv.setFont(font)
        self.zhengquelv.setObjectName("zhengquelv")
        self.horizontalLayout.addWidget(self.zhengquelv)
        self.zhengquelv_input = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(50)
        self.zhengquelv_input.setFont(font)
        self.zhengquelv_input.setObjectName("zhengquelv_input")
        self.horizontalLayout.addWidget(self.zhengquelv_input)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Beidanci_Finally)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 140, 401, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cuo_wulist = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.cuo_wulist.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.cuo_wulist.setFont(font)
        self.cuo_wulist.setObjectName("cuo_wulist")
        self.horizontalLayout_2.addWidget(self.cuo_wulist)
        self.cuowu_input = MyQLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setUnderline(False)
        self.cuowu_input.setFont(font)
        self.cuowu_input.setWordWrap(True)
        self.cuowu_input.setObjectName("cuowu_input")
        self.horizontalLayout_2.addWidget(self.cuowu_input)
        self.xiangmu = QtWidgets.QLabel(Beidanci_Finally)
        self.xiangmu.setGeometry(QtCore.QRect(190, 20, 201, 16))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setUnderline(True)
        self.xiangmu.setFont(font)
        self.xiangmu.setObjectName("xiangmu")
        self.good = QtWidgets.QLabel(Beidanci_Finally)
        self.good.setGeometry(QtCore.QRect(10, 230, 371, 21))
        self.good.setObjectName("good")
        self.star1 = QtWidgets.QPushButton(Beidanci_Finally)
        self.star1.setGeometry(QtCore.QRect(70, 250, 41, 31))
        self.star1.setStyleSheet("border-image: url(:/小窗口图标/图片文件夹/星星.png);\n"
"border-image: url(:/小窗口图标/图片文件夹/星星 (1).png);")
        self.star1.setText("")
        self.star1.setObjectName("star1")
        self.star1_2 = QtWidgets.QPushButton(Beidanci_Finally)
        self.star1_2.setGeometry(QtCore.QRect(120, 250, 41, 31))
        self.star1_2.setStyleSheet("border-image: url(:/小窗口图标/图片文件夹/星星.png);\n"
"border-image: url(:/小窗口图标/图片文件夹/星星 (1).png);")
        self.star1_2.setText("")
        self.star1_2.setObjectName("star1_2")
        self.star1_3 = QtWidgets.QPushButton(Beidanci_Finally)
        self.star1_3.setGeometry(QtCore.QRect(170, 250, 41, 31))
        self.star1_3.setStyleSheet("border-image: url(:/小窗口图标/图片文件夹/星星.png);\n"
"border-image: url(:/小窗口图标/图片文件夹/星星 (1).png);")
        self.star1_3.setText("")
        self.star1_3.setObjectName("star1_3")
        self.star1_4 = QtWidgets.QPushButton(Beidanci_Finally)
        self.star1_4.setGeometry(QtCore.QRect(220, 250, 41, 31))
        self.star1_4.setStyleSheet("border-image: url(:/小窗口图标/图片文件夹/星星.png);\n"
"border-image: url(:/小窗口图标/图片文件夹/星星 (1).png);")
        self.star1_4.setText("")
        self.star1_4.setObjectName("star1_4")
        self.star1_5 = QtWidgets.QPushButton(Beidanci_Finally)
        self.star1_5.setGeometry(QtCore.QRect(270, 250, 41, 31))
        self.star1_5.setStyleSheet("border-image: url(:/小窗口图标/图片文件夹/星星.png);\n"
"border-image: url(:/小窗口图标/图片文件夹/星星 (1).png);")
        self.star1_5.setText("")
        self.star1_5.setObjectName("star1_5")
        self.back = QtWidgets.QPushButton(Beidanci_Finally)
        self.back.setGeometry(QtCore.QRect(284, 290, 91, 23))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.back.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/子标/图片文件夹/首页.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon1)
        self.back.setObjectName("back")
        self.retranslateUi(Beidanci_Finally)
        self.back.clicked.connect(Beidanci_Finally.close)
        QtCore.QMetaObject.connectSlotsByName(Beidanci_Finally)

    def retranslateUi(self, Beidanci_Finally):
        _translate = QtCore.QCoreApplication.translate
        Beidanci_Finally.setWindowTitle(_translate("Beidanci_Finally", "默写成绩单"))
        self.back.setShortcut(_translate("Beidanci_Finally", "Return"))
        self.zhengquelv.setText(_translate("Beidanci_Finally", "正确率："))
        self.zhengquelv_input.setText(_translate("Beidanci_Finally", "正确率输入框"))
        self.cuo_wulist.setText(_translate("Beidanci_Finally", "错误列表：(点击查看具体)"))
        self.cuowu_input.setText(_translate("Beidanci_Finally", "错误内容"))
        self.xiangmu.setText(_translate("Beidanci_Finally", "项目 ----------   背单词"))
        self.good.setText(_translate("Beidanci_Finally", ""))
        self.back.setText(_translate("Beidanci_Finally", "返回主页"))
        self.back.setFlat(True)
        self.star1.hide()
        self.star1_2.hide()
        self.star1_3.hide()
        self.star1_4.hide()
        self.star1_5.hide()
        self.back.hide()
        # 使窗口居中
        Beidanci_Finally.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) // 2
        newTop = (screen.height() - size.height()) // 2
        self.move(newLeft, newTop)
        _startPos = None
        _endPos = None
        _isTracking = False

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        try:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)
        except:
            pass

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def __init__(self,matt):
        Homepages.YWmessage = matt
        super(Ui_Beidanci_Finally,self).__init__()
        self.setupUi(self)
from 副文件 import img_rc




