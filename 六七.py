# _*_coding : utf-8 _*_
# @Time: 2022/2/18 7.30
# @author: Matt
# @File: 代码逻辑
# @Project: 考试复习系统文件夹
import os.path
import sys
from timeit import default_timer as timer
from 副文件.开锁 import *
from 副文件.等待界面 import *
from 副文件.管理者界面 import *
from 副文件.挑战失败背景 import *
from 副文件.背单词总结页面 import *
from 副文件.速算总结界面 import *
from 副文件.考试复习系统界面 import *
from 副文件.记事本界面 import *
from 副文件.用户登录界面 import *
from 副文件.信息界面 import *
from 副文件 import 物理单元总结界面
from 副文件 import img_rc
import sqlite3
from PyQt5.QtWidgets import QMessageBox
import matplotlib.pyplot as plt
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
import random
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator  # 正则表达式
from PyQt5.QtCore import QRegExp
from PyQt5 import QtMultimedia
from PyQt5.QtCore import QUrl


class MyQLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)

    def mousePressEvent(self, ev: QtGui.QMouseEvent, ):
        self.MESSAGE = Ui_KSFX_Message('多行通知', '错题详情', Homepages.YWmessage)
        self.MESSAGE.show()


class EmptyDelegate(QItemDelegate):  # 禁止修改单元格
    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None


class Homepages(QMainWindow, Ui_Homepage):
    YWmessage = ''  # 别删，用来具体展示错题的类属性
    DB = 0
    def __init__(self, parent=None):
        super(Homepages, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("#Homepage{border-image: url(:/背景/图片文件夹/壁纸 010.jpg);;}")
        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
        import os
        path = 'C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db'
        if os.path.exists(path):
            self.db = True
        else:
            self.db = False
            Homepages.DB = 1
            self.MESSAGE = Ui_KSFX_Message('警告', '数据库不存在', '没有数据源，请确保数据文件位与副文件文件夹！如有丢失，请联系作者！')
            self.MESSAGE.show()
            self.close()
        #使窗口居中
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        newLeft = (screen.width() - size.width()) // 2
        newTop = (screen.height() - size.height()) // 2
        self.move(newLeft, newTop)
        _translate = QtCore.QCoreApplication.translate
        self.YW_mxcomboBox.setMaxVisibleItems(6)
        self.actionyuwen.triggered.connect(self.ChineseData)
        self.actionjishiben.triggered.connect(self.JSB_window)
        self.actionks.triggered.connect(self.KSgame)
        self.actionshuxue.triggered.connect(self.MathData)
        self.actionyingyu.triggered.connect(self.EnglishData)
        self.actionwuli.triggered.connect(self.PhysicsData)
        self.actionhuaxue.triggered.connect(self.ChemistryData)
        self.actionshengwu.triggered.connect(self.BiologyData)
        self.actionshijian.triggered.connect(self.Shijian)
        self.actionauthor.triggered.connect(self.Zuozhejieshao)
        self.actionuse.triggered.connect(self.Actionuse_Prior)
        self.actionguanlizhe.triggered.connect(self.GLZ_window)
        self.EBcomboBox.setMaxVisibleItems(6)
        self.tabWidget.currentChanged.connect(self.Z_B)
        self.SSzhuye.clicked.connect(self.SS_ZHUYE)
        self.hour0 = int(time.strftime("%H"))
        self.minute0 = int(time.strftime("%M"))
        self.actionjishiben.setShortcut('ctrl+j')
        self.actionshijian.setShortcut('ctrl+t')
        self.tabWidget.setTabsClosable(True)
        self.daima()
        self.LCD_dayremaining.setProperty("value", self.Dayremaining)
        self.yincang = self.tabWidget.tabBar()
        self.yincang.setTabButton(0, self.yincang.RightSide, None)
        self.tabWidget.tabCloseRequested.connect(self.likai)
        self.frequency = 1  # 用来标注当前页码索引
        self.Echange_Mark = 0
        self.YWMXchange_Mark = 0
        self.EBtijiao.clicked.connect(self.Ehand)
        self.xiayiye.clicked.connect(self.Enext)
        self.shangyiye.clicked.connect(self.Eback)
        self.shangyiye.hide()
        self.xiayiye.show()
        self.English.clicked.connect(self.ENGLISH)
        self.Chinese.clicked.connect(self.CHINESE)
        self.Math.clicked.connect(self.MATH)
        self.Physics.clicked.connect(self.PHYSICS)
        self.Chemistry.clicked.connect(self.CHEMISTRY)
        self.Biology.clicked.connect(self.BIOLOGY)
        self.EBcomboBox.currentIndexChanged.connect(self.Echange)
        self.SScomboBox.currentIndexChanged.connect(self.SSchange)
        self.YW_mxcomboBox.currentIndexChanged.connect(self.YWMXchange)
        self.SSkaishi.setShortcut(_translate("Homepage", "Return"))
        self.YW_mxyiwen_lable.clicked.connect(self.YW_mxyiwenEvent)
        self.SSkaishi.clicked.connect(self.SS)
        self.SStijiao.clicked.connect(self.SSTiJiao)
        self.SSxiayiti.clicked.connect(self.SSnext)
        self.YW_mxxiayiye_lable.clicked.connect(self.YW_mxnext)
        self.YW_mxtijiao_lable.clicked.connect(self.YW_mxhand)
        self.YW_mxshangyiye_lable.clicked.connect(self.YW_mxback)
        self.WL_danyuanzongjie_bixiu1_listWidget0.itemClicked.connect(self.WL_itemclicked_Event0)
        self.WL_danyuanzongjie_bixiu2_listWidget0.itemClicked.connect(self.WL_itemclicked_Event0)
        self.WL_danyuanzongjie_bixiu3_listWidget0.itemClicked.connect(self.WL_itemclicked_Event0)
        self.WL_danyuanzongjie_xbixiu1_listWidget0.itemClicked.connect(self.WL_itemclicked_Event0)
        self.WL_danyuanzongjie_xbixiu2_listWidget0.itemClicked.connect(self.WL_itemclicked_Event0)
        self.WL_danyuanzongjie_xbixiu3_listWidget0.itemClicked.connect(self.WL_itemclicked_Event0)
        self.WL_danyuanzongjie_bixiu1_listWidget1.itemClicked.connect(self.WL_itemclicked_Event1)
        self.WL_danyuanzongjie_bixiu2_listWidget1.itemClicked.connect(self.WL_itemclicked_Event1)
        self.WL_danyuanzongjie_bixiu3_listWidget1.itemClicked.connect(self.WL_itemclicked_Event1)
        self.WL_danyuanzongjie_xbixiu1_listWidget1.itemClicked.connect(self.WL_itemclicked_Event1)
        self.WL_danyuanzongjie_xbixiu2_listWidget1.itemClicked.connect(self.WL_itemclicked_Event1)
        self.WL_danyuanzongjie_xbixiu3_listWidget1.itemClicked.connect(self.WL_itemclicked_Event1)
        self.WL_danyuanzongjie_lefttoolbox.setCurrentIndex(0)
        self.WL_danyuanzongjie_righttoolbox.setCurrentIndex(0)
        self.WL_danyuanzongjie_RB1 = []
        self.WL_danyuanzongjie_RB2 = []
        self.WL_danyuanzongjie_RB3 = []
        self.WL_danyuanzongjie_RB4 = []
        self.WL_danyuanzongjie_RB5 = []
        self.WL_danyuanzongjie_RB6 = []
        self.WL_danyuanzongjie_LB1 = []
        self.WL_danyuanzongjie_LB2 = []
        self.WL_danyuanzongjie_LB3 = []
        self.WL_danyuanzongjie_LB4 = []
        self.WL_danyuanzongjie_LB5 = []
        self.WL_danyuanzongjie_LB6 = []
        self.WL_danyuanzongjie_findtime = 0  # 用于标记是否是第一次进入单元总结界面
        if self.db == True:
            starttime = timer()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 操作数据 where  操作命令 = "音乐" ')
            result = cursor.fetchone()
            if result != None:
                self.bj_music = result[2]
            else:
                self.bj_music = False
            if result != None:
                if result[2] == True:
                    self.music_marktime = 0
                    self.music_timer = QTimer(self)
                    self.music_timer.timeout.connect(self.Background_Music)
                    self.music_timer.start(100)
                    endtime = timer()
                    if endtime - starttime > 0.0001:
                        self.MESSAGE = Ui_KSFX_Message('通知', '友情提醒', '检测到您的电脑配置较低，程序运行可能会较为卡顿，建议您前往管理者模式关闭音乐选项！')
                        self.MESSAGE.show()
            else:
                pass
        else:
            pass

    def matt_change(self):
        _translate = QtCore.QCoreApplication.translate
        list = ['业精于勤荒于嬉，行成于思毁于随', '黄金百战穿金甲，不破楼兰终不还', '海纳百川有容乃大，壁立千仞无欲则刚', '居安思危，有备无患']
        text = random.choice(list)
        self.matt.setText(_translate("Homepage", text))

    def JSB_window(self):
        biaoji = 0
        conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
        cursor = conn.cursor()
        cursor.execute('select * from 操作数据 where 操作命令 = "自动登录" ')
        result = cursor.fetchall()
        cursor.execute('select * from 账户信息 ')
        zhanghu = cursor.fetchall()
        cursor.close()
        conn.close()
        for i in result:
            if i[2] == True:  # 已经设置自动登录
                self.JSB_nowuser = i[0]
                self.JSB_Action()
                biaoji = 1
        if biaoji == 0:
            self.jsblogon = Ui_JSB_logon()
            self.jsblogon.show()
            self.hide()
            self.jsblogon.LOGON_logonbutton.clicked.connect(self.logonevent)
            if zhanghu != []:  # 已有账户则禁止注册
                self.jsblogon.LOGON_zhucebutton.setEnabled(False)
            else:
                self.jsblogon.LOGON_zhucebutton.clicked.connect(self.zhuceevent)
            self.jsblogon.LOGON_backbutton.clicked.connect(self.LOGON_back)
            self.jsblogon.LOGON_forgetbutton.clicked.connect(self.Logon_Forgetevent)

    def automatic_logon(self):
        if self.jsblogon.LOGON_neverlogon.isChecked():
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            try:
                cursor.execute('update 操作数据 set 值 = ? and 账户名 = ? where 操作命令 = ? ', (True, self.JSB_nowuser, '自动登录'))
            except:
                cursor.execute('update 操作数据 set 值 = ? and 账户名 = ? where 操作命令 = ? ', (True, self.GLZ_nowuser, '自动登录'))
            cursor.close()
            conn.commit()
            conn.close()

    def Logon_Forgetevent(self):
        _translate = QtCore.QCoreApplication.translate
        self.jsblogon.LOGON_warning.clear()
        self.jsblogon.LOGON_forgetbutton.hide()
        self.jsblogon.LOGON_zhanghu.setText(_translate("JSB_logon", "旧账户："))
        self.jsblogon.LOGON_zhucebutton.setEnabled(False)
        self.jsblogon.LOGON_backbutton.setText(_translate("JiShiBen", "返回"))

    def LOGON_back(self):
        _translate = QtCore.QCoreApplication.translate
        if self.jsblogon.LOGON_zhanghu.text() == '账户：':  # 判断是否处于忘记密码界面
            self.jsblogon.close()
            self.show()
        else:
            self.jsblogon.LOGON_warning.clear()
            self.jsblogon.LOGON_forgetbutton.show()
            self.jsblogon.LOGON_zhanghu.setText(_translate("JSB_logon", "账户："))
            self.jsblogon.LOGON_backbutton.setText(_translate("JiShiBen", "退出"))
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 账户信息 ')
            zhanghu = cursor.fetchall()
            cursor.close()
            conn.close()
            if zhanghu != []:
                pass
            else:
                self.jsblogon.LOGON_zhucebutton.setEnabled(True)
            self.jsblogon.LOGON_zhanghu_input.clear()
            self.jsblogon.LOGON_key1_input.clear()

    def zhuceevent(self):
        _translate = QtCore.QCoreApplication.translate
        zhanghu = self.jsblogon.LOGON_zhanghu_input.text()
        key = self.jsblogon.LOGON_key1_input.text()
        if zhanghu != '' and key != '':
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('insert into 账户信息(账户名,密码) values (?,?)', (zhanghu, key))
            cursor.execute('insert into 操作数据(账户名,操作命令,值) values (?,?,?)', (zhanghu, "自动登录", False))
            cursor.execute('insert into 操作数据(账户名,操作命令,值) values (?,?,?)', (zhanghu, "免爬虫等待", False))
            cursor.execute('insert into 操作数据(账户名,操作命令,值) values (?,?,?)', (zhanghu, "音乐", False))
            cursor.close()
            conn.commit()
            conn.close()
            self.LOGtime = 0
            self.JSBtimer = QTimer(self)
            self.JSBtimer.start(100)
            self.JSBtimer.timeout.connect(self.JSB_logTimer)
            self.jsblogon.LOGON_warning.setStyleSheet("color: rgb(85, 255, 0);")
            self.jsblogon.LOGON_warning.setText(_translate("JSB_logon", '注册成功，欢迎使用！'))
            self.jsblogon.LOGON_warning.show()
            self.JSB_nowuser = zhanghu
            self.automatic_logon()
            self.jsblogon.LOGON_neverlogon.setEnabled(False)
            self.jsblogon.LOGON_logonbutton.setEnabled(False)
            self.jsblogon.LOGON_logonbutton.setEnabled(False)
            self.jsblogon.LOGON_backbutton.setEnabled(False)
            self.jsblogon.LOGON_forgetbutton.setEnabled(False)
        else:
            self.jsblogon.LOGON_warning.setStyleSheet("color: rgb(255, 0, 0);")
            self.jsblogon.LOGON_warning.setText(_translate("JSB_logon", '账号或密码不能为空！'))
            self.jsblogon.LOGON_warning.show()

    def logonevent(self):  # 登录按钮绑定的事件
        if self.jsblogon.LOGON_zhanghu.text() == '账户：':  # 判断是否是处于忘记密码界面
            _translate = QtCore.QCoreApplication.translate
            zhanghu = self.jsblogon.LOGON_zhanghu_input.text()
            key = self.jsblogon.LOGON_key1_input.text()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 账户信息 where 账户名 = ? and 密码 = ?', (zhanghu, key))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            if result != []:
                self.LOGtime = 0
                self.JSBtimer = QTimer(self)
                self.JSBtimer.start(100)
                self.JSBtimer.timeout.connect(self.JSB_logTimer)
                self.jsblogon.LOGON_warning.show()
                self.jsblogon.LOGON_warning.setStyleSheet("color: rgb(85, 255, 0);")
                self.jsblogon.LOGON_warning.setText(_translate("JSB_logon", '登录成功，欢迎使用！'))
                self.JSB_nowuser = zhanghu
                self.automatic_logon()
                self.jsblogon.LOGON_neverlogon.setEnabled(False)
                self.jsblogon.LOGON_logonbutton.setEnabled(False)
                self.jsblogon.LOGON_zhucebutton.setEnabled(False)
                self.jsblogon.LOGON_backbutton.setEnabled(False)
                self.jsblogon.LOGON_forgetbutton.setEnabled(False)
            else:
                self.jsblogon.LOGON_warning.setStyleSheet("color: rgb(255, 0, 0);")
                self.jsblogon.LOGON_warning.setText(_translate("JSB_logon", '账户或密码错误，请检查或前往注册'))
                self.jsblogon.LOGON_warning.show()
                self.jsblogon.LOGON_zhanghu_input.clear()
                self.jsblogon.LOGON_key1_input.clear()
        else:
            _translate = QtCore.QCoreApplication.translate
            zhanghu = self.jsblogon.LOGON_zhanghu_input.text()
            key = self.jsblogon.LOGON_key1_input.text()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 账户信息 where 账户名 = ? ', (zhanghu,))
            result = cursor.fetchall()
            if result != []:
                cursor.execute('update 账户信息 set 密码 = ? where 账户名 = ?', (key, zhanghu))
                cursor.execute('update 操作数据 set 值 = ? where 账户名 = ?', (False, zhanghu))
                cursor.close()
                conn.commit()
                conn.close()
                self.LOGtime = 0
                self.JSBtimer = QTimer(self)
                self.JSBtimer.start(100)
                self.JSBtimer.timeout.connect(self.JSB_logTimer)
                self.jsblogon.LOGON_warning.show()
                self.jsblogon.LOGON_warning.setStyleSheet("color: rgb(85, 255, 0);")
                self.jsblogon.LOGON_warning.setText(_translate("JSB_logon", '登录成功，欢迎使用！'))
                self.JSB_nowuser = zhanghu
                self.automatic_logon()
                self.jsblogon.LOGON_neverlogon.setEnabled(False)
                self.jsblogon.LOGON_logonbutton.setEnabled(False)
                self.jsblogon.LOGON_zhucebutton.setEnabled(False)
                self.jsblogon.LOGON_backbutton.setEnabled(False)
                self.jsblogon.LOGON_forgetbutton.setEnabled(False)
            else:
                self.jsblogon.LOGON_warning.setStyleSheet("color: rgb(255, 0, 0);")
                self.jsblogon.LOGON_warning.setText(_translate("JSB_logon", '账户不存在，请检查或前往注册'))
                self.jsblogon.LOGON_warning.show()
                self.jsblogon.LOGON_zhanghu_input.clear()
                self.jsblogon.LOGON_key1_input.clear()
                cursor.close()
                conn.close()

    def JSB_logTimer(self):
        _translate = QtCore.QCoreApplication.translate
        self.LOGtime += 0.1
        if self.LOGtime >= 0.7:
            self.JSBtimer.stop()
            self.jsblogon.LOGON_forgetbutton.show()
            self.jsblogon.LOGON_zhanghu.setText(_translate("JSB_logon", "账户："))
            self.jsblogon.LOGON_backbutton.setText(_translate("JiShiBen", "退出"))
            self.jsblogon.LOGON_zhanghu_input.clear()
            self.jsblogon.LOGON_key1_input.clear()
            self.jsblogon.LOGON_neverlogon.setEnabled(True)
            self.jsblogon.LOGON_logonbutton.setEnabled(True)
            self.jsblogon.LOGON_zhucebutton.setEnabled(True)
            self.jsblogon.LOGON_backbutton.setEnabled(True)
            self.jsblogon.LOGON_forgetbutton.setEnabled(True)
            self.jsblogon.close()
            self.JSB_Action()

    def JSB_Action(self):
        self.jsb = Ui_JiShiBen()
        self.hide()
        try:
            self.music_timer.stop()
            self.musicplayer.pause()
        except:
            pass
        conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
        cursor = conn.cursor()
        cursor.execute('select * from 记事本文件数据 where 记事账户 = ?', (self.JSB_nowuser,))
        result = cursor.fetchall()
        self.JSB_comboboxlist = ['选择要编辑的文件']
        if result != []:
            for i in result:
                self.JSB_comboboxlist.append(i[0])
            self.jsb.JSB_combobox.addItems(self.JSB_comboboxlist)
        self.jsb.show()
        # 设置下拉栏隐藏，（隐藏 = 透明加禁用）
        self.jsb.JSB_combobox.setEnabled(False)
        self.jsb.JSB_combobox.setStyleSheet("color: rgb(255, 255,255,0);background-color: rgb(255, 255, 255,0);")
        self.jsb.JSB_combobox.currentIndexChanged.connect(self.JSB_comboboxchangeevent)
        self.jsb.JSB_toolBar.actionTriggered[QtWidgets.QAction].connect(self.JSB_Event)
        self.JSB_open_mark = '未打开'
        self.JSB_shanchu_mark = '未删除'
        self.JSB_clear_A_combobox_mark = 0
        self.quit_mark = -1

    def JSB_xinjianevent(self):
        if self.jsb.JSB_lineEdit.text() != '':
            self.biaoti = self.jsb.JSB_lineEdit.text()
            self.text = self.jsb.JSB_textBrowser.toPlainText()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 记事本文件数据 where 标题 =? and 记事账户 = ?', (self.biaoti, self.JSB_nowuser))
            result = cursor.fetchall()
            if result == []:
                title = '是否保存' + ' “ ' + self.biaoti + ' “ ' + '的内容?'
                self.MESSAGE = Ui_KSFX_Message('询问', title, '检测到该文件还不存在于，是否进行保存？')
                self.MESSAGE.show()
                self.MESSAGE_timer = QTimer(self)
                self.MESSAGE_timer.start(100)
                self.MESSAGE_timer.timeout.connect(self.ME_result0)
                cursor.close()
                conn.close()
            else:
                if result[0][1] == self.text:  # 内容没有改动
                    cursor.close()
                    conn.close()
                else:  # 内容改动了
                    title = '是否改动' + ' ” ' + self.biaoti + ' " ' + '的内容?'
                    self.MESSAGE = Ui_KSFX_Message('询问', '', title)
                    self.MESSAGE.show()
                    self.MESSAGE_timer = QTimer(self)
                    self.MESSAGE_timer.start(100)
                    self.MESSAGE_timer.timeout.connect(self.ME_result1)
                    cursor.close()
                    conn.close()
        self.jsb.JSB_textBrowser.clear()
        self.jsb.JSB_lineEdit.clear()

    def ME_result0(self):  # 当选择确定后绑定的新增函数
        self.MESSAGE.Result()
        if self.MESSAGE.Answer == 1:  # 选择了确定
            self.MESSAGE_timer.stop()
            self.MESSAGE.close()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('insert  into 记事本文件数据 (标题,记事内容,记事账户) values (?,?,?)',
                           (self.biaoti, self.text, self.JSB_nowuser))
            cursor.close()
            conn.commit()
            conn.close()
            self.JSB_comboboxlist.append(self.biaoti)
            self.jsb.JSB_combobox.addItem(self.biaoti)
            if self.quit_mark == 1:
                self.jsb.close()
                self.show()
            else:
                self.MESSAGE = Ui_KSFX_Message('通知', '保存成功！', '文件已保存，可前往查看！')
                self.MESSAGE.show()
        elif self.MESSAGE.Answer == 0:
            self.MESSAGE_timer.stop()
            self.MESSAGE.close()
            if self.quit_mark == 1:
                self.jsb.close()
                self.show()
        else:
            pass

    def ME_result1(self):  # 当选择确定后绑定的修改函数
        self.MESSAGE.Result()
        if self.MESSAGE.Answer == 1:
            self.MESSAGE_timer.stop()
            self.MESSAGE.close()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('update 记事本文件数据 set 记事内容 = ? where 标题 = ? and 记事账户 = ?',
                           (self.text, self.biaoti, self.JSB_nowuser))
            cursor.close()
            conn.commit()
            conn.close()
            self.JSB_comboboxlist.append(self.biaoti)
            self.jsb.JSB_combobox.addItem(self.biaoti)
            if self.quit_mark == 1:
                self.jsb.close()
                self.show()
            else:
                self.MESSAGE = Ui_KSFX_Message('通知', '保存成功！', '文件已保存，可前往查看！')
                self.MESSAGE.show()
        elif self.MESSAGE.Answer == 0:
            self.MESSAGE_timer.stop()
            self.MESSAGE.close()
            if self.quit_mark == 1:
                self.jsb.close()
                self.show()
        else:
            pass

    def JSB_saveevent(self):
        self.biaoti = self.jsb.JSB_lineEdit.text()
        if self.biaoti != '':
            neirong = self.jsb.JSB_textBrowser.toPlainText()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 记事本文件数据 where 标题 =? and 记事账户 = ?', (self.biaoti, self.JSB_nowuser))
            result = cursor.fetchall()
            if result == []:  # 文件不存在，直接保存！
                cursor.execute('insert into 记事本文件数据 (标题,记事内容,记事账户) values(?,?,?)',
                               (self.biaoti, neirong, self.JSB_nowuser))
                cursor.close()
                conn.commit()
                conn.close()
                self.JSB_comboboxlist.append(self.biaoti)
                self.jsb.JSB_combobox.addItem(self.biaoti)
                self.MESSAGE = Ui_KSFX_Message('通知', '保存成功', '记事内容已保存至数据库！')
                self.MESSAGE.show()
            else:  # 文件存在，询问是否更改！
                title = '是否改动' + ' “ ' + self.biaoti + ' “ ' + '的内容?'
                self.MESSAGE = Ui_KSFX_Message('询问', '', title)
                self.MESSAGE.show()
                self.MESSAGE_timer = QTimer(self)
                self.MESSAGE_timer.start(100)
                self.MESSAGE_timer.timeout.connect(self.ME_result1)
                cursor.close()
                conn.close()
        else:
            self.MESSAGE = Ui_KSFX_Message('通知', '保存失败', '记事内容不能为空！')
            self.MESSAGE.show()

    def JSB_giveupevent(self):
        self.JSB_ing(False)
        self.JSB_open_mark = '未打开'
        self.JSB_shanchu_mark = '未删除'

    def JSB_shanchuevent(self):
        self.JSB_ing(True, '删除')
        self.JSB_shanchu_mark = '删除'

    def JSB_helpevent(self):
        self.MESSAGE = Ui_KSFX_Message('通知', '帮助', '非常好用的软件！')
        self.MESSAGE.show()

    def JSB_quitevent(self):
        self.quit_mark = 1
        if self.jsb.JSB_lineEdit.text() != '':
            self.biaoti = self.jsb.JSB_lineEdit.text()
            self.text = self.jsb.JSB_textBrowser.toPlainText()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 记事本文件数据 where 标题 =? and 记事账户 = ?', (self.biaoti, self.JSB_nowuser))
            result = cursor.fetchall()
            if result == []:  # 文件不存在，询问是否保存！
                title = '是否保存' + ' “ ' + self.biaoti + ' “ ' + '的内容?'
                self.MESSAGE = Ui_KSFX_Message('询问', title, '检测到该文件还不存在于，是否进行保存？')
                self.MESSAGE.show()
                self.MESSAGE_timer = QTimer(self)
                self.MESSAGE_timer.start(100)
                self.MESSAGE_timer.timeout.connect(self.ME_result0)
                cursor.close()
                conn.close()
            else:
                if result[0][1] == self.text:  # 内容没有改动
                    cursor.close()
                    conn.close()
                    self.jsb.close()
                    self.show()
                else:  # 内容改动了
                    title = '是否改动' + ' “ ' + self.biaoti + ' “ ' + '的内容?'
                    self.MESSAGE = Ui_KSFX_Message('询问', '', title)
                    self.MESSAGE.show()
                    self.MESSAGE_timer = QTimer(self)
                    self.MESSAGE_timer.start(100)
                    self.MESSAGE_timer.timeout.connect(self.ME_result1)
                    cursor.close()
                    conn.close()
        else:
            self.jsb.close()
            self.show()
            if self.bj_music != None:
                if self.bj_music == True:
                    self.music_marktime = 0
                    self.music_timer = QTimer(self)
                    self.music_timer.timeout.connect(self.Background_Music)
                    self.music_timer.start(100)
            else:
                pass

    def JSB_openevent(self):
        if self.jsb.JSB_lineEdit.text() != '':
            self.biaoti = self.jsb.JSB_lineEdit.text()
            self.text = self.jsb.JSB_textBrowser.toPlainText()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 记事本文件数据 where 标题 = ? and 记事账户 = ?', (self.biaoti, self.JSB_nowuser))
            result = cursor.fetchall()
            if result == []:
                title = '是否保存' + ' “ ' + self.biaoti + ' “ ' + '的内容?'
                self.MESSAGE = Ui_KSFX_Message('询问', title, '检测到该文件还不存在于，是否进行保存？')
                self.MESSAGE.show()
                self.MESSAGE_timer = QTimer(self)
                self.MESSAGE_timer.start(100)
                self.MESSAGE_timer.timeout.connect(self.ME_result0)
                cursor.close()
                conn.close()
            else:
                if result[0][1] == self.text:  # 内容没有改动
                    cursor.close()
                    conn.close()
                else:  # 内容改动了
                    title = '是否改动' + ' “ ' + self.biaoti + ' “ ' + '的内容?'
                    self.MESSAGE = Ui_KSFX_Message('询问', '', title)
                    self.MESSAGE.show()
                    self.MESSAGE_timer = QTimer(self)
                    self.MESSAGE_timer.start(100)
                    self.MESSAGE_timer.timeout.connect(self.ME_result1)
                    cursor.close()
                    conn.close()
        self.JSB_ing(True, '打开')
        self.JSB_open_mark = '打开'

    def JSB_ing(self, value, work=None):
        if value == False:  # 隐藏下拉组合框
            self.jsb.JSB_xinjian.setEnabled(True)
            self.jsb.JSB_help.setEnabled(True)
            self.jsb.JSB_open.setEnabled(True)
            self.jsb.JSB_baocun.setEnabled(True)
            self.jsb.JSB_shanchu.setEnabled(True)
            self.jsb.JSB_tuichu.setEnabled(True)
            self.jsb.JSB_combobox.setEnabled(False)
            self.jsb.JSB_combobox.setStyleSheet("color: rgb(255, 255,255,0);background-color: rgb(255, 255, 255,0);")
        else:  # 显示下拉组合框
            self.jsb.JSB_combobox.setEnabled(True)
            self.jsb.JSB_combobox.setStyleSheet("color: rgb(0,0,0);background-color: rgb(255, 255, 255);")
            if work == '新建':
                self.jsb.JSB_open.setEnabled(False)
                self.jsb.JSB_help.setEnabled(False)
                self.jsb.JSB_baocun.setEnabled(False)
                self.jsb.JSB_shanchu.setEnabled(False)
                self.jsb.JSB_tuichu.setEnabled(False)
            elif work == '打开':
                self.jsb.JSB_xinjian.setEnabled(False)
                self.jsb.JSB_help.setEnabled(False)
                self.jsb.JSB_baocun.setEnabled(False)
                self.jsb.JSB_shanchu.setEnabled(False)
                self.jsb.JSB_tuichu.setEnabled(False)
            elif work == '保存':
                self.jsb.JSB_xinjian.setEnabled(False)
                self.jsb.JSB_help.setEnabled(False)
                self.jsb.JSB_open.setEnabled(False)
                self.jsb.JSB_shanchu.setEnabled(False)
                self.jsb.JSB_tuichu.setEnabled(False)
            elif work == '删除':
                self.jsb.JSB_xinjian.setEnabled(False)
                self.jsb.JSB_help.setEnabled(False)
                self.jsb.JSB_baocun.setEnabled(False)
                self.jsb.JSB_open.setEnabled(False)
                self.jsb.JSB_tuichu.setEnabled(False)
            else:
                pass

    def JSB_comboboxchangeevent(self):
        if self.JSB_clear_A_combobox_mark == 0:  # 在正常情况下，即不是由于清除导致的改变走这边！
            _translate = QtCore.QCoreApplication.translate
            self.JSB_While = False
            if self.JSB_open_mark == '打开':
                self.JSB_open_mark = '未打开'
                self.biaoti = self.jsb.JSB_combobox.currentText()
                conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
                cursor = conn.cursor()
                cursor.execute('select * from 记事本文件数据 where 标题 = ? and 记事账户 = ? ', (self.biaoti, self.JSB_nowuser))
                result = cursor.fetchall()
                cursor.close()
                conn.close()
                self.jsb.JSB_lineEdit.setText(_translate("JiShiBen", result[0][0]))
                self.jsb.JSB_textBrowser.setText(_translate("JiShiBen", result[0][1]))
                self.JSB_ing(False)
            if self.JSB_shanchu_mark == '删除':
                self.biaoti = self.jsb.JSB_combobox.currentText()
                if self.biaoti != self.JSB_comboboxlist[0]:
                    self.JSB_Delete_MESSAGE = Ui_KSFX_Message('询问', '删除', '是否确认删除:' + '\n' + self.biaoti)
                    self.JSB_Delete_MESSAGE.show()
                    self.JSB_Deletetimer = QTimer(self)
                    self.JSB_Deletetimer.start(100)
                    self.JSB_Deletetimer.timeout.connect(self.JSB_DeletetimerEvent)
        else:
            self.JSB_clear_A_combobox_mark -= 1

    def JSB_DeletetimerEvent(self):
        self.JSB_Delete_MESSAGE.Result()
        if self.JSB_Delete_MESSAGE.Answer == 1:  # 选择了确定
            self.JSB_While = True
            self.JSB_Deletetimer.stop()
            self.JSB_Delete_MESSAGE.close()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('delete from 记事本文件数据 where 标题 = ? and 记事账户 = ?', (self.biaoti, self.JSB_nowuser))
            cursor.close()
            conn.commit()
            conn.close()
            self.MESSAGE = Ui_KSFX_Message('通知', '删除成功', '成功删除目标记事！')
            self.MESSAGE.show()
            self.JSB_clear_A_combobox_mark = 2
            self.jsb.JSB_combobox.clear()
            self.JSB_comboboxlist.remove(self.biaoti)
            self.jsb.JSB_combobox.addItems(self.JSB_comboboxlist)
            self.JSB_shanchu_mark = '未删除'
            self.JSB_ing(False)
        elif self.JSB_Delete_MESSAGE.Answer == 0:  # 选择了取消
            self.JSB_While = True
            self.JSB_Deletetimer.stop()
            self.JSB_Delete_MESSAGE.close()
        else:
            pass

    def JSB_Event(self, m):
        if m.text() == '新建':
            self.JSB_xinjianevent()
        elif m.text() == '保存':
            self.JSB_saveevent()
        elif m.text() == '删除':
            self.JSB_shanchuevent()
        elif m.text() == '帮助':
            self.JSB_helpevent()
        elif m.text() == '退出':
            self.JSB_quitevent()
        elif m.text() == '打开':
            self.JSB_openevent()
        elif m.text() == '取消':
            self.JSB_giveupevent()
        else:
            pass

    def YWMX_xunwen_timerevent(self):
        _translate = QtCore.QCoreApplication.translate
        self.YWMX_MESSAGE.Result()
        if self.YWMX_MESSAGE.Answer == 1:  # 选择了确定
            self.ywmx_xunwen_timer.stop()
            self.YWMX_MESSAGE.close()
            Yright = 0
            Ywrong = 0
            frequency0 = 0
            frequency1 = 0
            self.YW_mxWronglist = []
            self.YW_mxRightlist = []
            string = ''
            for i in self.YW_mx_YourAnswer:
                if i == self.YW_mxanswer[frequency0]:
                    Yright += 1
                    frequency0 += 1
                else:
                    Ywrong += 1
                    self.YW_mxRightlist.append(self.YW_mxanswer[frequency0])
                    self.YW_mxWronglist.append(self.YW_mxquestion[frequency0])
                    frequency0 += 1
            for i in range(Ywrong):
                string += self.YW_mxWronglist[frequency1] + '  ---  ' + self.YW_mxRightlist[frequency1] + '\n'
                frequency1 += 1
            self.YW_mxAccuracyrate = round(Yright / len(self.YW_mx_YourAnswer), 2) * 100  # 计算正确率
            self.YW_mxTWQ = Ui_Beidanci_Finally(string)
            self.YW_mxTWQ.zhengquelv_input.setText(
                _translate("Beidanci_Finally", str(int(self.YW_mxAccuracyrate)) + '(正确：' + str(
                    Yright) + ' 错误：' + str(Ywrong) + ')'))
            self.YW_mxTWQ.cuowu_input.setText(_translate("Beidanci_Finally", string))
            self.YW_mxTWQ.xiangmu.setText(_translate("Beidanci_Finally", "项目 --- 古诗词理解性默写"))
            self.YW_mxTWQ.back.setShortcut(_translate("Beidanci_Finally", "Return"))
            self.YW_mxTWQ.show()
            self.hide()
            if self.YW_mxAccuracyrate == 100:
                self.YW_mxTWQ.good.setText(_translate("Beidanci_Finally", "满分！你真是太棒啦！"))
                self.YW_mxTWQ.star1.show()
                self.YW_mxTWQ.star1_2.show()
                self.YW_mxTWQ.star1_3.show()
                self.YW_mxTWQ.star1_4.show()
                self.YW_mxTWQ.star1_5.show()
                self.YW_mxTWQ.back.show()
            elif 100 > self.YW_mxAccuracyrate >= 90:
                self.YW_mxTWQ.good.setText(_translate("Beidanci_Finally", "完成得不错，继续加油哦"))
                self.YW_mxTWQ.star1.show()
                self.YW_mxTWQ.star1_2.show()
                self.YW_mxTWQ.star1_3.show()
                self.YW_mxTWQ.star1_4.show()
                self.YW_mxTWQ.back.show()
            elif 90 > self.YW_mxAccuracyrate >= 60:
                self.YW_mxTWQ.good.setText(_translate("Beidanci_Finally", "革命还未胜利，同志还需努力！"))
                self.YW_mxTWQ.star1.show()
                self.YW_mxTWQ.star1_2.show()
                self.YW_mxTWQ.star1_3.show()
                self.YW_mxTWQ.back.show()
            else:
                self.YW_mxTWQ.good.setText(_translate("Beidanci_Finally", "完成得太糟糕了，再试一次吧！"))
                self.YW_mxTWQ.star1.show()
                self.YW_mxTWQ.star1_2.show()
                self.YW_mxTWQ.back.show()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select*from 语文古诗词理解性默写正确率数据')
            result = cursor.fetchall()
            cursor.execute('insert into 语文古诗词理解性默写正确率数据(序号,正确率) values (?,?)',
                           (str(len(result) + 1), str(int(self.YW_mxAccuracyrate))))
            cursor.close()
            conn.commit()
            conn.close()
            self.YW_mxTWQ.back.clicked.connect(self.Finally)
        elif self.YWMX_MESSAGE.Answer == 0:  # 选择了取消
            self.ywmx_xunwen_timer.stop()
            self.YWMX_MESSAGE.close()
        else:
            pass

    def YW_mxyiwenEvent(self):
        self.YW_mx_Message = Ui_KSFX_Message('通知', '帮助', '语文默写题库由您的数据库提供，操作数据库请前往管理者模式，感谢您的使用！')
        self.YW_mx_Message.show()

    def YW_mxhand(self):
        _translate = QtCore.QCoreApplication.translate
        if self.YW_mxpage == self.YW_mxxiayiyeshuliang:
            try:
                self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4] = self.YW_mx_input1.text()
            except:
                pass
            try:
                self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 1] = self.YW_mx_input2.text()
            except:
                pass
            try:
                self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 2] = self.YW_mx_input3.text()
            except:
                pass
            try:
                self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 3] = self.YW_mx_input4.text()
            except:
                pass
        else:
            self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4] = self.YW_mx_input1.text()
            self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 1] = self.YW_mx_input2.text()
            self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 2] = self.YW_mx_input3.text()
            self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 3] = self.YW_mx_input4.text()
        if '' not in self.YW_mx_YourAnswer:  # 是否有没作答题目
            self.YWMX_MESSAGE = Ui_KSFX_Message('询问', '是否确认提交？', '您已作答完毕，但请仔细检查哦！')
            self.YWMX_MESSAGE.show()
            self.ywmx_xunwen_timer = QTimer(self)
            self.ywmx_xunwen_timer.start(100)
            self.ywmx_xunwen_timer.timeout.connect(self.YWMX_xunwen_timerevent)
        else:
            self.YWMX_MESSAGE = Ui_KSFX_Message('询问', '是否确认提交？', '您还有尚未作答的题目，是否确认提交？')
            self.YWMX_MESSAGE.show()
            self.ywmx_xunwen_timer = QTimer(self)
            self.ywmx_xunwen_timer.start(100)
            self.ywmx_xunwen_timer.timeout.connect(self.YWMX_xunwen_timerevent)

    def YW_mxback(self):
        _translate = QtCore.QCoreApplication.translate
        self.YW_mxpage -= 1
        self.YW_mxxiayiye_lable.setEnabled(True)
        self.YW_mx_input1.setFocus()
        if self.YW_mxpage == 1:
            self.YW_mxshangyiye_lable.setEnabled(False)
        self.YW_mx_input2.setEnabled(True)
        self.YW_mx_input3.setEnabled(True)
        self.YW_mx_input4.setEnabled(True)
        self.YW_mx_YourAnswer[self.YW_mxpage * 4] = self.YW_mx_input1.text()
        if self.YW_mx_input2.text() != '暂无数据':  # 存在这一行，将这行作答放到作答列表中
            self.YW_mx_YourAnswer[self.YW_mxpage * 4 + 1] = self.YW_mx_input2.text()
        if self.YW_mx_input3.text() != '暂无数据':
            self.YW_mx_YourAnswer[self.YW_mxpage * 4 + 2] = self.YW_mx_input3.text()
        if self.YW_mx_input4.text() != '暂无数据':
            self.YW_mx_YourAnswer[self.YW_mxpage * 4 + 3] = self.YW_mx_input4.text()
        self.YW_mx_tm1.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4]))
        self.YW_mx_tm2.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4 + 1]))
        self.YW_mx_tm3.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4 + 2]))
        self.YW_mx_tm4.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4 + 3]))
        self.YW_mx_input1.setText(_translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4]))
        self.YW_mx_input2.setText(
            _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 1]))
        self.YW_mx_input3.setText(
            _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 2]))
        self.YW_mx_input4.setText(
            _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 3]))

    def YW_mxnext(self):
        _translate = QtCore.QCoreApplication.translate
        if self.YW_mxcomboBox.currentIndex() != 0:
            self.YW_mxpage = 1 + self.YW_mxpage
            self.YW_mx_input1.setFocus()
            self.YW_mxshangyiye_lable.setEnabled(True)
            if self.YW_mxpage >= self.YW_mxxiayiyeshuliang:
                self.YW_mxxiayiye_lable.setEnabled(False)
            if self.YW_mx_biao == True and self.YW_mxpage < self.YW_mxxiayiyeshuliang or self.YW_mx_biao == False and self.YW_mxpage <= self.YW_mxxiayiyeshuliang:  # 够下一页的所有内容
                self.YW_mx_tm1.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4]))
                self.YW_mx_tm2.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4 + 1]))
                self.YW_mx_tm3.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4 + 2]))
                self.YW_mx_tm4.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4 + 3]))
                self.YW_mx_YourAnswer[(self.YW_mxpage - 2) * 4] = self.YW_mx_input1.text()
                self.YW_mx_YourAnswer[(self.YW_mxpage - 2) * 4 + 1] = self.YW_mx_input2.text()
                self.YW_mx_YourAnswer[(self.YW_mxpage - 2) * 4 + 2] = self.YW_mx_input3.text()
                self.YW_mx_YourAnswer[(self.YW_mxpage - 2) * 4 + 3] = self.YW_mx_input4.text()
                self.YW_mx_input1.setText(
                    _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4]))
                self.YW_mx_input2.setText(
                    _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 1]))
                self.YW_mx_input3.setText(
                    _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 2]))
                self.YW_mx_input4.setText(
                    _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 3]))
            else:  # 下一页内容不完全了
                self.YW_mx_YourAnswer[(self.YW_mxpage - 2) * 4] = self.YW_mx_input1.text()
                self.YW_mx_YourAnswer[(self.YW_mxpage - 2) * 4 + 1] = self.YW_mx_input2.text()
                self.YW_mx_YourAnswer[(self.YW_mxpage - 2) * 4 + 2] = self.YW_mx_input3.text()
                self.YW_mx_YourAnswer[(self.YW_mxpage - 2) * 4 + 3] = self.YW_mx_input4.text()
                self.YW_mx_tm1.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4]))
                self.YW_mx_input1.setText(
                    _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4]))
                try:
                    self.YW_mx_input2.setText(
                        _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 1]))
                    self.YW_mx_tm2.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4 + 1]))
                    self.YW_mxguo2 = 0
                except:
                    self.YW_mx_input2.setText((_translate("Homepage", '暂无数据')))
                    self.YW_mx_tm2.setText(_translate("Homepage", '暂无数据'))
                    self.YW_mxguo2 = 1
                try:
                    self.YW_mx_tm3.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4 + 2]))
                    self.YW_mx_input3.setText(
                        _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 2]))
                    self.YW_mxguo3 = 0
                except:
                    self.YW_mx_input3.setText((_translate("Homepage", '暂无数据')))
                    self.YW_mx_tm3.setText(_translate("Homepage", '暂无数据'))
                    self.YW_mxguo3 = 1
                try:
                    self.YW_mx_input4.setText(
                        _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 3]))
                    self.YW_mx_tm4.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4 + 3]))
                    self.YW_mxguo4 = 0
                except:
                    self.YW_mx_input4.setText((_translate("Homepage", '暂无数据')))
                    self.YW_mx_tm4.setText(_translate("Homepage", '暂无数据'))
                    self.YW_mxguo4 = 1
                if self.YW_mxguo2 == 1:
                    self.YW_mx_input2.setEnabled(False)
                else:
                    self.YW_mx_input2.setText(
                        _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 1]))
                if self.YW_mxguo3 == 1:
                    self.YW_mx_input3.setEnabled(False)
                else:
                    self.YW_mx_input3.setText(
                        _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 2]))
                if self.YW_mxguo4 == 1:
                    self.YW_mx_input4.setEnabled(False)
                else:
                    self.YW_mx_input4.setText(
                        _translate("Homepage", self.YW_mx_YourAnswer[(self.YW_mxpage - 1) * 4 + 3]))
        else:
            self.YW_mxshangyiye_lable.setEnabled(False)
            self.YW_mxxiayiye_lable.setEnabled(False)

    def YWMXchange(self):
        _translate = QtCore.QCoreApplication.translate
        if self.YWMXchange_Mark == 0:  # 清理的时候会报错，要用这个！！
            self.YW_mxlable.setText(_translate("Homepage", self.YW_mxcomboBox.currentText()))
            self.YW_mxpage = 1
            self.YW_mxxiayiyeshuliang = 0
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 语文默写古诗文 where 古诗文诗名 = ? ', (self.YW_mxcomboBox.currentText(),))
            result = cursor.fetchall()
            cursor.close()
            conn.commit()
            conn.close()
            self.YW_mxquestion = []
            self.YW_mxanswer = []
            self.YW_mx_input1.clear()
            self.YW_mx_input2.clear()
            self.YW_mx_input3.clear()
            self.YW_mx_input4.clear()
            for i in result:
                self.YW_mxquestion.append(i[1])
                self.YW_mxanswer.append(i[2])
            many = len(self.YW_mxquestion)
            if many % 4 != 0:  # 有参与就True
                self.YW_mxxiayiyeshuliang = int(many / 4) + 1
                self.YW_mx_biao = True
            else:  # 刚刚好就是False
                self.YW_mxxiayiyeshuliang = many / 4
                self.YW_mx_biao = False
            self.YW_mx_YourAnswer = []
            self.YW_mx_YourAnswer = [''] * many
            if many == 1:
                self.YW_mx_tm1.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4]))
                self.YW_mx_input2.setText((_translate("Homepage", '暂无数据')))
                self.YW_mx_tm2.setText(_translate("Homepage", '暂无数据'))
                self.YW_mx_input3.setText((_translate("Homepage", '暂无数据')))
                self.YW_mx_tm3.setText(_translate("Homepage", '暂无数据'))
                self.YW_mx_input4.setText((_translate("Homepage", '暂无数据')))
                self.YW_mx_tm4.setText(_translate("Homepage", '暂无数据'))
                self.YW_mx_input1.setEnabled(True)
                self.YW_mx_input2.setEnabled(False)
                self.YW_mx_input3.setEnabled(False)
                self.YW_mx_input4.setEnabled(False)
                self.YW_mxxiayiye_lable.setEnabled(False)
            elif many == 2:
                self.YW_mx_input3.setText((_translate("Homepage", '暂无数据')))
                self.YW_mx_tm3.setText(_translate("Homepage", '暂无数据'))
                self.YW_mx_input4.setText((_translate("Homepage", '暂无数据')))
                self.YW_mx_tm4.setText(_translate("Homepage", '暂无数据'))
                self.YW_mx_input1.setEnabled(True)
                self.YW_mx_input2.setEnabled(True)
                self.YW_mx_input3.setEnabled(False)
                self.YW_mx_input4.setEnabled(False)
                self.YW_mxxiayiye_lable.setEnabled(False)
            elif many == 3:
                self.YW_mx_input4.setText((_translate("Homepage", '暂无数据')))
                self.YW_mx_tm4.setText(_translate("Homepage", '暂无数据'))
                self.YW_mx_input1.setEnabled(True)
                self.YW_mx_input2.setEnabled(True)
                self.YW_mx_input3.setEnabled(True)
                self.YW_mx_input4.setEnabled(False)
                self.YW_mxxiayiye_lable.setEnabled(False)
            else:
                self.YW_mx_tm1.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4]))
                self.YW_mx_tm2.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4 + 1]))
                self.YW_mx_tm3.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4 + 2]))
                self.YW_mx_tm4.setText(_translate("Homepage", self.YW_mxquestion[(self.YW_mxpage - 1) * 4 + 3]))
                self.YW_mx_input1.setEnabled(True)
                self.YW_mx_input2.setEnabled(True)
                self.YW_mx_input3.setEnabled(True)
                self.YW_mx_input4.setEnabled(True)
                self.YW_mxxiayiye_lable.setEnabled(True)
            self.YW_mx_input1.setFocus()
            self.YW_mxyiwen_lable.hide()
            self.YW_mxtijiao_lable.show()
            self.YW_mxcomboBox.hide()
        else:  # 执行清理任务
            self.YW_mxtijiao_lable.hide()
            self.YW_mxyiwen_lable.show()
            self.YW_mx_input1.setEnabled(False)
            self.YW_mx_input2.setEnabled(False)
            self.YW_mx_input3.setEnabled(False)
            self.YW_mx_input4.setEnabled(False)
            self.YW_mxshangyiye_lable.setEnabled(False)
            self.YW_mxxiayiye_lable.setEnabled(False)
            self.YW_mxlable.setText(_translate("Homepage", "请选择默写诗词"))
            self.YW_mx_tm1.setText(_translate("Homepage",
                                              "<html><head/><body><p><span style=\" font-weight:600;\">默写第一行题目</span></p></body></html>"))
            self.YW_mx_tm2.setText(_translate("Homepage",
                                              "<html><head/><body><p><span style=\" font-weight:600;\">默写第二行题目</span></p></body></html>"))
            self.YW_mx_tm3.setText(_translate("Homepage",
                                              "<html><head/><body><p><span style=\" font-weight:600;\">默写第三行题目</span></p></body></html>"))
            self.YW_mx_tm4.setText(_translate("Homepage",
                                              "<html><head/><body><p><span style=\" font-weight:600;\">默写第四行题目</span></p></body></html>"))
            self.YWMXchange_Mark -= 1
            self.YW_mxcomboBox.show()

    def SS_ZHUYE(self):
        text = '四个难度只在答题时间和题目数量上有所不同，均为20—40的两位数乘法。' + '\n' + '四个难度对应时间和题目数量如下：' + '\n' + \
               '简单：12s，8题   普通：9s,12题    困难：7s，15题    地狱：5s，20题'
        self.MESSAGE = Ui_KSFX_Message('通知', '速算规则', text)
        self.MESSAGE.show()

    def SSnext(self):
        _translate = QtCore.QCoreApplication.translate
        if self.SSxiaable == 1:  # 可以开始下一题操作
            self.SSxiaable = 0
            self.SStimeprogress.setFormat(_translate("Homepage", '100%'))
            self.SSpicture.hide()
            self.SShuida.hide()
            self.SStishi.setText(_translate("Homepage", "请输入你的答案"))
            self.SSlineEdit.setEnabled(True)
            self.SSlineEdit.clear()
            self.SSlineEdit.setFocus()
            self.SSxiayiti.hide()
            self.SSkaishi.show()
            self.SStijiao.hide()
            self.lcdNumber1.hide()
            self.lcdNumber2.hide()
            self.SSlineEdit.hide()
            self.SStishi.hide()
            self.SSlable_cheng.hide()
            self.SStishi.setStyleSheet("")
            if self.SSnandubiaozhu == '简单':
                self.SStimeprogress.setProperty("value", 12)
                self.SSLCDshengyu.setProperty("value", 12)
                self.SStime0 = 12
            elif self.SSnandubiaozhu == '普通':
                self.SStimeprogress.setProperty("value", 9)
                self.SSLCDshengyu.setProperty("value", 9)
                self.SStime0 = 9
            elif self.SSnandubiaozhu == '困难':
                self.SStimeprogress.setProperty("value", 7)
                self.SSLCDshengyu.setProperty("value", 7)
                self.SStime0 = 7
            else:
                self.SStimeprogress.setProperty("value", 5)
                self.SSLCDshengyu.setProperty("value", 5)
                self.SStime0 = 5
        else:
            self.SS_MESSAGE = Ui_KSFX_Message('警告', '', '请先完成当前作答！')
            self.SS_MESSAGE.show()

    def SS(self):
        self.SScomboBox.hide()
        self.SStijiao.show()
        self.SSxiayiti.show()
        self.SStishi.show()
        self.SSlineEdit.show()
        self.SSlineEdit.setFocus()
        self.SSlineEdit.setValidator(QtGui.QIntValidator(000, 2147483647))
        self.SSkaishi.hide()
        self.SSnumber1 = random.randint(20, 40)
        self.SSnumber2 = random.randint(20, 40)
        self.lcdNumber1.setProperty("intValue", self.SSnumber1)
        self.lcdNumber2.setProperty("intValue", self.SSnumber2)
        self.lcdNumber1.show()
        self.lcdNumber2.show()
        self.SSlable_cheng.show()
        self.SStimer0 = QTimer(self)
        self.SStimer0.start(1000)
        self.SStimeA = self.SStime0
        self.SStimer0.timeout.connect(self.SS_Jian)

    def SSTiJiao(self):
        if self.SSxiaable != 1:  # 还没提交
            _translate = QtCore.QCoreApplication.translate
            if self.SSlineEdit.text() == str(self.SSnumber1 * self.SSnumber2):  # 回答正确
                self.SSpicture.setStyleSheet("border-image: url(:/速算/图片文件夹/正确.png);")
                self.SSlineEdit.setEnabled(False)
                self.SShuida.setStyleSheet("color: rgb(85, 255, 127);")
                self.SShuida.setText(_translate("Homepage", "回答正确！"))
                self.SSpicture.show()
                self.SShuida.show()
                self.SSxiaable = 1
                self.SStishu += 1
                self.SSright += 1
                self.SSwanchengshu.setText(_translate("Homepage", "已完成 " + str(self.SStishu) + " 题"))
            else:  # 回答错误
                self.SSlineEdit.setText(str(self.SSnumber1 * self.SSnumber2))
                self.SSlineEdit.setEnabled(False)
                self.SStishi.setStyleSheet("color: rgb(255, 0, 0);")
                self.SStishi.setText(_translate("Homepage", "正确答案："))
                self.SSpicture.setStyleSheet("border-image: url(:/速算/图片文件夹/错误.png);")
                self.SShuida.setText(_translate("Homepage", "回答错误！"))
                self.SShuida.setStyleSheet("color: rgb(255, 0, 0);")
                self.SSpicture.show()
                self.SShuida.show()
                self.SSxiaable = 1
                self.SStishu += 1
                self.SSwrong += 1
                self.SSwanchengshu.setText(_translate("Homepage", "已完成 " + str(self.SStishu) + " 题"))
            self.SStimer0.stop()
            if self.SStishu == self.SStimushuliang:
                self.hide()
                self.SSRightvalue = (self.SSright / self.SStimushuliang) * 100
                self.SS_zongjie = Ui_SS_Finally()
                self.SS_zongjie.SSnandu_input.setText(_translate("SS_Finally", self.SSnandubiaozhu))
                self.SS_zongjie.SSzhengquelv_input.setText(_translate("SS_Finally", str(self.SSRightvalue) + "%"))
                self.SS_zongjie.show()
                if self.SSRightvalue == 100:
                    self.SS_zongjie.star1.show()
                    self.SS_zongjie.star1_2.show()
                    self.SS_zongjie.star1_3.show()
                    self.SS_zongjie.star1_4.show()
                    self.SS_zongjie.star1_5.show()
                    self.SS_zongjie.good.setText(_translate("SS_Finally", "完美通过,你真棒！"))
                elif self.SSRightvalue >= 90 and self.SSRightvalue < 100:
                    self.SS_zongjie.star1.show()
                    self.SS_zongjie.star1_2.show()
                    self.SS_zongjie.star1_3.show()
                    self.SS_zongjie.star1_4.show()
                    self.SS_zongjie.good.setText(_translate("SS_Finally", "差一点就满分了，继续加油哦！"))
                elif self.SSRightvalue >= 60 and self.SSRightvalue < 90:
                    self.SS_zongjie.star1.show()
                    self.SS_zongjie.star1_2.show()
                    self.SS_zongjie.star1_3.show()
                    self.SS_zongjie.good.setText(_translate("SS_Finally", "还有待加强哦！"))
                else:
                    self.SS_zongjie.star1.show()
                    self.SS_zongjie.star1_2.show()
                    self.SS_zongjie.good.setText(_translate("SS_Finally", "你的水平太糟糕了，要多加练习哦！"))
                self.SShuida.hide()
                self.SStishi.setStyleSheet("color: rgb(0, 0, 0);")
                self.SStishi.setText(_translate("Homepage", "请输入你的答案"))
                self.SSlineEdit.setEnabled(True)
                self.SSlineEdit.clear()
                self.SSlineEdit.setFocus()
                conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
                cursor = conn.cursor()
                cursor.execute('select*from 速算正确率数据')
                result = cursor.fetchall()
                cursor.execute('insert into 速算正确率数据(序号,正确率) values (?,?)',
                               (str(len(result) + 1), str(int(self.SSRightvalue))))
                cursor.close()
                conn.commit()
                conn.close()
                self.SS_zongjie.back.clicked.connect(self.SS_back)
                self.SS_zongjie.back.setShortcut(_translate("SS_Finally", "Return"))
                try:
                    self.TWQ1.close()
                except:
                    pass
        else:  # 已提交，并重复提交
            self.SS_MESSAGE = Ui_KSFX_Message('警告', '', '请不要反复提交！')
            self.SS_MESSAGE.show()

    def SS_back(self):
        self.SS_zongjie.hide()
        self.show()
        self.likai()

    def SS_Jian(self):
        _translate = QtCore.QCoreApplication.translate
        if self.SStime0 > 0:
            self.SStime0 -= 1
            string = str(round((self.SStime0 / self.SStimeA) * 100)) + '%'
            self.SStimeprogress.setProperty("value", self.SStime0)
            self.SSLCDshengyu.setProperty("value", self.SStime0)
            self.SStimeprogress.setFormat(_translate("Homepage", string))
        else:  # 超时未作答
            self.SS_Guantimer = QTimer(self)
            self.SS_Guanbianliang = 0
            if self.SStishu != self.SStimushuliang - 1:  # 不是最后一题,提交并且做下一题函数
                self.SStimer0.stop()
                self.TWQ1 = Ui_Shi_Bai()
                self.TWQ1.lable.setText(_translate("Shi_Bai", "超时未提交，系统自动为您进行跳转！"))
                self.TWQ1.show()
                self.SS_Guantimer.start(500)
                self.SS_Guantimer.timeout.connect(self.SS_Guan)
                self.SSTiJiao()
                self.SSnext()
            else:  # 最后一题并超时作答，提交但不做下一题函数
                self.SStimer0.stop()
                self.SSwrong += 1
                self.SSTiJiao()

    def SS_Guan(self):
        self.SS_Guanbianliang += 0.5
        if self.SS_Guanbianliang == 1:
            self.TWQ1.hide()
            self.SS_Guantimer.stop()

    def SSchange(self):
        _translate = QtCore.QCoreApplication.translate
        self.SSxiaable = 0
        self.SStishu = 0
        self.SSwanchengshu.setText(_translate("Homepage", "已完成 0 题"))
        self.SSright = 0
        self.SSwrong = 0
        self.SSkaishi.show()
        self.SSzhuye.show()
        self.SSkaishi.setGeometry(QtCore.QRect(410, 460, 75, 31))
        self.SSshengyushijian.show()
        self.SSLCDshengyu.show()
        self.SSS.show()
        self.SSwanchengshu.show()
        self.SSlable.show()
        self.SStimeprogress.show()
        self.SScomboBox.setGeometry(QtCore.QRect(380, 120, 131, 22))
        try:
            if self.SScomboBox.currentText() == '简单':
                self.SStimeprogress.setMaximum(12)
                self.SStimeprogress.setProperty("value", 12)
                self.SSLCDshengyu.setProperty("value", 12)
                self.SStime0 = 12
                self.SSlable.setText(_translate("Homepage", "共 8 题"))
                self.SStimushuliang = 8
                self.SSnandubiaozhu = '简单'
            if self.SScomboBox.currentText() == '普通':
                self.SStimeprogress.setMaximum(9)
                self.SStimeprogress.setProperty("value", 9)
                self.SSLCDshengyu.setProperty("value", 9)
                self.SSlable.setText(_translate("Homepage", "共 12 题"))
                self.SStime0 = 9
                self.SStimushuliang = 12
                self.SSnandubiaozhu = '普通'
            if self.SScomboBox.currentText() == '困难':
                self.SStimeprogress.setMaximum(7)
                self.SStimeprogress.setProperty("value", 7)
                self.SSLCDshengyu.setProperty("value", 7)
                self.SSlable.setText(_translate("Homepage", "共 15 题"))
                self.SStime0 = 7
                self.SStimushuliang = 15
                self.SSnandubiaozhu = '困难'
            if self.SScomboBox.currentText() == '地狱':
                self.SStimeprogress.setMaximum(5)
                self.SStimeprogress.setProperty("value", 5)
                self.SSLCDshengyu.setProperty("value", 5)
                self.SSlable.setText(_translate("Homepage", "共 20 题"))
                self.SStimushuliang = 20
                self.SStime0 = 5
                self.SSnandubiaozhu = '地狱'
        except:
            pass

    def Background_Music(self):
        if self.music_marktime == 0:
            url = QUrl.fromLocalFile('C:/Users/Administrator/Desktop/六&七文件夹/副文件/主页bgm.mp3')
            content = QtMultimedia.QMediaContent(url)
            self.musicplayer = QtMultimedia.QMediaPlayer()
            self.musicplayer.setMedia(content)
            self.music_marktime += 0.1
            time.sleep(0.05)
            self.musicplayer.play()
        elif self.music_marktime >= 66:
            self.music_marktime = 0
        else:
            self.music_marktime += 0.1

    def Z_B(self):
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabsClosable(True)
        list0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        list1 = []
        index = self.tabWidget.currentIndex()
        text = self.tabWidget.tabText(index)
        for i in list0:
            if i <= self.frequency:
                list1.append(i)
        if list1 != '' and index != 0:
            list1.remove(index)
        for p in list1:
            self.yincang.setTabButton(p, self.yincang.RightSide, None)
        if text != '首页':
            try:
                self.music_timer.stop()
                self.musicplayer.pause()
            except:
                pass
        if text == '首页':
            if self.bj_music != None:
                if self.bj_music == True:
                    self.music_marktime = 0
                    self.music_timer = QTimer(self)
                    self.music_timer.timeout.connect(self.Background_Music)
                    self.music_timer.start(100)
            else:
                pass
            self.setStyleSheet("#Homepage{border-image: url(:/背景/图片文件夹/壁纸 010.jpg);;}}")
            self.gaokao.show()
            self.LCD_dayremaining.show()
            self.tian.show()
            self.matt_change()
            try:
                self.ywmx_xunwen_timer.stop()
            except:
                pass
            try:
                self.ebdc_message_timer.stop()
            except:
                pass
            try:
                self.MESSAGE_timer.stop()
            except:
                pass
        else:
            self.gaokao.hide()
            self.LCD_dayremaining.hide()
            self.tian.hide()
        if text == '单元总结':
            self.setStyleSheet("#Homepage{border-image: url(:/背景/图片文件夹/011.jpg);}")
        elif text == '背单词':
            self.setStyleSheet("#Homepage{border-image: url(:/背景/图片文件夹/003.jpg);}")
        elif text == '速算':
            self.setStyleSheet("#Homepage{border-image: url(:/背景/图片文件夹/002.jpeg);}")
        elif text == '诗词理解性默写':
            self.setStyleSheet("#Homepage{border-image: url(:/背景/图片文件夹/001.jpeg);}")
        elif text == '课本知识点':
            self.setStyleSheet("#Homepage{border-image: url(:/背景/图片文件夹/生物背景.jpeg);}")
        elif text == '基础知识':
            self.setStyleSheet("#Homepage{border-image: url(:/背景/图片文件夹/化学背景.jpeg);}")
        else:
            pass

    def Zuozhejieshao(self):
        message = '本软件作者由马特独立原创制作，自2月18日开始项目制作，目前仍在更新中！'
        self.MESSAGE = Ui_KSFX_Message('通知', '公告', message)
        self.MESSAGE.show()

    def Actionuse_Prior(self):
        message = '1.部分使用说明在项目内部，此处只解释部分使用须知\n'
        message1 = '2.请您在使用前优先注册账号，以便开启更多功能。（账号位于管理者模式注册）\n'
        message2 = '3.为保证私密性,本产品规定一台电脑只允许一个账户登录。\n'
        message3 = '4.如您在使用过程中遇到困难或BUG请联系作者!\n'
        self.MESSAGE = Ui_KSFX_Message('多行通知', '使用须知', message+message1+message2+message3)
        self.MESSAGE.show()

    def Shijian(self):
        self.hour1 = int(time.strftime("%H"))
        self.minute1 = int(time.strftime("%M"))
        message = '当前在线时间：' + '\n' + str(self.hour1 - self.hour0) + '小时' + '\n' + str(
            self.minute1 - self.minute0) + '分钟'
        self.MESSAGE = Ui_KSFX_Message('通知', '在线时长',message)
        self.MESSAGE.show()

    def EBDC_MESSAGE_timerevent(self):
        self.EBDC_MESSAGE.Result()
        _translate = QtCore.QCoreApplication.translate
        if self.EBDC_MESSAGE.answer == 1:  # 点击确认
            self.ebdc_message_timer.stop()
            self.EBDC_MESSAGE.close()
            Eright = 0
            Ewrong = 0
            frequency0 = 0
            frequency1 = 0
            string = ''
            self.EBWronglist = []
            self.EBRightlist = []
            for i in self.YourYingyuAnswer:
                if i == self.answer[frequency0]:
                    Eright += 1
                    frequency0 += 1
                else:
                    Ewrong += 1
                    self.EBRightlist.append(self.answer[frequency0])
                    self.EBWronglist.append(self.question[frequency0])
                    frequency0 += 1
            self.EAccuracyrate = round(Eright / len(self.YourYingyuAnswer), 2) * 100  # 计算正确率
            if self.EBWronglist == []:
                string = '恭喜你，全部正确，没有错题！'
            else:
                for i in range(Ewrong):
                    string += self.EBWronglist[frequency1] + '  ---  ' + self.EBRightlist[frequency1] + '\n'
                    frequency1 += 1
            self.TWQ = Ui_Beidanci_Finally(string)
            self.TWQ.zhengquelv_input.setText(_translate("Beidanci_Finally",
                                                         str(int(self.EAccuracyrate)) + '(正确：' + str(
                                                             Eright) + ' 错误：' + str(Ewrong) + ')'))
            self.TWQ.cuowu_input.setText(_translate("Beidanci_Finally", string))
            self.TWQ.show()
            self.BDCtimer.stop()
            self.hide()
            if self.EAccuracyrate == 100:
                self.TWQ.good.setText(_translate("Beidanci_Finally", "满分！你真是太棒啦！"))
                self.TWQ.star1.show()
                self.TWQ.star1_2.show()
                self.TWQ.star1_3.show()
                self.TWQ.star1_4.show()
                self.TWQ.star1_5.show()
                self.TWQ.back.show()
            elif 100 > self.EAccuracyrate >= 90:
                self.TWQ.good.setText(_translate("Beidanci_Finally", "完成得不错，继续加油哦"))
                self.TWQ.star1.show()
                self.TWQ.star1_2.show()
                self.TWQ.star1_3.show()
                self.TWQ.star1_4.show()
                self.TWQ.back.show()
            elif 90 > self.EAccuracyrate >= 60:
                self.TWQ.good.setText(_translate("Beidanci_Finally", "革命还未胜利，同志还需努力！"))
                self.TWQ.star1.show()
                self.TWQ.star1_2.show()
                self.TWQ.star1_3.show()
                self.TWQ.back.show()
            else:
                self.TWQ.good.setText(_translate("Beidanci_Finally", "完成得太糟糕了，再试一次吧！"))
                self.TWQ.star1.show()
                self.TWQ.star1_2.show()
                self.TWQ.back.show()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select*from 背单词正确率数据')
            result = cursor.fetchall()
            cursor.execute('insert into 背单词正确率数据(序号,正确率) values (?,?)',
                           (str(len(result) + 1), str(int(self.EAccuracyrate))))
            cursor.close()
            conn.commit()
            conn.close()
            self.TWQ.back.clicked.connect(self.Finally)
        elif self.EBDC_MESSAGE.answer == 0:
            self.ebdc_message_timer.stop()
            self.EBDC_MESSAGE.close()
        else:
            pass

    def Ehand(self):
        _translate = QtCore.QCoreApplication.translate
        if self.EBcomboBox.currentIndex() != 0:
            if self.Epage == self.xiayiyeshuliang:  # 在尾页提交答案
                try:
                    self.YourYingyuAnswer[(self.Epage - 1) * 6] = self.yingyuyihang.text()
                except:
                    pass
                try:
                    self.YourYingyuAnswer[(self.Epage - 1) * 6 + 1] = self.yingyuerhang.text()
                except:
                    pass
                try:
                    self.YourYingyuAnswer[(self.Epage - 1) * 6 + 2] = self.yingyusanhang.text()
                except:
                    pass
                try:
                    self.YourYingyuAnswer[(self.Epage - 1) * 6 + 3] = self.yingyusihang.text()
                except:
                    pass
                try:
                    self.YourYingyuAnswer[(self.Epage - 1) * 6 + 4] = self.yingyuwuhang.text()
                except:
                    pass
                try:
                    self.YourYingyuAnswer[(self.Epage - 1) * 6 + 5] = self.yingyuliuhang.text()
                except:
                    pass
            else:  # 在非尾页提交答案:
                self.YourYingyuAnswer[(self.Epage - 1) * 6] = self.yingyuyihang.text()
                self.YourYingyuAnswer[(self.Epage - 1) * 6 + 1] = self.yingyuerhang.text()
                self.YourYingyuAnswer[(self.Epage - 1) * 6 + 2] = self.yingyusanhang.text()
                self.YourYingyuAnswer[(self.Epage - 1) * 6 + 3] = self.yingyusihang.text()
                self.YourYingyuAnswer[(self.Epage - 1) * 6 + 4] = self.yingyuwuhang.text()
                self.YourYingyuAnswer[(self.Epage - 1) * 6 + 5] = self.yingyuliuhang.text()
            if '' not in self.YourYingyuAnswer:
                self.EBDC_MESSAGE = Ui_KSFX_Message('询问', '', '是否确认提交？')
                self.EBDC_MESSAGE.show()
                self.ebdc_message_timer = QTimer(self)
                self.ebdc_message_timer.start(100)
                self.ebdc_message_timer.timeout.connect(self.EBDC_MESSAGE_timerevent)
            else:
                self.EBDC_MESSAGE = Ui_KSFX_Message('询问', '', '您尚有未完成的题目，是否确认提交？')
                self.EBDC_MESSAGE.show()
                self.ebdc_message_timer = QTimer(self)
                self.ebdc_message_timer.start(100)
                self.ebdc_message_timer.timeout.connect(self.EBDC_MESSAGE_timerevent)
        else:
            self.MESSAGE = Ui_KSFX_Message('警告', '未选择单元', '请先选择默写单元再进行操作！')
            self.MESSAGE.show()

    def Finally(self):
        self.show()
        self.likai()

    def Eback(self):
        _translate = QtCore.QCoreApplication.translate
        self.Epage -= 1
        self.xiayiye.show()
        self.shangyiye.setGeometry(QtCore.QRect(220, 437, 75, 24))
        self.yingyuyihang.setFocus()
        if self.Epage == 1:
            self.shangyiye.hide()
        self.yingyuerhang.setEnabled(True)
        self.yingyusanhang.setEnabled(True)
        self.yingyusihang.setEnabled(True)
        self.yingyuwuhang.setEnabled(True)
        self.yingyuliuhang.setEnabled(True)
        self.YourYingyuAnswer[self.Epage * 6] = self.yingyuyihang.text()
        if self.yingyuerhang.text() != '暂无数据':
            self.YourYingyuAnswer[self.Epage * 6 + 1] = self.yingyuerhang.text()
        if self.yingyusanhang.text() != '暂无数据':
            self.YourYingyuAnswer[self.Epage * 6 + 2] = self.yingyusanhang.text()
        if self.yingyusihang.text() != '暂无数据':
            self.YourYingyuAnswer[self.Epage * 6 + 3] = self.yingyusihang.text()
        if self.yingyuwuhang.text() != '暂无数据':
            self.YourYingyuAnswer[self.Epage * 6 + 4] = self.yingyuwuhang.text()
        if self.yingyuliuhang.text() != '暂无数据':
            self.YourYingyuAnswer[self.Epage * 6 + 5] = self.yingyuliuhang.text()
        self.yihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6]))
        self.erhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 1]))
        self.sanhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 2]))
        self.sihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 3]))
        self.wuhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 4]))
        self.liuhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 5]))
        self.yingyuyihang.setText(_translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6]))
        self.yingyuerhang.setText(
            _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 1]))
        self.yingyusanhang.setText(
            _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 2]))
        self.yingyusihang.setText(
            _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 3]))
        self.yingyuwuhang.setText(
            _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 4]))
        self.yingyuliuhang.setText(
            _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 5]))

    def Enext(self):
        _translate = QtCore.QCoreApplication.translate
        if self.EBcomboBox.currentIndex() != 0:
            self.Epage = 1 + self.Epage
            self.yingyuyihang.setFocus()
            if self.Epage >= self.xiayiyeshuliang:
                self.xiayiye.hide()
                self.shangyiye.setGeometry(QtCore.QRect(220, 437, 75, 24))
            if self.Epage != 1:
                self.shangyiye.show()
            if self.Ebiao == True and self.Epage < self.xiayiyeshuliang or self.Ebiao == False and self.Epage <= self.xiayiyeshuliang:  # 够下一页的所有内容
                self.yihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6]))
                self.erhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 1]))
                self.sanhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 2]))
                self.sihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 3]))
                self.wuhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 4]))
                self.liuhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 5]))
                self.YourYingyuAnswer[(self.Epage - 2) * 6] = self.yingyuyihang.text()
                self.YourYingyuAnswer[(self.Epage - 2) * 6 + 1] = self.yingyuerhang.text()
                self.YourYingyuAnswer[(self.Epage - 2) * 6 + 2] = self.yingyusanhang.text()
                self.YourYingyuAnswer[(self.Epage - 2) * 6 + 3] = self.yingyusihang.text()
                self.YourYingyuAnswer[(self.Epage - 2) * 6 + 4] = self.yingyuwuhang.text()
                self.YourYingyuAnswer[(self.Epage - 2) * 6 + 5] = self.yingyuliuhang.text()
                self.yingyuyihang.setText(_translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6]))
                self.yingyuerhang.setText(
                    _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 1]))
                self.yingyusanhang.setText(
                    _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 2]))
                self.yingyusihang.setText(
                    _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 3]))
                self.yingyuwuhang.setText(
                    _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 4]))
                self.yingyuliuhang.setText(
                    _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 5]))
            else:  # 下一页内容不完全了
                self.YourYingyuAnswer[(self.Epage - 2) * 6] = self.yingyuyihang.text()
                self.YourYingyuAnswer[(self.Epage - 2) * 6 + 1] = self.yingyuerhang.text()
                self.YourYingyuAnswer[(self.Epage - 2) * 6 + 2] = self.yingyusanhang.text()
                self.YourYingyuAnswer[(self.Epage - 2) * 6 + 3] = self.yingyusihang.text()
                self.YourYingyuAnswer[(self.Epage - 2) * 6 + 4] = self.yingyuwuhang.text()
                self.YourYingyuAnswer[(self.Epage - 2) * 6 + 5] = self.yingyuliuhang.text()
                self.yingyuyihang.setText(_translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6]))
                self.yihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6]))
                try:
                    self.erhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 1]))
                    self.guo2 = 0
                except:
                    self.erhangdanci.setText((_translate("Homepage", '暂无数据')))
                    self.yingyuerhang.setText(_translate("Homepage", '暂无数据'))
                    self.guo2 = 1
                try:
                    self.sanhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 2]))
                    self.guo3 = 0
                except:
                    self.sanhangdanci.setText((_translate("Homepage", '暂无数据')))
                    self.yingyusanhang.setText(_translate("Homepage", '暂无数据'))
                    self.guo3 = 1
                try:
                    self.sihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 3]))
                    self.guo4 = 0
                except:
                    self.sihangdanci.setText((_translate("Homepage", '暂无数据')))
                    self.yingyusihang.setText(_translate("Homepage", '暂无数据'))
                    self.guo4 = 1
                try:
                    self.wuhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 4]))
                    self.guo5 = 0
                except:
                    self.wuhangdanci.setText((_translate("Homepage", '暂无数据')))
                    self.yingyuwuhang.setText(_translate("Homepage", '暂无数据'))
                    self.guo5 = 1
                try:
                    self.liuhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 5]))
                    self.guo6 = 0
                except:
                    self.liuhangdanci.setText((_translate("Homepage", '暂无数据')))
                    self.yingyuliuhang.setText(_translate("Homepage", '暂无数据'))
                    self.guo6 = 1
                if self.guo2 == 1:
                    self.yingyuerhang.setEnabled(False)
                else:
                    self.yingyuerhang.setText(
                        _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 1]))
                if self.guo3 == 1:
                    self.yingyusanhang.setEnabled(False)
                else:
                    self.yingyusanhang.setText(
                        _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 2]))
                if self.guo4 == 1:
                    self.yingyusihang.setEnabled(False)
                else:
                    self.yingyusihang.setText(
                        _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 3]))
                if self.guo5 == 1:
                    self.yingyuwuhang.setEnabled(False)
                else:
                    self.yingyuwuhang.setText(
                        _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 4]))
                if self.guo6 == 1:
                    self.yingyuliuhang.setEnabled(False)
                else:
                    self.yingyuliuhang.setText(
                        _translate("Homepage", self.YourYingyuAnswer[(self.Epage - 1) * 6 + 5]))
        else:
            self.MESSAGE = Ui_KSFX_Message('警告', '未选择单元', '请先选择默写单元！')
            self.MESSAGE.show()

    def Echange(self):
        _translate = QtCore.QCoreApplication.translate
        if self.Echange_Mark == 0:
            self.EBdangqian_zuoda.setGeometry(QtCore.QRect(160, 10, 320, 16))
            _translate = QtCore.QCoreApplication.translate
            self.EBdangqian_danyuan = self.EBcomboBox.currentText()
            self.xuanzedanyuan.hide()
            self.EBcomboBox.hide()
            self.Epage = 1
            self.xiayiyeshuliang = 0
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 背单词 where 书名和单元 = ? ', (self.EBcomboBox.currentText(),))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            self.question = []
            self.answer = []
            for bdc in result:
                self.question.append(bdc[1])
                self.answer.append(bdc[2])
            many = len(self.question)
            if self.EBdangqian_danyuan != '请选择单元':
                self.EBdangqian_zuoda.setText(_translate("Homepage",
                                                         self.EBdangqian_danyuan + "       当前作答情况： " + "0/" + str(
                                                             many)))
            else:
                pass
            self.BDCtimer = QTimer(self)
            self.BDCtimer.start(1000)
            self.BDCtimer.timeout.connect(self.BDC_zuoda)
            if many % 6 != 0:
                self.xiayiyeshuliang = int(many / 6) + 1
                self.Ebiao = True
            else:
                self.xiayiyeshuliang = many / 6
                self.Ebiao = False
            self.YourYingyuAnswer = []
            for EZ in range(many):
                self.YourYingyuAnswer.append('')
            self.yingyuyihang.clear()
            self.yingyuerhang.clear()
            self.yingyusanhang.clear()
            self.yingyusihang.clear()
            self.yingyuwuhang.clear()
            self.yingyuliuhang.clear()
            if many == 1:
                self.yihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6]))
                self.yingyuyihang.setEnabled(True)
                self.erhangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyuerhang.setText(_translate("Homepage", '暂无数据'))
                self.sanhangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyusanhang.setText(_translate("Homepage", '暂无数据'))
                self.sihangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyusihang.setText(_translate("Homepage", '暂无数据'))
                self.wuhangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyuwuhang.setText(_translate("Homepage", '暂无数据'))
                self.liuhangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyuliuhang.setText(_translate("Homepage", '暂无数据'))
                self.yingyuerhang.setEnabled(False)
                self.yingyusanhang.setEnabled(False)
                self.yingyusihang.setEnabled(False)
                self.yingyuwuhang.setEnabled(False)
                self.yingyuliuhang.setEnabled(False)
                self.xiayiye.show()
                self.shangyiye.show()
                self.xiayiye.setEnabled(False)
                self.shangyiye.setEnabled(False)
                self.EBtijiao.show()
            elif many == 2:
                self.yihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6]))
                self.erhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 1]))
                self.yingyuyihang.setEnabled(True)
                self.yingyuerhang.setEnabled(True)
                self.sanhangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyusanhang.setText(_translate("Homepage", '暂无数据'))
                self.sihangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyusihang.setText(_translate("Homepage", '暂无数据'))
                self.wuhangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyuwuhang.setText(_translate("Homepage", '暂无数据'))
                self.liuhangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyuliuhang.setText(_translate("Homepage", '暂无数据'))
                self.yingyusanhang.setEnabled(False)
                self.yingyusihang.setEnabled(False)
                self.yingyuwuhang.setEnabled(False)
                self.yingyuliuhang.setEnabled(False)
                self.xiayiye.show()
                self.shangyiye.show()
                self.xiayiye.setEnabled(False)
                self.shangyiye.setEnabled(False)
                self.EBtijiao.show()
            elif many == 3:
                self.yihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6]))
                self.erhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 1]))
                self.sanhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 2]))
                self.sihangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyusihang.setText(_translate("Homepage", '暂无数据'))
                self.wuhangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyuwuhang.setText(_translate("Homepage", '暂无数据'))
                self.liuhangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyuliuhang.setText(_translate("Homepage", '暂无数据'))
                self.yingyuyihang.setEnabled(True)
                self.yingyuerhang.setEnabled(True)
                self.yingyusanhang.setEnabled(True)
                self.yingyusihang.setEnabled(False)
                self.yingyuwuhang.setEnabled(False)
                self.yingyuliuhang.setEnabled(False)
                self.xiayiye.show()
                self.shangyiye.show()
                self.xiayiye.setEnabled(False)
                self.shangyiye.setEnabled(False)
                self.EBtijiao.show()
            elif many == 4:
                self.yihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6]))
                self.erhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 1]))
                self.sanhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 2]))
                self.sihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 3]))
                self.wuhangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyuwuhang.setText(_translate("Homepage", '暂无数据'))
                self.liuhangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyuliuhang.setText(_translate("Homepage", '暂无数据'))
                self.yingyuyihang.setEnabled(True)
                self.yingyuerhang.setEnabled(True)
                self.yingyusanhang.setEnabled(True)
                self.yingyusihang.setEnabled(True)
                self.yingyuwuhang.setEnabled(False)
                self.yingyuliuhang.setEnabled(False)
                self.xiayiye.show()
                self.shangyiye.show()
                self.xiayiye.setEnabled(False)
                self.shangyiye.setEnabled(False)
                self.EBtijiao.show()
            elif many == 5:
                self.yihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6]))
                self.erhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 1]))
                self.sanhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 2]))
                self.sihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 3]))
                self.wuhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 4]))
                self.liuhangdanci.setText((_translate("Homepage", '暂无数据')))
                self.yingyuliuhang.setText(_translate("Homepage", '暂无数据'))
                self.yingyuyihang.setEnabled(True)
                self.yingyuerhang.setEnabled(True)
                self.yingyusanhang.setEnabled(True)
                self.yingyusihang.setEnabled(True)
                self.yingyuwuhang.setEnabled(True)
                self.yingyuwuhang.setEnabled(False)
                self.yingyuliuhang.setEnabled(False)
                self.xiayiye.show()
                self.shangyiye.show()
                self.xiayiye.setEnabled(False)
                self.shangyiye.setEnabled(False)
                self.EBtijiao.show()
            else:
                self.yihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6]))
                self.erhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 1]))
                self.sanhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 2]))
                self.sihangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 3]))
                self.wuhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 4]))
                self.liuhangdanci.setText(_translate("Homepage", self.question[(self.Epage - 1) * 6 + 5]))
                self.yingyuyihang.setEnabled(True)
                self.yingyuerhang.setEnabled(True)
                self.yingyusanhang.setEnabled(True)
                self.yingyusihang.setEnabled(True)
                self.yingyuwuhang.setEnabled(True)
                self.yingyuliuhang.setEnabled(True)
                self.shangyiye.hide()
                self.shangyiye.setEnabled(True)
                self.xiayiye.setEnabled(True)
            self.xiayiye.show()
            self.yingyuyihang.setFocus()

        else:  # 执行清理任务
            self.Echange_Mark -= 1
            self.shangyiye.hide()
            self.xiayiye.show()
            self.xuanzedanyuan.show()
            self.EBcomboBox.show()
            self.EBdangqian_zuoda.setGeometry(QtCore.QRect(340, 10, 320, 16))

    def BDC_zuoda(self):
        _translate = QtCore.QCoreApplication.translate
        self.BDC_weizuoda = 0
        for i in self.YourYingyuAnswer:
            if i == '':
                self.BDC_weizuoda += 1
        self.EBdangqian_zuoda.setText(_translate("Homepage", self.EBdangqian_danyuan + "       当前作答情况： " + str(
            len(self.question) - self.BDC_weizuoda) + "/" + str(len(self.question))))

    def ENGLISH(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.English.currentItem()
        if item.text(0) == '背单词':
            self.Edanyuanxuanzelist = ['请选择单元']
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select*from 背单词')
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            for i in result:
                if i[0] not in self.Edanyuanxuanzelist:
                    self.Edanyuanxuanzelist.append(i[0])
            if self.EBcomboBox.count() == 0:
                self.Echange_Mark = 1
                self.EBcomboBox.addItems(self.Edanyuanxuanzelist)
            self.icon13 = QtGui.QIcon()
            self.icon13.addPixmap(QtGui.QPixmap(":/子标/图片文件夹/背单词.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tabWidget.addTab(self.beidanci, self.icon13, "背单词")
            self.yingyuyihang.setEnabled(False)
            self.yingyuerhang.setEnabled(False)
            self.yingyusanhang.setEnabled(False)
            self.yingyusihang.setEnabled(False)
            self.yingyuwuhang.setEnabled(False)
            self.yingyuliuhang.setEnabled(False)
            self.EBdangqian_zuoda.setText(_translate("self", "当前作答情况： "))
            self.tabWidget.setCurrentIndex(self.frequency)
            reg = QRegExp('[a-zA-Z0- ]+$')  # 字母加空格的正则表达式
            validator = QRegExpValidator()
            validator.setRegExp(reg)
            self.yingyuyihang.setValidator(validator)  # 设置校验器
            self.yingyuerhang.setValidator(validator)
            self.yingyusanhang.setValidator(validator)
            self.yingyusihang.setValidator(validator)
            self.yingyuwuhang.setValidator(validator)
            self.yingyuliuhang.setValidator(validator)

        if item.text(0) == '语法':
            self.frequency -= 1
        if item.text(0) == '满分作文':
            self.frequency -= 1
        self.frequency += 1

    def CHINESE(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.Chinese.currentItem()
        if item.text(0) == '诗词理解性默写':
            if self.YW_mxcomboBox.count() == 0:
                self.YW_mxxuanzelist = ['请选择古诗文']
                conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
                cursor = conn.cursor()
                cursor.execute('select*from 语文默写古诗文')
                result = cursor.fetchall()
                cursor.close()
                conn.close()
                for i in result:
                    if i[0] not in self.YW_mxxuanzelist:
                        self.YW_mxxuanzelist.append(i[0])
                self.YWMXchange_Mark = 1
                self.YW_mxcomboBox.addItems(self.YW_mxxuanzelist)
            self.icon15 = QtGui.QIcon()
            self.icon15.addPixmap(QtGui.QPixmap(":/子标/图片文件夹/理解性默写.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tabWidget.addTab(self.shicimoxie, self.icon15, "诗词理解性默写")
            self.tabWidget.setCurrentIndex(self.frequency)
            self.YW_mxtijiao_lable.hide()
            self.YW_mx_input1.setEnabled(False)
            self.YW_mx_input2.setEnabled(False)
            self.YW_mx_input3.setEnabled(False)
            self.YW_mx_input4.setEnabled(False)
            self.YW_mxshangyiye_lable.setEnabled(False)
            self.YW_mxxiayiye_lable.setEnabled(False)
            self.YW_mxlable.setText(_translate("Homepage", "请选择默写诗词"))
            self.YW_mxcomboBox.show()
        if item.text(0) == '答题模板':
            self.frequency -= 1
        if item.text(0) == '满分作文':
            self.frequency -= 1
        self.frequency += 1

    def MATH(self):
        item = self.Math.currentItem()
        if item.text(0) == '速算':
            self.icon2 = QtGui.QIcon()
            self.icon2.addPixmap(QtGui.QPixmap(":/子标/图片文件夹/速算.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tabWidget.addTab(self.susuan, self.icon2, "速算")
            self.tabWidget.setCurrentIndex(self.frequency)
            self.SSkaishi.hide()
            self.SSlable_cheng.hide()
            self.SStimeprogress.hide()
            self.SSlable.hide()
            self.SSpicture.hide()
            self.SSS.hide()
            self.SStimeprogress.hide()
            self.SShuida.hide()
            self.lcdNumber1.hide()
            self.lcdNumber2.hide()
            self.SSLCDshengyu.hide()
            self.SSlineEdit.hide()
            self.SSwanchengshu.hide()
            self.SSshengyushijian.hide()
            self.SStishi.hide()
            self.SStijiao.hide()
            self.SSzhuye.hide()
            self.SSxiayiti.hide()
            self.SScomboBox.show()
            self.SScomboBox.setGeometry(QtCore.QRect(380, 30, 131, 22))
        if item.text(0) == '错题案例':
            self.frequency -= 1
        if item.text(0) == '二级结论':
            self.frequency -= 1
        self.frequency += 1

    def PHYSICS(self):
        item = self.Physics.currentItem()
        if item.text(0) == '单元总结':
            self.Physics_Wait = 0
            self.random_number = random.uniform(0, 1.5)
            self.Wait_Picture = Ui_Wait_jiemian()
            self.Wait_Picture.show()
            self.hide()
            self.Physics_WaitTimer = QTimer(self)
            self.Physics_WaitTimer.start(100)
            self.Physics_WaitTimer.timeout.connect(self.Physics_WaitTimer_Event)
            self.icon9 = QtGui.QIcon()
            self.icon9.addPixmap(QtGui.QPixmap(":/子标/图片文件夹/单元总结.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tabWidget.addTab(self.danyuanzongjie, self.icon9, "单元总结")
            if self.WL_danyuanzongjie_findtime == 0:
                conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
                cursor = conn.cursor()
                cursor.execute('select * from 物理单元总结知识点')
                result = cursor.fetchall()
                cursor.execute('select * from 物理单元总结例题')
                result1 = cursor.fetchall()
                cursor.close()
                conn.close()
                if result != []:
                    for i in result:
                        if i[0] == '必修一':
                            self.WL_danyuanzongjie_RB1.append(i[1])
                        elif i[0] == '必修二':
                            self.WL_danyuanzongjie_RB2.append(i[1])
                        elif i[0] == '必修三':
                            self.WL_danyuanzongjie_RB3.append(i[1])
                        elif i[0] == '选择性必修一':
                            self.WL_danyuanzongjie_RB4.append(i[1])
                        elif i[0] == '选择性必修二':
                            self.WL_danyuanzongjie_RB5.append(i[1])
                        elif i[0] == '选择性必修三':
                            self.WL_danyuanzongjie_RB6.append(i[1])
                        else:
                            pass
                if result1 != []:
                    for i in result1:
                        if i[0] == '必修一' and i[1] not in self.WL_danyuanzongjie_LB1:
                            self.WL_danyuanzongjie_LB1.append(i[1])
                        elif i[0] == '必修二' and i[1] not in self.WL_danyuanzongjie_LB2:
                            self.WL_danyuanzongjie_LB2.append(i[1])
                        elif i[0] == '必修三' and i[1] not in self.WL_danyuanzongjie_LB3:
                            self.WL_danyuanzongjie_LB3.append(i[1])
                        elif i[0] == '选择性必修一' and i[1] not in self.WL_danyuanzongjie_LB4:
                            self.WL_danyuanzongjie_LB4.append(i[1])
                        elif i[0] == '选择性必修二' and i[1] not in self.WL_danyuanzongjie_LB5:
                            self.WL_danyuanzongjie_LB5.append(i[1])
                        elif i[0] == '选择性必修三' and i[1] not in self.WL_danyuanzongjie_LB6:
                            self.WL_danyuanzongjie_LB6.append(i[1])
                        else:
                            pass
                if self.WL_danyuanzongjie_RB1 != []:
                    for i in self.WL_danyuanzongjie_RB1:
                        self.WL_danyuanzongjie_bixiu1_listWidget0.addItem(i)
                else:
                    self.WL_danyuanzongjie_bixiu1_listWidget0.addItem('暂无数据')
                if self.WL_danyuanzongjie_RB2 != []:
                    for i in self.WL_danyuanzongjie_RB2:
                        self.WL_danyuanzongjie_bixiu2_listWidget0.addItem(i)
                else:
                    self.WL_danyuanzongjie_bixiu2_listWidget0.addItem('暂无数据')
                if self.WL_danyuanzongjie_RB3 != []:
                    for i in self.WL_danyuanzongjie_RB2:
                        self.WL_danyuanzongjie_bixiu3_listWidget0.addItem(i)
                else:
                    self.WL_danyuanzongjie_bixiu3_listWidget0.addItem('暂无数据')
                if self.WL_danyuanzongjie_RB4 != []:
                    for i in self.WL_danyuanzongjie_RB3:
                        self.WL_danyuanzongjie_xbixiu1_listWidget0.addItem(i)
                else:
                    self.WL_danyuanzongjie_xbixiu1_listWidget0.addItem('暂无数据')
                if self.WL_danyuanzongjie_RB5 != []:
                    for i in self.WL_danyuanzongjie_RB4:
                        self.WL_danyuanzongjie_xbixiu2_listWidget0.addItem(i)
                else:
                    self.WL_danyuanzongjie_xbixiu2_listWidget0.addItem('暂无数据')
                if self.WL_danyuanzongjie_RB6 != []:
                    for i in self.WL_danyuanzongjie_RB5:
                        self.WL_danyuanzongjie_xbixiu3_listWidget0.addItem(i)
                else:
                    self.WL_danyuanzongjie_xbixiu3_listWidget0.addItem('暂无数据')
                if self.WL_danyuanzongjie_LB1 != []:
                    for i in self.WL_danyuanzongjie_LB1:
                        self.WL_danyuanzongjie_bixiu1_listWidget1.addItem(i)
                else:
                    self.WL_danyuanzongjie_bixiu1_listWidget1.addItem('暂无数据')
                if self.WL_danyuanzongjie_LB2 != []:
                    for i in self.WL_danyuanzongjie_LB2:
                        self.WL_danyuanzongjie_bixiu2_listWidget1.addItem(i)
                else:
                    self.WL_danyuanzongjie_bixiu2_listWidget1.addItem('暂无数据')
                if self.WL_danyuanzongjie_LB3 != []:
                    for i in self.WL_danyuanzongjie_LB3:
                        self.WL_danyuanzongjie_bixiu3_listWidget1.addItem(i)
                else:
                    self.WL_danyuanzongjie_bixiu3_listWidget1.addItem('暂无数据')
                if self.WL_danyuanzongjie_LB4 != []:
                    for i in self.WL_danyuanzongjie_LB4:
                        self.WL_danyuanzongjie_xbixiu1_listWidget1.addItem(i)
                else:
                    self.WL_danyuanzongjie_xbixiu1_listWidget1.addItem('暂无数据')
                if self.WL_danyuanzongjie_LB5 != []:
                    for i in self.WL_danyuanzongjie_LB5:
                        self.WL_danyuanzongjie_xbixiu2_listWidget1.addItem(i)
                else:
                    self.WL_danyuanzongjie_xbixiu2_listWidget1.addItem('暂无数据')
                if self.WL_danyuanzongjie_LB6 != []:
                    for i in self.WL_danyuanzongjie_LB6:
                        self.WL_danyuanzongjie_xbixiu3_listWidget1.addItem(i)
                else:
                    self.WL_danyuanzongjie_xbixiu3_listWidget1.addItem('暂无数据')
                self.WL_danyuanzongjie_findtime = 1
            self.tabWidget.setCurrentIndex(self.frequency)
        if item.text(0) == '公式':
            self.frequency -= 1
        if item.text(0) == '错题案例':
            self.frequency -= 1
        self.frequency += 1

    def CHEMISTRY(self):
        item = self.Chemistry.currentItem()
        if item.text(0) == '基础知识':
            self.icon6 = QtGui.QIcon()
            self.icon6.addPixmap(QtGui.QPixmap(":/子标/图片文件夹/基础知识.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tabWidget.addTab(self.jichuzhishi, self.icon6, "基础知识")
            self.tabWidget.setCurrentIndex(self.frequency)
        if item.text(0) == '化学方程式':
            self.frequency -= 1
        if item.text(0) == '经典错题':
            self.frequency -= 1
        self.frequency += 1

    def BIOLOGY(self):
        item = self.Biology.currentItem()
        if item.text(0) == '课本知识点':
            self.icon12 = QtGui.QIcon()
            self.icon12.addPixmap(QtGui.QPixmap(":/子标/图片文件夹/课本知识点.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.tabWidget.addTab(self.kebenguina, self.icon12, "课本知识点")
            self.tabWidget.setCurrentIndex(self.frequency)
        if item.text(0) == '经典错题':
            self.frequency -= 1
        if item.text(0) == '考题':
            self.frequency -= 1
        self.frequency += 1

    def likai(self):
        _translate = QtCore.QCoreApplication.translate
        if self.tabWidget.tabText(self.tabWidget.currentIndex()) == '背单词':
            self.Beidanci_clear()
        if self.tabWidget.tabText(self.tabWidget.currentIndex()) == '速算':
            self.SScomboBox.clear()
            icon30 = QtGui.QIcon()
            icon30.addPixmap(QtGui.QPixmap(":/png/图片文件夹/5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.SScomboBox.addItem(icon30, "")
            icon31 = QtGui.QIcon()
            icon31.addPixmap(QtGui.QPixmap(":/速算/图片文件夹/简单.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.SScomboBox.addItem(icon31, "")
            icon32 = QtGui.QIcon()
            icon32.addPixmap(QtGui.QPixmap(":/速算/图片文件夹/普通.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.SScomboBox.addItem(icon32, "")
            icon33 = QtGui.QIcon()
            icon33.addPixmap(QtGui.QPixmap(":/速算/图片文件夹/困难.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.SScomboBox.addItem(icon33, "")
            icon34 = QtGui.QIcon()
            icon34.addPixmap(QtGui.QPixmap(":/速算/图片文件夹/地狱.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.SScomboBox.addItem(icon34, "")
            self.SScomboBox.setItemText(0, _translate("Homepage", "请选择挑战难度"))
            self.SScomboBox.setItemText(1, _translate("Homepage", "简单"))
            self.SScomboBox.setItemText(2, _translate("Homepage", "普通"))
            self.SScomboBox.setItemText(3, _translate("Homepage", "困难"))
            self.SScomboBox.setItemText(4, _translate("Homepage", "地狱"))
            try:
                self.SS_Guantimer.stop()
            except:
                pass
            try:
                self.SStimer0.stop()
            except:
                pass
        if self.tabWidget.tabText(self.tabWidget.currentIndex()) == '诗词理解性默写':
            self.YWMXchange_Mark = 1
            self.YW_mxcomboBox.clear()
            self.YW_mx_input1.clear()
            self.YW_mx_input2.clear()
            self.YW_mx_input3.clear()
            self.YW_mx_input4.clear()
        if self.tabWidget.tabText(self.tabWidget.currentIndex()) == '单元总结':
            self.WL_danyuanzongjie_clear()
        self.tabWidget.removeTab(self.tabWidget.currentIndex())
        self.frequency -= 1

    def WL_danyuanzongjie_clear(self):
        self.WL_danyuanzongjie_lefttoolbox.setCurrentIndex(0)
        self.WL_danyuanzongjie_righttoolbox.setCurrentIndex(0)

    def Beidanci_clear(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            self.BDCtimer.stop()
        except:
            pass
        self.EBdangqian_zuoda.setGeometry(QtCore.QRect(340, 10, 320, 16))
        self.Echange_Mark = 1
        self.EBcomboBox.clear()
        self.Echange_Mark = 1
        self.EBcomboBox.addItems(self.Edanyuanxuanzelist)
        self.yihangdanci.setText(_translate("Homepage", "一行单词"))
        self.yingyuyihang.setText(_translate("Homepage", "一行单词"))
        self.erhangdanci.setText(_translate("Homepage", "二行单词"))
        self.yingyuerhang.setText(_translate("Homepage", "二行单词"))
        self.sanhangdanci.setText(_translate("Homepage", "三行单词"))
        self.yingyusanhang.setText(_translate("Homepage", "三行单词"))
        self.sihangdanci.setText(_translate("Homepage", "四行单词"))
        self.yingyusihang.setText(_translate("Homepage", "四行单词"))
        self.wuhangdanci.setText(_translate("Homepage", "五行单词"))
        self.yingyuwuhang.setText(_translate("Homepage", "五行单词"))
        self.liuhangdanci.setText(_translate("Homepage", "六行单词"))
        self.yingyuliuhang.setText(_translate("Homepage", "六行单词"))

    def ChineseData(self):
        X = []
        Y = []
        conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
        cursor = conn.cursor()
        cursor.execute('select *from 语文古诗词理解性默写正确率数据')
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        frequency = 1
        if len(result) >= 5:
            for i in result:
                X.append(frequency)
                Y.append(int(i[1]))
                frequency += 1
            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.rcParams['axes.unicode_minus'] = False
            plt.plot(X, Y, 'r-')
            plt.title('语文古诗词理解性默写')
            plt.xticks(X)  # 设置横坐标刻度
            plt.xlabel('近日场次')  # 设置横坐标轴标题
            plt.ylabel('正确率%')
            plt.show()  # 显示图形
        else:
            self.Chinese_data_Message = Ui_KSFX_Message('警告', '数据不足', '请前往训练并获得成绩后再来查看！')
            self.Chinese_data_Message.show()

    def MathData(self):
        X = []
        Y = []
        conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
        cursor = conn.cursor()
        cursor.execute('select *from 速算正确率数据')
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        frequency = 1
        if len(result) >= 5:
            for i in result:
                X.append(frequency)
                Y.append(int(i[1]))
                frequency += 1
            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.rcParams['axes.unicode_minus'] = False
            plt.plot(X, Y, 'r-')
            plt.title('速算')
            plt.xticks(X)  # 设置横坐标刻度
            plt.xlabel('近日场次')  # 设置横坐标轴标题
            plt.ylabel('正确率%')
            plt.show()  # 显示图形
        else:
            self.Math_data_Message = Ui_KSFX_Message('警告', '数据不足', '请前往训练并获得成绩后再来查看！')
            self.Math_data_Message.show()

    def EnglishData(self):
        X = []
        Y = []
        conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
        cursor = conn.cursor()
        cursor.execute('select *from 背单词正确率数据')
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        frequency = 1
        if len(result) >= 5:
            for i in result:
                X.append(frequency)
                Y.append(int(i[1]))
                frequency += 1
            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.rcParams['axes.unicode_minus'] = False
            plt.plot(X, Y, 'r-')
            plt.title('单词默写')
            plt.xticks(X)  # 设置横坐标刻度
            plt.xlabel('近日场次')  # 设置横坐标轴标题
            plt.ylabel('正确率%')
            plt.show()  # 显示图形
        else:
            self.English_data_Message = Ui_KSFX_Message('警告', '数据不足', '请前往训练并获得成绩后再来查看！')
            self.English_data_Message.show()

    def PhysicsData(self):
        self.Physics_data_Message = Ui_KSFX_Message('警告', '功能暂未开放', '功能暂未开放，感谢您的支持！')
        self.Physics_data_Message.show()

    def ChemistryData(self):
        self.Chemistry_data_Message = Ui_KSFX_Message('警告', '功能暂未开放', '功能暂未开放，感谢您的支持！')
        self.Chemistry_data_Message.show()

    def BiologyData(self):
        self.Biology_data_Message = Ui_KSFX_Message('警告', '功能暂未开放', '功能暂未开放，感谢您的支持！')
        self.Biology_data_Message.show()

    def daima(self):
        import time
        self.Dayremaining = 0
        thirty = [2, 4, 6, 9, 11]
        thirtyone = [1, 3, 5, 7, 8, 10, 12]
        thirty0 = [2, 4, 6]
        thirtyone0 = [1, 3, 5]
        year = int(time.strftime('%y'))
        month = int(time.strftime('%m'))
        date = int(time.strftime('%d'))
        if year < 2023:
            self.Dayremaining = 157
            for i in thirty:
                if month < i:
                    self.Dayremaining = self.Dayremaining + 30
                if month == i:
                    if i == 2:
                        self.Dayremaining = self.Dayremaining + 28 - date
                    else:
                        self.Dayremaining = self.Dayremaining + 30 - date
            for m in thirtyone:
                if month < m:
                    self.Dayremaining = self.Dayremaining + 31
                if month == m:
                    self.Dayremaining = self.Dayremaining + 31 - date
        else:
            for q in thirty0:
                if month < q:
                    if q == 6:
                        self.Dayremaining = self.Dayremaining + 6
                    else:
                        self.Dayremaining = self.Dayremaining + 30
                if month == q:
                    if q == 2:
                        self.Dayremaining = self.Dayremaining + 28 - date
                    elif q == 6:
                        self.Dayremaining = 6 - date
                    else:
                        self.Dayremaining = self.Dayremaining + 30 - date
            for t in thirtyone0:
                if month < t:
                    self.Dayremaining = self.Dayremaining + 31
                if month == t:
                    self.Dayremaining = self.Dayremaining + 31 - date

    def WL_itemclicked_Event0(self, item):
        itemtext = item.text()
        if itemtext != '暂无数据':
            self.hide()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 物理单元总结知识点 where 所属范围 = ?', (itemtext,))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            self.WL_jiemian0 = 物理单元总结界面.Ui_WL_jiemian('知识点', result[0][1], result[0][2])
            self.WL_jiemian0.show()
            self.WL_jiemian0.back.clicked.connect(self.WL_danyuanxuanze_jiemianquit)
        else:
            self.MESSAGE = Ui_KSFX_Message('通知', '暂无数据', '请前往管理者模式自行添加数据！')
            self.MESSAGE.show()

    def WL_itemclicked_Event1(self, item):
        itemtext = item.text()
        if itemtext != '暂无数据':
            self.hide()
            self.WL_jiemian0 = 物理单元总结界面.Ui_WL_jiemian('例题', itemtext)
            self.WL_jiemian0.show()
            self.WL_jiemian0.back.clicked.connect(self.WL_danyuanxuanze_jiemianquit)
        else:
            self.MESSAGE = Ui_KSFX_Message('通知', '暂无数据', '请前往管理者模式自行添加数据！')
            self.MESSAGE.show()

    def WL_danyuanxuanze_jiemianquit(self):
        self.show()

    def Physics_WaitTimer_Event(self):
        if self.Physics_Wait < self.random_number:
            self.Physics_Wait += 0.1
        else:
            self.Wait_Picture.close()
            self.show()
            self.WL_danyuanzongjie_picture2.clicked.connect(self.WL_danyuanzongjie_MESSAGE)
            self.Physics_WaitTimer.stop()

    def WL_danyuanzongjie_MESSAGE(self):
        self.MESSAGE = Ui_KSFX_Message('通知', '单元总结',
                                       '左边为各单元知识点，右边为例题。您可根据自身需要在管理者模式中添加您的数据。例题部分提供图片服务，您可点击上方进行图片大小检测，最后在管理者模式添加该图片完整路径')
        self.MESSAGE.show()

    def GLZ_window(self):
        biaoji = 0
        conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
        cursor = conn.cursor()
        cursor.execute('select * from 操作数据 where 操作命令 = "自动登录" ')
        result = cursor.fetchall()
        cursor.execute('select * from 账户信息')
        zhanghu = cursor.fetchall()
        cursor.close()
        conn.close()
        for i in result:
            if i[2] == True:  # 已经设置自动登录
                self.GLZ_nowuser = i[0]
                self.GLZ_Action()
                biaoji = 1
        if biaoji == 0:
            self.jsblogon = Ui_JSB_logon()
            self.jsblogon.show()
            self.hide()
            self.jsblogon.LOGON_logonbutton.clicked.connect(self.GLZ_logonevent)
            if zhanghu != []:  # 已有账户则禁止注册
                self.jsblogon.LOGON_zhucebutton.setEnabled(False)
            else:
                self.jsblogon.LOGON_zhucebutton.clicked.connect(self.GLZ_zhuceevent)
            self.jsblogon.LOGON_backbutton.clicked.connect(self.LOGON_back)
            self.jsblogon.LOGON_forgetbutton.clicked.connect(self.Logon_Forgetevent)

    def GLZ_zhuceevent(self):
        _translate = QtCore.QCoreApplication.translate
        zhanghu = self.jsblogon.LOGON_zhanghu_input.text()
        key = self.jsblogon.LOGON_key1_input.text()
        if zhanghu != '' and key != '':
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('insert into 账户信息(账户名,密码) values (?,?)', (zhanghu, key))
            cursor.execute('insert into 操作数据(账户名,操作命令,值) values (?,?,?)', (zhanghu, "自动登录", False))
            cursor.execute('insert into 操作数据(账户名,操作命令,值) values (?,?,?)', (zhanghu, "免爬虫等待", False))
            cursor.execute('insert into 操作数据(账户名,操作命令,值) values (?,?,?)', (zhanghu, "音乐", False))
            cursor.close()
            conn.commit()
            conn.close()
            self.LOGtime = 0
            self.JSBtimer = QTimer(self)
            self.JSBtimer.start(100)
            self.JSBtimer.timeout.connect(self.GLZ_logTimer)
            self.jsblogon.LOGON_warning.setStyleSheet("color: rgb(85, 255, 0);")
            self.jsblogon.LOGON_warning.setText(_translate("JSB_logon", '注册成功，欢迎使用！'))
            self.jsblogon.LOGON_warning.show()
            self.GLZ_nowuser = zhanghu
            self.automatic_logon()
            self.jsblogon.LOGON_neverlogon.setEnabled(False)
            self.jsblogon.LOGON_logonbutton.setEnabled(False)
            self.jsblogon.LOGON_logonbutton.setEnabled(False)
            self.jsblogon.LOGON_backbutton.setEnabled(False)
            self.jsblogon.LOGON_forgetbutton.setEnabled(False)
        else:
            self.jsblogon.LOGON_warning.setStyleSheet("color: rgb(255, 0, 0);")
            self.jsblogon.LOGON_warning.setText(_translate("JSB_logon", '账号或密码不能为空！'))
            self.jsblogon.LOGON_warning.show()

    def GLZ_logonevent(self):  # 登录按钮绑定的事件
        if self.jsblogon.LOGON_zhanghu.text() == '账户：':  # 判断是否是处于忘记密码界面
            _translate = QtCore.QCoreApplication.translate
            zhanghu = self.jsblogon.LOGON_zhanghu_input.text()
            key = self.jsblogon.LOGON_key1_input.text()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 账户信息 where 账户名 = ? and 密码 = ?', (zhanghu, key))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            if result != []:
                self.LOGtime = 0
                self.JSBtimer = QTimer(self)
                self.JSBtimer.start(100)
                self.JSBtimer.timeout.connect(self.GLZ_logTimer)
                self.jsblogon.LOGON_warning.show()
                self.jsblogon.LOGON_warning.setStyleSheet("color: rgb(85, 255, 0);")
                self.jsblogon.LOGON_warning.setText(_translate("JSB_logon", '登录成功，欢迎使用！'))
                self.GLZ_nowuser = zhanghu
                self.automatic_logon()
                self.jsblogon.LOGON_neverlogon.setEnabled(False)
                self.jsblogon.LOGON_logonbutton.setEnabled(False)
                self.jsblogon.LOGON_zhucebutton.setEnabled(False)
                self.jsblogon.LOGON_backbutton.setEnabled(False)
                self.jsblogon.LOGON_forgetbutton.setEnabled(False)
            else:
                self.jsblogon.LOGON_warning.setStyleSheet("color: rgb(255, 0, 0);")
                self.jsblogon.LOGON_warning.setText(_translate("JSB_logon", '账户或密码错误，请检查或前往注册'))
                self.jsblogon.LOGON_warning.show()
                self.jsblogon.LOGON_zhanghu_input.clear()
                self.jsblogon.LOGON_key1_input.clear()
        else:
            _translate = QtCore.QCoreApplication.translate
            zhanghu = self.jsblogon.LOGON_zhanghu_input.text()
            key = self.jsblogon.LOGON_key1_input.text()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            cursor.execute('select * from 账户信息 where 账户名 = ? ', (zhanghu,))
            result = cursor.fetchall()
            if result != []:
                cursor.execute('update 账户信息 set 密码 = ? where 账户名 = ?', (key, zhanghu))
                cursor.execute('update 操作数据 set 值 = ? where 账户名 = ?', (False, zhanghu))
                cursor.close()
                conn.commit()
                conn.close()
                self.LOGtime = 0
                self.JSBtimer = QTimer(self)
                self.JSBtimer.start(100)
                self.JSBtimer.timeout.connect(self.GLZ_logTimer)
                self.jsblogon.LOGON_warning.show()
                self.jsblogon.LOGON_warning.setStyleSheet("color: rgb(85, 255, 0);")
                self.jsblogon.LOGON_warning.setText(_translate("JSB_logon", '登录成功，欢迎使用！'))
                self.GLZ_nowuser = zhanghu
                self.automatic_logon()
                self.jsblogon.LOGON_neverlogon.setEnabled(False)
                self.jsblogon.LOGON_logonbutton.setEnabled(False)
                self.jsblogon.LOGON_zhucebutton.setEnabled(False)
                self.jsblogon.LOGON_backbutton.setEnabled(False)
                self.jsblogon.LOGON_forgetbutton.setEnabled(False)
            else:
                self.jsblogon.LOGON_warning.setStyleSheet("color: rgb(255, 0, 0);")
                self.jsblogon.LOGON_warning.setText(_translate("JSB_logon", '账户不存在，请检查或前往注册'))
                self.jsblogon.LOGON_warning.show()
                self.jsblogon.LOGON_zhanghu_input.clear()
                self.jsblogon.LOGON_key1_input.clear()
                cursor.close()
                conn.close()

    def GLZ_logTimer(self):
        _translate = QtCore.QCoreApplication.translate
        self.LOGtime += 0.1
        if self.LOGtime >= 0.7:
            self.JSBtimer.stop()
            self.jsblogon.LOGON_forgetbutton.show()
            self.jsblogon.LOGON_zhanghu.setText(_translate("JSB_logon", "账户："))
            self.jsblogon.LOGON_backbutton.setText(_translate("JiShiBen", "退出"))
            self.jsblogon.LOGON_zhanghu_input.clear()
            self.jsblogon.LOGON_key1_input.clear()
            self.jsblogon.LOGON_neverlogon.setEnabled(True)
            self.jsblogon.LOGON_logonbutton.setEnabled(True)
            self.jsblogon.LOGON_zhucebutton.setEnabled(True)
            self.jsblogon.LOGON_backbutton.setEnabled(True)
            self.jsblogon.LOGON_forgetbutton.setEnabled(True)
            self.jsblogon.close()
            self.GLZ_Action()

    def GLZ_Action(self):
        self.glz = Ui_GLZ_jiemian()
        self.GLZ_page = 1
        self.GLZ_column = '-1'
        self.GLZ_row = '-1'
        self.GLZ_rowText = '-1'
        self.GLZ_rowMiddleText = '-1'
        self.GLZ_rowRightMiddleText = '-1'
        self.GLZ_HeadercolumnText = '-1'
        self.GLZ_touchtime = 0
        self.GLZ_columnText = -1
        self.GLZ_HsList = []
        self.glz.GLZ_quitpicture.clicked.connect(self.GLZ_Quit)
        self.glz.GLZ_rightbutton.clicked.connect(self.GLZ_RIGHT)
        self.glz.GLZ_leftbutton.clicked.connect(self.GLZ_LEFT)
        self.glz.GLZ_increasebutton.clicked.connect(self.GLZ_INCREASE)
        self.glz.GLZ_deletebutton.clicked.connect(self.GLZ_DELETE)
        self.glz.GLZ_editbutton.clicked.connect(self.GLZ_EDIT)
        self.glz.GLZ_backbutton.clicked.connect(self.GLZ_BACK)
        self.glz.GLZ_tableWidget.itemClicked.connect(self.getItem)
        self.glz.GLZ_tableWidget.currentCellChanged.connect(self.GLZ_GET)
        self.glz.GLZ_tableWidget.itemChanged.connect(self.GLZ_itemchangedEvent)
        self.glz.GLZ_questionbutton.clicked.connect(self.GLZ_Question)
        self.glz.GLZ_editbutton.setEnabled(True)
        self.glz.GLZ_deletebutton.setEnabled(False)
        self.glz.GLZ_increasebutton.setEnabled(False)
        self.glz.GLZ_backbutton.setEnabled(True)
        conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
        cursor = conn.cursor()
        cursor.execute('select * from 操作数据 where 账户名 = ? ', (self.GLZ_nowuser,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        row = len(result)
        column = 3
        self.glz.GLZ_tableWidget.setRowCount(row)
        self.glz.GLZ_tableWidget.setColumnCount(column)
        self.GLZ_list = ['账户名', '操作命令', '值']
        self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
        for i in range(row):
            for j in range(column):
                if j != 2:
                    data = QTableWidgetItem(str(result[i][j]))
                    data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.glz.GLZ_tableWidget.setItem(i, j, data)
                else:
                    self.GLZ_checkButton = QtWidgets.QCheckBox()
                    if result[i][2] == 1:
                        self.GLZ_checkButton.setChecked(True)
                    self.GLZ_checkButton.stateChanged.connect(self.GLZ_C_Bchanged)
                    self.glz.GLZ_tableWidget.setCellWidget(i, 2, self.GLZ_checkButton)
        self.hide()
        try:
            self.music_timer.stop()
            self.musicplayer.pause()
        except:
            pass
        self.glz.show()

    def GLZ_Question(self):
        if self.GLZ_page == 1 :
            text = '1.自动登录：在以后不再需要输入密码而自动登录。\n' \
                    '2.免爬虫等待：在加载界面不进行爬虫操作，节省加载时间。\n' \
                    '3.音乐：主页播放音乐（可能造成电脑卡顿）\n'
        elif self.GLZ_page == 2 :
            text = '1.默认数据库中为高中必背词汇。若您发现有误差请自行更改并联系作者。\n' \
                   '2. 短语中，单词之间只有一个空格。one\'s的输入方法就是一撇加S，输入时，请保证输入法为英文。\n'\
                   '3.点击增加后，填写完相关数据，再点击修改即可更新至数据库。\n' \
                   '4.书名和单元可以随您而定，但请尽量多的输入同一个书名和单元，否则数量太少，无训练性。\n' \
                   '5.选择一行点击删除即可将该行数据删除。'
        elif self.GLZ_page == 3:
            text = '1.点击增加后，填写完相关数据，再点击修改即可更新至数据库。\n' \
                   '2.古诗文诗名可以随您而定，但请尽量多的输入同一个古诗文诗名，否则数量太少，无训练性。\n' \
                   '3.选择一行点击删除即可将该行数据删除。'
        elif self.GLZ_page == 4:
            text = '1.书名请按规定填写，所属范围是书名下的子目录名，由您决定。\n' \
                   '2.点击增加后，填写完相关数据，再点击修改即可更新至数据库。\n' \
                   '3.选择一行点击删除即可将该行数据删除。'
        elif self.GLZ_page == 5:
            text = '1.书名请按规定填写，所属范围是书名下的子目录名，由您决定。\n' \
                   '2.点击增加后，填写完相关数据，再点击修改即可更新至数据库。\n' \
                   '3.选择一行点击删除即可将该行数据删除。\n' \
                   '4.图片地址是该图片的绝对路径，可以不填写。'
        elif self.GLZ_page == 6:
            text = '正在更新中！'
        else:
            text = '正在更新中！'
        self.MESSAGE = Ui_KSFX_Message('多行通知',self.glz.GLZ_title.text(),text)
        self.MESSAGE.show()


    def GLZ_C_Bchanged(self):
        self.GLZ_rowText = self.GLZ_nowuser# 本行排头内容
        if self.glz.GLZ_tableWidget.cellWidget(int(self.GLZ_row),2).isChecked() :
            self.GLZ_columnText = 1
        else:
            self.GLZ_columnText = -1
        if int(self.GLZ_row) == 0 :
            self.GLZ_rowMiddleText = '自动登录'  # 本行中间内容（只有三列时）
            self.GLZ_HeadercolumnText = '值'  # 纵排标题
            self.GLZ_touchtime = 1
        elif int(self.GLZ_row) == 1 :
            self.GLZ_rowMiddleText = '免爬虫等待'  # 本行中间内容（只有三列时）
            self.GLZ_HeadercolumnText = '值'  # 纵排标题
            self.GLZ_touchtime = 1
        elif int(self.GLZ_row) == 2 :
            self.GLZ_rowMiddleText = '音乐'  # 本行中间内容（只有三列时）
            self.GLZ_HeadercolumnText = '值'  # 纵排标题
            self.GLZ_touchtime = 1
        else:
            pass

    def GLZ_Quit(self):
        self.glz.close()
        self.show()
        if self.bj_music != None:
            if self.bj_music == True:
                self.music_marktime = 0
                self.music_timer = QTimer(self)
                self.music_timer.start(100)
                self.music_timer.timeout.connect(self.Background_Music)
        else:
            pass

    def GLZ_RIGHT(self, value=True):
        _translate = QtCore.QCoreApplication.translate
        self.GLZ_page += 1
        self.GLZ_column = '-1'
        self.GLZ_row = '-1'
        self.GLZ_rowText = '-1'
        self.GLZ_rowMiddleText = '-1'
        self.GLZ_rowRightMiddleText = '-1'
        self.GLZ_HeadercolumnText = '-1'
        self.GLZ_touchtime = 0
        self.GLZ_columnText = -1
        self.glz.GLZ_tableWidget.setRowCount(0)  # 清除表格
        if value == True:
            self.GLZ_HsList = []  # 清除回溯列表
        conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
        cursor = conn.cursor()
        if self.GLZ_page == 2:
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "背单词"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 背单词')
            result = cursor.fetchall()
            row = len(result)
            column = 4
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['书名和单元', '中文', '英文单词', '单词序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 3 :
                        data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.glz.GLZ_tableWidget.setItem(i, j, data)
        elif self.GLZ_page == 3:
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "语文默写古诗文"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 语文默写古诗文')
            result = cursor.fetchall()
            row = len(result)
            column = 4
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['古诗文诗名', '问题', '答案', '序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 3:
                        data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.glz.GLZ_tableWidget.setItem(i, j, data)
        elif self.GLZ_page == 4:
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "物理单元总结知识点"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 物理单元总结知识点')
            result = cursor.fetchall()
            row = len(result)
            column = 4
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['书名', '所属范围', '内容','序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 0:
                        self.WL_ComboBox = QtWidgets.QComboBox()
                        WL_list = ['必修一','必修二','必修三','选择性必修一','选择性必修二','选择性必修三']
                        self.WL_ComboBox.addItems(WL_list)
                        self.WL_ComboBox.setFrame(False)
                        self.WL_ComboBox.setStyleSheet('background-color: rgb(216, 225, 255);')
                        self.glz.GLZ_tableWidget.setCellWidget(i, 0, self.WL_ComboBox)
                        self.WL_ComboBox.setCurrentText(result[i][0])
                        self.WL_ComboBox.activated.connect(self.GLZ_WLcomboboxActivedEvent)
                    else:
                        if j == 3:
                            data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.glz.GLZ_tableWidget.setItem(i, j, data)
        elif self.GLZ_page == 5:
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "物理单元总结例题"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 物理单元总结例题')
            result = cursor.fetchall()
            row = len(result)
            column = 5
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['书名', '所属范围', '内容', '图片地址','序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 0:
                        self.WL_ComboBox = QtWidgets.QComboBox()
                        WL_list = ['必修一', '必修二', '必修三', '选择性必修一', '选择性必修二', '选择性必修三']
                        self.WL_ComboBox.addItems(WL_list)
                        self.WL_ComboBox.setFrame(False)
                        self.WL_ComboBox.setStyleSheet('background-color: rgb(216, 225, 255);')
                        self.glz.GLZ_tableWidget.setCellWidget(i, 0, self.WL_ComboBox)
                        self.WL_ComboBox.setCurrentText(result[i][0])
                        self.WL_ComboBox.activated.connect(self.GLZ_WLcomboboxActivedEvent)
                    else:
                        if j == 4 :
                            data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.glz.GLZ_tableWidget.setItem(i, j, data)
        elif self.GLZ_page == 6 :
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "化学基础知识"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 化学基础知识')
            result = cursor.fetchall()
            row = len(result)
            column = 7
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['题目', 'A选项', 'B选项', 'C选项', 'D选项','答案','题目序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 5 :
                        self.HX_ComboBox = QtWidgets.QComboBox()
                        HX_list = ['A','B','C','D']
                        self.HX_ComboBox.addItems(HX_list)
                        self.HX_ComboBox.setFrame(False)
                        self.HX_ComboBox.setStyleSheet('background-color: rgb(216, 225, 255);')
                        self.glz.GLZ_tableWidget.setCellWidget(i, 0, self.HX_ComboBox)
                        self.HX_ComboBox.setCurrentText(result[i][0])
                        self.HX_ComboBox.activated.connect(self.GLZ_HXcomboboxActivedEvent)
                    else:
                        if j == 6 :
                            data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.glz.GLZ_tableWidget.setItem(i, j, data)
        elif self.GLZ_page == 7:
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "生物捡苹果"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 生物捡苹果')
            result = cursor.fetchall()
            row = len(result)
            column = 4
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['范围', '题目', '答案', '题目序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 3:
                        data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.glz.GLZ_tableWidget.setItem(i, j, data)
        else:
            self.GLZ_page = 1
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "操作数据"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(False)
            self.glz.GLZ_increasebutton.setEnabled(False)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 操作数据 where 账户名 = ? ', (self.GLZ_nowuser,))
            result = cursor.fetchall()
            row = len(result)
            column = 3
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['账户名', '操作命令', '值']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    if j != 2:
                        data = QTableWidgetItem(str(result[i][j]))
                        data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.glz.GLZ_tableWidget.setItem(i, j, data)
                    else:
                        self.GLZ_checkButton = QtWidgets.QCheckBox()
                        if result[i][2] == 1:
                            self.GLZ_checkButton.setChecked(True)
                        self.GLZ_checkButton.stateChanged.connect(self.GLZ_C_Bchanged)
                        self.glz.GLZ_tableWidget.setCellWidget(i, 2, self.GLZ_checkButton)
        cursor.close()
        conn.close()

    def GLZ_LEFT(self, value=True):
        _translate = QtCore.QCoreApplication.translate
        self.GLZ_page -= 1
        self.GLZ_column = '-1'
        self.GLZ_row = '-1'
        self.GLZ_rowText = '-1'
        self.GLZ_rowMiddleText = '-1'
        self.GLZ_rowRightMiddleText = '-1'
        self.GLZ_HeadercolumnText = '-1'
        self.GLZ_touchtime = 0
        self.GLZ_columnText = -1
        self.glz.GLZ_tableWidget.setRowCount(0)  # 清除表格
        if value == True:
            self.GLZ_HsList = []  # 清除回溯列表
        conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
        cursor = conn.cursor()
        if self.GLZ_page == 1:
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "操作数据"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(False)
            self.glz.GLZ_increasebutton.setEnabled(False)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 操作数据 where 账户名 = ? ', (self.GLZ_nowuser,))
            result = cursor.fetchall()
            row = len(result)
            column = 3
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['账户名', '操作命令', '值']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    if j != 2:
                        data = QTableWidgetItem(str(result[i][j]))
                        data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.glz.GLZ_tableWidget.setItem(i, j, data)
                    else:
                        self.GLZ_checkButton = QtWidgets.QCheckBox()
                        if result[i][2] == 1:
                            self.GLZ_checkButton.setChecked(True)
                        self.GLZ_checkButton.stateChanged.connect(self.GLZ_C_Bchanged)
                        self.glz.GLZ_tableWidget.setCellWidget(i, 2, self.GLZ_checkButton)
        elif self.GLZ_page == 2:
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "背单词"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 背单词 ')
            result = cursor.fetchall()
            row = len(result)
            column = 4
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['书名和单元', '中文', '英文单词', '单词序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 3:
                        data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.glz.GLZ_tableWidget.setItem(i, j, data)
        elif self.GLZ_page == 3:
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "语文默写古诗文"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 语文默写古诗文')
            result = cursor.fetchall()
            row = len(result)
            column = 4
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['古诗文诗名', '问题', '答案', '序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 3:
                        data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.glz.GLZ_tableWidget.setItem(i, j, data)
        elif self.GLZ_page == 4:
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "物理单元总结知识点"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 物理单元总结知识点')
            result = cursor.fetchall()
            row = len(result)
            column = 4
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['书名', '所属范围', '内容', '序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 0:
                        self.WL_ComboBox = QtWidgets.QComboBox()
                        WL_list = ['必修一', '必修二', '必修三', '选择性必修一', '选择性必修二', '选择性必修三']
                        self.WL_ComboBox.addItems(WL_list)
                        self.WL_ComboBox.setFrame(False)
                        self.WL_ComboBox.setStyleSheet('background-color: rgb(216, 225, 255);')
                        self.glz.GLZ_tableWidget.setCellWidget(i, 0, self.WL_ComboBox)
                        self.WL_ComboBox.setCurrentText(result[i][0])
                        self.WL_ComboBox.activated.connect(self.GLZ_WLcomboboxActivedEvent)
                    else:
                        if j == 3:
                            data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.glz.GLZ_tableWidget.setItem(i, j, data)
        elif self.GLZ_page == 5:
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "物理单元总结例题"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 物理单元总结例题')
            result = cursor.fetchall()
            row = len(result)
            column = 5
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['书名', '所属范围', '内容', '图片地址', '序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 0:
                        self.WL_ComboBox = QtWidgets.QComboBox()
                        WL_list = ['必修一', '必修二', '必修三', '选择性必修一', '选择性必修二', '选择性必修三']
                        self.WL_ComboBox.addItems(WL_list)
                        self.WL_ComboBox.setFrame(False)
                        self.WL_ComboBox.setStyleSheet('background-color: rgb(216, 225, 255);')
                        self.glz.GLZ_tableWidget.setCellWidget(i, 0, self.WL_ComboBox)
                        self.WL_ComboBox.setCurrentText(result[i][0])
                        self.WL_ComboBox.activated.connect(self.GLZ_WLcomboboxActivedEvent)
                    else:
                        if j == 4:
                            data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.glz.GLZ_tableWidget.setItem(i, j, data)
        elif self.GLZ_page == 6 :
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "化学基础知识"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 化学基础知识')
            result = cursor.fetchall()
            row = len(result)
            column = 7
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['题目', 'A选项', 'B选项', 'C选项', 'D选项','答案','题目序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 5 :
                        self.HX_ComboBox = QtWidgets.QComboBox()
                        HX_list = ['A','B','C','D']
                        self.HX_ComboBox.addItems(HX_list)
                        self.HX_ComboBox.setFrame(False)
                        self.HX_ComboBox.setStyleSheet('background-color: rgb(216, 225, 255);')
                        self.glz.GLZ_tableWidget.setCellWidget(i, 0, self.HX_ComboBox)
                        self.HX_ComboBox.setCurrentText(result[i][0])
                        self.HX_ComboBox.activated.connect(self.GLZ_HXcomboboxActivedEvent)
                    else:
                        if j == 6 :
                            data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.glz.GLZ_tableWidget.setItem(i, j, data)
        elif self.GLZ_page == 7:
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "生物捡苹果"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 生物捡苹果')
            result = cursor.fetchall()
            row = len(result)
            column = 4
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['范围', '题目', '答案', '题目序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 3:
                        data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.glz.GLZ_tableWidget.setItem(i, j, data)
        else:
            self.GLZ_page = 7
            self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "生物捡苹果"))
            self.glz.GLZ_editbutton.setEnabled(True)
            self.glz.GLZ_deletebutton.setEnabled(True)
            self.glz.GLZ_increasebutton.setEnabled(True)
            self.glz.GLZ_backbutton.setEnabled(True)
            cursor.execute('select * from 生物捡苹果')
            result = cursor.fetchall()
            row = len(result)
            column = 4
            self.glz.GLZ_tableWidget.setRowCount(row)
            self.glz.GLZ_tableWidget.setColumnCount(column)
            self.GLZ_list = ['范围', '题目', '答案', '题目序号']
            self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
            for i in range(row):
                for j in range(column):
                    data = QTableWidgetItem(str(result[i][j]))
                    if j == 3:
                        data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                    self.glz.GLZ_tableWidget.setItem(i, j, data)
        cursor.close()
        conn.close()


    def GLZ_WLcomboboxActivedEvent(self):
        self.GLZ_rowText = self.glz.GLZ_tableWidget.cellWidget(self.GLZ_row,0).currentText()

    def GLZ_HXcomboboxActivedEvent(self):
        pass

    def GLZ_GET(self,row,column):#针对有widget控件获取相关信息
        if self.glz.GLZ_title.text() == '物理单元总结知识点':
            columncount = self.glz.GLZ_tableWidget.columnCount()
            self.GLZ_column = column
            self.GLZ_row = row  # 横坐标
            try:
                self.GLZ_rowText = self.glz.GLZ_tableWidget.cellWidget(row,0).currentText()
                self.GLZ_rowMiddleText = self.glz.GLZ_tableWidget.item(row, 1).text()  # 本行中间内容（只有三列时）
                self.GLZ_rowRightMiddleText = self.glz.GLZ_tableWidget.item(row, 2).text()  # 本行中间靠右内容（四列时）
                self.GLZ_columnText = int(self.glz.GLZ_tableWidget.item(row, columncount - 1).text())  # 本行最右内容
            except:
                pass
            self.GLZ_touchtime = 1
        elif self.glz.GLZ_title.text() == '物理单元总结例题':
            columncount = self.glz.GLZ_tableWidget.columnCount()
            self.GLZ_column = column
            self.GLZ_row = row  # 横坐标
            try:
                self.GLZ_rowText = self.glz.GLZ_tableWidget.cellWidget(row,0).currentText()
                self.GLZ_rowMiddleText = self.glz.GLZ_tableWidget.item(row, 1).text()  # 本行中间内容（只有三列时）
                self.GLZ_rowRightMiddleText = self.glz.GLZ_tableWidget.item(row, 2).text()  # 本行中间靠右内容（四列时）
                self.GLZ_rowRightRightMiddleText = self.glz.GLZ_tableWidget.item(row, 3).text()  # 本行中间靠右右内容（五列时）
                self.GLZ_columnText = int(self.glz.GLZ_tableWidget.item(row, columncount - 1).text())  # 本行最右内容
            except:
                pass
            self.GLZ_touchtime = 1
        elif self.glz.GLZ_title.text() == '操作数据':
            columncount = self.glz.GLZ_tableWidget.columnCount()
            self.GLZ_column = column
            self.GLZ_row = row  # 横坐标
            try:
                self.GLZ_rowText = self.glz.GLZ_tableWidget.cellWidget(row,0).text()
                self.GLZ_rowMiddleText = self.glz.GLZ_tableWidget.item(row, 1).text()  # 本行中间内容（只有三列时）
                self.GLZ_columnText = int(self.glz.GLZ_tableWidget.item(row, columncount - 1).text())  # 本行最右内容
            except:
                pass
        else:
            pass

    def getItem(self, item):
        if self.glz.GLZ_title.text() == '背单词' or self.glz.GLZ_title.text() == '语文默写古诗文':
            columncount = self.glz.GLZ_tableWidget.columnCount()
            self.GLZ_column = item.column()  # 纵坐标
            self.GLZ_row = item.row()  # 横坐标
            try:
                self.GLZ_rowText = self.glz.GLZ_tableWidget.item(item.row(), 0).text()  # 本行排头内容
            except :
                pass
            try:
                self.GLZ_rowMiddleText = self.glz.GLZ_tableWidget.item(item.row(), 1).text()  # 本行中间内容（只有三列时）
            except:
                pass
            try:
                self.GLZ_rowRightMiddleText = self.glz.GLZ_tableWidget.item(item.row(), 2).text()  # 本行中间靠右内容（四列时）
                self.GLZ_columnText = int(self.glz.GLZ_tableWidget.item(item.row(), columncount - 1).text())  # 本行最右内容
            except:
                pass
            self.GLZ_HeadercolumnText = self.GLZ_list[item.column()]  # 纵排标题
            self.GLZ_touchtime = 1

    def GLZ_itemchangedEvent(self):#当单元格数据有改动时触发
        if self.glz.GLZ_title.text() != '物理单元总结知识点' and self.glz.GLZ_title.text() != '物理单元总结例题':
            columncount = self.glz.GLZ_tableWidget.columnCount()
            try:
                self.GLZ_rowText = self.glz.GLZ_tableWidget.item(self.GLZ_row, 0).text()  # 本行排头内容
            except:
                pass
            try:
                self.GLZ_rowMiddleText = self.glz.GLZ_tableWidget.item(self.GLZ_row, 1).text()  # 本行中间内容（只有三列时）
            except:
                pass
            try:
                self.GLZ_rowRightMiddleText = self.glz.GLZ_tableWidget.item(self.GLZ_row, 2).text()  # 本行中间靠右内容（四列时）
                self.GLZ_columnText = int(self.glz.GLZ_tableWidget.item(self.GLZ_row, columncount - 1).text())  # 本行最右内容
            except:
                pass
        elif self.glz.GLZ_title.text() == '物理单元总结知识点':
            columncount = self.glz.GLZ_tableWidget.columnCount()
            try:
                self.GLZ_rowText = self.glz.GLZ_tableWidget.cellWidget(int(self.GLZ_row),0).currentText()
                self.GLZ_rowMiddleText = self.glz.GLZ_tableWidget.item(self.GLZ_row, 1).text()  # 本行中间内容（只有三列时）
                self.GLZ_rowRightMiddleText = self.glz.GLZ_tableWidget.item(self.GLZ_row, 2).text()  # 本行中间靠右内容（四列时）
                self.GLZ_columnText = int(self.glz.GLZ_tableWidget.item(self.GLZ_row,columncount - 1).text())  # 本行最右内容
            except :
                pass
        elif self.glz.GLZ_title.text() == '物理单元总结例题':
            columncount = self.glz.GLZ_tableWidget.columnCount()
            try:
                self.GLZ_rowText = self.glz.GLZ_tableWidget.cellWidget(int(self.GLZ_row), 0).currentText()
                self.GLZ_rowMiddleText = self.glz.GLZ_tableWidget.item(self.GLZ_row, 1).text()  # 本行中间内容（只有三列时）
                self.GLZ_rowRightMiddleText = self.glz.GLZ_tableWidget.item(self.GLZ_row, 2).text()  # 本行中间靠右内容（四列时）
                self.GLZ_rowRightRightMiddleText = self.glz.GLZ_tableWidget.item(self.GLZ_row,3).text()  # 本行中间靠右右内容（五列时）
                self.GLZ_columnText = int(self.glz.GLZ_tableWidget.item(self.GLZ_row, columncount - 1).text())  # 本行最右内容
            except :
                pass
        else:
            pass



    def GLZ_INCREASE(self):
        _translate = QtCore.QCoreApplication.translate
        conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
        cursor = conn.cursor()
        title = self.glz.GLZ_title.text()
        if title == '背单词':
            cursor.execute('select * from 背单词 where 书名和单元 = "请填写"')
            result = cursor.fetchone()
            cursor.execute('select * from 背单词 ')
            lenth = len(cursor.fetchall())
            if result != None:
                self.MESSAGE = Ui_KSFX_Message('警告', '空白行存在', '请在空白行进行修改！')
                self.MESSAGE.show()
            else:  # 没有空白行则添加空白行
                cursor.execute('insert into 背单词 (书名和单元,中文,英文单词,单词序号) values ("请填写","请填写","请填写",?)', (lenth + 1,))
                conn.commit()
                self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "背单词"))
                self.glz.GLZ_editbutton.setEnabled(True)
                self.glz.GLZ_deletebutton.setEnabled(True)
                self.glz.GLZ_increasebutton.setEnabled(True)
                self.glz.GLZ_backbutton.setEnabled(True)
                cursor.execute('select * from 背单词 ')
                result = cursor.fetchall()
                row = len(result)
                column = 4
                self.glz.GLZ_tableWidget.setRowCount(row)
                self.glz.GLZ_tableWidget.setColumnCount(column)
                self.GLZ_list = ['书名和单元', '中文', '英文单词', '单词序号']
                self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
                for i in range(row):
                    for j in range(column):
                        data = QTableWidgetItem(str(result[i][j]))
                        if j == 3:
                            data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.glz.GLZ_tableWidget.setItem(i, j, data)
                self.GLZ_HsList = ['增', '背单词']
        elif title == '语文默写古诗文':
            cursor.execute('select * from 语文默写古诗文 where 古诗文诗名 = "请填写"')
            result = cursor.fetchone()
            cursor.execute('select * from 语文默写古诗文 ')
            lenth = len(cursor.fetchall())
            if result != None:
                self.MESSAGE = Ui_KSFX_Message('警告', '空白行存在', '请在空白行进行修改！')
                self.MESSAGE.show()
            else:  # 没有空白行则添加空白行
                cursor.execute('insert into 语文默写古诗文 (古诗文诗名,问题,答案,序号) values ("请填写","请填写","请填写",?)', (lenth + 1,))
                conn.commit()
                self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "语文默写古诗文"))
                self.glz.GLZ_editbutton.setEnabled(True)
                self.glz.GLZ_deletebutton.setEnabled(True)
                self.glz.GLZ_increasebutton.setEnabled(True)
                self.glz.GLZ_backbutton.setEnabled(True)
                cursor.execute('select * from 语文默写古诗文 ')
                result = cursor.fetchall()
                row = len(result)
                column = 4
                self.glz.GLZ_tableWidget.setRowCount(row)
                self.glz.GLZ_tableWidget.setColumnCount(column)
                self.GLZ_list = ['古诗文诗名', '问题', '答案', '序号']
                self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
                for i in range(row):
                    for j in range(column):
                        data = QTableWidgetItem(str(result[i][j]))
                        if j == 3:
                            data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        self.glz.GLZ_tableWidget.setItem(i, j, data)
                self.GLZ_HsList = ['增', '语文默写古诗文']
        elif title == '物理单元总结知识点':
            cursor.execute('select * from 物理单元总结知识点 where 所属范围 = "请填写"')
            result = cursor.fetchone()
            cursor.execute('select * from 物理单元总结知识点')
            lenth = len(cursor.fetchall())
            if result != None:
                self.MESSAGE = Ui_KSFX_Message('警告', '空白行存在', '请在空白行进行修改！')
                self.MESSAGE.show()
            else:  # 没有空白行则添加空白行
                cursor.execute('insert into 物理单元总结知识点 (书名,所属范围,内容,序号) values ("必修一","请填写","请填写",?)', (lenth + 1,))
                conn.commit()
                self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "物理单元总结知识点"))
                self.glz.GLZ_editbutton.setEnabled(True)
                self.glz.GLZ_deletebutton.setEnabled(True)
                self.glz.GLZ_increasebutton.setEnabled(True)
                self.glz.GLZ_backbutton.setEnabled(True)
                cursor.execute('select * from 物理单元总结知识点 ')
                result = cursor.fetchall()
                row = len(result)
                column = 4
                self.glz.GLZ_tableWidget.setRowCount(row)
                self.glz.GLZ_tableWidget.setColumnCount(column)
                self.GLZ_list = ['书名', '所属范围', '内容', '序号']
                self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
                for i in range(row):
                    for j in range(column):
                        data = QTableWidgetItem(str(result[i][j]))
                        if j == 0:
                            self.WL_ComboBox = QtWidgets.QComboBox()
                            WL_list = ['必修一', '必修二', '必修三', '选择性必修一', '选择性必修二', '选择性必修三']
                            self.WL_ComboBox.addItems(WL_list)
                            self.WL_ComboBox.setFrame(False)
                            self.WL_ComboBox.setStyleSheet('background-color: rgb(216, 225, 255);')
                            self.glz.GLZ_tableWidget.setCellWidget(i, 0, self.WL_ComboBox)
                            self.WL_ComboBox.setCurrentText(result[i][0])
                            self.WL_ComboBox.activated.connect(self.GLZ_WLcomboboxActivedEvent)
                        else:
                            if j == 3:
                                data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                            self.glz.GLZ_tableWidget.setItem(i, j, data)
                self.GLZ_HsList = ['增', '物理单元总结知识点']
        elif title == '物理单元总结例题':
            cursor.execute('select * from 物理单元总结例题 where 所属范围 = "请填写"')
            result = cursor.fetchone()
            cursor.execute('select * from 物理单元总结例题')
            lenth = len(cursor.fetchall())
            if result != None:
                self.MESSAGE = Ui_KSFX_Message('警告', '空白行存在', '请在空白行进行修改！')
                self.MESSAGE.show()
            else:  # 没有空白行则添加空白行
                cursor.execute('insert into 物理单元总结例题 (书名,所属范围,内容,图片地址,序号) values ("必修一","请填写","请填写","请填写",?)', (lenth + 1,))
                conn.commit()
                self.glz.GLZ_title.setText(_translate("GLZ_jiemian", "物理单元总结例题"))
                self.glz.GLZ_editbutton.setEnabled(True)
                self.glz.GLZ_deletebutton.setEnabled(True)
                self.glz.GLZ_increasebutton.setEnabled(True)
                self.glz.GLZ_backbutton.setEnabled(True)
                cursor.execute('select * from 物理单元总结例题 ')
                result = cursor.fetchall()
                row = len(result)
                column = 5
                self.glz.GLZ_tableWidget.setRowCount(row)
                self.glz.GLZ_tableWidget.setColumnCount(column)
                self.GLZ_list = ['书名', '所属范围', '内容', '图片地址', '序号']
                self.glz.GLZ_tableWidget.setHorizontalHeaderLabels(self.GLZ_list)
                for i in range(row):
                    for j in range(column):
                        data = QTableWidgetItem(str(result[i][j]))
                        if j == 0:
                            self.WL_ComboBox = QtWidgets.QComboBox()
                            WL_list = ['必修一', '必修二', '必修三', '选择性必修一', '选择性必修二', '选择性必修三']
                            self.WL_ComboBox.addItems(WL_list)
                            self.WL_ComboBox.setFrame(False)
                            self.WL_ComboBox.setStyleSheet('background-color: rgb(216, 225, 255);')
                            self.glz.GLZ_tableWidget.setCellWidget(i, 0, self.WL_ComboBox)
                            self.WL_ComboBox.setCurrentText(result[i][0])
                            self.WL_ComboBox.activated.connect(self.GLZ_WLcomboboxActivedEvent)
                        else:
                            if j == 4:
                                data.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                            self.glz.GLZ_tableWidget.setItem(i, j, data)
                self.GLZ_HsList = ['增', '物理单元总结例题']
        else:
            pass
        cursor.close()
        conn.close()

    def GLZ_DELETE(self):  # 没点过，无数据数据删除
        if self.GLZ_touchtime != 0:
            self.GLZ_MESSAGE = Ui_KSFX_Message('询问', '', '是否确认删除第' + str(self.GLZ_row + 1) + '行？')
            self.GLZ_MESSAGE.show()
            self.GLZ_message_timer = QTimer(self)
            self.GLZ_message_timer.start(100)
            self.GLZ_message_timer.timeout.connect(self.GLZ_MESSAGE_DELETE)
        else:
            self.MESSAGE = Ui_KSFX_Message('警告', '无目标', '请先选择您要删除的数据行！')
            self.MESSAGE.show()

    def GLZ_MESSAGE_DELETE(self):
        self.GLZ_MESSAGE.Result()
        if self.GLZ_MESSAGE.Answer == 1:  # 选择确认删除
            self.GLZ_MESSAGE.close()
            self.GLZ_message_timer.stop()
            self.glz.GLZ_backbutton.setEnabled(True)
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            if self.glz.GLZ_title.text() == '背单词':
                cursor.execute('select * from 背单词 where 单词序号 = ? ', (self.GLZ_columnText,))
                result = cursor.fetchone()
                self.GLZ_HsList = ['删', self.glz.GLZ_title.text(), result[0],result[1],result[2],result[3]]
                cursor.execute('delete from 背单词 where 单词序号 = ?', (self.GLZ_columnText,))
            elif self.glz.GLZ_title.text() == '语文默写古诗文':
                cursor.execute('select * from 语文默写古诗文 where 序号 = ? ', (self.GLZ_columnText,))
                result = cursor.fetchone()
                self.GLZ_HsList = ['删', self.glz.GLZ_title.text(), result[0], result[1], result[2], result[3]]
                cursor.execute('delete from 语文默写古诗文 where 序号 = ?', (self.GLZ_columnText,))
            elif self.glz.GLZ_title.text() == '物理单元总结知识点':
                cursor.execute('select * from 物理单元总结知识点 where 序号 = ?', (self.GLZ_columnText,))
                result = cursor.fetchone()
                self.GLZ_HsList = ['删', self.glz.GLZ_title.text(), result[0], result[1], result[2], result[3]]
                cursor.execute('delete from 物理单元总结知识点 where 序号 = ?', (self.GLZ_columnText,))
            elif self.glz.GLZ_title.text() == '物理单元总结例题':
                cursor.execute('select * from 物理单元总结例题 where 序号 = ?', (self.GLZ_columnText,))
                result = cursor.fetchone()
                self.GLZ_HsList = ['删', self.glz.GLZ_title.text(), result[0], result[1], result[2], result[3],result[4]]
                cursor.execute('delete from 物理单元总结例题 where 序号 = ?', (self.GLZ_columnText,))
            else:
                pass
            cursor.close()
            conn.commit()
            conn.close()
            self.MESSAGE = Ui_KSFX_Message('通知', '删除成功', '数据已删除，您有一次撤销的机会！')
            self.MESSAGE.show()
            self.GLZ_page -= 1
            self.GLZ_RIGHT(False)
        elif self.GLZ_MESSAGE.Answer == 0:
            self.GLZ_MESSAGE.close()
            self.GLZ_message_timer.stop()
        else:
            pass

    def GLZ_EDIT(self):  # 删除判断
        if self.GLZ_rowText != '' and self.GLZ_rowMiddleText != '' and self.GLZ_rowRightMiddleText != '' and self.GLZ_columnText != '':
            if self.GLZ_touchtime != 0:
                if self.glz.GLZ_title.text() == '操作数据':
                    self.GLZ_MESSAGE = Ui_KSFX_Message('询问', '', '是否确认修改' + self.GLZ_rowMiddleText + '的设置?')
                    self.GLZ_MESSAGE.show()
                    self.GLZ_message_timer = QTimer(self)
                    self.GLZ_message_timer.start(100)
                    self.GLZ_message_timer.timeout.connect(self.GLZ_MESSAGE_EDIT)
                elif self.glz.GLZ_title.text() == '背单词':
                    self.GLZ_MESSAGE = Ui_KSFX_Message('询问', '',
                                                       '是否确认修改序号为' + str(self.GLZ_columnText) + '的内容？')
                    self.GLZ_MESSAGE.show()
                    self.GLZ_message_timer = QTimer(self)
                    self.GLZ_message_timer.start(100)
                    self.GLZ_message_timer.timeout.connect(self.GLZ_MESSAGE_EDIT)
                elif self.glz.GLZ_title.text() == '语文默写古诗文':
                    self.GLZ_MESSAGE = Ui_KSFX_Message('询问', '',
                                                       '是否确认修改序号为' + str(self.GLZ_columnText) + '的内容？')
                    self.GLZ_MESSAGE.show()
                    self.GLZ_message_timer = QTimer(self)
                    self.GLZ_message_timer.start(100)
                    self.GLZ_message_timer.timeout.connect(self.GLZ_MESSAGE_EDIT)
                elif self.glz.GLZ_title.text() == '物理单元总结知识点':
                    self.GLZ_MESSAGE = Ui_KSFX_Message('询问', '',
                                                       '是否确认修改序号为' + str(self.GLZ_columnText) + '的内容？')
                    self.GLZ_MESSAGE.show()
                    self.GLZ_message_timer = QTimer(self)
                    self.GLZ_message_timer.start(100)
                    self.GLZ_message_timer.timeout.connect(self.GLZ_MESSAGE_EDIT)
                elif self.glz.GLZ_title.text() == '物理单元总结例题':
                    self.GLZ_MESSAGE = Ui_KSFX_Message('询问', '',
                                                       '是否确认修改序号为' + str(self.GLZ_columnText) + '的内容？')
                    self.GLZ_MESSAGE.show()
                    self.GLZ_message_timer = QTimer(self)
                    self.GLZ_message_timer.start(100)
                    self.GLZ_message_timer.timeout.connect(self.GLZ_MESSAGE_EDIT)
            else:
                self.MESSAGE = Ui_KSFX_Message('警告', '无目标', '请先选择您要修改的数据！')
                self.MESSAGE.show()
        else:
            self.MESSAGE = Ui_KSFX_Message('警告', '修改无效', '修改内容中不能有空白内容！')
            self.MESSAGE.show()

    def GLZ_MESSAGE_EDIT(self):  # 修改执行函数
        self.GLZ_MESSAGE.Result()
        if self.GLZ_MESSAGE.Answer == 1:  # 选择确认修改
            self.GLZ_MESSAGE.close()
            self.GLZ_message_timer.stop()
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            self.glz.GLZ_backbutton.setEnabled(True)
            if self.glz.GLZ_title.text() == '操作数据':
                cursor.execute('select * from 操作数据 where 账户名 = ? and 操作命令 = ?',(self.GLZ_rowText, self.GLZ_rowMiddleText))
                result = cursor.fetchone()
                cursor.execute('update 操作数据 set 值 = ? where 操作命令 = ? and 账户名 = ? ',(self.GLZ_columnText, self.GLZ_rowMiddleText, self.GLZ_nowuser))
                self.GLZ_HsList = ['改', '操作数据', result[0], result[1], result[2]]
            elif self.glz.GLZ_title.text() == '背单词':
                cursor.execute('select * from 背单词 where 单词序号 = ?', (self.GLZ_columnText,))
                result = cursor.fetchone()
                cursor.execute('update 背单词 set 书名和单元 = ? where 单词序号 = ?', (self.GLZ_rowText, self.GLZ_columnText))
                cursor.execute('update 背单词 set 中文 = ? where 单词序号 = ?', (self.GLZ_rowMiddleText, self.GLZ_columnText))
                cursor.execute('update 背单词 set 英文单词 = ? where 单词序号 = ?',
                               (self.GLZ_rowRightMiddleText, self.GLZ_columnText))
                self.GLZ_HsList = ['改', self.glz.GLZ_title.text(), result[0], result[1], result[2], result[3]]
            elif self.glz.GLZ_title.text() == '语文默写古诗文':
                cursor.execute('select * from 语文默写古诗文 where 序号 = ?', (self.GLZ_columnText,))
                result = cursor.fetchone()
                cursor.execute('update 语文默写古诗文 set 古诗文诗名 = ? where 序号 = ?', (self.GLZ_rowText, self.GLZ_columnText))
                cursor.execute('update 语文默写古诗文 set 问题 = ? where 序号 = ?', (self.GLZ_rowMiddleText, self.GLZ_columnText))
                cursor.execute('update 语文默写古诗文 set 答案 = ? where 序号 = ?',(self.GLZ_rowRightMiddleText, self.GLZ_columnText))
                self.GLZ_HsList = ['改', self.glz.GLZ_title.text(), result[0], result[1], result[2], result[3]]
            elif self.glz.GLZ_title.text() == '物理单元总结知识点':
                cursor.execute('select * from 物理单元总结知识点 where 序号 = ?', (self.GLZ_columnText,))
                result = cursor.fetchone()
                cursor.execute('update 物理单元总结知识点 set 书名 = ? where 序号 = ?', (self.GLZ_rowText, self.GLZ_columnText))
                cursor.execute('update 物理单元总结知识点 set 所属范围 = ? where 序号 = ?', (self.GLZ_rowMiddleText, self.GLZ_columnText))
                cursor.execute('update 物理单元总结知识点 set 内容 = ? where 序号 = ?',(self.GLZ_rowRightMiddleText, self.GLZ_columnText))
                self.GLZ_HsList = ['改', self.glz.GLZ_title.text(), result[0], result[1], result[2], result[3]]
            elif self.glz.GLZ_title.text() == '物理单元总结例题':
                cursor.execute('select * from 物理单元总结例题 where 序号 = ?', (self.GLZ_columnText,))
                result = cursor.fetchone()
                cursor.execute('update 物理单元总结例题 set 书名 = ? where 序号 = ?', (self.GLZ_rowText, self.GLZ_columnText))
                cursor.execute('update 物理单元总结例题 set 所属范围 = ? where 序号 = ?',(self.GLZ_rowMiddleText, self.GLZ_columnText))
                cursor.execute('update 物理单元总结例题 set 内容 = ? where 序号 = ?',(self.GLZ_rowRightMiddleText, self.GLZ_columnText))
                cursor.execute('update 物理单元总结例题 set 图片地址 = ? where 序号 = ?',(self.GLZ_rowRightRightMiddleText, self.GLZ_columnText))
                self.GLZ_HsList = ['改', self.glz.GLZ_title.text(), result[0], result[1], result[2], result[3],result[4]]
            else:
                pass
            cursor.close()
            conn.commit()
            conn.close()
            self.MESSAGE = Ui_KSFX_Message('通知', '修改成功', '数据更新，您有一次撤销的机会！')
            self.MESSAGE.show()
            self.GLZ_page -= 1
            self.GLZ_RIGHT(False)
        elif self.GLZ_MESSAGE.Answer == 0:
            self.GLZ_MESSAGE.close()
            self.GLZ_message_timer.stop()
        else:
            pass

    def GLZ_BACK(self):
        _translate = QtCore.QCoreApplication.translate
        if self.GLZ_HsList != []:
            conn = sqlite3.connect('C:/Users/Administrator/Desktop/六&七文件夹/副文件/考试复习系统数据.db')
            cursor = conn.cursor()
            if self.GLZ_HsList[0] == '增':
                if self.GLZ_HsList[1] == '背单词':
                    cursor.execute('select * from 背单词 ')
                    result = cursor.fetchall()
                    cursor.execute('delete from 背单词 where 单词序号 = ?', (len(result),))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    self.GLZ_page -= 1
                    self.GLZ_RIGHT()
                elif self.GLZ_HsList[1] == '语文默写古诗文':
                    cursor.execute('select * from 语文默写古诗文 ')
                    result = cursor.fetchall()
                    cursor.execute('delete from 语文默写古诗文 where 序号 = ?', (len(result),))
                    conn.commit()
                    self.GLZ_page -= 1
                    self.GLZ_RIGHT()
                    cursor.close()
                    conn.close()
                elif self.GLZ_HsList[1] == '物理单元总结知识点':
                    cursor.execute('select * from 物理单元总结知识点')
                    result = cursor.fetchall()
                    cursor.execute('delete from 物理单元总结知识点 where 序号 = ?', (len(result),))
                    conn.commit()
                    self.GLZ_page -= 1
                    self.GLZ_RIGHT()
                    cursor.close()
                    conn.close()
                elif self.GLZ_HsList[1] == '物理单元总结例题':
                    cursor.execute('select * from 物理单元总结例题')
                    result = cursor.fetchall()
                    cursor.execute('delete from 物理单元总结例题 where 序号 = ?', (len(result),))
                    conn.commit()
                    self.GLZ_page -= 1
                    self.GLZ_RIGHT()
                    cursor.close()
                    conn.close()
                else:
                    pass
            elif self.GLZ_HsList[0] == '删':
                if self.GLZ_HsList[1] == '背单词':
                    cursor.execute('insert into 背单词 (书名和单元,中文,英文单词,单词序号) values (?,?,?,?)',
                                   (self.GLZ_HsList[2], self.GLZ_HsList[3], self.GLZ_HsList[4], self.GLZ_HsList[5]))
                    conn.commit()
                    self.GLZ_page -= 1
                    self.GLZ_RIGHT()
                elif self.GLZ_HsList[1] == '语文默写古诗文':
                    cursor.execute('insert into 语文默写古诗文 (古诗文诗名,问题,答案,序号) values (?,?,?,?)',
                                   (self.GLZ_HsList[2], self.GLZ_HsList[3], self.GLZ_HsList[4], self.GLZ_HsList[5]))
                    conn.commit()
                    self.GLZ_page -= 1
                    self.GLZ_RIGHT()
                    cursor.close()
                    conn.close()
                elif self.GLZ_HsList[1] == '物理单元总结知识点':
                    cursor.execute('insert into 物理单元总结知识点 (书名,所属范围,内容,序号) values (?,?,?,?)',
                                   (self.GLZ_HsList[2], self.GLZ_HsList[3], self.GLZ_HsList[4], self.GLZ_HsList[5]))
                    conn.commit()
                    self.GLZ_page -= 1
                    self.GLZ_RIGHT()
                    cursor.close()
                    conn.close()
                elif self.GLZ_HsList[1] == '物理单元总结例题':
                    cursor.execute('insert into 物理单元总结例题 (书名,所属范围,内容,图片地址,序号) values (?,?,?,?,?)',
                                   (self.GLZ_HsList[2], self.GLZ_HsList[3], self.GLZ_HsList[4], self.GLZ_HsList[5],self.GLZ_HsList[6]))
                    conn.commit()
                    self.GLZ_page -= 1
                    self.GLZ_RIGHT()
                    cursor.close()
                    conn.close()
                else:
                    pass
            else:  # 改
                if self.GLZ_HsList[1] == '操作数据':
                    cursor.execute('update 操作数据 set 值 = ? where 操作命令 = ? and 账户名 = ? ',
                                   (self.GLZ_HsList[4], self.GLZ_HsList[3], self.GLZ_HsList[2]))
                    conn.commit()
                    self.GLZ_page += 1
                    cursor.close()
                    conn.close()
                    self.GLZ_LEFT()
                elif self.GLZ_HsList[1] == '背单词':
                    cursor.execute('update 背单词 set 书名和单元 = ? where 单词序号 = ?', (self.GLZ_HsList[2], self.GLZ_HsList[5]))
                    cursor.execute('update 背单词 set 中文 = ? where 单词序号 = ?', (self.GLZ_HsList[3], self.GLZ_HsList[5]))
                    cursor.execute('update 背单词 set 英文单词 = ? where 单词序号 = ?', (self.GLZ_HsList[4], self.GLZ_HsList[5]))
                    conn.commit()
                    self.GLZ_page -= 1
                    self.GLZ_RIGHT()
                    cursor.close()
                    conn.close()
                elif self.GLZ_HsList[1] == '语文默写古诗文':
                    cursor.execute('update 语文默写古诗文 set 古诗文诗名 = ? where 序号 = ?',(self.GLZ_HsList[2], self.GLZ_HsList[5]))
                    cursor.execute('update 语文默写古诗文 set 问题 = ? where 序号 = ?', (self.GLZ_HsList[3], self.GLZ_HsList[5]))
                    cursor.execute('update 语文默写古诗文 set 答案 = ? where 序号 = ?', (self.GLZ_HsList[4], self.GLZ_HsList[5]))
                    conn.commit()
                    self.GLZ_page -= 1
                    self.GLZ_RIGHT()
                    cursor.close()
                    conn.close()
                elif self.GLZ_HsList[1] == '物理单元总结知识点':
                    cursor.execute('update 物理单元总结知识点 set 书名 = ? where 序号 = ?',(self.GLZ_HsList[2], self.GLZ_HsList[5]))
                    cursor.execute('update 物理单元总结知识点 set 所属范围 = ? where 序号 = ?', (self.GLZ_HsList[3], self.GLZ_HsList[5]))
                    cursor.execute('update 物理单元总结知识点 set 内容 = ? where 序号 = ?', (self.GLZ_HsList[4], self.GLZ_HsList[5]))
                    conn.commit()
                    self.GLZ_page -= 1
                    self.GLZ_RIGHT()
                    cursor.close()
                    conn.close()
                elif self.GLZ_HsList[1] == '物理单元总结例题':
                    cursor.execute('update 物理单元总结例题 set 书名 = ? where 序号 = ?',(self.GLZ_HsList[2], self.GLZ_HsList[6]))
                    cursor.execute('update 物理单元总结例题 set 所属范围 = ? where 序号 = ?', (self.GLZ_HsList[3], self.GLZ_HsList[6]))
                    cursor.execute('update 物理单元总结例题 set 内容 = ? where 序号 = ?', (self.GLZ_HsList[4], self.GLZ_HsList[6]))
                    cursor.execute('update 物理单元总结例题 set 图片地址 = ? where 序号 = ?', (self.GLZ_HsList[5], self.GLZ_HsList[6]))
                    conn.commit()
                    self.GLZ_page -= 1
                    self.GLZ_RIGHT()
                    cursor.close()
                    conn.close()
                else:
                    pass
        else:
            pass

    def KSgame(self):
        _translate = QtCore.QCoreApplication.translate
        try:
            self.music_timer.stop()
            self.musicplayer.pause()
        except:
            pass
        self.hide()
        self.KS_game = Ui_KS()
        self.KS_BallClear()
        self.KS_game.show()
        self.KS_game.KS_backButton.clicked.connect(self.KS_Back)
        self.KS_game.KS_actionButton.clicked.connect(self.KS_game_Action)
        self.KS_game.KS_questionButton.clicked.connect(self.KS_question)
        self.KS_PlayFrequency = 0

    def KS_Back(self):
        self.KS_game.close()
        self.show()
        if self.bj_music != None:
            if self.bj_music == True:
                self.music_marktime = 0
                self.music_timer = QTimer(self)
                self.music_timer.start(100)
                self.music_timer.timeout.connect(self.Background_Music)
        else:
            pass
        try:
            self.KS_spendTime_timer.stop()
        except :
            pass

    def KS_question(self):
        string1 = '1.开锁是一项智力与运气并存的游戏，玩家需要在七次规定的次数内猜出系统给定的四位数字（无数字意义）\n'
        string2 = '2.红灯即代表您输入的数字中有数字存在于目标秘钥中，但位置不正确\n'
        string3 = '3.红灯即代表您输入的数字中有数字存在于目标秘钥中且位置正确\n'
        string4 = '4.若灯不亮，则表示您输入的数字不存在与目标秘钥中\n'
        string5 = '5.灯的顺序没有意义，与您输入的数字顺序没有直接练习，系统将绿灯优先展示!\n'
        string6 = '6.若一个数字在您的输入中多次存在，若该数字也存在于目标秘钥中，则会有多盏灯亮起！'
        string = string1+string2+string3+string4+string5+string6
        self.MESSAGE = Ui_KSFX_Message('多行通知', '玩法介绍',string)
        self.MESSAGE.show()

    def KS_game_Action(self):
        _translate = QtCore.QCoreApplication.translate
        self.KS_chance  = 1
        self.min = 0
        self.second = 0
        self.KS_answerList = []
        self.KS_inputList = []
        if self.KS_game.KS_actionButton.text() == '再来一局':
            self.KS_BallClear()
        self.KS_game.KS_firstText.setText(_translate("KS", "请输入您的答案："))
        self.KS_game.KS_secondText.setText(_translate("KS", "您的第二次答案："))
        self.KS_game.KS_thirdText.setText(_translate("KS", "您的第三次答案："))
        self.KS_game.KS_fourthText.setText(_translate("KS", "您的第四次答案："))
        self.KS_game.KS_fifthText.setText(_translate("KS", "您的第五次答案："))
        self.KS_game.KS_seventhText.setText(_translate("KS", "您的第七次答案："))
        self.KS_game.KS_sixthText.setText(_translate("KS", "您的第六次答案："))
        self.KS_game.KS_actionButton.setText(_translate("KS", "再来一局"))
        self.KS_game.KS_evaluate.setStyleSheet("color: rgb(0,255,0);")
        try:
            self.KS_spendTime_timer.stop()
        except:
            pass
        self.KS_spendTime_timer = QTimer(self)
        self.KS_spendTime_timer.start(1000)
        self.KS_spendTime_timer.timeout.connect(self.KS_SpendTime_Timerevent)
        one = str(random.randint(0,9))
        two = str(random.randint(0,9))
        three = str(random.randint(0,9))
        four = str(random.randint(0,9))
        self.KS_key = one+two+three+four
        self.KS_answerList.append(one)
        self.KS_answerList.append(two)
        self.KS_answerList.append(three)
        self.KS_answerList.append(four)
        if self.KS_PlayFrequency == 0 :
            self.KS_game.KS_one.clicked.connect(self.KS_oneevent)
            self.KS_game.KS_two.clicked.connect(self.KS_twoevent)
            self.KS_game.KS_three.clicked.connect(self.KS_threeevent)
            self.KS_game.KS_four.clicked.connect(self.KS_fourevent)
            self.KS_game.KS_five.clicked.connect(self.KS_fiveevent)
            self.KS_game.KS_six.clicked.connect(self.KS_sixevent)
            self.KS_game.KS_seven.clicked.connect(self.KS_sevenevent)
            self.KS_game.KS_eight.clicked.connect(self.KS_eightevent)
            self.KS_game.KS_nine.clicked.connect(self.KS_nineevent)
            self.KS_game.KS_zero.clicked.connect(self.KS_zeroevent)
            self.KS_game.KS_deletebutton.clicked.connect(self.KS_deleteButtonevent)
            self.KS_game.KS_SureButton.clicked.connect(self.KS_SureButtonevent)
            self.KS_PlayFrequency = 1




    def KS_SpendTime_Timerevent(self):
        _translate = QtCore.QCoreApplication.translate
        self.second += 1
        if self.second == 60 :
            self.second = 0
            self.min += 1
        string = '用时：'+str(self.min)+'分'+str(self.second)+'秒'
        self.KS_game.KS_spendTime.setText(_translate("KS", string))

    def KS_BallClear(self):
        _translate = QtCore.QCoreApplication.translate
        self.KS_game.ball_1_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_1_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_1_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_1_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_2_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_2_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_2_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_2_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_3_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_3_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_3_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_3_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_4_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_4_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_4_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_4_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_5_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_5_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_5_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_5_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_6_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_6_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_6_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_6_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_7_1.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_7_2.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_7_3.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.ball_7_4.setStyleSheet("background-color: rgb(200, 198, 200);")
        self.KS_game.KS_try1.clear()
        self.KS_game.KS_try2.setText(_translate("KS", ""))
        self.KS_game.KS_try3.setText(_translate("KS", ""))
        self.KS_game.KS_try4.setText(_translate("KS", ""))
        self.KS_game.KS_try5.setText(_translate("KS", ""))
        self.KS_game.KS_try6.setText(_translate("KS", ""))
        self.KS_game.KS_try7.setText(_translate("KS", ""))
        self.KS_game.KS_evaluate.hide()
        self.KS_game.KS_answer.hide()
        self.KS_game.KS_spendTime.setText(_translate("KS", "用时：0分0秒"))
        self.KS_game.KS_one.show()
        self.KS_game.KS_two.show()
        self.KS_game.KS_three.show()
        self.KS_game.KS_four.show()
        self.KS_game.KS_five.show()
        self.KS_game.KS_six.show()
        self.KS_game.KS_seven.show()
        self.KS_game.KS_eight.show()
        self.KS_game.KS_nine.show()
        self.KS_game.KS_zero.show()
        self.KS_game.KS_deletebutton.show()
        self.KS_game.KS_SureButton.show()
        self.KS_game.KS_evaluate.setText(_translate("KS", "恭喜你，成功解开秘钥！"))






    def KS_oneevent(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.KS_inputList) != 4 :
            if self.KS_chance  == 1:
                self.KS_inputList.append('1')
                text = self.KS_game.KS_try1.text() + '1'
                self.KS_game.KS_try1.setText(_translate("KS", text))
            elif self.KS_chance  == 2:
                self.KS_inputList.append('1')
                text = self.KS_game.KS_try2.text() + '1'
                self.KS_game.KS_try2.setText(_translate("KS", text))
            elif self.KS_chance == 3:
                self.KS_inputList.append('1')
                text = self.KS_game.KS_try3.text() + '1'
                self.KS_game.KS_try3.setText(_translate("KS", text))
            elif self.KS_chance == 4:
                self.KS_inputList.append('1')
                text = self.KS_game.KS_try4.text() + '1'
                self.KS_game.KS_try4.setText(_translate("KS", text))
            elif self.KS_chance == 5:
                self.KS_inputList.append('1')
                text = self.KS_game.KS_try5.text() + '1'
                self.KS_game.KS_try5.setText(_translate("KS", text))
            elif self.KS_chance == 6:
                self.KS_inputList.append('1')
                text = self.KS_game.KS_try6.text() + '1'
                self.KS_game.KS_try6.setText(_translate("KS", text))
            elif self.KS_chance == 7:
                self.KS_inputList.append('1')
                text = self.KS_game.KS_try7.text() + '1'
                self.KS_game.KS_try7.setText(_translate("KS", text))

    def KS_twoevent(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.KS_inputList) != 4:
            if self.KS_chance == 1:
                self.KS_inputList.append('2')
                text = self.KS_game.KS_try1.text() + '2'
                self.KS_game.KS_try1.setText(_translate("KS", text))
            elif self.KS_chance == 2:
                self.KS_inputList.append('2')
                text = self.KS_game.KS_try2.text() + '2'
                self.KS_game.KS_try2.setText(_translate("KS", text))
            elif self.KS_chance == 3:
                self.KS_inputList.append('2')
                text = self.KS_game.KS_try3.text() + '2'
                self.KS_game.KS_try3.setText(_translate("KS", text))
            elif self.KS_chance == 4:
                self.KS_inputList.append('2')
                text = self.KS_game.KS_try4.text() + '2'
                self.KS_game.KS_try4.setText(_translate("KS", text))
            elif self.KS_chance == 5:
                self.KS_inputList.append('2')
                text = self.KS_game.KS_try5.text() + '2'
                self.KS_game.KS_try5.setText(_translate("KS", text))
            elif self.KS_chance == 6:
                self.KS_inputList.append('2')
                text = self.KS_game.KS_try6.text() + '2'
                self.KS_game.KS_try6.setText(_translate("KS", text))
            elif self.KS_chance == 7:
                self.KS_inputList.append('2')
                text = self.KS_game.KS_try7.text() + '2'
                self.KS_game.KS_try7.setText(_translate("KS", text))
    def KS_threeevent(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.KS_inputList) != 4:
            if self.KS_chance == 1:
                self.KS_inputList.append('3')
                text = self.KS_game.KS_try1.text() + '3'
                self.KS_game.KS_try1.setText(_translate("KS", text))
            elif self.KS_chance == 2:
                self.KS_inputList.append('3')
                text = self.KS_game.KS_try2.text() + '3'
                self.KS_game.KS_try2.setText(_translate("KS", text))
            elif self.KS_chance == 3:
                self.KS_inputList.append('3')
                text = self.KS_game.KS_try3.text() + '3'
                self.KS_game.KS_try3.setText(_translate("KS", text))
            elif self.KS_chance == 4:
                self.KS_inputList.append('3')
                text = self.KS_game.KS_try4.text() + '3'
                self.KS_game.KS_try4.setText(_translate("KS", text))
            elif self.KS_chance == 5:
                self.KS_inputList.append('3')
                text = self.KS_game.KS_try5.text() + '3'
                self.KS_game.KS_try5.setText(_translate("KS", text))
            elif self.KS_chance == 6:
                self.KS_inputList.append('3')
                text = self.KS_game.KS_try6.text() + '3'
                self.KS_game.KS_try6.setText(_translate("KS", text))
            elif self.KS_chance == 7:
                self.KS_inputList.append('3')
                text = self.KS_game.KS_try7.text() + '3'
                self.KS_game.KS_try7.setText(_translate("KS", text))
    def KS_fourevent(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.KS_inputList) != 4:
            if self.KS_chance == 1:
                self.KS_inputList.append('4')
                text = self.KS_game.KS_try1.text() + '4'
                self.KS_game.KS_try1.setText(_translate("KS", text))
            elif self.KS_chance == 2:
                self.KS_inputList.append('4')
                text = self.KS_game.KS_try2.text() + '4'
                self.KS_game.KS_try2.setText(_translate("KS", text))
            elif self.KS_chance == 3:
                self.KS_inputList.append('4')
                text = self.KS_game.KS_try3.text() + '4'
                self.KS_game.KS_try3.setText(_translate("KS", text))
            elif self.KS_chance == 4:
                self.KS_inputList.append('4')
                text = self.KS_game.KS_try4.text() + '4'
                self.KS_game.KS_try4.setText(_translate("KS", text))
            elif self.KS_chance == 5:
                self.KS_inputList.append('4')
                text = self.KS_game.KS_try5.text() + '4'
                self.KS_game.KS_try5.setText(_translate("KS", text))
            elif self.KS_chance == 6:
                self.KS_inputList.append('4')
                text = self.KS_game.KS_try6.text() + '4'
                self.KS_game.KS_try6.setText(_translate("KS", text))
            elif self.KS_chance == 7:
                self.KS_inputList.append('4')
                text = self.KS_game.KS_try7.text() + '4'
                self.KS_game.KS_try7.setText(_translate("KS", text))
    def KS_fiveevent(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.KS_inputList) != 4:
            if self.KS_chance == 1:
                self.KS_inputList.append('5')
                text = self.KS_game.KS_try1.text() + '5'
                self.KS_game.KS_try1.setText(_translate("KS", text))
            elif self.KS_chance == 2:
                self.KS_inputList.append('5')
                text = self.KS_game.KS_try2.text() + '5'
                self.KS_game.KS_try2.setText(_translate("KS", text))
            elif self.KS_chance == 3:
                self.KS_inputList.append('5')
                text = self.KS_game.KS_try3.text() + '5'
                self.KS_game.KS_try3.setText(_translate("KS", text))
            elif self.KS_chance == 4:
                self.KS_inputList.append('5')
                text = self.KS_game.KS_try4.text() + '5'
                self.KS_game.KS_try4.setText(_translate("KS", text))
            elif self.KS_chance == 5:
                self.KS_inputList.append('5')
                text = self.KS_game.KS_try5.text() + '5'
                self.KS_game.KS_try5.setText(_translate("KS", text))
            elif self.KS_chance == 6:
                self.KS_inputList.append('5')
                text = self.KS_game.KS_try6.text() + '5'
                self.KS_game.KS_try6.setText(_translate("KS", text))
            elif self.KS_chance == 7:
                self.KS_inputList.append('5')
                text = self.KS_game.KS_try7.text() + '5'
                self.KS_game.KS_try7.setText(_translate("KS", text))
    def KS_sixevent(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.KS_inputList) != 4:
            if self.KS_chance == 1:
                self.KS_inputList.append('6')
                text = self.KS_game.KS_try1.text() + '6'
                self.KS_game.KS_try1.setText(_translate("KS", text))
            elif self.KS_chance == 2:
                self.KS_inputList.append('6')
                text = self.KS_game.KS_try2.text() + '6'
                self.KS_game.KS_try2.setText(_translate("KS", text))
            elif self.KS_chance == 3:
                self.KS_inputList.append('6')
                text = self.KS_game.KS_try3.text() + '6'
                self.KS_game.KS_try3.setText(_translate("KS", text))
            elif self.KS_chance == 4:
                self.KS_inputList.append('6')
                text = self.KS_game.KS_try4.text() + '6'
                self.KS_game.KS_try4.setText(_translate("KS", text))
            elif self.KS_chance == 5:
                self.KS_inputList.append('6')
                text = self.KS_game.KS_try5.text() + '6'
                self.KS_game.KS_try5.setText(_translate("KS", text))
            elif self.KS_chance == 6:
                self.KS_inputList.append('6')
                text = self.KS_game.KS_try6.text() + '6'
                self.KS_game.KS_try6.setText(_translate("KS", text))
            elif self.KS_chance == 7:
                self.KS_inputList.append('6')
                text = self.KS_game.KS_try7.text() + '6'
                self.KS_game.KS_try7.setText(_translate("KS", text))
    def KS_sevenevent(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.KS_inputList) != 4:
            if self.KS_chance == 1:
                self.KS_inputList.append('7')
                text = self.KS_game.KS_try1.text() + '7'
                self.KS_game.KS_try1.setText(_translate("KS", text))
            elif self.KS_chance == 2:
                self.KS_inputList.append('7')
                text = self.KS_game.KS_try2.text() + '7'
                self.KS_game.KS_try2.setText(_translate("KS", text))
            elif self.KS_chance == 3:
                self.KS_inputList.append('7')
                text = self.KS_game.KS_try3.text() + '7'
                self.KS_game.KS_try3.setText(_translate("KS", text))
            elif self.KS_chance == 4:
                self.KS_inputList.append('7')
                text = self.KS_game.KS_try4.text() + '7'
                self.KS_game.KS_try4.setText(_translate("KS", text))
            elif self.KS_chance == 5:
                self.KS_inputList.append('7')
                text = self.KS_game.KS_try5.text() + '7'
                self.KS_game.KS_try5.setText(_translate("KS", text))
            elif self.KS_chance == 6:
                self.KS_inputList.append('7')
                text = self.KS_game.KS_try6.text() + '7'
                self.KS_game.KS_try6.setText(_translate("KS", text))
            elif self.KS_chance == 7:
                self.KS_inputList.append('7')
                text = self.KS_game.KS_try7.text() + '7'
                self.KS_game.KS_try7.setText(_translate("KS", text))
    def KS_eightevent(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.KS_inputList) != 4:
            if self.KS_chance == 1:
                self.KS_inputList.append('8')
                text = self.KS_game.KS_try1.text() + '8'
                self.KS_game.KS_try1.setText(_translate("KS", text))
            elif self.KS_chance == 2:
                self.KS_inputList.append('8')
                text = self.KS_game.KS_try2.text() + '8'
                self.KS_game.KS_try2.setText(_translate("KS", text))
            elif self.KS_chance == 3:
                self.KS_inputList.append('8')
                text = self.KS_game.KS_try3.text() + '8'
                self.KS_game.KS_try3.setText(_translate("KS", text))
            elif self.KS_chance == 4:
                self.KS_inputList.append('8')
                text = self.KS_game.KS_try4.text() + '8'
                self.KS_game.KS_try4.setText(_translate("KS", text))
            elif self.KS_chance == 5:
                self.KS_inputList.append('8')
                text = self.KS_game.KS_try5.text() + '8'
                self.KS_game.KS_try5.setText(_translate("KS", text))
            elif self.KS_chance == 6:
                self.KS_inputList.append('8')
                text = self.KS_game.KS_try6.text() + '8'
                self.KS_game.KS_try6.setText(_translate("KS", text))
            elif self.KS_chance == 7:
                self.KS_inputList.append('8')
                text = self.KS_game.KS_try7.text() + '8'
                self.KS_game.KS_try7.setText(_translate("KS", text))
    def KS_nineevent(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.KS_inputList) != 4:
            if self.KS_chance == 1:
                self.KS_inputList.append('9')
                text = self.KS_game.KS_try1.text() + '9'
                self.KS_game.KS_try1.setText(_translate("KS", text))
            elif self.KS_chance == 2:
                self.KS_inputList.append('9')
                text = self.KS_game.KS_try2.text() + '9'
                self.KS_game.KS_try2.setText(_translate("KS", text))
            elif self.KS_chance == 3:
                self.KS_inputList.append('9')
                text = self.KS_game.KS_try3.text() + '9'
                self.KS_game.KS_try3.setText(_translate("KS", text))
            elif self.KS_chance == 4:
                self.KS_inputList.append('9')
                text = self.KS_game.KS_try4.text() + '9'
                self.KS_game.KS_try4.setText(_translate("KS", text))
            elif self.KS_chance == 5:
                self.KS_inputList.append('9')
                text = self.KS_game.KS_try5.text() + '9'
                self.KS_game.KS_try5.setText(_translate("KS", text))
            elif self.KS_chance == 6:
                self.KS_inputList.append('9')
                text = self.KS_game.KS_try6.text() + '9'
                self.KS_game.KS_try6.setText(_translate("KS", text))
            elif self.KS_chance == 7:
                self.KS_inputList.append('9')
                text = self.KS_game.KS_try7.text() + '9'
                self.KS_game.KS_try7.setText(_translate("KS", text))
    def KS_zeroevent(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.KS_inputList) != 4:
            if self.KS_chance == 1:
                self.KS_inputList.append('0')
                text = self.KS_game.KS_try1.text() + '0'
                self.KS_game.KS_try1.setText(_translate("KS", text))
            elif self.KS_chance == 2:
                self.KS_inputList.append('0')
                text = self.KS_game.KS_try2.text() + '0'
                self.KS_game.KS_try2.setText(_translate("KS", text))
            elif self.KS_chance == 3:
                self.KS_inputList.append('0')
                text = self.KS_game.KS_try3.text() + '0'
                self.KS_game.KS_try3.setText(_translate("KS", text))
            elif self.KS_chance == 4:
                self.KS_inputList.append('0')
                text = self.KS_game.KS_try4.text() + '0'
                self.KS_game.KS_try4.setText(_translate("KS", text))
            elif self.KS_chance == 5:
                self.KS_inputList.append('0')
                text = self.KS_game.KS_try5.text() + '0'
                self.KS_game.KS_try5.setText(_translate("KS", text))
            elif self.KS_chance == 6:
                self.KS_inputList.append('0')
                text = self.KS_game.KS_try6.text() + '0'
                self.KS_game.KS_try6.setText(_translate("KS", text))
            elif self.KS_chance == 7:
                self.KS_inputList.append('0')
                text = self.KS_game.KS_try7.text() + '0'
                self.KS_game.KS_try7.setText(_translate("KS", text))

    def KS_deleteButtonevent(self):
        _translate = QtCore.QCoreApplication.translate
        if len(self.KS_inputList) != 0:
            text = ''
            if self.KS_chance == 1:
                del self.KS_inputList[len(self.KS_inputList)-1]
                for i in self.KS_inputList:
                    text += i
                self.KS_game.KS_try1.setText(_translate("KS", text))
            elif self.KS_chance == 2:
                del self.KS_inputList[len(self.KS_inputList )-1]
                for i in self.KS_inputList:
                    text += i
                self.KS_game.KS_try2.setText(_translate("KS", text))
            elif self.KS_chance == 3:
                del self.KS_inputList[len(self.KS_inputList )-1]
                for i in self.KS_inputList:
                    text += i
                self.KS_game.KS_try3.setText(_translate("KS", text))
            elif self.KS_chance == 4:
                del self.KS_inputList[len(self.KS_inputList )-1]
                for i in self.KS_inputList:
                    text += i
                self.KS_game.KS_try4.setText(_translate("KS", text))
            elif self.KS_chance == 5:
                del self.KS_inputList[len(self.KS_inputList )-1]
                for i in self.KS_inputList:
                    text += i
                self.KS_game.KS_try5.setText(_translate("KS", text))
            elif self.KS_chance == 6:
                del self.KS_inputList[len(self.KS_inputList )-1]
                for i in self.KS_inputList:
                    text += i
                self.KS_game.KS_try6.setText(_translate("KS", text))
            elif self.KS_chance == 7:
                del self.KS_inputList[len(self.KS_inputList )-1]
                for i in self.KS_inputList:
                    text += i
                self.KS_game.KS_try7.setText(_translate("KS", text))

    def KS_SureButtonevent(self):
        answer = False
        right = 0
        halfright = 0
        _translate = QtCore.QCoreApplication.translate
        if len(self.KS_inputList) == 4:
            if self.KS_chance == 1:
                text = self.KS_game.KS_try1.text()
                if text == self.KS_key:
                    answer = True
                    self.KS_game.KS_firstText.setText(_translate("KS", "您的第一次答案："))
                else:
                    self.KS_game.KS_firstText.setText(_translate("KS", "您的第一次答案："))
                    self.KS_game.KS_secondText.setText(_translate("KS", "请输入您的答案："))
            elif self.KS_chance == 2:
                text = self.KS_game.KS_try2.text()
                if text == self.KS_key:
                    answer = True
                    self.KS_game.KS_secondText.setText(_translate("KS", "您的第二次答案："))
                else:
                    self.KS_game.KS_secondText.setText(_translate("KS", "您的第二次答案："))
                    self.KS_game.KS_thirdText.setText(_translate("KS", "请输入您的答案："))
            elif self.KS_chance == 3:
                text = self.KS_game.KS_try3.text()
                if text == self.KS_key:
                    answer = True
                    self.KS_game.KS_thirdText.setText(_translate("KS", "您的第三次答案："))
                else:
                    self.KS_game.KS_thirdText.setText(_translate("KS", "您的第三次答案："))
                    self.KS_game.KS_fourthText.setText(_translate("KS", "请输入您的答案："))
            elif self.KS_chance == 4:
                text = self.KS_game.KS_try4.text()
                if text == self.KS_key:
                    answer = True
                    self.KS_game.KS_fourthText.setText(_translate("KS", "您的第四次答案："))
                else:
                    self.KS_game.KS_fourthText.setText(_translate("KS", "您的第四次答案："))
                    self.KS_game.KS_fifthText.setText(_translate("KS", "请输入您的答案："))
            elif self.KS_chance == 5:
                text = self.KS_game.KS_try5.text()
                if text == self.KS_key:
                    answer = True
                    self.KS_game.KS_fifthText.setText(_translate("KS", "您的第五次答案："))
                else:
                    self.KS_game.KS_fifthText.setText(_translate("KS", "您的第五次答案："))
                    self.KS_game.KS_sixthText.setText(_translate("KS", "请输入您的答案："))
            elif self.KS_chance == 6:
                text = self.KS_game.KS_try6.text()
                if text == self.KS_key:
                    answer = True
                    self.KS_game.KS_sixthText.setText(_translate("KS", "您的第六次答案："))
                else:
                    self.KS_game.KS_sixthText.setText(_translate("KS", "您的第六次答案："))
                    self.KS_game.KS_seventhText.setText(_translate("KS", "请输入您的答案："))
            elif self.KS_chance == 7:
                text = self.KS_game.KS_try7.text()
                if text == self.KS_key:
                    answer = True
                else:
                    pass
                self.KS_game.KS_seventhText.setText(_translate("KS", "您的第七次答案："))
            else:
                pass
            if answer == True:
                self.KS_game.KS_answer.setText(_translate("KS", "正确答案："+self.KS_key))
                self.KS_game.KS_one.hide()
                self.KS_game.KS_two.hide()
                self.KS_game.KS_three.hide()
                self.KS_game.KS_four.hide()
                self.KS_game.KS_five.hide()
                self.KS_game.KS_six.hide()
                self.KS_game.KS_seven.hide()
                self.KS_game.KS_eight.hide()
                self.KS_game.KS_nine.hide()
                self.KS_game.KS_zero.hide()
                self.KS_game.KS_deletebutton.hide()
                self.KS_game.KS_SureButton.hide()
                self.KS_game.KS_evaluate.show()
                self.KS_game.KS_answer.show()
                self.KS_spendTime_timer.stop()
                if self.KS_chance == 1:
                    self.KS_game.ball_1_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_1_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_1_3.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_1_4.setStyleSheet("background-color: rgb(0, 255, 0);")
                elif self.KS_chance == 2:
                    self.KS_game.ball_2_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_2_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_2_3.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_2_4.setStyleSheet("background-color: rgb(0, 255, 0);")
                elif self.KS_chance == 3:
                    self.KS_game.ball_3_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_3_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_3_3.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_3_4.setStyleSheet("background-color: rgb(0, 255, 0);")
                elif self.KS_chance == 4 :
                    self.KS_game.ball_4_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_4_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_4_3.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_4_4.setStyleSheet("background-color: rgb(0, 255, 0);")
                elif self.KS_chance == 5:
                    self.KS_game.ball_5_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_5_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_5_3.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_5_4.setStyleSheet("background-color: rgb(0, 255, 0);")
                elif self.KS_chance == 6:
                    self.KS_game.ball_6_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_6_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_6_3.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_6_4.setStyleSheet("background-color: rgb(0, 255, 0);")
                elif self.KS_chance == 7:
                    self.KS_game.ball_7_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_7_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_7_3.setStyleSheet("background-color: rgb(0, 255, 0);")
                    self.KS_game.ball_7_4.setStyleSheet("background-color: rgb(0, 255, 0);")
            elif answer == False and self.KS_chance != 7:
                index = 0
                for i in self.KS_inputList :
                    if i in self.KS_answerList :
                        if self.KS_answerList[index] == i :
                            right += 1
                        else:
                            halfright += 1
                    index += 1
                if self.KS_chance == 1:
                    if right != 0:
                        for i in range(right):
                            if i == 0 :
                                self.KS_game.ball_1_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                            elif i == 1:
                                self.KS_game.ball_1_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                            elif i == 2 :
                                self.KS_game.ball_1_3.setStyleSheet("background-color: rgb(0, 255 , 0);")
                            else:
                                pass
                    else:
                        i = -1
                    if halfright != 0 :
                        for p in range(halfright):
                            if i == -1 :
                                self.KS_game.ball_1_1.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            elif i == 0 :
                                self.KS_game.ball_1_2.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            elif i == 1 :
                                self.KS_game.ball_1_3.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            else:
                                self.KS_game.ball_1_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                elif self.KS_chance == 2 :
                    if right != 0:
                        for i in range(right):
                            if i == 0 :
                                self.KS_game.ball_2_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                            elif i == 1:
                                self.KS_game.ball_2_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                            elif i == 2 :
                                self.KS_game.ball_2_3.setStyleSheet("background-color: rgb(0, 255 , 0);")
                            else:
                                pass
                    else:
                        i = -1
                    if halfright != 0 :
                        for p in range(halfright):
                            if i == -1 :
                                self.KS_game.ball_2_1.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            elif i == 0 :
                                self.KS_game.ball_2_2.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            elif i == 1 :
                                self.KS_game.ball_2_3.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            else:
                                self.KS_game.ball_2_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                elif self.KS_chance == 3 :
                    if right != 0:
                        for i in range(right):
                            if i == 0 :
                                self.KS_game.ball_3_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                            elif i == 1:
                                self.KS_game.ball_3_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                            elif i == 2 :
                                self.KS_game.ball_3_3.setStyleSheet("background-color: rgb(0, 255 , 0);")
                            else:
                                pass
                    else:
                        i = -1
                    if halfright != 0 :
                        for p in range(halfright):
                            if i == -1 :
                                self.KS_game.ball_3_1.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            elif i == 0 :
                                self.KS_game.ball_3_2.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            elif i == 1 :
                                self.KS_game.ball_3_3.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            else:
                                self.KS_game.ball_3_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                elif self.KS_chance == 4 :
                    if right != 0:
                        for i in range(right):
                            if i == 0:
                                self.KS_game.ball_4_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                            elif i == 1:
                                self.KS_game.ball_4_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                            elif i == 2:
                                self.KS_game.ball_4_3.setStyleSheet("background-color: rgb(0, 255 , 0);")
                            else:
                                pass
                    else:
                        i = -1
                    if halfright != 0:
                        for p in range(halfright):
                            if i == -1:
                                self.KS_game.ball_4_1.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            elif i == 0:
                                self.KS_game.ball_4_2.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            elif i == 1:
                                self.KS_game.ball_4_3.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            else:
                                self.KS_game.ball_4_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                elif self.KS_chance == 5:
                    if right != 0:
                        for i in range(right):
                            if i == 0:
                                self.KS_game.ball_5_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                            elif i == 1:
                                self.KS_game.ball_5_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                            elif i == 2:
                                self.KS_game.ball_5_3.setStyleSheet("background-color: rgb(0, 255 , 0);")
                            else:
                                pass
                    else:
                        i = -1
                    if halfright != 0:
                        for p in range(halfright):
                            if i == -1:
                                self.KS_game.ball_5_1.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            elif i == 0:
                                self.KS_game.ball_5_2.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            elif i == 1:
                                self.KS_game.ball_5_3.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            else:
                                self.KS_game.ball_5_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                elif self.KS_chance == 6:
                    if right != 0:
                        for i in range(right):
                            if i == 0:
                                self.KS_game.ball_6_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                            elif i == 1:
                                self.KS_game.ball_6_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                            elif i == 2:
                                self.KS_game.ball_6_3.setStyleSheet("background-color: rgb(0, 255 , 0);")
                            else:
                                pass
                    else:
                        i = -1
                    if halfright != 0:
                        for p in range(halfright):
                            if i == -1:
                                self.KS_game.ball_6_1.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            elif i == 0:
                                self.KS_game.ball_6_2.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            elif i == 1:
                                self.KS_game.ball_6_3.setStyleSheet("background-color: rgb(255, 0, 0);")
                                i += 1
                            else:
                                self.KS_game.ball_6_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.KS_inputList = []
                self.KS_chance += 1
            else:
                index = 0
                for i in self.KS_inputList:
                    if i in self.KS_answerList:
                        if self.KS_answerList[index] == i:
                            right += 1
                        else:
                            halfright += 1
                    index += 1
                if right != 0:
                    for i in range(right):
                        if i == 0 :
                            self.KS_game.ball_7_1.setStyleSheet("background-color: rgb(0, 255, 0);")
                        elif i == 1:
                            self.KS_game.ball_7_2.setStyleSheet("background-color: rgb(0, 255, 0);")
                        elif i == 2 :
                            self.KS_game.ball_7_3.setStyleSheet("background-color: rgb(0, 255 , 0);")
                        else:
                            pass
                else:
                    i == -1
                if halfright != 0 :
                    for p in range(halfright):
                        if i == -1 :
                            self.KS_game.ball_7_1.setStyleSheet("background-color: rgb(255, 0, 0);")
                            i += 1
                        elif i == 0 :
                            self.KS_game.ball_7_2.setStyleSheet("background-color: rgb(255, 0, 0);")
                            i += 1
                        elif i == 1 :
                            self.KS_game.ball_7_3.setStyleSheet("background-color: rgb(255, 0, 0);")
                            i += 1
                        else:
                            self.KS_game.ball_7_4.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.KS_game.KS_evaluate.setStyleSheet("color: rgb(255,0,0);")
                self.KS_game.KS_evaluate.setText(_translate("KS", "失败了！，再试一次吧！"))
                self.KS_game.KS_answer.setText(_translate("KS", "正确答案：" + self.KS_key))
                self.KS_game.KS_one.hide()
                self.KS_game.KS_two.hide()
                self.KS_game.KS_three.hide()
                self.KS_game.KS_four.hide()
                self.KS_game.KS_five.hide()
                self.KS_game.KS_six.hide()
                self.KS_game.KS_seven.hide()
                self.KS_game.KS_eight.hide()
                self.KS_game.KS_nine.hide()
                self.KS_game.KS_zero.hide()
                self.KS_game.KS_deletebutton.hide()
                self.KS_game.KS_SureButton.hide()
                self.KS_game.KS_evaluate.show()
                self.KS_game.KS_answer.show()
                self.KS_spendTime_timer.stop()
        else:
            pass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Home = Homepages()
    if Home.DB == 0:
        Home.show()
    sys.exit(app.exec_())
