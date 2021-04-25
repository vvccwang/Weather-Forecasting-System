# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from Dao import oper_database
# import oper_database
#
#
# class FirstMainWindow(QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.setWindowTitle('气象分析预测系统')
#
#         ###### 创建界面 ######
#         self.startWidget = QWidget()
#         self.setCentralWidget(self.startWidget)
#         self.startlayout = QVBoxLayout(self.startWidget)
#
#         self.centralwidget = QWidget()
#         # self.setCentralWidget(self.centralwidget)
#         self.Layout = QVBoxLayout(self.centralwidget) #垂直布局:
#
#         #登录
#         self.loginwidget = QWidget()
#         self.loginLayout = QVBoxLayout(self.loginwidget)
#         self.lineEdit_ID = QLineEdit()
#         self.lineEdit_ID.setPlaceholderText('请输入帐号')
#         self.lineEdit_PWD = QLineEdit()
#         self.lineEdit_PWD.setPlaceholderText('请输入密码')
#
#         #设置密码回显模式
#         self.lineEdit_PWD.setEchoMode(2)
#
#         # 设置输入只能是字符和数字
#         reg = QRegExp('[a-zA-Z0-9]+$')
#         validator = QRegExpValidator(self)
#         validator.setRegExp(reg)
#
#         self.lineEdit_ID.setValidator(validator)  # 只能输入字符或者数字
#         self.lineEdit_PWD.setValidator(validator)
#
#         self.pushButton_login = QPushButton()
#         self.pushButton_login.setText('登录')
#
#         self.loginLayout.addWidget(self.lineEdit_ID)
#         self.loginLayout.addWidget(self.lineEdit_PWD)
#         self.loginLayout.addWidget(self.pushButton_login)
#
#         self.startlayout.addWidget(self.loginwidget)
#
#
#
#
#         # 设置stackedWidgetstart
#         self.stackedWidget_start = QStackedWidget()
#         self.startlayout.addWidget(self.stackedWidget_start)
#         self.stackedWidget_start.addWidget(self.loginwidget)
#         self.stackedWidget_start.addWidget(self.centralwidget)
#
#         self.pushButton_login.clicked.connect(self.on_pushButton_login_clicked)
#
#
#
#         # 设置顶部功能按钮
#         self.topwidget = QWidget()
#
#         self.buttonLayout = QHBoxLayout(self.topwidget) #水平布局
#
#         self.pushButton_mainpage = QPushButton()
#         self.pushButton_mainpage.setText("主页")
#         self.buttonLayout.addWidget(self.pushButton_mainpage)
#
#         self.pushButton_quary = QPushButton()
#         self.pushButton_quary.setText("数据查询")
#         self.buttonLayout.addWidget(self.pushButton_quary)
#
#         self.pushButton_updata = QPushButton()
#         self.pushButton_updata.setText("数据更新")
#         self.buttonLayout.addWidget(self.pushButton_updata)
#
#         self.pushButton_analyse = QPushButton()
#         self.pushButton_analyse.setText("气象分析")
#         self.buttonLayout.addWidget(self.pushButton_analyse)
#
#         self.pushButton_predict = QPushButton()
#         self.pushButton_predict.setText("气象预测")
#         self.buttonLayout.addWidget(self.pushButton_predict)
#
#         self.pushButton_signout = QPushButton()
#         self.pushButton_signout.setText("退出登录")
#         self.buttonLayout.addWidget(self.pushButton_signout)
#
#         self.Layout.addWidget(self.topwidget)
#
#         # 设置stackedWidget
#         self.stackedWidget = QStackedWidget()
#         self.Layout.addWidget(self.stackedWidget)
#
#         #设置主面板
#         self.form_main = QWidget()
#         self.formLayout_main = QHBoxLayout(self.form_main)
#         self.label0 = QLabel()
#         self.label0.setText("主页")
#         self.label0.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
#         self.label0.setAlignment(Qt.AlignCenter)
#         self.label0.setFont(QFont("Roman times", 50, QFont.Bold))
#         self.formLayout_main.addWidget(self.label0)
#
#         # 设置第一个面板
#         self.form_quary = QWidget()
#         self.formLayout_quary = QHBoxLayout(self.form_quary)
#         self.label1 = QLabel()
#         self.label1.setText("第一个面板")
#         self.label1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
#         self.label1.setAlignment(Qt.AlignCenter)
#         self.label1.setFont(QFont("Roman times", 50, QFont.Bold))
#         self.formLayout_quary.addWidget(self.label1)
#
#         # 设置第二个面板
#         self.form_updata = QWidget()
#         self.formLayout_updata = QHBoxLayout(self.form_updata)
#         self.label2 = QLabel()
#         self.label2.setText("第二个面板")
#         self.label2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
#         self.label2.setAlignment(Qt.AlignCenter)
#         self.label2.setFont(QFont("Roman times", 50, QFont.Bold))
#         self.formLayout_updata.addWidget(self.label2)
#
#         # 设置第三个面板
#         self.form_analyse = QWidget()
#         self.formLayout_analyse = QHBoxLayout(self.form_analyse)
#         self.label3 = QLabel()
#         self.label3.setText("第三个面板")
#         self.label3.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
#         self.label3.setAlignment(Qt.AlignCenter)
#         self.label3.setFont(QFont("Roman times", 50, QFont.Bold))
#         self.formLayout_analyse.addWidget(self.label3)
#
#         # 设置第四个面板
#         self.form_predict = QWidget()
#         self.formLayout_predict = QHBoxLayout(self.form_predict)
#         self.label4 = QLabel()
#         self.label4.setText("第四个面板")
#         self.label4.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
#         self.label4.setAlignment(Qt.AlignCenter)
#         self.label4.setFont(QFont("Roman times", 50, QFont.Bold))
#         self.formLayout_predict.addWidget(self.label4)
#
#         # 将5个面板，加入stackedWidget
#         self.stackedWidget.addWidget(self.form_main)
#         self.stackedWidget.addWidget(self.form_quary)
#         self.stackedWidget.addWidget(self.form_updata)
#         self.stackedWidget.addWidget(self.form_analyse)
#         self.stackedWidget.addWidget(self.form_predict)
#
#
#         # 设置状态栏
#         self.statusBar().showMessage("欢迎使用")
#
#         # 窗口最大化
#         # self.showMaximized()
#
#         ###### 三个按钮事件 ######
#         self.pushButton_quary.clicked.connect(self.on_pushButton_quary_clicked)
#         self.pushButton_updata.clicked.connect(self.on_pushButton_updata_clicked)
#         self.pushButton_analyse.clicked.connect(self.on_pushButton_analyse_clicked)
#         self.pushButton_predict.clicked.connect(self.on_pushButton_predict_clicked)
#         self.pushButton_signout.clicked.connect(self.on_pushButton_signout_clicked)
#         self.pushButton_mainpage.clicked.connect(self.on_pushButton_mainpage_clicked)
#
#     #登录验证
#     def on_pushButton_login_clicked(self):
#         username=self.lineEdit_ID.text()
#         password=self.lineEdit_PWD.text()
#         dc=oper_database.ConnectDB()
#         if dc.Error_flag == 0:
#             f=dc.login(username,password)
#             if f==1:
#                 message="当前用户："+self.lineEdit_ID.text()
#                 self.statusBar().showMessage(message)
#                 # 窗口最大化
#                 self.showMaximized()
#                 self.stackedWidget_start.setCurrentIndex(1)
#             elif f==-1:
#                 QMessageBox.critical(self,'ERROR','密码错误')
#                 # print('密码错误')
#                 # pass
#             else:
#                 QMessageBox.critical(self, 'ERROR', '账户不存在')
#                 # print('账户不存在')
#                 # pass
#         else:
#             QMessageBox.critical(self, 'ERROR', '数据库连接异常')
#
#     #退出登录
#     def on_pushButton_signout_clicked(self):
#         self.stackedWidget.setCurrentIndex(0)
#         # self.lineEdit_ID.setText('')
#         self.lineEdit_PWD.setText('')
#         self.statusBar().showMessage("欢迎使用")
#         # 窗口
#         self.showNormal()
#         self.stackedWidget_start.setCurrentIndex(0)
#
#     #主页
#     def on_pushButton_mainpage_clicked(self):
#         self.stackedWidget.setCurrentIndex(0)
#
#     # 按钮一：打开第一个面板
#     def on_pushButton_quary_clicked(self):
#         self.stackedWidget.setCurrentIndex(1)
#
#     # 按钮二：打开第二个面板
#     def on_pushButton_updata_clicked(self):
#         self.stackedWidget.setCurrentIndex(2)
#
#     # 按钮三：打开第三个面板
#     def on_pushButton_analyse_clicked(self):
#         self.stackedWidget.setCurrentIndex(3)
#
#     # 按钮四：打开第四个面板
#     def on_pushButton_predict_clicked(self):
#         self.stackedWidget.setCurrentIndex(4)
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setWindowIcon(QIcon('F:\project2021\GUI\image\logo.jpg'))
#     the_mainwindow = FirstMainWindow()
#     the_mainwindow.show()
#     sys.exit(app.exec_())

#具体的登录窗口控件self.widget
#功能按键具体窗口self.widget1

import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets

import oper_database


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.widget_mainpage.hide()
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

        self.pushButton_quary = QtWidgets.QPushButton(self.widget1)
        self.pushButton_quary.setObjectName("pushButton_quary")
        self.HLayout_func.addWidget(self.pushButton_quary)

        self.pushButton_updata = QtWidgets.QPushButton(self.widget1)
        self.pushButton_updata.setObjectName("pushButton_updata")
        self.HLayout_func.addWidget(self.pushButton_updata)

        self.pushButton_analyse = QtWidgets.QPushButton(self.widget1)
        self.pushButton_analyse.setObjectName("pushButton_analyse")
        self.HLayout_func.addWidget(self.pushButton_analyse)

        self.pushButton_predict = QtWidgets.QPushButton(self.widget1)
        self.pushButton_predict.setObjectName("pushButton_predict")
        self.HLayout_func.addWidget(self.pushButton_predict)

        self.pushButton_signout = QtWidgets.QPushButton(self.widget1)
        self.pushButton_signout.setObjectName("pushButton_signout")
        self.HLayout_func.addWidget(self.pushButton_signout)
        self.pushButton_signout.clicked.connect(self.on_pushButton_signout_clicked)

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

    #登录验证
    def on_pushButton_login_clicked(self):
        username=self.lineEdit_id.text()
        password=self.lineEdit_pwd.text()
        if username == '' or password == '':
            QMessageBox.critical(self, 'ERROR', '帐号或密码不能为空')
        else:
            dc=oper_database.ConnectDB()
            if dc.Error_flag == 0:
                f=dc.login(username,password)
                if f==1:
                    message="当前用户："+self.lineEdit_id.text()
                    self.statusBar().showMessage(message)
                    self.widget_login.hide()
                    self.widget_mainpage.show()
                elif f==-1:
                    QMessageBox.critical(self,'ERROR','密码错误')
                    # print('密码错误')
                    # pass
                else:
                    QMessageBox.critical(self.centralwidget, 'ERROR', '账户不存在')
                    # print('账户不存在')
                    # pass
            else:
                QMessageBox.critical(self, 'ERROR', '数据库连接异常')

    #退出登录
    def on_pushButton_signout_clicked(self):
        self.lineEdit_pwd.setText('')
        self.statusBar().showMessage("欢迎使用")
        # 窗口
        self.widget_login.show()
        self.widget_mainpage.hide()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('GUI/image/logo.jpg'))
    mainWindow = Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec())






