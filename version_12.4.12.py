#具体的登录窗口控件self.widget
#功能按键具体窗口self.widget1
#查询页面内容self.widget2
# 更新页面内容self.widget3

import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QAbstractItemView, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets

import Data_quary
import Func_Login
import oper_database


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.widget_mainpage.hide()
        self.widget_quary.hide()
        self.widget_updata.hide()
        self.widget_analyse.hide()
        self.widget_predict.hide()


    def setupUi(self, MainWindow):
        #app窗口设置，名字设置，大小固定不可变，
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1114, 859)
        MainWindow.setMinimumSize(QtCore.QSize(1114, 859))
        MainWindow.setMaximumSize(QtCore.QSize(1114, 859))
        #定义主窗口
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # size策略
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        #主窗口大小固定
        self.centralwidget.setMinimumSize(QtCore.QSize(1114, 834))
        self.centralwidget.setMaximumSize(QtCore.QSize(1114, 834))
        self.centralwidget.setObjectName("centralwidget")
 #登录窗口
        self.widget_login = QtWidgets.QWidget(self.centralwidget)
        #QtCore.QRect(340, 240, 411, 231)定义矩形
        self.widget_login.setGeometry(QtCore.QRect(340, 240, 411, 231))
        self.widget_login.setObjectName("widget_login")
        #具体的登录窗口控件self.widget
        self.widget = QtWidgets.QWidget(self.widget_login)
        self.widget.setGeometry(QtCore.QRect(80, 70, 252, 86))
        self.widget.setObjectName("widget")
        #登录表单控件
        self.formLayout_login = QtWidgets.QFormLayout(self.widget)

        #设置左侧、顶部、右侧和底部边距
        self.formLayout_login.setContentsMargins(0, 0, 0, 0)

        self.formLayout_login.setObjectName("formLayout_login")
        self.label_id = QtWidgets.QLabel(self.widget)
        self.label_id.setObjectName("label_id")
        #
        self.formLayout_login.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_id)
        self.lineEdit_id = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.lineEdit_id.setText('sdut001')
        #
        self.formLayout_login.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_id)
        self.label_pwd = QtWidgets.QLabel(self.widget)
        self.label_pwd.setObjectName("label_pwd")
        #
        self.formLayout_login.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_pwd)
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        #
        self.formLayout_login.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_pwd)
        self.pushButton_login = QtWidgets.QPushButton(self.widget)
        self.pushButton_login.setObjectName("pushButton_login")
        #
        self.formLayout_login.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.pushButton_login)

        #设置输入提示
        self.lineEdit_id.setPlaceholderText('字母或数字组合')
        self.lineEdit_pwd.setPlaceholderText('字母或数字组合')

        # 设置密码回显模式
        self.lineEdit_pwd.setEchoMode(2)

        # 设置输入只能是字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        self.lineEdit_id.setValidator(validator)  # 只能输入字符或者数字
        self.lineEdit_pwd.setValidator(validator)

        #登录按钮信号连接
        self.pushButton_login.clicked.connect(self.on_pushButton_login_clicked)

#功能窗口
        self.widget_mainpage = QtWidgets.QWidget(self.centralwidget)
        self.widget_mainpage.setGeometry(QtCore.QRect(10, 10, 1091, 821))
        self.widget_mainpage.setObjectName("widget_mainpage")
        #功能按键具体窗口self.widget1
        self.widget1 = QtWidgets.QWidget(self.widget_mainpage)
        self.widget1.setGeometry(QtCore.QRect(30, 20, 1031, 30))
        self.widget1.setObjectName("widget1")
        #功能按键水平控件
        self.HLayout_func = QtWidgets.QHBoxLayout(self.widget1)
        #设置左侧、顶部、右侧和底部边距
        self.HLayout_func.setContentsMargins(0, 0, 0, 0)
        self.HLayout_func.setObjectName("HLayout_func")
        #功能按键设置
        self.pushButton_mainpage = QtWidgets.QPushButton(self.widget1)
        self.pushButton_mainpage.setObjectName("pushButton_mainpage")
        self.HLayout_func.addWidget(self.pushButton_mainpage)
        #切换到主页
        self.pushButton_login.clicked.connect(self.on_pushButton_login_clicked)

        self.pushButton_quary = QtWidgets.QPushButton(self.widget1)
        self.pushButton_quary.setObjectName("pushButton_quary")
        self.HLayout_func.addWidget(self.pushButton_quary)
        # 切换到查询
        self.pushButton_quary.clicked.connect(self.on_pushButton_quary_clicked)

        self.pushButton_updata = QtWidgets.QPushButton(self.widget1)
        self.pushButton_updata.setObjectName("pushButton_updata")
        self.HLayout_func.addWidget(self.pushButton_updata)
        # 切换到更新
        self.pushButton_updata.clicked.connect(self.on_pushButton_updata_clicked)

        self.pushButton_analyse = QtWidgets.QPushButton(self.widget1)
        self.pushButton_analyse.setObjectName("pushButton_analyse")
        self.HLayout_func.addWidget(self.pushButton_analyse)
        # 切换到分析
        self.pushButton_analyse.clicked.connect(self.on_pushButton_analyse_clicked)

        self.pushButton_predict = QtWidgets.QPushButton(self.widget1)
        self.pushButton_predict.setObjectName("pushButton_predict")
        self.HLayout_func.addWidget(self.pushButton_predict)
        # 切换到预测
        self.pushButton_predict.clicked.connect(self.on_pushButton_predict_clicked)

        self.pushButton_signout = QtWidgets.QPushButton(self.widget1)
        self.pushButton_signout.setObjectName("pushButton_signout")
        self.HLayout_func.addWidget(self.pushButton_signout)
        self.pushButton_signout.clicked.connect(self.on_pushButton_signout_clicked)

        #设置重合的四个功能显示widget和主页显示widget

#设置主页widget
        self.widget_mainshow = QtWidgets.QWidget(self.widget_mainpage)
        self.widget_mainshow .setGeometry(QtCore.QRect(30, 70, 1031, 731))
        self.widget_mainshow .setMinimumSize(QtCore.QSize(1031, 731))
        self.widget_mainshow .setMaximumSize(QtCore.QSize(1031, 731))
        self.widget_mainshow .setObjectName("widget_quary")
        #主页内容设置
        self.pushButton_mainenter = QtWidgets.QPushButton(self.widget_mainshow)
        self.pushButton_mainenter.setGeometry(QtCore.QRect(420, 110, 93, 28))
        self.pushButton_mainenter.setObjectName("pushButton_mainenter")

#信息查询widget
        self.widget_quary = QtWidgets.QWidget(self.widget_mainpage)
        self.widget_quary.setGeometry(QtCore.QRect(30, 70, 1031, 731))
        self.widget_quary.setMinimumSize(QtCore.QSize(1031, 731))
        self.widget_quary.setMaximumSize(QtCore.QSize(1031, 731))
        self.widget_quary.setObjectName("widget_quary")
        #信息查询widget内容
        self.widget2 = QtWidgets.QWidget(self.widget_quary)
        self.widget2.setGeometry(QtCore.QRect(10, 6, 1011, 721))
        self.widget2.setObjectName("widget2")
        #水平布局，左边查询城市、起始终止时间等，右边为表格控件
        self.HLayout_quary = QtWidgets.QHBoxLayout(self.widget2)
        self.HLayout_quary.setContentsMargins(0, 0, 0, 0)
        self.HLayout_quary.setObjectName("HLayout_quary")
        #垂直布局，查询城市、起始终止时间、查询按钮
        self.VLayout_quary = QtWidgets.QVBoxLayout()
        self.VLayout_quary.setContentsMargins(-1, 20, 15, 550)
        self.VLayout_quary.setSpacing(7)
        self.VLayout_quary.setObjectName("VLayout_quary")
        #表单布局，查询条件组合
        self.FLayout_quary = QtWidgets.QFormLayout()
        self.FLayout_quary.setObjectName("FLayout_quary")

        #查询条件控件设置（左半部分垂直布局中）
        self.label_city = QtWidgets.QLabel(self.widget2)
        self.label_city.setObjectName("label_city")
        self.FLayout_quary.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_city)
        #城市选择下拉框
        self.comboBox_city = QtWidgets.QComboBox(self.widget2)
        self.comboBox_city.setObjectName("comboBox_city")
        self.FLayout_quary.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_city)
        #下拉框添加城市 311淄博城区、811高青、936桓台、1281临淄、2087沂源、2347淄川、2348博山、2349周村
        self.comboBox_city.addItems(['张店区311', '高青县811', '桓台县936', '临淄区1281', '沂源县2087', '淄川区2347', '博山区2348', '周村区2349'])

        self.label_start = QtWidgets.QLabel(self.widget2)
        self.label_start.setObjectName("label_start")
        self.FLayout_quary.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_start)
        # 起始时间
        self.dateEdit_start = QtWidgets.QDateEdit(self.widget2)
        self.dateEdit_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_start.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.FLayout_quary.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateEdit_start)

        self.label_end = QtWidgets.QLabel(self.widget2)
        self.label_end.setObjectName("label_end")
        self.FLayout_quary.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_end)
        # 终止时间
        self.dateEdit_end = QtWidgets.QDateEdit(self.widget2)
        self.dateEdit_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_end.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_end.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.FLayout_quary.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit_end)
        self.VLayout_quary.addLayout(self.FLayout_quary)
        #查询按钮
        self.pushButton_quaryone = QtWidgets.QPushButton(self.widget2)
        self.pushButton_quaryone.setObjectName("pushButton_quaryone")
        self.VLayout_quary.addWidget(self.pushButton_quaryone)
        self.pushButton_quaryone.clicked.connect(self.on_pushButton_quaryone_clicked)

        self.pushButton_quarymany = QtWidgets.QPushButton(self.widget2)
        self.pushButton_quarymany.setObjectName("pushButton_quarymany")
        self.VLayout_quary.addWidget(self.pushButton_quarymany)
        self.pushButton_quarymany.clicked.connect(self.on_pushButton_quarymany_clicked)

        #左侧垂直布局加入整体水平布局
        self.HLayout_quary.addLayout(self.VLayout_quary)

        #分割线水平布局左右分割
        self.line_quary = QtWidgets.QFrame(self.widget2)
        self.line_quary.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_quary.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_quary.setObjectName("line_quary")
        self.HLayout_quary.addWidget(self.line_quary)

        #右侧表格显示数据控件
        self.tableWidget_quary = QtWidgets.QTableWidget(self.widget2)
        self.tableWidget_quary.setMinimumSize(QtCore.QSize(780, 680))
        self.tableWidget_quary.setMaximumSize(QtCore.QSize(780, 680))
        self.tableWidget_quary.setObjectName("tableWidget_quary")
        #列宽自动调整
        self.tableWidget_quary.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        #设置行列数
        self.tableWidget_quary.setColumnCount(0)
        self.tableWidget_quary.setRowCount(0)
        self.HLayout_quary.addWidget(self.tableWidget_quary)


#更新页面widget
        self.widget_updata = QtWidgets.QWidget(self.widget_mainpage)
        self.widget_updata.setEnabled(True)
        self.widget_updata.setGeometry(QtCore.QRect(30, 70, 1031, 731))
        self.widget_updata.setMinimumSize(QtCore.QSize(1031, 731))
        self.widget_updata.setMaximumSize(QtCore.QSize(1031, 731))
        self.widget_updata.setObjectName("widget_updata")
        #具体的更新widget
        self.widget3 = QtWidgets.QWidget(self.widget_updata)
        self.widget3.setGeometry(QtCore.QRect(330, 110, 373, 558))
        self.widget3.setObjectName("widget3")
        # 垂直布局
        self.VLayout_updata = QtWidgets.QVBoxLayout(self.widget3)
        self.VLayout_updata.setContentsMargins(0, 0, 0, 0)
        self.VLayout_updata.setObjectName("VLayout_updata")
        # 按钮和显示标签
        self.pushButton_updataenter = QtWidgets.QPushButton(self.widget3)
        self.pushButton_updataenter.setObjectName("pushButton_updataenter")
        self.VLayout_updata.addWidget(self.pushButton_updataenter)
        self.pushButton_updataenter.clicked.connect(self.on_pushButton_updataenter_clicked)

        self.label_db_datetime = QtWidgets.QLabel(self.widget3)
        self.label_db_datetime.setObjectName("label_db_datetime")
        self.VLayout_updata.addWidget(self.label_db_datetime)

        self.line_updata1 = QtWidgets.QFrame(self.widget3)
        self.line_updata1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_updata1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_updata1.setObjectName("line_updata1")
        self.VLayout_updata.addWidget(self.line_updata1)

        self.label_newtime = QtWidgets.QLabel(self.widget3)
        self.label_newtime.setObjectName("label_newtime")
        self.VLayout_updata.addWidget(self.label_newtime)

        self.line_updata2 = QtWidgets.QFrame(self.widget3)
        self.line_updata2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_updata2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_updata2.setObjectName("line_updata2")
        self.VLayout_updata.addWidget(self.line_updata2)

        self.label_counttip = QtWidgets.QLabel(self.widget3)
        self.label_counttip.setObjectName("label_counttip")
        self.VLayout_updata.addWidget(self.label_counttip)



#分析widget
        self.widget_analyse = QtWidgets.QWidget(self.widget_mainpage)
        self.widget_analyse.setGeometry(QtCore.QRect(30, 70, 1031, 731))
        self.widget_analyse.setMinimumSize(QtCore.QSize(1031, 731))
        self.widget_analyse.setMaximumSize(QtCore.QSize(1031, 731))
        self.widget_analyse.setObjectName("widget_analyse")

        self.pushButton_analyseenter = QtWidgets.QPushButton(self.widget_analyse)
        self.pushButton_analyseenter.setGeometry(QtCore.QRect(420, 110, 93, 28))
        self.pushButton_analyseenter.setObjectName("pushButton_analyseenter")
#预测widget
        self.widget_predict = QtWidgets.QWidget(self.widget_mainpage)
        self.widget_predict.setGeometry(QtCore.QRect(30, 70, 1031, 731))
        self.widget_predict.setMinimumSize(QtCore.QSize(1031, 731))
        self.widget_predict.setMaximumSize(QtCore.QSize(1031, 731))
        self.widget_predict.setObjectName("widget_predict")

        self.pushButton_predictenter = QtWidgets.QPushButton(self.widget_predict)
        self.pushButton_predictenter.setGeometry(QtCore.QRect(420, 110, 93, 28))
        self.pushButton_predictenter.setObjectName("pushButton_predictenter")

        #分割线，上方按钮和下方显示区
        self.line_func = QtWidgets.QFrame(self.widget_mainpage)
        self.line_func.setGeometry(QtCore.QRect(30, 56, 1031, 20))
        self.line_func.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_func.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_func.setObjectName("line_func")

        #设置中心窗口
        MainWindow.setCentralWidget(self.centralwidget)
        # 设置状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusBar().showMessage("欢迎使用")

        #功能按键设置
        self.retranslateUi(MainWindow)

        #其作用是如其名称一样，用来将QObject 里的子孙QObject的某些信号按照其objectName连接到相应的槽上
        # QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        #件需要运行在不同的语言环境下时，我们要针对特定的语言环境来改变界面显示
        _translate = QtCore.QCoreApplication.translate
        #
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #
        self.label_id.setText(_translate("MainWindow", "帐号："))
        self.label_pwd.setText(_translate("MainWindow", "密码："))
        self.pushButton_login.setText(_translate("MainWindow", "登录"))
        self.pushButton_mainpage.setText(_translate("MainWindow", "主页"))
        self.pushButton_quary.setText(_translate("MainWindow", "数据查询"))
        self.pushButton_updata.setText(_translate("MainWindow", "数据更新"))
        self.pushButton_analyse.setText(_translate("MainWindow", "气象分析"))
        self.pushButton_predict.setText(_translate("MainWindow", "气象预测"))
        self.pushButton_signout.setText(_translate("MainWindow", "退出登录"))

        self.pushButton_mainenter.setText(_translate("MainWindow", "主页"))
        self.label_city.setText(_translate("MainWindow", "城市选择："))
        self.label_start.setText(_translate("MainWindow", "起始时间："))
        self.label_end.setText(_translate("MainWindow", "结束时间："))
        self.pushButton_quaryone.setText(_translate("MainWindow", "查询起始日单日"))
        self.pushButton_quarymany.setText(_translate("MainWindow", "查询起止日期多日"))
        self.pushButton_analyseenter.setText(_translate("MainWindow", "分析"))
        self.pushButton_predictenter.setText(_translate("MainWindow", "预测"))

        self.pushButton_updataenter.setText(_translate("MainWindow", "更新"))
        self.label_db_datetime.setText(_translate("MainWindow", "更新前数据库截止日期为："))
        self.label_newtime.setText(_translate("MainWindow", "更新后数据库截止日期为："))
        self.label_counttip.setText(_translate("MainWindow", "数据更新条数："))

    #登录验证
    def on_pushButton_login_clicked(self):
        username=self.lineEdit_id.text()
        password=self.lineEdit_pwd.text()
        fl=Func_Login.Func_Login()
        flag=fl.Login(username,password)
        if flag == 0:
            QMessageBox.critical(self, 'ERROR', '帐号或密码不能为空')
        elif flag == 1:
            message="当前用户："+self.lineEdit_id.text()
            self.statusBar().showMessage(message)
            self.widget_login.hide()
            self.widget_mainpage.show()
        elif flag == -1:
            QMessageBox.critical(self,'ERROR','密码错误')
        elif flag == 2:
            QMessageBox.critical(self.centralwidget, 'ERROR', '账户不存在')
        else:
            QMessageBox.critical(self, 'ERROR', '数据库连接异常')

    #退出登录
    def on_pushButton_signout_clicked(self):
        self.lineEdit_pwd.setText('')
        self.statusBar().showMessage("欢迎使用")
        # 窗口
        self.widget_login.show()
        self.widget_mainpage.hide()

    #点击主页按钮
    def on_pushButton_mainpage_clicked(self):
        self.widget_mainshow.show()
        self.widget_quary.hide()
        self.widget_updata.hide()
        self.widget_analyse.hide()
        self.widget_predict.hide()
    # 点击查询按钮
    def on_pushButton_quary_clicked(self):
        self.widget_mainshow.hide()
        self.widget_quary.show()
        self.widget_updata.hide()
        self.widget_analyse.hide()
        self.widget_predict.hide()
    # 点击更新按钮
    def on_pushButton_updata_clicked(self):
        self.widget_mainshow.hide()
        self.widget_quary.hide()
        self.widget_updata.show()
        self.widget_analyse.hide()
        self.widget_predict.hide()
    # 点击分析按钮
    def on_pushButton_analyse_clicked(self):
        self.widget_mainshow.hide()
        self.widget_quary.hide()
        self.widget_updata.hide()
        self.widget_analyse.show()
        self.widget_predict.hide()
    # 点击预测按钮
    def on_pushButton_predict_clicked(self):
        self.widget_mainshow.hide()
        self.widget_quary.hide()
        self.widget_updata.hide()
        self.widget_analyse.hide()
        self.widget_predict.show()

    #点击查询单天天气数据
    def on_pushButton_quaryone_clicked(self):
        self.tableWidget_quary.setColumnCount(7)
        self.tableWidget_quary.setHorizontalHeaderLabels(['时间', '天气状况', '温度', '湿度', '空气质量', '风向', '风力等级'])
        #设置时间列宽
        self.tableWidget_quary.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        #获取下拉框选择的城市并去掉汉字名称，只留下代号
        city=self.comboBox_city.currentText()[3:]
        #获取起始日期和终止日期，并转换格式
        startdate=self.dateEdit_start.date().toString("yyyy-MM-dd")
        #查询start当天数据
        dq = Data_quary.Data_Quary()
        onedata = dq.Quary_one(city, startdate)
        if onedata == 0:
            QMessageBox.critical(self, 'ERROR', '数据库无此数据')
        elif onedata == -1:
            QMessageBox.critical(self, 'ERROR', '数据库连接异常')
        else:
            self.tableWidget_quary.setRowCount(len(onedata))
            for index, item in enumerate(onedata):
                timeItem = QTableWidgetItem(item[0])
                self.tableWidget_quary.setItem(index, 0, timeItem)
                weaItem = QTableWidgetItem(item[1])
                self.tableWidget_quary.setItem(index, 1, weaItem)
                tempItem = QTableWidgetItem(str(item[2]))
                self.tableWidget_quary.setItem(index, 2, tempItem)
                humItem = QTableWidgetItem(item[3])
                self.tableWidget_quary.setItem(index, 3, humItem)
                aqiItem = QTableWidgetItem(item[4])
                self.tableWidget_quary.setItem(index, 4, aqiItem)
                windItem = QTableWidgetItem(item[5])
                self.tableWidget_quary.setItem(index, 5, windItem)
                levelItem = QTableWidgetItem(item[6])
                self.tableWidget_quary.setItem(index, 6, levelItem)
                # 禁止编辑
                self.tableWidget_quary.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # 点击查询多天天气数据
    def on_pushButton_quarymany_clicked(self):
        self.tableWidget_quary.setColumnCount(4)
        self.tableWidget_quary.setHorizontalHeaderLabels(['日期', '天气状况', '最高温度', '最低温度'])

        # 获取下拉框选择的城市并去掉汉字名称，只留下代号
        city = self.comboBox_city.currentText()[3:]
        # 获取起始日期和终止日期，并转换格式
        startdate = self.dateEdit_start.date().toString("yyyy-MM-dd")
        enddate=self.dateEdit_end.date().toString("yyyy-MM-dd")
        # 查询多天数据
        dq = Data_quary.Data_Quary()
        manydata = dq.Quary_many(city,startdate,enddate)
        if manydata == 0:
            QMessageBox.critical(self, 'ERROR', '数据库无此数据')
        elif manydata == -1:
            QMessageBox.critical(self, 'ERROR', '数据库连接异常')
        else:
            # print(manydata)
            self.tableWidget_quary.setRowCount(len(manydata))
            for index, item in enumerate(manydata):
                timeItem = QTableWidgetItem(item['date'])
                self.tableWidget_quary.setItem(index, 0, timeItem)
                weaItem = QTableWidgetItem(item['weather'])
                self.tableWidget_quary.setItem(index, 1, weaItem)
                maxtempItem = QTableWidgetItem(item['max'])
                self.tableWidget_quary.setItem(index, 2, maxtempItem)
                mintempItem = QTableWidgetItem(item['min'])
                self.tableWidget_quary.setItem(index, 3, mintempItem)
                # 禁止编辑
                self.tableWidget_quary.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def on_pushButton_updataenter_clicked(self):
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            data=dc.UpdateWeaData()
            if data == -1:
                QMessageBox.critical(self, 'ERROR', 'API Error')
            elif data == 0:
                QMessageBox.critical(self, 'ERROR', 'Limit Error')
            else:
                # print(data)
                self.label_db_datetime.setText("更新前数据库截止日期为："+data[0])
                self.label_newtime.setText("更新后数据库截止日期为："+data[2])
                self.label_counttip.setText("数据更新条数："+data[1])

        else:
            QMessageBox.critical(self, 'ERROR', '数据库连接异常')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('GUI/image/logo.jpg'))
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec())






