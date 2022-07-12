# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '开锁.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from 副文件 import img_rc


class Ui_KS(QMainWindow):
    def setupUi(self, KS):
        KS.setObjectName("KS")
        KS.resize(647, 636)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        KS.setFont(font)
        KS.setFocusPolicy(QtCore.Qt.WheelFocus)
        KS.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/开锁/图片文件夹/开锁.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        KS.setWindowIcon(icon)
        KS.setStyleSheet("#KS{border-image: url(:/开锁/图片文件夹/开锁背景.jpeg);}\n"
"")
        self.centralwidget = QtWidgets.QWidget(KS)
        self.centralwidget.setObjectName("centralwidget")
        self.KS_firstText = QtWidgets.QLabel(self.centralwidget)
        self.KS_firstText.setGeometry(QtCore.QRect(270, 0, 171, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.KS_firstText.setFont(font)
        self.KS_firstText.setStyleSheet("color: rgb(0, 0, 0);")
        self.KS_firstText.setObjectName("KS_firstText")
        self.ball_1_2 = QtWidgets.QDial(self.centralwidget)
        self.ball_1_2.setGeometry(QtCore.QRect(60, 0, 41, 41))
        self.ball_1_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.ball_1_2.setMaximum(0)
        self.ball_1_2.setSingleStep(0)
        self.ball_1_2.setPageStep(0)
        self.ball_1_2.setTracking(True)
        self.ball_1_2.setNotchesVisible(False)
        self.ball_1_2.setObjectName("ball_1_2")
        self.ball_1_4 = QtWidgets.QDial(self.centralwidget)
        self.ball_1_4.setGeometry(QtCore.QRect(160, 0, 41, 41))
        self.ball_1_4.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.ball_1_4.setMaximum(0)
        self.ball_1_4.setSingleStep(0)
        self.ball_1_4.setPageStep(0)
        self.ball_1_4.setTracking(True)
        self.ball_1_4.setNotchesVisible(False)
        self.ball_1_4.setObjectName("ball_1_4")
        self.ball_1_3 = QtWidgets.QDial(self.centralwidget)
        self.ball_1_3.setGeometry(QtCore.QRect(110, 0, 41, 41))
        self.ball_1_3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.ball_1_3.setMaximum(0)
        self.ball_1_3.setSingleStep(0)
        self.ball_1_3.setPageStep(0)
        self.ball_1_3.setTracking(True)
        self.ball_1_3.setNotchesVisible(False)
        self.ball_1_3.setObjectName("ball_1_3")
        self.ball_1_1 = QtWidgets.QDial(self.centralwidget)
        self.ball_1_1.setGeometry(QtCore.QRect(10, 0, 41, 41))
        self.ball_1_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_1_1.setMaximum(0)
        self.ball_1_1.setSingleStep(0)
        self.ball_1_1.setPageStep(0)
        self.ball_1_1.setTracking(True)
        self.ball_1_1.setNotchesVisible(False)
        self.ball_1_1.setObjectName("ball_1_1")
        self.ball_2_1 = QtWidgets.QDial(self.centralwidget)
        self.ball_2_1.setGeometry(QtCore.QRect(10, 60, 41, 41))
        self.ball_2_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_2_1.setMaximum(0)
        self.ball_2_1.setSingleStep(0)
        self.ball_2_1.setPageStep(0)
        self.ball_2_1.setTracking(True)
        self.ball_2_1.setNotchesVisible(False)
        self.ball_2_1.setObjectName("ball_2_1")
        self.ball_2_3 = QtWidgets.QDial(self.centralwidget)
        self.ball_2_3.setGeometry(QtCore.QRect(110, 60, 41, 41))
        self.ball_2_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_2_3.setMaximum(0)
        self.ball_2_3.setSingleStep(0)
        self.ball_2_3.setPageStep(0)
        self.ball_2_3.setTracking(True)
        self.ball_2_3.setNotchesVisible(False)
        self.ball_2_3.setObjectName("ball_2_3")
        self.ball_2_2 = QtWidgets.QDial(self.centralwidget)
        self.ball_2_2.setGeometry(QtCore.QRect(60, 60, 41, 41))
        self.ball_2_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_2_2.setMaximum(0)
        self.ball_2_2.setSingleStep(0)
        self.ball_2_2.setPageStep(0)
        self.ball_2_2.setTracking(True)
        self.ball_2_2.setNotchesVisible(False)
        self.ball_2_2.setObjectName("ball_2_2")
        self.ball_2_4 = QtWidgets.QDial(self.centralwidget)
        self.ball_2_4.setGeometry(QtCore.QRect(160, 60, 41, 41))
        self.ball_2_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_2_4.setMaximum(0)
        self.ball_2_4.setSingleStep(0)
        self.ball_2_4.setPageStep(0)
        self.ball_2_4.setTracking(True)
        self.ball_2_4.setNotchesVisible(False)
        self.ball_2_4.setObjectName("ball_2_4")
        self.ball_3_1 = QtWidgets.QDial(self.centralwidget)
        self.ball_3_1.setGeometry(QtCore.QRect(10, 120, 41, 41))
        self.ball_3_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_3_1.setMaximum(0)
        self.ball_3_1.setSingleStep(0)
        self.ball_3_1.setPageStep(0)
        self.ball_3_1.setTracking(True)
        self.ball_3_1.setNotchesVisible(False)
        self.ball_3_1.setObjectName("ball_3_1")
        self.ball_3_2 = QtWidgets.QDial(self.centralwidget)
        self.ball_3_2.setGeometry(QtCore.QRect(60, 120, 41, 41))
        self.ball_3_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_3_2.setMaximum(0)
        self.ball_3_2.setSingleStep(0)
        self.ball_3_2.setPageStep(0)
        self.ball_3_2.setTracking(True)
        self.ball_3_2.setNotchesVisible(False)
        self.ball_3_2.setObjectName("ball_3_2")
        self.ball_3_3 = QtWidgets.QDial(self.centralwidget)
        self.ball_3_3.setGeometry(QtCore.QRect(110, 120, 41, 41))
        self.ball_3_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_3_3.setMaximum(0)
        self.ball_3_3.setSingleStep(0)
        self.ball_3_3.setPageStep(0)
        self.ball_3_3.setTracking(True)
        self.ball_3_3.setNotchesVisible(False)
        self.ball_3_3.setObjectName("ball_3_3")
        self.ball_3_4 = QtWidgets.QDial(self.centralwidget)
        self.ball_3_4.setGeometry(QtCore.QRect(160, 120, 41, 41))
        self.ball_3_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_3_4.setMaximum(0)
        self.ball_3_4.setSingleStep(0)
        self.ball_3_4.setPageStep(0)
        self.ball_3_4.setTracking(True)
        self.ball_3_4.setNotchesVisible(False)
        self.ball_3_4.setObjectName("ball_3_4")
        self.ball_4_1 = QtWidgets.QDial(self.centralwidget)
        self.ball_4_1.setGeometry(QtCore.QRect(10, 180, 41, 41))
        self.ball_4_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_4_1.setMaximum(0)
        self.ball_4_1.setSingleStep(0)
        self.ball_4_1.setPageStep(0)
        self.ball_4_1.setTracking(True)
        self.ball_4_1.setNotchesVisible(False)
        self.ball_4_1.setObjectName("ball_4_1")
        self.ball_4_2 = QtWidgets.QDial(self.centralwidget)
        self.ball_4_2.setGeometry(QtCore.QRect(60, 180, 41, 41))
        self.ball_4_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_4_2.setMaximum(0)
        self.ball_4_2.setSingleStep(0)
        self.ball_4_2.setPageStep(0)
        self.ball_4_2.setTracking(True)
        self.ball_4_2.setNotchesVisible(False)
        self.ball_4_2.setObjectName("ball_4_2")
        self.ball_4_3 = QtWidgets.QDial(self.centralwidget)
        self.ball_4_3.setGeometry(QtCore.QRect(110, 180, 41, 41))
        self.ball_4_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_4_3.setMaximum(0)
        self.ball_4_3.setSingleStep(0)
        self.ball_4_3.setPageStep(0)
        self.ball_4_3.setTracking(True)
        self.ball_4_3.setNotchesVisible(False)
        self.ball_4_3.setObjectName("ball_4_3")
        self.ball_4_4 = QtWidgets.QDial(self.centralwidget)
        self.ball_4_4.setGeometry(QtCore.QRect(160, 180, 41, 41))
        self.ball_4_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_4_4.setMaximum(0)
        self.ball_4_4.setSingleStep(0)
        self.ball_4_4.setPageStep(0)
        self.ball_4_4.setTracking(True)
        self.ball_4_4.setNotchesVisible(False)
        self.ball_4_4.setObjectName("ball_4_4")
        self.ball_5_1 = QtWidgets.QDial(self.centralwidget)
        self.ball_5_1.setGeometry(QtCore.QRect(10, 240, 41, 41))
        self.ball_5_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_5_1.setMaximum(0)
        self.ball_5_1.setSingleStep(0)
        self.ball_5_1.setPageStep(0)
        self.ball_5_1.setTracking(True)
        self.ball_5_1.setNotchesVisible(False)
        self.ball_5_1.setObjectName("ball_5_1")
        self.ball_5_2 = QtWidgets.QDial(self.centralwidget)
        self.ball_5_2.setGeometry(QtCore.QRect(60, 240, 41, 41))
        self.ball_5_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_5_2.setMaximum(0)
        self.ball_5_2.setSingleStep(0)
        self.ball_5_2.setPageStep(0)
        self.ball_5_2.setTracking(True)
        self.ball_5_2.setNotchesVisible(False)
        self.ball_5_2.setObjectName("ball_5_2")
        self.ball_5_3 = QtWidgets.QDial(self.centralwidget)
        self.ball_5_3.setGeometry(QtCore.QRect(110, 240, 41, 41))
        self.ball_5_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_5_3.setMaximum(0)
        self.ball_5_3.setSingleStep(0)
        self.ball_5_3.setPageStep(0)
        self.ball_5_3.setTracking(True)
        self.ball_5_3.setNotchesVisible(False)
        self.ball_5_3.setObjectName("ball_5_3")
        self.ball_5_4 = QtWidgets.QDial(self.centralwidget)
        self.ball_5_4.setGeometry(QtCore.QRect(160, 240, 41, 41))
        self.ball_5_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_5_4.setMaximum(0)
        self.ball_5_4.setSingleStep(0)
        self.ball_5_4.setPageStep(0)
        self.ball_5_4.setTracking(True)
        self.ball_5_4.setNotchesVisible(False)
        self.ball_5_4.setObjectName("ball_5_4")
        self.ball_6_2 = QtWidgets.QDial(self.centralwidget)
        self.ball_6_2.setGeometry(QtCore.QRect(60, 300, 41, 41))
        self.ball_6_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_6_2.setMaximum(0)
        self.ball_6_2.setSingleStep(0)
        self.ball_6_2.setPageStep(0)
        self.ball_6_2.setTracking(True)
        self.ball_6_2.setNotchesVisible(False)
        self.ball_6_2.setObjectName("ball_6_2")
        self.ball_6_1 = QtWidgets.QDial(self.centralwidget)
        self.ball_6_1.setGeometry(QtCore.QRect(10, 300, 41, 41))
        self.ball_6_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_6_1.setMaximum(0)
        self.ball_6_1.setSingleStep(0)
        self.ball_6_1.setPageStep(0)
        self.ball_6_1.setTracking(True)
        self.ball_6_1.setNotchesVisible(False)
        self.ball_6_1.setObjectName("ball_6_1")
        self.ball_6_3 = QtWidgets.QDial(self.centralwidget)
        self.ball_6_3.setGeometry(QtCore.QRect(110, 300, 41, 41))
        self.ball_6_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_6_3.setMaximum(0)
        self.ball_6_3.setSingleStep(0)
        self.ball_6_3.setPageStep(0)
        self.ball_6_3.setTracking(True)
        self.ball_6_3.setNotchesVisible(False)
        self.ball_6_3.setObjectName("ball_6_3")
        self.ball_6_4 = QtWidgets.QDial(self.centralwidget)
        self.ball_6_4.setGeometry(QtCore.QRect(160, 300, 41, 41))
        self.ball_6_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_6_4.setMaximum(0)
        self.ball_6_4.setSingleStep(0)
        self.ball_6_4.setPageStep(0)
        self.ball_6_4.setTracking(True)
        self.ball_6_4.setNotchesVisible(False)
        self.ball_6_4.setObjectName("ball_6_4")
        self.ball_7_1 = QtWidgets.QDial(self.centralwidget)
        self.ball_7_1.setGeometry(QtCore.QRect(10, 360, 41, 41))
        self.ball_7_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_7_1.setMaximum(0)
        self.ball_7_1.setSingleStep(0)
        self.ball_7_1.setPageStep(0)
        self.ball_7_1.setTracking(True)
        self.ball_7_1.setNotchesVisible(False)
        self.ball_7_1.setObjectName("ball_7_1")
        self.ball_7_2 = QtWidgets.QDial(self.centralwidget)
        self.ball_7_2.setGeometry(QtCore.QRect(60, 360, 41, 41))
        self.ball_7_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_7_2.setMaximum(0)
        self.ball_7_2.setSingleStep(0)
        self.ball_7_2.setPageStep(0)
        self.ball_7_2.setTracking(True)
        self.ball_7_2.setNotchesVisible(False)
        self.ball_7_2.setObjectName("ball_7_2")
        self.ball_7_3 = QtWidgets.QDial(self.centralwidget)
        self.ball_7_3.setGeometry(QtCore.QRect(110, 360, 41, 41))
        self.ball_7_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_7_3.setMaximum(0)
        self.ball_7_3.setSingleStep(0)
        self.ball_7_3.setPageStep(0)
        self.ball_7_3.setTracking(True)
        self.ball_7_3.setNotchesVisible(False)
        self.ball_7_3.setObjectName("ball_7_3")
        self.ball_7_4 = QtWidgets.QDial(self.centralwidget)
        self.ball_7_4.setGeometry(QtCore.QRect(160, 360, 41, 41))
        self.ball_7_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.ball_7_4.setMaximum(0)
        self.ball_7_4.setSingleStep(0)
        self.ball_7_4.setPageStep(0)
        self.ball_7_4.setTracking(True)
        self.ball_7_4.setNotchesVisible(False)
        self.ball_7_4.setObjectName("ball_7_4")
        self.KS_zero = QtWidgets.QPushButton(self.centralwidget)
        self.KS_zero.setGeometry(QtCore.QRect(240, 420, 81, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.KS_zero.setFont(font)
        self.KS_zero.setStyleSheet("border-image: url(:/开锁/图片文件夹/0.png);")
        self.KS_zero.setFlat(True)
        self.KS_zero.setObjectName("KS_zero")
        self.KS_one = QtWidgets.QPushButton(self.centralwidget)
        self.KS_one.setGeometry(QtCore.QRect(350, 420, 81, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.KS_one.setFont(font)
        self.KS_one.setStyleSheet("border-image: url(:/开锁/图片文件夹/1 (1).png);")
        self.KS_one.setFlat(True)
        self.KS_one.setObjectName("KS_one")
        self.KS_two = QtWidgets.QPushButton(self.centralwidget)
        self.KS_two.setGeometry(QtCore.QRect(460, 420, 81, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.KS_two.setFont(font)
        self.KS_two.setStyleSheet("border-image: url(:/开锁/图片文件夹/2 (1).png);")
        self.KS_two.setFlat(True)
        self.KS_two.setObjectName("KS_two")
        self.KS_three = QtWidgets.QPushButton(self.centralwidget)
        self.KS_three.setGeometry(QtCore.QRect(570, 420, 81, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.KS_three.setFont(font)
        self.KS_three.setStyleSheet("border-image: url(:/开锁/图片文件夹/3 (1).png);")
        self.KS_three.setFlat(True)
        self.KS_three.setObjectName("KS_three")
        self.KS_five = QtWidgets.QPushButton(self.centralwidget)
        self.KS_five.setGeometry(QtCore.QRect(460, 490, 81, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.KS_five.setFont(font)
        self.KS_five.setStyleSheet("border-image: url(:/开锁/图片文件夹/0.png);")
        self.KS_five.setFlat(True)
        self.KS_five.setObjectName("KS_five")
        self.KS_eight = QtWidgets.QPushButton(self.centralwidget)
        self.KS_eight.setGeometry(QtCore.QRect(460, 560, 81, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.KS_eight.setFont(font)
        self.KS_eight.setStyleSheet("border-image: url(:/开锁/图片文件夹/0.png);")
        self.KS_eight.setFlat(True)
        self.KS_eight.setObjectName("KS_eight")
        self.KS_seven = QtWidgets.QPushButton(self.centralwidget)
        self.KS_seven.setGeometry(QtCore.QRect(350, 560, 81, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.KS_seven.setFont(font)
        self.KS_seven.setStyleSheet("border-image: url(:/开锁/图片文件夹/0.png);")
        self.KS_seven.setFlat(True)
        self.KS_seven.setObjectName("KS_seven")
        self.KS_nine = QtWidgets.QPushButton(self.centralwidget)
        self.KS_nine.setGeometry(QtCore.QRect(570, 560, 81, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.KS_nine.setFont(font)
        self.KS_nine.setStyleSheet("border-image: url(:/开锁/图片文件夹/0.png);")
        self.KS_nine.setFlat(True)
        self.KS_nine.setObjectName("KS_nine")
        self.KS_six = QtWidgets.QPushButton(self.centralwidget)
        self.KS_six.setGeometry(QtCore.QRect(570, 490, 81, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        self.KS_six.setFont(font)
        self.KS_six.setStyleSheet("border-image: url(:/开锁/图片文件夹/0.png);")
        self.KS_six.setFlat(True)
        self.KS_six.setObjectName("KS_six")
        self.KS_four = QtWidgets.QPushButton(self.centralwidget)
        self.KS_four.setGeometry(QtCore.QRect(350, 490, 81, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.KS_four.setFont(font)
        self.KS_four.setStyleSheet("border-image: url(:/开锁/图片文件夹/0.png);")
        self.KS_four.setFlat(True)
        self.KS_four.setObjectName("KS_four")
        self.KS_deletebutton = QtWidgets.QPushButton(self.centralwidget)
        self.KS_deletebutton.setGeometry(QtCore.QRect(240, 490, 101, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.KS_deletebutton.setFont(font)
        self.KS_deletebutton.setStyleSheet("")
        self.KS_deletebutton.setFlat(True)
        self.KS_deletebutton.setObjectName("KS_deletebutton")
        self.KS_SureButton = QtWidgets.QPushButton(self.centralwidget)
        self.KS_SureButton.setGeometry(QtCore.QRect(230, 560, 111, 61))
        self.KS_SureButton.setStyleSheet('color: rgb(255, 0, 0);')
        self.KS_deletebutton.setStyleSheet('color: rgb(255, 0, 0);')
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.KS_SureButton.setFont(font)
        self.KS_SureButton.setFlat(True)
        self.KS_SureButton.setObjectName("KS_SureButton")
        self.KS_actionButton = QtWidgets.QPushButton(self.centralwidget)
        self.KS_actionButton.setGeometry(QtCore.QRect(10, 430, 225, 51))
        self.KS_actionButton.setStyleSheet("QPushButton{color: rgb(255, 0, 0);\n"
"background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));\n"
"font: 75 18pt \"Aharoni\";\n"
"border-radius:10px}\n"
"QPushButton:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/开锁/图片文件夹/开锁-开始游戏.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KS_actionButton.setIcon(icon1)
        self.KS_actionButton.setObjectName("KS_actionButton")
        self.KS_questionButton = QtWidgets.QPushButton(self.centralwidget)
        self.KS_questionButton.setGeometry(QtCore.QRect(130, 500, 105, 71))
        self.KS_questionButton.setStyleSheet("QPushButton{color: rgb(255, 0, 0);\n"
"    background-color: rgb(255, 255, 127);\n"
"font: 75 18pt \"Aharoni\";\n"
"border-radius:10px}\n"
"QPushButton:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/开锁/图片文件夹/开锁-疑问.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KS_questionButton.setIcon(icon2)
        self.KS_questionButton.setObjectName("KS_questionButton")
        self.KS_backButton = QtWidgets.QPushButton(self.centralwidget)
        self.KS_backButton.setGeometry(QtCore.QRect(10, 500, 105, 71))
        self.KS_backButton.setStyleSheet("QPushButton{color: rgb(255, 0, 0);\n"
"background-color: rgb(255, 255, 127);\n"
"font: 75 18pt \"Aharoni\";\n"
"border-radius:10px}\n"
"QPushButton:pressed{padding-top:5px;padding-left:5px;}\n"
"\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/开锁/图片文件夹/开锁-离开.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KS_backButton.setIcon(icon3)
        self.KS_backButton.setObjectName("KS_backButton")
        self.KS_secondText = QtWidgets.QLabel(self.centralwidget)
        self.KS_secondText.setGeometry(QtCore.QRect(270, 60, 171, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.KS_secondText.setFont(font)
        self.KS_secondText.setStyleSheet("color: rgb(0, 0, 0);")
        self.KS_secondText.setObjectName("KS_secondText")
        self.KS_thirdText = QtWidgets.QLabel(self.centralwidget)
        self.KS_thirdText.setGeometry(QtCore.QRect(270, 120, 171, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.KS_thirdText.setFont(font)
        self.KS_thirdText.setStyleSheet("color: rgb(0, 0, 0);")
        self.KS_thirdText.setObjectName("KS_thirdText")
        self.KS_fourthText = QtWidgets.QLabel(self.centralwidget)
        self.KS_fourthText.setGeometry(QtCore.QRect(270, 180, 171, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.KS_fourthText.setFont(font)
        self.KS_fourthText.setStyleSheet("color: rgb(0, 0, 0);")
        self.KS_fourthText.setObjectName("KS_fourthText")
        self.KS_fifthText = QtWidgets.QLabel(self.centralwidget)
        self.KS_fifthText.setGeometry(QtCore.QRect(270, 240, 171, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.KS_fifthText.setFont(font)
        self.KS_fifthText.setStyleSheet("color: rgb(0, 0, 0);")
        self.KS_fifthText.setObjectName("KS_fifthText")
        self.KS_seventhText = QtWidgets.QLabel(self.centralwidget)
        self.KS_seventhText.setGeometry(QtCore.QRect(270, 360, 171, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.KS_seventhText.setFont(font)
        self.KS_seventhText.setStyleSheet("color: rgb(0, 0, 0);")
        self.KS_seventhText.setObjectName("KS_seventhText")
        self.KS_sixthText = QtWidgets.QLabel(self.centralwidget)
        self.KS_sixthText.setGeometry(QtCore.QRect(270, 300, 171, 51))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.KS_sixthText.setFont(font)
        self.KS_sixthText.setStyleSheet("color: rgb(0, 0, 0);")
        self.KS_sixthText.setObjectName("KS_sixthText")
        self.KS_spendTime = QtWidgets.QLabel(self.centralwidget)
        self.KS_spendTime.setGeometry(QtCore.QRect(10, 590, 221, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.KS_spendTime.setFont(font)
        self.KS_spendTime.setObjectName("KS_spendTime")
        self.KS_evaluate = QtWidgets.QLabel(self.centralwidget)
        self.KS_evaluate.setGeometry(QtCore.QRect(250, 420, 391, 71))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.KS_evaluate.setFont(font)
        self.KS_evaluate.setStyleSheet("color: rgb(0, 255, 0);")
        self.KS_evaluate.setAlignment(QtCore.Qt.AlignCenter)
        self.KS_evaluate.setObjectName("KS_evaluate")
        self.KS_answer = QtWidgets.QLabel(self.centralwidget)
        self.KS_answer.setGeometry(QtCore.QRect(270, 500, 341, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(28)
        self.KS_answer.setFont(font)
        self.KS_answer.setStyleSheet("color: rgb(85, 255, 0);")
        self.KS_answer.setAlignment(QtCore.Qt.AlignCenter)
        self.KS_answer.setObjectName("KS_answer")
        self.KS_try1 = QtWidgets.QLabel(self.centralwidget)
        self.KS_try1.setGeometry(QtCore.QRect(440, 0, 211, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.KS_try1.setFont(font)
        self.KS_try1.setAlignment(QtCore.Qt.AlignCenter)
        self.KS_try1.setObjectName("KS_try1")
        self.KS_try2 = QtWidgets.QLabel(self.centralwidget)
        self.KS_try2.setGeometry(QtCore.QRect(440, 60, 211, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.KS_try2.setFont(font)
        self.KS_try2.setAlignment(QtCore.Qt.AlignCenter)
        self.KS_try2.setObjectName("KS_try1_2")
        self.KS_try3 = QtWidgets.QLabel(self.centralwidget)
        self.KS_try3.setGeometry(QtCore.QRect(440, 120, 211, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.KS_try3.setFont(font)
        self.KS_try3.setAlignment(QtCore.Qt.AlignCenter)
        self.KS_try3.setObjectName("KS_try1_3")
        self.KS_try4 = QtWidgets.QLabel(self.centralwidget)
        self.KS_try4.setGeometry(QtCore.QRect(440, 180, 211, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.KS_try4.setFont(font)
        self.KS_try4.setAlignment(QtCore.Qt.AlignCenter)
        self.KS_try4.setObjectName("KS_try1_4")
        self.KS_try5 = QtWidgets.QLabel(self.centralwidget)
        self.KS_try5.setGeometry(QtCore.QRect(440, 240, 211, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.KS_try5.setFont(font)
        self.KS_try5.setAlignment(QtCore.Qt.AlignCenter)
        self.KS_try5.setObjectName("KS_try1_5")
        self.KS_try6 = QtWidgets.QLabel(self.centralwidget)
        self.KS_try6.setGeometry(QtCore.QRect(440, 300, 211, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.KS_try6.setFont(font)
        self.KS_try6.setAlignment(QtCore.Qt.AlignCenter)
        self.KS_try6.setObjectName("KS_try1_6")
        self.KS_try7 = QtWidgets.QLabel(self.centralwidget)
        self.KS_try7.setGeometry(QtCore.QRect(440, 360, 211, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(22)
        self.KS_try7.setFont(font)
        self.KS_try7.setAlignment(QtCore.Qt.AlignCenter)
        self.KS_try7.setObjectName("KS_try1_7")
        KS.setCentralWidget(self.centralwidget)

        self.retranslateUi(KS)
        QtCore.QMetaObject.connectSlotsByName(KS)

    def retranslateUi(self, KS):
        _translate = QtCore.QCoreApplication.translate
        KS.setWindowTitle(_translate("KS", "开锁"))
        self.KS_firstText.setText(_translate("KS", "您的第一次答案："))
        self.KS_zero.setText(_translate("KS", "0"))
        self.KS_zero.setShortcut(_translate("KS", "0"))
        self.KS_one.setText(_translate("KS", "1"))
        self.KS_one.setShortcut(_translate("KS", "1"))
        self.KS_two.setText(_translate("KS", "2"))
        self.KS_two.setShortcut(_translate("KS", "2"))
        self.KS_three.setText(_translate("KS", "3"))
        self.KS_three.setShortcut(_translate("KS", "3"))
        self.KS_five.setText(_translate("KS", "5"))
        self.KS_five.setShortcut(_translate("KS", "5"))
        self.KS_eight.setText(_translate("KS", "8"))
        self.KS_eight.setShortcut(_translate("KS", "8"))
        self.KS_seven.setText(_translate("KS", "7"))
        self.KS_seven.setShortcut(_translate("KS", "7"))
        self.KS_nine.setText(_translate("KS", "9"))
        self.KS_nine.setShortcut(_translate("KS", "9"))
        self.KS_six.setText(_translate("KS", "6"))
        self.KS_six.setShortcut(_translate("KS", "6"))
        self.KS_four.setText(_translate("KS", "4"))
        self.KS_four.setShortcut(_translate("KS", "4"))
        self.KS_deletebutton.setText(_translate("KS", "删除"))
        self.KS_deletebutton.setShortcut(_translate("KS", "Backspace"))
        self.KS_SureButton.setText(_translate("KS", "确定"))
        self.KS_SureButton.setShortcut(_translate("KS", "Return"))
        self.KS_actionButton.setText(_translate("KS", "开始游戏"))
        self.KS_questionButton.setText(_translate("KS", "疑问"))
        self.KS_backButton.setText(_translate("KS", "离开"))
        self.KS_secondText.setText(_translate("KS", "您的第二次答案："))
        self.KS_thirdText.setText(_translate("KS", "您的第三次答案："))
        self.KS_fourthText.setText(_translate("KS", "您的第四次答案："))
        self.KS_fifthText.setText(_translate("KS", "您的第五次答案："))
        self.KS_seventhText.setText(_translate("KS", "您的第七次答案："))
        self.KS_sixthText.setText(_translate("KS", "您的第六次答案："))
        self.KS_spendTime.setText(_translate("KS", "用时：10分55秒"))
        self.KS_evaluate.setText(_translate("KS", "恭喜你，成功解开秘钥！"))
        self.KS_answer.setText(_translate("KS", "正确答案：1987"))
        self.KS_try1.setText(_translate("KS", "0"))
        self.KS_try2.setText(_translate("KS", "0"))
        self.KS_try3.setText(_translate("KS", "0"))
        self.KS_try4.setText(_translate("KS", "0"))
        self.KS_try5.setText(_translate("KS", "0"))
        self.KS_try6.setText(_translate("KS", "0"))
        self.KS_try7.setText(_translate("KS", "0"))
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) // 2
        newTop = (screen.height() - size.height()) // 2
        self.move(newLeft, newTop)
        KS.setWindowFlags(QtCore.Qt.FramelessWindowHint)
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
            super(Ui_KS, self).__init__()
            self.setupUi(self)
