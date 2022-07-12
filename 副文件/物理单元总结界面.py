import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Ui_WL_jiemian(QMainWindow):
    def setupUi(self, WL_jiemian):
        WL_jiemian.setObjectName("WL_jiemian")
        WL_jiemian.resize(520, 414)
        font = QtGui.QFont()
        font.setFamily("楷体")
        WL_jiemian.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/子标/图片文件夹/单元总结.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # 使窗口居中
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) // 2
        newTop = (screen.height() - size.height()) // 2
        self.move(newLeft, newTop)
        WL_jiemian.setWindowIcon(icon)
        WL_jiemian.setStyleSheet("#WL_jiemian{border-image: url(:/背景/图片文件夹/壁纸005.jpeg);}")
        self.shangyiye = QtWidgets.QPushButton(WL_jiemian)
        self.shangyiye.setGeometry(QtCore.QRect(60, 370, 121, 41))
        self.shangyiye.setStyleSheet("border-image: url(:/小窗口图标/图片文件夹/物理界面上一页.png);")
        self.shangyiye.setText("")
        self.shangyiye.setFlat(True)
        self.shangyiye.setObjectName("shangyiye")
        self.xiayiye = QtWidgets.QPushButton(WL_jiemian)
        self.xiayiye.setGeometry(QtCore.QRect(334, 370, 121, 41))
        self.xiayiye.setStyleSheet("border-image: url(:/小窗口图标/图片文件夹/物理界面下一页.png);")
        self.xiayiye.setText("")
        self.xiayiye.setFlat(True)
        self.xiayiye.setObjectName("xiayiye")
        self.title = QtWidgets.QLabel(WL_jiemian)
        self.title.setGeometry(QtCore.QRect(0, 0, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.back = QtWidgets.QPushButton(WL_jiemian)
        self.back.setGeometry(QtCore.QRect(480, 0, 41, 31))
        self.back.setStyleSheet("border-image: url(:/小窗口图标/图片文件夹/物理退出登录.png);")
        self.back.setText("")
        self.back.setObjectName("back")
        self.text = QtWidgets.QPlainTextEdit(WL_jiemian)
        self.text.setGeometry(QtCore.QRect(0, 130, 521, 231))
        font = QtGui.QFont()
        font.setFamily("楷体")
        self.text.setFont(font)
        self.text.setStyleSheet("background-color: rgb(255, 255, 255,0);")
        self.text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text.setReadOnly(True)
        self.text.setCenterOnScroll(False)
        self.text.setPlaceholderText("")
        self.text.setObjectName("text")
        self.picture = QtWidgets.QPushButton(WL_jiemian)
        self.picture.setGeometry(QtCore.QRect(0, 32, 521, 81))
        self.picture.setFlat(True)
        self.picture.setObjectName("picture")

        self.retranslateUi(WL_jiemian)
        QtCore.QMetaObject.connectSlotsByName(WL_jiemian)

    def retranslateUi(self, WL_jiemian):
        _translate = QtCore.QCoreApplication.translate
        WL_jiemian.setWindowTitle(_translate("WL_jiemian", "单元总结"))
        self.shangyiye.setToolTip(_translate("WL_jiemian", "Alt + 左"))
        self.shangyiye.setShortcut(_translate("WL_jiemian", "Alt+Left"))
        self.xiayiye.setToolTip(_translate("WL_jiemian", "Alt + 右"))
        self.xiayiye.setShortcut(_translate("WL_jiemian", "Alt+Right"))
        self.title.setText(_translate("WL_jiemian", "选择的内容"))
        self.text.setPlainText(_translate("WL_jiemian", "内容输出"))
        self.picture.setText(_translate("WL_jiemian", "这个是图片"))
        WL_jiemian.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.back.clicked.connect(self.backEvent)

        self.frequency = 0
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

    def FileDialog(self):
        dir = QFileDialog()
        dir.setFileMode(QFileDialog.ExistingFile)
        dir.setDirectory('c:\\')
        dir.setNameFilter('图片文件(*.jpg *.png *.bmp)')
        if dir.exec_():
            ip = dir.selectedFiles()
            string = 'border-image:url(' + ip[0] + ')'
            self.picture.setStyleSheet(string)

    def xiayiyeEvent(self):
        _translate = QtCore.QCoreApplication.translate
        self.frequency += 1
        self.shangyiye.setEnabled(True)
        if self.frequency == len(self.textlist)-1 :
            self.xiayiye.setEnabled(False)
        if self.picturelist[self.frequency] != 'None':
            ip = self.picturelist[self.frequency]
            string = 'border-image:url(' + ip + ')'
            self.picture.setStyleSheet(string)
            self.picture.setText(_translate("WL_jiemian", ''))
        else:
            self.picture.setStyleSheet('')
            self.picture.setText(_translate("WL_jiemian",'暂无图片'))
        self.text.setPlainText(_translate("WL_jiemian",self.textlist[self.frequency]))

    def shangyiyeEvent(self):
        _translate = QtCore.QCoreApplication.translate
        self.frequency -= 1
        self.xiayiye.setEnabled(True)
        if self.frequency == 0:
            self.shangyiye.setEnabled(False)
        if self.picturelist[self.frequency] != 'None':
            ip = self.picturelist[self.frequency]
            string = 'border-image:url(' + ip + ')'
            self.picture.setStyleSheet(string)
            self.picture.setText(_translate("WL_jiemian", ''))
        else:
            self.picture.setStyleSheet('')
            self.picture.setText(_translate("WL_jiemian", '暂无图片'))
        self.text.setPlainText(_translate("WL_jiemian", self.textlist[self.frequency]))

    def backEvent(self):
        self.close()


    def __init__(self,father,title,text=''):
        _translate = QtCore.QCoreApplication.translate
        super(Ui_WL_jiemian, self).__init__()
        self.setupUi(self)
        conn = sqlite3.connect('考试复习系统数据.db')
        cursor = conn.cursor()
        if father == '知识点':
            cursor.execute('select * from 物理单元总结知识点 where 所属范围 = ?',(title,))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            self.xiayiye.hide()
            self.shangyiye.hide()
            self.title.setText(_translate("WL_jiemian", father))
            self.picture.setText(_translate("WL_jiemian", title))
            self.text.setPlainText(_translate("WL_jiemian", text))
        elif father == '例题':
            self.xiayiye.clicked.connect(self.xiayiyeEvent)
            self.shangyiye.clicked.connect(self.shangyiyeEvent)
            self.picture.clicked.connect(self.FileDialog)
            self.shangyiye.setEnabled(False)
            self.textlist = []
            self.picturelist = []
            self.title.setText(_translate("WL_jiemian", father+'  '+title))
            cursor.execute('select * from 物理单元总结例题 where 所属范围 = ?',(title,))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            for i in result :
                self.textlist.append(i[2])
                self.picturelist.append(i[3])
            if len(self.textlist) >= 2 :
                self.xiayiye.setEnabled(True)
            else:
                self.xiayiye.setEnabled(False)
            self.text.setPlainText(_translate("WL_jiemian",result[0][2]))
            if result[0][3] != 'None' :
                ip = result[0][3]
                string = 'border-image:url(' + ip + ')'
                self.picture.setStyleSheet(string)
            else:
                self.picture.setText(_translate("WL_jiemian",'暂无图片'))
        else:
            cursor.close()
            conn.close()
            print('father有误，请确认输入！')
