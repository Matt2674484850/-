# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '用户登录界面.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from 副文件 import img_rc
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_JSB_logon(QMainWindow):
    def setupUi(self, JSB_logon):
        JSB_logon.setObjectName("JSB_logon")
        JSB_logon.resize(400, 342)
        font = QtGui.QFont()
        font.setFamily("楷体")
        JSB_logon.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/数据图标/图片文件夹/记事本 .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        JSB_logon.setWindowIcon(icon)
        JSB_logon.setStyleSheet("#JSB_logon{border-image: url(:/背景/图片文件夹/壁纸 008.jpg);}")
        # 使窗口居中
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) // 2
        newTop = (screen.height() - size.height()) // 2
        self.move(newLeft, newTop)
        self.centralwidget = QtWidgets.QWidget(JSB_logon)
        self.centralwidget.setObjectName("centralwidget")
        self.LOGON_title = QtWidgets.QLabel(self.centralwidget)
        self.LOGON_title.setGeometry(QtCore.QRect(0, 0, 401, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        self.LOGON_title.setFont(font)
        self.LOGON_title.setStyleSheet("color: rgb(255, 0, 0);")
        self.LOGON_title.setAlignment(QtCore.Qt.AlignCenter)
        self.LOGON_title.setObjectName("LOGON_title")
        self.LOGON_zhanghu = QtWidgets.QLabel(self.centralwidget)
        self.LOGON_zhanghu.setGeometry(QtCore.QRect(0, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.LOGON_zhanghu.setFont(font)
        self.LOGON_zhanghu.setStyleSheet("color: rgb(255, 255, 255);")
        self.LOGON_zhanghu.setAlignment(QtCore.Qt.AlignCenter)
        self.LOGON_zhanghu.setObjectName("LOGON_zhanghu")
        self.LOGON_key1 = QtWidgets.QLabel(self.centralwidget)
        self.LOGON_key1.setGeometry(QtCore.QRect(0, 130, 71, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(11)
        self.LOGON_key1.setFont(font)
        self.LOGON_key1.setStyleSheet("color: rgb(255, 255, 255);")
        self.LOGON_key1.setAlignment(QtCore.Qt.AlignCenter)
        self.LOGON_key1.setObjectName("LOGON_key1")
        self.LOGON_zhanghu_input = QtWidgets.QLineEdit(self.centralwidget)
        self.LOGON_zhanghu_input.setGeometry(QtCore.QRect(160, 85, 221, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        self.LOGON_zhanghu_input.setFont(font)
        self.LOGON_zhanghu_input.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);")
        self.LOGON_zhanghu_input.setMaxLength(15)
        self.LOGON_zhanghu_input.setFrame(False)
        self.LOGON_zhanghu_input.setObjectName("LOGON_zhanghu_input")
        self.LOGON_key1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.LOGON_key1_input.setGeometry(QtCore.QRect(160, 135, 221, 20))
        font = QtGui.QFont()
        font.setFamily("楷体")
        self.LOGON_key1_input.setFont(font)
        self.LOGON_key1_input.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);")
        self.LOGON_key1_input.setInputMask("")
        self.LOGON_key1_input.setMaxLength(8)
        self.LOGON_key1_input.setFrame(False)
        self.LOGON_key1_input.setCursorPosition(0)
        self.LOGON_key1_input.setObjectName("LOGON_key1_input")
        self.LOGON_logonbutton = QtWidgets.QPushButton(self.centralwidget)
        self.LOGON_logonbutton.setGeometry(QtCore.QRect(160, 230, 80, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.LOGON_logonbutton.setFont(font)
        self.LOGON_logonbutton.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/日记本图标/图片文件夹/记事本用户登录.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LOGON_logonbutton.setIcon(icon1)
        self.LOGON_logonbutton.setDefault(False)
        self.LOGON_logonbutton.setFlat(False)
        self.LOGON_logonbutton.setObjectName("LOGON_logonbutton")
        self.LOGON_zhucebutton = QtWidgets.QPushButton(self.centralwidget)
        self.LOGON_zhucebutton.setGeometry(QtCore.QRect(50, 230, 80, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.LOGON_zhucebutton.setFont(font)
        self.LOGON_zhucebutton.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/日记本图标/图片文件夹/记事本注册.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LOGON_zhucebutton.setIcon(icon2)
        self.LOGON_zhucebutton.setObjectName("LOGON_zhucebutton")
        self.LOGON_backbutton = QtWidgets.QPushButton(self.centralwidget)
        self.LOGON_backbutton.setGeometry(QtCore.QRect(270, 230, 80, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.LOGON_backbutton.setFont(font)
        self.LOGON_backbutton.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/日记本图标/图片文件夹/记事本退出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LOGON_backbutton.setIcon(icon3)
        self.LOGON_backbutton.setObjectName("LOGON_backbutton")
        self.LOGON_warning = QtWidgets.QLabel(self.centralwidget)
        self.LOGON_warning.setGeometry(QtCore.QRect(30, 170, 341, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.LOGON_warning.setFont(font)
        self.LOGON_warning.setStyleSheet("color: rgb(255, 0, 0);\n"
"color: rgb(85, 255, 0);")
        self.LOGON_warning.setAlignment(QtCore.Qt.AlignCenter)
        self.LOGON_warning.setObjectName("LOGON_warning")
        self.LOGON_neverlogon = QtWidgets.QRadioButton(self.centralwidget)
        self.LOGON_neverlogon.setGeometry(QtCore.QRect(60, 270, 89, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.LOGON_neverlogon.setFont(font)
        self.LOGON_neverlogon.setObjectName("LOGON_neverlogon")
        self.LOGON_forgetbutton = QtWidgets.QPushButton(self.centralwidget)
        self.LOGON_forgetbutton.setGeometry(QtCore.QRect(270, 270, 131, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.LOGON_forgetbutton.setFont(font)
        self.LOGON_forgetbutton.setStyleSheet("background-color: rgb(255, 255, 255,0);\n"
"")
        self.LOGON_forgetbutton.setObjectName("LOGON_forgetbutton")
        JSB_logon.setCentralWidget(self.centralwidget)

        self.retranslateUi(JSB_logon)
        QtCore.QMetaObject.connectSlotsByName(JSB_logon)

    def retranslateUi(self, JSB_logon):
        _translate = QtCore.QCoreApplication.translate
        JSB_logon.setWindowTitle(_translate("JSB_logon", "MainWindow"))
        self.LOGON_title.setText(_translate("JSB_logon", "登录界面"))
        self.LOGON_zhanghu.setText(_translate("JSB_logon", "账户："))
        self.LOGON_key1.setText(_translate("JSB_logon", "密码："))
        self.LOGON_zhanghu_input.setPlaceholderText(_translate("JSB_logon", "账户名最多15个字"))
        self.LOGON_key1_input.setPlaceholderText(_translate("JSB_logon", "密码只能8位整数"))
        self.LOGON_logonbutton.setToolTip(_translate("JSB_logon", "Ctrl+Enter"))
        self.LOGON_logonbutton.setText(_translate("JSB_logon", "登录"))
        self.LOGON_logonbutton.setShortcut(_translate("JSB_logon", "Ctrl+Return"))
        self.LOGON_zhucebutton.setToolTip(_translate("JSB_logon", "Ctrl+N"))
        self.LOGON_zhucebutton.setText(_translate("JSB_logon", "注册"))
        self.LOGON_zhucebutton.setShortcut(_translate("JSB_logon", "Ctrl+N"))
        self.LOGON_backbutton.setToolTip(_translate("JSB_logon", "Ctrl+B"))
        self.LOGON_backbutton.setText(_translate("JSB_logon", "退出"))
        self.LOGON_backbutton.setShortcut(_translate("JSB_logon", "Ctrl+B"))
        self.LOGON_warning.setText(_translate("JSB_logon", "账号已存在，换一个注册吧！"))
        self.LOGON_neverlogon.setToolTip(_translate("JSB_logon", "此后不再弹出登录界面"))
        self.LOGON_neverlogon.setText(_translate("JSB_logon", "自动登录"))
        self.LOGON_forgetbutton.setText(_translate("JSB_logon", "忘记密码？重新设置"))
        self.LOGON_key1_input.setValidator(QtGui.QIntValidator(10000000,99999999))
        self.LOGON_key1_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.LOGON_warning.hide()
        JSB_logon.setWindowFlags( QtCore.Qt.FramelessWindowHint)
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

    def __init__(self):
        super(Ui_JSB_logon, self).__init__()
        self.setupUi(self)

