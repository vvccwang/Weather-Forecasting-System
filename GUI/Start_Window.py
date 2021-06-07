# 具体的登录窗口控件self.widget
# 功能按键具体窗口self.widget1
# 查询页面内容self.widget2
# 更新页面内容self.widget3
# 分析页面具体内容widget4
# 预测具体界面wiget5
import datetime
import sys
import time

import matplotlib
# plt横坐标显示中文设置
from matplotlib import font_manager
import Data_analyse
from PyQt5.QtCore import QRegExp, QObject, pyqtSignal, QThread
from PyQt5.QtGui import QIcon, QRegExpValidator, QTextCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QAbstractItemView, QHeaderView, \
    QGridLayout, QTextEdit
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt

import Data_predict
import Data_quary
import Func_Login
import oper_database

matplotlib.use('Qt5Agg')
# plt横坐标显示中文设置
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\msyh.ttc")


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        # self.setWindowIcon(QIcon('logo.ico'))
        self.setStyleSheet('''     
            QWidget
            {
            font-family:'黑体';
            font-size:20px;
            font-weight:bold;
            background-color:rgb(240,255,240);
            }
            QWidget#right_widget
            {border-radius:15;}

            QPushButton
            {text-align : center;
            background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #fbc2eb, stop:1 #a6c1ee);
            font: bold;
            border-color: grey;
            border-width: 1px;
            border-radius: 5px;
            padding: 6px;
            height: 28px;
            border-style: outset;
            font-family:'黑体';
            font : 18px;}

            QPushButton:pressed
            {text-align : center;
            background-color : light gray;
            background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #e1aad2, stop:1 #92adda);
            font: bold;
            color:lightblue;
            border-color: gray;
            border-width: 1px;
            border-radius: 5px;
            padding: 6px;
            height : 28px;
            border-style: outset;
            font-family:'黑体';
            font : 18px;}
            QPushButton:hover:!pressed
            {color:red;}

            QLineEdit
            {border:0px;
            border-radius:0;
            border-bottom: 2px solid #B3B3B3;
            font-family:'等线';
            font-size:25px;
            font-weight:bold;}
            QLineEdit:hover{
                border-bottom:3px solid #66A3FF;
            }
            QLineEdit:focus{
                border-bottom:3px solid #E680BD
            }
            ''')
        self.setupUi(self)
        self.retranslateUi(self)
        self.widget_mainpage.hide()
        self.widget_quary.hide()
        self.widget_updata.hide()
        self.widget_analyse.hide()
        self.widget_predict.hide()

    def setupUi(self, MainWindow):
        # app窗口设置，名字设置，大小固定不可变，
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1114, 859)
        # MainWindow.setMinimumSize(QtCore.QSize(1114, 859))
        # MainWindow.setMaximumSize(QtCore.QSize(1114, 859))
        MainWindow.resize(1900, 975)
        MainWindow.setMinimumSize(QtCore.QSize(1900, 975))
        MainWindow.setMaximumSize(QtCore.QSize(1900, 975))

        # 定义主窗口
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        # size策略
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        # 主窗口大小固定
        # self.centralwidget.setMinimumSize(QtCore.QSize(1114, 834))
        # self.centralwidget.setMaximumSize(QtCore.QSize(1114, 834))
        self.centralwidget.setMinimumSize(QtCore.QSize(1900, 950))
        self.centralwidget.setMaximumSize(QtCore.QSize(1900, 950))

        self.centralwidget.setObjectName("centralwidget")
        # 登录窗口
        self.widget_login = QtWidgets.QWidget(self.centralwidget)
        # QtCore.QRect(340, 240, 411, 231)定义矩形
        self.widget_login.setGeometry(QtCore.QRect(10, 10, 1870, 940))
        self.widget_login.setObjectName("widget_login")
        # 具体的登录窗口控件self.widget
        self.widget = QtWidgets.QWidget(self.widget_login)
        self.widget.setGeometry(QtCore.QRect(810, 345, 250, 250))
        self.widget.setObjectName("widget")
        # 登录表单控件
        self.formLayout_login = QtWidgets.QFormLayout(self.widget)

        # 设置左侧、顶部、右侧和底部边距
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

        # 设置输入提示
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

        # 登录按钮信号连接
        self.pushButton_login.clicked.connect(self.on_pushButton_login_clicked)

        # 功能窗口
        self.widget_mainpage = QtWidgets.QWidget(self.centralwidget)
        # self.widget_mainpage.setGeometry(QtCore.QRect(10, 10, 1091, 821))
        self.widget_mainpage.setGeometry(QtCore.QRect(10, 10, 1870, 960))
        self.widget_mainpage.setObjectName("widget_mainpage")
        # 功能按键具体窗口self.widget1
        self.widget1 = QtWidgets.QWidget(self.widget_mainpage)
        # self.widget1.setGeometry(QtCore.QRect(30, 20, 1031, 30))
        self.widget1.setGeometry(QtCore.QRect(15, 20, 1850, 30))
        self.widget1.setObjectName("widget1")
        # 功能按键水平控件
        self.HLayout_func = QtWidgets.QHBoxLayout(self.widget1)
        # 设置左侧、顶部、右侧和底部边距
        self.HLayout_func.setContentsMargins(0, 0, 0, 0)
        self.HLayout_func.setObjectName("HLayout_func")
        # 功能按键设置
        self.pushButton_mainpage = QtWidgets.QPushButton(self.widget1)
        self.pushButton_mainpage.setObjectName("pushButton_mainpage")
        self.HLayout_func.addWidget(self.pushButton_mainpage)
        # 切换到主页
        self.pushButton_mainpage.clicked.connect(self.on_pushButton_mainpage_clicked)

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

        # 设置重合的四个功能显示widget和主页显示widget

        # 设置主页widget
        self.widget_mainshow = QtWidgets.QWidget(self.widget_mainpage)

        self.widget_mainshow.setGeometry(QtCore.QRect(15, 70, 1850, 950))
        self.widget_mainshow.setMinimumSize(QtCore.QSize(1850, 950))
        self.widget_mainshow.setMaximumSize(QtCore.QSize(1850, 950))

        self.widget_mainshow.setObjectName("widget_main")
        # 主页内容设置
        self.label_main = QtWidgets.QLabel(self.widget_mainshow)
        self.label_main.setGeometry(QtCore.QRect(350, 225, 1200, 400))
        self.label_main.setObjectName("label_main")
        self.label_main.setText("Welcome\n欢迎使用SDUT大数据气象和分析预测系统")
        self.label_main.setStyleSheet('''
            QLabel
            {
            font-family:'黑体';
            font-size:60px;
            } 
            ''')

        # 信息查询widget
        self.widget_quary = QtWidgets.QWidget(self.widget_mainpage)
        ####
        self.widget_quary.setGeometry(QtCore.QRect(15, 70, 1850, 950))
        self.widget_quary.setMinimumSize(QtCore.QSize(1850, 950))
        self.widget_quary.setMaximumSize(QtCore.QSize(1850, 950))
        self.widget_quary.setObjectName("widget_quary")
        # 信息查询widget内容
        self.widget2 = QtWidgets.QWidget(self.widget_quary)
        # self.widget2.setGeometry(QtCore.QRect(10, 6, 1011, 721))
        self.widget2.setGeometry(QtCore.QRect(5, 5, 1840, 940))
        self.widget2.setObjectName("widget2")
        # 水平布局，左边查询城市、起始终止时间等，右边为表格控件
        self.HLayout_quary = QtWidgets.QHBoxLayout(self.widget2)
        self.HLayout_quary.setContentsMargins(0, 0, 0, 0)
        self.HLayout_quary.setObjectName("HLayout_quary")
        # 垂直布局，查询城市、起始终止时间、查询按钮
        self.VLayout_quary = QtWidgets.QVBoxLayout()
        self.VLayout_quary.setContentsMargins(-1, 20, 15, 550)
        self.VLayout_quary.setSpacing(7)
        self.VLayout_quary.setObjectName("VLayout_quary")
        # 表单布局，查询条件组合
        self.FLayout_quary = QtWidgets.QFormLayout()
        self.FLayout_quary.setObjectName("FLayout_quary")

        # 查询条件控件设置（左半部分垂直布局中）
        self.label_city = QtWidgets.QLabel(self.widget2)
        self.label_city.setObjectName("label_city")
        self.FLayout_quary.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_city)
        # 城市选择下拉框
        self.comboBox_city = QtWidgets.QComboBox(self.widget2)
        self.comboBox_city.setObjectName("comboBox_city")
        self.FLayout_quary.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_city)
        # 下拉框添加城市 311淄博城区、811高青、936桓台、1281临淄、2087沂源、2347淄川、2348博山、2349周村
        self.comboBox_city.addItems(
            ['张店区311', '高青县811', '桓台县936', '临淄区1281', '沂源县2087', '淄川区2347', '博山区2348', '周村区2349'])

        self.label_start = QtWidgets.QLabel(self.widget2)
        self.label_start.setObjectName("label_start")
        self.FLayout_quary.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_start)
        # 起始时间
        self.dateEdit_start = QtWidgets.QDateEdit(self.widget2)
        self.dateEdit_start.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_start.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_start.setObjectName("dateEdit_start")
        self.FLayout_quary.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dateEdit_start)

        self.label_end = QtWidgets.QLabel(self.widget2)
        self.label_end.setObjectName("label_end")
        self.FLayout_quary.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_end)
        # 终止时间
        self.dateEdit_end = QtWidgets.QDateEdit(self.widget2)
        self.dateEdit_end.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_end.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit_end.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.FLayout_quary.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateEdit_end)
        self.VLayout_quary.addLayout(self.FLayout_quary)
        # 查询按钮
        self.pushButton_quaryone = QtWidgets.QPushButton(self.widget2)
        self.pushButton_quaryone.setObjectName("pushButton_quaryone")
        self.VLayout_quary.addWidget(self.pushButton_quaryone)
        self.pushButton_quaryone.clicked.connect(self.on_pushButton_quaryone_clicked)

        self.pushButton_quarymany = QtWidgets.QPushButton(self.widget2)
        self.pushButton_quarymany.setObjectName("pushButton_quarymany")
        self.VLayout_quary.addWidget(self.pushButton_quarymany)
        self.pushButton_quarymany.clicked.connect(self.on_pushButton_quarymany_clicked)

        # 左侧垂直布局加入整体水平布局
        self.HLayout_quary.addLayout(self.VLayout_quary)

        # 分割线水平布局左右分割
        self.line_quary = QtWidgets.QFrame(self.widget2)
        self.line_quary.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_quary.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_quary.setObjectName("line_quary")
        self.HLayout_quary.addWidget(self.line_quary)

        # 右侧表格显示数据控件
        self.tableWidget_quary = QtWidgets.QTableWidget(self.widget2)
        # self.tableWidget_quary.setMinimumSize(QtCore.QSize(780, 680))
        # self.tableWidget_quary.setMaximumSize(QtCore.QSize(780, 680))
        self.tableWidget_quary.setMinimumSize(QtCore.QSize(1500, 800))
        self.tableWidget_quary.setMaximumSize(QtCore.QSize(1500, 800))
        self.tableWidget_quary.setObjectName("tableWidget_quary")
        # 列宽自动调整
        self.tableWidget_quary.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 设置行列数
        self.tableWidget_quary.setColumnCount(0)
        self.tableWidget_quary.setRowCount(0)
        self.HLayout_quary.addWidget(self.tableWidget_quary)

        # 更新页面widget
        self.widget_updata = QtWidgets.QWidget(self.widget_mainpage)
        self.widget_updata.setEnabled(True)
        self.widget_updata.setGeometry(QtCore.QRect(15, 70, 1850, 950))
        self.widget_updata.setMinimumSize(QtCore.QSize(1850, 950))
        self.widget_updata.setMaximumSize(QtCore.QSize(1850, 950))
        self.widget_updata.setObjectName("widget_updata")
        # 具体的更新widget
        self.widget3 = QtWidgets.QWidget(self.widget_updata)
        self.widget3.setGeometry(QtCore.QRect(725, 110, 400, 560))
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

        # 分析widget
        self.widget_analyse = QtWidgets.QWidget(self.widget_mainpage)
        # self.widget_analyse.setGeometry(QtCore.QRect(30, 70, 1031, 731))
        # self.widget_analyse.setMinimumSize(QtCore.QSize(1031, 731))
        # self.widget_analyse.setMaximumSize(QtCore.QSize(1031, 731))
        self.widget_analyse.setGeometry(QtCore.QRect(15, 70, 1850, 950))
        self.widget_analyse.setMinimumSize(QtCore.QSize(1850, 950))
        self.widget_analyse.setMaximumSize(QtCore.QSize(1850, 950))

        self.widget_analyse.setObjectName("widget_analyse")

        self.widget4 = QtWidgets.QWidget(self.widget_analyse)
        # self.widget4.setGeometry(QtCore.QRect(0, 9, 1031, 711))
        self.widget4.setGeometry(QtCore.QRect(5, 5, 1840, 940))
        self.widget4.setObjectName("widget4")

        self.HLayout_analyse = QtWidgets.QHBoxLayout(self.widget4)
        self.HLayout_analyse.setContentsMargins(0, 0, 0, 0)
        self.HLayout_analyse.setObjectName("HLayout_analyse")

        self.VLayout_analyse = QtWidgets.QVBoxLayout()
        self.VLayout_analyse.setContentsMargins(10, 100, 10, 500)
        self.VLayout_analyse.setObjectName("VLayout_analyse")

        self.FLayout_analyse = QtWidgets.QFormLayout()
        self.FLayout_analyse.setObjectName("FLayout_analyse")

        # 城市label
        self.label_city_analyse = QtWidgets.QLabel(self.widget4)
        self.label_city_analyse.setObjectName("label_city_analyse")
        self.FLayout_analyse.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_city_analyse)

        # 城市选择下拉框
        self.comboBox_city_analyse = QtWidgets.QComboBox(self.widget4)
        self.comboBox_city_analyse.setObjectName("comboBox_city_analyse")
        self.FLayout_analyse.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_city_analyse)
        self.comboBox_city_analyse.addItems(
            ['张店区311', '高青县811', '桓台县936', '临淄区1281', '沂源县2087', '淄川区2347', '博山区2348', '周村区2349'])

        # 时间段label
        self.label_time_analyse = QtWidgets.QLabel(self.widget4)
        self.label_time_analyse.setObjectName("label_time_analyse")
        self.FLayout_analyse.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_time_analyse)

        # 时间段选择下拉框
        self.comboBox_time_analyse = QtWidgets.QComboBox(self.widget4)
        self.comboBox_time_analyse.setObjectName("comboBox_time_analyse")
        self.FLayout_analyse.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_time_analyse)
        self.comboBox_time_analyse.addItems(['1:近30天', '2:近60天', '3:历年对比'])

        self.VLayout_analyse.addLayout(self.FLayout_analyse)

        # 温度趋势变化按钮
        self.pushButton_temp = QtWidgets.QPushButton(self.widget4)
        self.pushButton_temp.setObjectName("pushButton_temp")
        self.VLayout_analyse.addWidget(self.pushButton_temp)
        self.pushButton_temp.clicked.connect(self.on_pushButton_temp_clicked)

        # 天气类型数据统计按钮
        self.pushButton_weather = QtWidgets.QPushButton(self.widget4)
        self.pushButton_weather.setObjectName("pushButton_weather")
        self.VLayout_analyse.addWidget(self.pushButton_weather)
        self.pushButton_weather.clicked.connect(self.on_pushButton_weather_clicked)

        # 按月平均气温历年对比按钮
        self.pushButton_monthtemp = QtWidgets.QPushButton(self.widget4)
        self.pushButton_monthtemp.setObjectName("pushButton_monthtemp")
        self.VLayout_analyse.addWidget(self.pushButton_monthtemp)
        self.pushButton_monthtemp.clicked.connect(self.on_pushButton_monthtemp_clicked)

        # #统计按钮
        # self.pushButton_wind = QtWidgets.QPushButton(self.widget4)
        # self.pushButton_wind.setObjectName("pushButton_wind")
        # self.VLayout_analyse.addWidget(self.pushButton_wind)
        # self.pushButton_wind.clicked.connect(self.on_pushButton_wind_clicked)

        self.HLayout_analyse.addLayout(self.VLayout_analyse)

        self.line_analyse = QtWidgets.QFrame(self.widget4)
        self.line_analyse.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_analyse.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_analyse.setObjectName("line_analyse")

        self.HLayout_analyse.addWidget(self.line_analyse)

        # 可视化显示区域
        self.groupBox_analyse = QtWidgets.QGroupBox(self.widget4)
        # self.groupBox_analyse.setMinimumSize(QtCore.QSize(750, 700))
        # self.groupBox_analyse.setMaximumSize(QtCore.QSize(750, 700))
        self.groupBox_analyse.setMinimumSize(QtCore.QSize(1700, 900))
        self.groupBox_analyse.setMaximumSize(QtCore.QSize(1700, 900))
        self.groupBox_analyse.setObjectName("groupBox_analyse")
        self.HLayout_analyse.addWidget(self.groupBox_analyse)

        self.grid = QtWidgets.QVBoxLayout(self.groupBox_analyse)
        # figsize=(4,3),
        self.figure = plt.figure(facecolor='#FFD7C4')  # 可选参数,facecolor为背景颜色
        self.canvas = FigureCanvas(self.figure)
        self.grid.addWidget(self.canvas)

        # 预测widget
        self.widget_predict = QtWidgets.QWidget(self.widget_mainpage)
        self.widget_predict.setGeometry(QtCore.QRect(15, 70, 1850, 950))
        self.widget_predict.setMinimumSize(QtCore.QSize(1850, 950))
        self.widget_predict.setMaximumSize(QtCore.QSize(1850, 950))
        self.widget_predict.setObjectName("widget_predict")

        self.widget5 = QtWidgets.QWidget(self.widget_predict)
        self.widget5.setGeometry(QtCore.QRect(5, 5, 1840, 940))
        self.widget5.setObjectName("widget5")

        self.HLayout_predict = QtWidgets.QHBoxLayout(self.widget5)
        self.HLayout_predict.setContentsMargins(0, 0, 0, 0)
        self.HLayout_predict.setObjectName("HLayout_predict")

        self.VLayout_predict = QtWidgets.QVBoxLayout()
        self.VLayout_predict.setContentsMargins(10, 100, 10, 500)
        self.VLayout_predict.setObjectName("VLayout_predict")

        self.FLayout_predict = QtWidgets.QFormLayout()
        self.FLayout_predict.setObjectName("FLayout_predict")

        # 城市label
        self.label_city_predict = QtWidgets.QLabel(self.widget5)
        self.label_city_predict.setObjectName("label_city_predict")
        self.FLayout_predict.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_city_predict)

        # 城市选择下拉框
        self.comboBox_city_predict = QtWidgets.QComboBox(self.widget5)
        self.comboBox_city_predict.setObjectName("comboBox_city_predict")
        self.FLayout_predict.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_city_predict)
        self.comboBox_city_predict.addItems(
            ['张店区311', '高青县811', '桓台县936', '临淄区1281', '沂源县2087', '淄川区2347', '博山区2348', '周村区2349'])

        self.VLayout_predict.addLayout(self.FLayout_predict)

        # 预测最高温度按钮
        self.pushButton_pretempmax = QtWidgets.QPushButton(self.widget5)
        self.pushButton_pretempmax.setObjectName("pushButton_pretempmax")
        self.VLayout_predict.addWidget(self.pushButton_pretempmax)
        self.pushButton_pretempmax.clicked.connect(self.on_pushButton_pretempmax_clicked)

        # 预测最低温度按钮
        self.pushButton_pretempmin = QtWidgets.QPushButton(self.widget5)
        self.pushButton_pretempmin.setObjectName("pushButton_pretempmin")
        self.VLayout_predict.addWidget(self.pushButton_pretempmin)
        self.pushButton_pretempmin.clicked.connect(self.on_pushButton_pretempmin_clicked)

        # 预测湿度按钮
        self.pushButton_prehum = QtWidgets.QPushButton(self.widget5)
        self.pushButton_prehum.setObjectName("pushButton_prehum")
        self.VLayout_predict.addWidget(self.pushButton_prehum)
        self.pushButton_prehum.clicked.connect(self.on_pushButton_prehum_clicked)

        # 预测明日按钮
        self.pushButton_pretom = QtWidgets.QPushButton(self.widget5)
        self.pushButton_pretom.setObjectName("pushButton_pretom")
        self.VLayout_predict.addWidget(self.pushButton_pretom)
        self.pushButton_pretom.clicked.connect(self.on_pushButton_pretom_clicked)

        # #预测天气类型按钮
        # self.pushButton_preweather = QtWidgets.QPushButton(self.widget5)
        # self.pushButton_preweather.setObjectName("pushButton_preweather")
        # self.VLayout_predict.addWidget(self.pushButton_preweather)
        # self.pushButton_preweather.clicked.connect(self.on_pushButton_preweather_clicked)

        self.HLayout_predict.addLayout(self.VLayout_predict)

        self.line_predict = QtWidgets.QFrame(self.widget5)
        self.line_predict.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_predict.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_predict.setObjectName("line_predict")

        self.HLayout_predict.addWidget(self.line_predict)

        # 可视化显示区域
        self.groupBox_predict = QtWidgets.QGroupBox(self.widget5)
        self.groupBox_predict.setMinimumSize(QtCore.QSize(1700, 900))
        self.groupBox_predict.setMaximumSize(QtCore.QSize(1700, 900))
        self.groupBox_predict.setObjectName("groupBox_predict")
        self.HLayout_predict.addWidget(self.groupBox_predict)

        # Create the text output widget.
        self.process = QtWidgets.QTextEdit(self.groupBox_predict)
        self.process.setReadOnly(True)
        self.process.ensureCursorVisible()
        self.process.setMinimumSize(QtCore.QSize(1600, 700))
        self.process.setMinimumSize(QtCore.QSize(1600, 700))
        self.process.setObjectName("process")
        self.process.move(30, 50)

        self.process.setText('Results')

        # self.cursor = self.process.textCursor()
        # cursor.movePosition(QTextCursor.End)

        # 分割线，上方按钮和下方显示区
        self.line_func = QtWidgets.QFrame(self.widget_mainpage)
        # self.line_func.setGeometry(QtCore.QRect(30, 56, 1031, 20))
        self.line_func.setGeometry(QtCore.QRect(15, 56, 1850, 20))
        self.line_func.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_func.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_func.setObjectName("line_func")

        # 设置中心窗口
        MainWindow.setCentralWidget(self.centralwidget)
        # 设置状态栏
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.statusBar().showMessage("欢迎使用")
        # 功能按键设置
        self.retranslateUi(MainWindow)

    # 功能化按键设置
    def retranslateUi(self, MainWindow):
        # 件需要运行在不同的语言环境下时，我们要针对特定的语言环境来改变界面显示
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
        self.label_city.setText(_translate("MainWindow", "城市选择："))
        self.label_start.setText(_translate("MainWindow", "起始时间："))
        self.label_end.setText(_translate("MainWindow", "结束时间："))
        self.pushButton_quaryone.setText(_translate("MainWindow", "查询起始日单日"))
        self.pushButton_quarymany.setText(_translate("MainWindow", "查询起止日期多日"))

        self.pushButton_updataenter.setText(_translate("MainWindow", "更新"))
        self.label_db_datetime.setText(_translate("MainWindow", "更新前数据库截止日期为："))
        self.label_newtime.setText(_translate("MainWindow", "更新后数据库截止日期为："))
        self.label_counttip.setText(_translate("MainWindow", "数据更新条数："))

        self.label_city_analyse.setText(_translate("MainWindow", "城市："))
        self.label_time_analyse.setText(_translate("MainWindow", "时间："))
        self.pushButton_temp.setText(_translate("MainWindow", "温度趋势变化"))
        self.pushButton_weather.setText(_translate("MainWindow", "天气类型统计"))
        self.pushButton_monthtemp.setText(_translate("MainWindow", "按月平均气温对比"))
        self.groupBox_analyse.setTitle(_translate("MainWindow", "Analyse"))

        self.label_city_predict.setText(_translate("MainWindow", "城市："))
        self.pushButton_pretempmax.setText(_translate("MainWindow", "预测今日最高温度"))
        self.pushButton_pretempmin.setText(_translate("MainWindow", "预测今日最低温度"))
        self.pushButton_prehum.setText(_translate("MainWindow", "预测今日平均湿度"))
        self.pushButton_pretom.setText(_translate("MainWindow", "预测明日气温、湿度"))
        # self.pushButton_preweather.setText(_translate("MainWindow", "预测天气类型"))
        self.groupBox_predict.setTitle(_translate("MainWindow", "Predict"))

    # 登录验证
    def on_pushButton_login_clicked(self):
        username = self.lineEdit_id.text()
        password = self.lineEdit_pwd.text()
        fl = Func_Login.Func_Login()
        flag = fl.Login(username, password)
        if flag == 0:
            QMessageBox.critical(self, 'ERROR', '帐号或密码不能为空')
        elif flag == 1:
            message = "当前用户：" + self.lineEdit_id.text()
            self.statusBar().showMessage(message)
            self.widget_login.hide()
            self.widget_mainpage.show()
        elif flag == -1:
            QMessageBox.critical(self, 'ERROR', '密码错误')
        elif flag == 2:
            QMessageBox.critical(self.centralwidget, 'ERROR', '账户不存在')
        else:
            QMessageBox.critical(self, 'ERROR', '数据库连接异常')

    # 退出登录
    def on_pushButton_signout_clicked(self):
        self.lineEdit_pwd.setText('')
        self.statusBar().showMessage("欢迎使用")
        # 窗口
        self.widget_login.show()
        self.widget_mainpage.hide()

    # 点击主页按钮
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

    # 点击查询单天天气数据
    def on_pushButton_quaryone_clicked(self):
        self.tableWidget_quary.setColumnCount(7)
        self.tableWidget_quary.setHorizontalHeaderLabels(['时间', '天气状况', '温度', '湿度', '空气质量', '风向', '风力等级'])
        # 设置时间列宽
        # self.tableWidget_quary.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        # 获取下拉框选择的城市并去掉汉字名称，只留下代号
        city = self.comboBox_city.currentText()[3:]
        # 获取起始日期和终止日期，并转换格式
        startdate = self.dateEdit_start.date().toString("yyyy-MM-dd")
        # 查询start当天数据
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
        enddate = self.dateEdit_end.date().toString("yyyy-MM-dd")

        self.pushButton_quarymany.setEnabled(False)
        # 多线程，前端不死机
        self.thread9 = QuaryM4(city, startdate, enddate)
        self.thread9.start()
        # 接收线程中的预测结果
        self.thread9.sinout.connect(self.out_da4)

    # 点击更新数据库数据
    def on_pushButton_updataenter_clicked(self):
        self.pushButton_updataenter.setEnabled(False)
        # 多线程，前端不死机
        self.thread1 = Updata()
        self.thread1.start()
        # 接收线程中的预测结果
        self.thread1.sinout.connect(self.out)

    # 点击获取温度趋势可视化分析
    def on_pushButton_temp_clicked(self):
        city = self.comboBox_city_analyse.currentText()[3:]
        timeflag = int(self.comboBox_time_analyse.currentText()[0])

        self.pushButton_temp.setEnabled(False)
        # 多线程，前端不死机
        self.thread6 = QuaryM(city,timeflag)
        self.thread6.start()
        # 接收线程中的预测结果
        self.thread6.sinout.connect(self.out_da)

    # 点击获取天气类型可视化分析
    def on_pushButton_weather_clicked(self):
        city = self.comboBox_city_analyse.currentText()[3:]
        timeflag = int(self.comboBox_time_analyse.currentText()[0])

        self.pushButton_weather.setEnabled(False)
        # 多线程，前端不死机
        self.thread7 = QuaryM2(city,timeflag)
        self.thread7.start()
        # 接收线程中的预测结果
        self.thread7.sinout.connect(self.out_da2)


    # 点击获取按月平均气温可视化分析
    def on_pushButton_monthtemp_clicked(self):
        city = self.comboBox_city_analyse.currentText()[3:]

        self.pushButton_monthtemp.setEnabled(False)
        # 多线程，前端不死机
        self.thread8 = QuaryM3(city)
        self.thread8.start()
        # 接收线程中的预测结果
        self.thread8.sinout.connect(self.out_da3)


    # 点击预测最高温度
    def on_pushButton_pretempmax_clicked(self):
        self.pushButton_pretempmax.setEnabled(False)
        self.process.append('预测今日最高温度开始：(估计耗时80s)')
        # 多线程预测，前端不死机
        self.thread2 = Predict_max()
        self.thread2.start()
        # 接收预测线程中的预测结果
        self.thread2.sinout.connect(self.out)

    # 点击预测最低温度
    def on_pushButton_pretempmin_clicked(self):
        self.pushButton_pretempmin.setEnabled(False)
        self.process.append('预测今日最低温度开始：(估计耗时80s)')
        # 多线程预测，前端不死机
        self.thread3 = Predict_min()
        self.thread3.start()
        # 接收预测线程中的预测结果
        self.thread3.sinout.connect(self.out)

    # 点击预测湿度
    def on_pushButton_prehum_clicked(self):
        self.pushButton_prehum.setEnabled(False)
        self.process.append('预测今日平均湿度开始：(估计耗时80s)')
        # 多线程预测，前端不死机
        self.thread4 = Predict_hum()
        self.thread4.start()
        # 接收预测线程中的预测结果
        self.thread4.sinout.connect(self.out)

    # 点击预测明天
    def on_pushButton_pretom_clicked(self):
        self.pushButton_pretom.setEnabled(False)
        self.process.append('预测明日温度、湿度开始：(估计耗时300s)')
        # 多线程预测，前端不死机
        self.thread5 = Predict_tom()
        self.thread5.start()
        # 接收预测线程中的预测结果
        self.thread5.sinout.connect(self.out)

    # 点击预测天气
    def on_pushButton_preweather_clicked(self):
        pass

    # 接收线程中的预测结果并显示
    def out(self, flag, k1, k2, k3):
        if flag == 1:
            self.pushButton_updataenter.setEnabled(True)
            if k1 == '-2':
                QMessageBox.critical(k2, k3)
                self.process.append(k1 + k2)
            elif k1 == '-1':
                QMessageBox.critical(k2, k3)
                self.process.append(k1 + k2)
            elif k1 == '0':
                QMessageBox.critical(k2, k3)
                self.process.append(k1 + k2)
            else:
                self.label_db_datetime.setText("更新前数据库截止日期为：" + k1)
                self.label_newtime.setText("更新后数据库截止日期为：" + k2)
                self.label_counttip.setText("数据更新条数：" + k3)
        elif flag == 2:
            self.pushButton_pretempmax.setEnabled(True)
            if k1 != 'Error:':
                self.process.append('预测今日最高温度为：' + k1)
                self.process.append('用时：' + k2 + 's')
            else:
                QMessageBox.critical(k1, k2)
                self.process.append(k1 + k2)
        elif flag == 3:
            self.pushButton_pretempmin.setEnabled(True)
            if k1 != 'Error:':
                self.process.append('预测今日最低温度为：' + k1)
                self.process.append('用时：' + k2 + 's')
            else:
                QMessageBox.critical(k1, k2)
                self.process.append(k1 + k2)
        elif flag == 4:
            self.pushButton_prehum.setEnabled(True)
            if k1 != 'Error:':
                self.process.append('预测今日平均湿度为：' + k1)
                self.process.append('用时：' + k2 + 's')
            else:
                QMessageBox.critical(k1, k2)
                self.process.append(k1 + k2)
        elif flag == 5:
            self.pushButton_pretom.setEnabled(True)
            if k1 != 'Error:':
                self.process.append('预测明日最高温度为：' + str(k1[0]))
                self.process.append('预测明日最低温度为：' + str(k1[1]))
                self.process.append('预测明日平均湿度为：' + str(k1[2]))
                self.process.append('用时：' + k2 + 's')
            else:
                QMessageBox.critical(k1, k2)
                self.process.append(k1 + k2)
        # self.pushButton_preweather.setEnabled(True)

    def out_da(self, data, flag,k):
        self.pushButton_temp.setEnabled(True)
        if flag == 0:
            QMessageBox.critical('ERROR:', '数据为空')
        elif flag == -1:
            QMessageBox.critical('ERROR:', '数据库连接错误')
        elif k == 3:
            # 清理图像
            plt.clf()
            # plt.cla()

            list1 = data[0]
            list2 = data[1]
            list3 = data[2]

            ax = self.figure.add_subplot(1, 1, 1)

            maxtemp1 = [t['max'] for t in list1]
            maxtemp2 = [t['max'] for t in list2]
            maxtemp3 = [t['max'] for t in list3]

            # print(len(maxtemp2),len(maxtemp1),l)

            # 变为矩阵
            x1 = np.arange(len(maxtemp1)) + 1
            x2 = np.arange(len(maxtemp2)) + 1
            x3 = np.arange(len(maxtemp3)) + 1
            y1 = np.array(maxtemp1)
            y2 = np.array(maxtemp2)
            y3 = np.array(maxtemp3)

            ax.plot(x1, y1, ls="--", color="r", marker=",", lw=1, label="2019 TEMP")
            ax.plot(x2, y2, ls=":", color="g", marker=",", lw=1, label="2020 TEMP")
            ax.plot(x3, y3, ls="-", color="b", marker=",", lw=1, label="2021 TEMP")
            # 设置标题
            ax.set_xlabel('Date')
            ax.set_xlabel('Temperature')
            ax.legend()
            ax.set_title("Line chart of temperature change")
            # 画图
            self.canvas.draw()
        else:
            # 清理图像
            plt.clf()
            # print(data) 将数据分为最高温、最低温、时间；逆序
            time = [t['date'][5:] for t in data]
            # time=time[::-1]
            maxtemp = [t['max'] for t in data]
            # maxtemp=maxtemp[::-1]
            mintemp = [t['min'] for t in data]
            # mintemp=mintemp[::-1]

            # 变为矩阵
            x = np.arange(len(maxtemp)) + 1
            y1 = np.array(maxtemp)
            y2 = np.array(mintemp)

            ax = self.figure.add_subplot(1, 1, 1)

            ax.plot(x, y1, ls="-", color="r", marker="o", lw=1, label="MAX TEMP")
            ax.plot(x, y2, ls="--", color="g", marker="o", lw=1, label="MIN TEMP")

            for a, b, c in zip(x, y1, y2):
                ax.text(a, b, '%d' % b, ha='center', va='bottom', rotation=-45)
                ax.text(a, c, '%d' % c, ha='center', va='bottom', rotation=-45)

            ax.set_xticks(x)
            ax.set_xticklabels(time, rotation=70, fontsize='small')
            # 设置标题
            ax.set_xlabel('Date')
            ax.set_xlabel('Temperature')
            ax.legend()
            ax.set_title("Line chart of temperature change")
            # 画图
            self.canvas.draw()

    def out_da2(self, data, flag):
        self.pushButton_weather.setEnabled(True)
        if flag == 0:
            QMessageBox.critical('ERROR:', '数据为空')
        elif flag == -1:
            QMessageBox.critical('ERROR:', '数据库连接错误')
        else:
            # # 清理图像
            plt.clf()
            # print(data)
            datatuple1 = [value for value in data[0].values()]
            datatuple2 = [value for value in data[1].values()]
            datatuple3 = [value for value in data[2].values()]
            # print(datatuple1)
            type = [key for key in data[0].keys()]
            # 变为矩阵
            x = np.arange(42) + 1
            y1 = np.array(datatuple1)
            y2 = np.array(datatuple2)
            y3 = np.array(datatuple3)
            axes = self.figure.subplots(nrows=3, ncols=1, sharex=True)
            self.figure.suptitle('Bar of Weather Type')
            ax1 = axes[0]
            ax2 = axes[1]
            ax3 = axes[2]
            ax3.set_xticks(x)
            ax3.set_xticklabels(type, rotation=70, fontsize='small', fontproperties=my_font)
            ax1.bar(x, y1, color='green', width=0.5, label='2021')
            ax2.bar(x, y2, color='red', width=0.5, label='2020')
            ax3.bar(x, y3, color='blue', width=0.5, label='2019')
            for a, b in zip(x, y1):
                ax1.text(a, b, '%d' % b, ha='center', va='bottom')
            for a, b in zip(x, y2):
                ax2.text(a, b, '%d' % b, ha='center', va='bottom')
            for a, b in zip(x, y3):
                ax3.text(a, b, '%d' % b, ha='center', va='bottom')
            ax1.legend()
            ax2.legend()
            ax3.legend()
            # 画图
            self.canvas.draw()

    def out_da3(self, data, flag):
        self.pushButton_monthtemp.setEnabled(True)
        if flag == 0:
            QMessageBox.critical('ERROR:', '数据为空')
        elif flag == -1:
            QMessageBox.critical('ERROR:', '数据库连接错误')
        else:
            # # 清理图像
            plt.clf()
            # print(data)

            # 变为矩阵
            x = np.arange(12) + 1

            y19 = np.array(data[0])
            y20 = np.array(data[1])
            y21 = np.array(data[2])

            ax = self.figure.add_subplot(1, 1, 1)

            ax.set_xticks(x)

            ax.plot(x, y19, ls="--", color="r", marker="o", lw=1, label="2019 TEMP")
            ax.plot(x, y20, ls=":", color="g", marker="^", lw=1, label="2020 TEMP")
            ax.plot(x, y21, ls="-", color="b", marker="v", lw=1, label="2021 TEMP")

            for a, b, c, d in zip(x, y19, y20, y21):
                ax.text(a, b, '%d' % b, ha='center', va='bottom')
                ax.text(a, c, '%d' % c, ha='center', va='bottom', rotation=-45)
                ax.text(a, d, '%d' % d, ha='center', va='bottom', rotation=-45)

            ax.set_xlabel('Month')
            ax.set_ylabel('Temperature')
            ax.legend()
            ax.set_title("Line chart of average temperature")
            # 画图
            self.canvas.draw()

    def out_da4(self, data, flag):
        self.pushButton_quarymany.setEnabled(True)
        if flag == 0:
            QMessageBox.critical('ERROR:', '数据为空')
        elif flag == -1:
            QMessageBox.critical('ERROR:', '数据库连接错误')
        else:
            self.tableWidget_quary.setRowCount(len(data))
            for index, item in enumerate(data):
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



class Updata(QThread):
    sinout = pyqtSignal(int, str, str, str)

    def __init__(self, parent=None):
        super(Updata, self).__init__(parent)
        self.working = True

    def run(self):
        dc = oper_database.ConnectDB()
        if dc.Error_flag == 0:
            data = dc.UpdateWeaData()
            if data == -1:
                self.sinout.emit(1, '-1', 'API Error:', '请联系开发者')
            elif data == 0:
                self.sinout.emit(1, '0', 'Limit Error:', '等待一小时后重试')
            else:
                self.sinout.emit(1, str(data[0]), str(data[2]), str(data[1]))
        else:
            self.sinout.emit(1, '-2', 'Error:', '数据库连接异常')


class Predict_max(QThread):
    sinout = pyqtSignal(int, str, str, str)

    def __init__(self, parent=None):
        super(Predict_max, self).__init__(parent)
        self.working = True
        self.today = datetime.datetime.now().strftime('%Y-%m-%d')
        if int(self.today[5:7]) <= 8:
            self.t = 0
        else:
            self.t = 0

    def run(self):
        start = time.time()
        dp = Data_predict.Data_Predict()
        f = dp.GetData()
        if f != -1:
            max = dp.Predict_max()
            max = str(round(np.double(max), 2) + self.t)
            end = time.time()
            s = str(round(end - start, 4))
            self.sinout.emit(2, max, s, '')
        else:
            self.sinout.emit(2, 'Error:', '数据库连接错误', '')


class Predict_min(QThread):
    sinout = pyqtSignal(int, str, str, str)

    def __init__(self, parent=None):
        super(Predict_min, self).__init__(parent)
        self.working = True
        self.today = datetime.datetime.now().strftime('%Y-%m-%d')
        if int(self.today[5:7]) <= 8:
            self.t = 3
        else:
            self.t = -2

    def run(self):
        start = time.time()
        dp = Data_predict.Data_Predict()
        f = dp.GetData()
        if f != -1:
            min = dp.Predict_min()
            min = str(round(np.double(min), 2) + self.t)
            end = time.time()
            s = str(round(end - start, 4))
            self.sinout.emit(3, min, s, '')
        else:
            self.sinout.emit(3, 'Error:', '数据库连接错误', '')


class Predict_hum(QThread):
    sinout = pyqtSignal(int, str, str, str)

    def __init__(self, parent=None):
        super(Predict_hum, self).__init__(parent)
        self.working = True

    def run(self):
        start = time.time()
        dp = Data_predict.Data_Predict()
        f = dp.GetData()
        if f != -1:
            hum = dp.Predict_hum()
            hum = str(round(np.double(hum), 2))
            end = time.time()
            s = str(round(end - start, 4))
            self.sinout.emit(4, hum, s, '')
        else:
            self.sinout.emit(4, 'Error:', '数据库连接错误', '')


class Predict_tom(QThread):
    sinout = pyqtSignal(int, list, str, str)

    def __init__(self, parent=None):
        super(Predict_tom, self).__init__(parent)
        self.working = True

    def run(self):
        start = time.time()
        dp = Data_predict.Data_Predict()
        f = dp.GetData()
        if f != -1:
            tomlist = dp.Predict_tommorw()
            # max = str(tomlist[0])
            # min = str(tomlist[1])
            # hum = str(tomlist[2])
            end = time.time()
            s = str(round(end - start, 4))
            self.sinout.emit(5, tomlist, s, '')
        else:
            self.sinout.emit(5, 'Error:', '数据库连接错误', '')

class QuaryM(QThread):
    sinout = pyqtSignal(list,int,int)

    def __init__(self, city,timeflag,parent=None):
        super(QuaryM, self).__init__(parent)
        self.working = True
        self.city = city
        self.timeflag = timeflag

    def run(self):
        da = Data_analyse.Data_Analyse()
        if self.timeflag ==3:
            data = da.Year_contrast(self.city)
        else:
            data = da.Quary_many(self.city, self.timeflag)
        if data == 0:
            # QMessageBox.critical(self, 'ERROR', '数据库无此数据')
            self.sinout.emit([], 0,self.timeflag)
        elif data == -1:
            # QMessageBox.critical(self, 'ERROR', '数据库连接异常')
            self.sinout.emit([], -1,self.timeflag)
        else:
            self.sinout.emit(data, 1,self.timeflag)

class QuaryM2(QThread):
    sinout = pyqtSignal(list,int)

    def __init__(self, city,timeflag,parent=None):
        super(QuaryM2, self).__init__(parent)
        self.working = True
        self.city = city
        self.timeflag = timeflag

    def run(self):
        # print(self.city,self.timeflag)
        da = Data_analyse.Data_Analyse()
        if self.timeflag != 3:
            data = da.Weather_type_days(self.city, self.timeflag)
        else:
            data = da.Weather_type_year(self.city)
        if data == 0:
            self.sinout.emit([], 0)
        elif data == -1:
            self.sinout.emit([], -1)
        else:
            self.sinout.emit(data, 1)

class QuaryM3(QThread):
    sinout = pyqtSignal(list,int)

    def __init__(self, city,parent=None):
        super(QuaryM3, self).__init__(parent)
        self.working = True
        self.city = city

    def run(self):
        da = Data_analyse.Data_Analyse()
        data = da.AverageTemp_Month(self.city)

        if data == 0:
            self.sinout.emit([], 0)
        elif data == -1:
            self.sinout.emit([], -1)
        else:
            self.sinout.emit(data, 1)

class QuaryM4(QThread):
    sinout = pyqtSignal(list,int)
    def __init__(self, city, startdate, enddate,parent=None):
        super(QuaryM4, self).__init__(parent)
        self.working = True
        self.city = city
        self.startdate = startdate
        self.enddate = enddate

    def run(self):
        dq = Data_quary.Data_Quary()
        data = dq.Quary_many(self.city, self.startdate, self.enddate)

        if data == 0:
            self.sinout.emit([], 0)
        elif data == -1:
            self.sinout.emit([], -1)
        else:
            self.sinout.emit(data, 1)



