import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Dao import oper_database
import oper_database


class FirstMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('气象分析预测系统')

        ###### 创建界面 ######
        self.startWidget = QWidget()
        self.setCentralWidget(self.startWidget)
        self.startlayout = QVBoxLayout(self.startWidget)

        self.centralwidget = QWidget()
        # self.setCentralWidget(self.centralwidget)
        self.Layout = QVBoxLayout(self.centralwidget) #垂直布局:

        #登录
        self.loginwidget = QWidget()
        self.loginLayout = QVBoxLayout(self.loginwidget)
        self.lineEdit_ID = QLineEdit()
        self.lineEdit_ID.setPlaceholderText('请输入帐号')
        self.lineEdit_PWD = QLineEdit()
        self.lineEdit_PWD.setPlaceholderText('请输入密码')

        #设置密码回显模式
        self.lineEdit_PWD.setEchoMode(2)

        # 设置输入只能是字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        self.lineEdit_ID.setValidator(validator)  # 只能输入字符或者数字
        self.lineEdit_PWD.setValidator(validator)

        self.pushButton_login = QPushButton()
        self.pushButton_login.setText('登录')

        self.loginLayout.addWidget(self.lineEdit_ID)
        self.loginLayout.addWidget(self.lineEdit_PWD)
        self.loginLayout.addWidget(self.pushButton_login)

        self.startlayout.addWidget(self.loginwidget)




        # 设置stackedWidgetstart
        self.stackedWidget_start = QStackedWidget()
        self.startlayout.addWidget(self.stackedWidget_start)
        self.stackedWidget_start.addWidget(self.loginwidget)
        self.stackedWidget_start.addWidget(self.centralwidget)

        self.pushButton_login.clicked.connect(self.on_pushButton_login_clicked)



        # 设置顶部功能按钮
        self.topwidget = QWidget()

        self.buttonLayout = QHBoxLayout(self.topwidget) #水平布局

        self.pushButton_mainpage = QPushButton()
        self.pushButton_mainpage.setText("主页")
        self.buttonLayout.addWidget(self.pushButton_mainpage)

        self.pushButton_quary = QPushButton()
        self.pushButton_quary.setText("数据查询")
        self.buttonLayout.addWidget(self.pushButton_quary)

        self.pushButton_updata = QPushButton()
        self.pushButton_updata.setText("数据更新")
        self.buttonLayout.addWidget(self.pushButton_updata)

        self.pushButton_analyse = QPushButton()
        self.pushButton_analyse.setText("气象分析")
        self.buttonLayout.addWidget(self.pushButton_analyse)

        self.pushButton_predict = QPushButton()
        self.pushButton_predict.setText("气象预测")
        self.buttonLayout.addWidget(self.pushButton_predict)

        self.pushButton_signout = QPushButton()
        self.pushButton_signout.setText("退出登录")
        self.buttonLayout.addWidget(self.pushButton_signout)

        self.Layout.addWidget(self.topwidget)

        # 设置stackedWidget
        self.stackedWidget = QStackedWidget()
        self.Layout.addWidget(self.stackedWidget)

        #设置主面板
        self.form_main = QWidget()
        self.formLayout_main = QHBoxLayout(self.form_main)
        self.label0 = QLabel()
        self.label0.setText("主页")
        self.label0.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label0.setAlignment(Qt.AlignCenter)
        self.label0.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout_main.addWidget(self.label0)

        # 设置第一个面板
        self.form_quary = QWidget()
        self.formLayout_quary = QHBoxLayout(self.form_quary)
        self.label1 = QLabel()
        self.label1.setText("第一个面板")
        self.label1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout_quary.addWidget(self.label1)

        # 设置第二个面板
        self.form_updata = QWidget()
        self.formLayout_updata = QHBoxLayout(self.form_updata)
        self.label2 = QLabel()
        self.label2.setText("第二个面板")
        self.label2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout_updata.addWidget(self.label2)

        # 设置第三个面板
        self.form_analyse = QWidget()
        self.formLayout_analyse = QHBoxLayout(self.form_analyse)
        self.label3 = QLabel()
        self.label3.setText("第三个面板")
        self.label3.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout_analyse.addWidget(self.label3)

        # 设置第四个面板
        self.form_predict = QWidget()
        self.formLayout_predict = QHBoxLayout(self.form_predict)
        self.label4 = QLabel()
        self.label4.setText("第四个面板")
        self.label4.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        self.label4.setAlignment(Qt.AlignCenter)
        self.label4.setFont(QFont("Roman times", 50, QFont.Bold))
        self.formLayout_predict.addWidget(self.label4)

        # 将5个面板，加入stackedWidget
        self.stackedWidget.addWidget(self.form_main)
        self.stackedWidget.addWidget(self.form_quary)
        self.stackedWidget.addWidget(self.form_updata)
        self.stackedWidget.addWidget(self.form_analyse)
        self.stackedWidget.addWidget(self.form_predict)


        # 设置状态栏
        self.statusBar().showMessage("欢迎使用")

        # 窗口最大化
        # self.showMaximized()

        ###### 三个按钮事件 ######
        self.pushButton_quary.clicked.connect(self.on_pushButton_quary_clicked)
        self.pushButton_updata.clicked.connect(self.on_pushButton_updata_clicked)
        self.pushButton_analyse.clicked.connect(self.on_pushButton_analyse_clicked)
        self.pushButton_predict.clicked.connect(self.on_pushButton_predict_clicked)
        self.pushButton_signout.clicked.connect(self.on_pushButton_signout_clicked)
        self.pushButton_mainpage.clicked.connect(self.on_pushButton_mainpage_clicked)

    #登录验证
    def on_pushButton_login_clicked(self):
        username=self.lineEdit_ID.text()
        password=self.lineEdit_PWD.text()
        dc=oper_database.ConnectDB()
        if dc.Error_flag == 0:
            f=dc.login(username,password)
            if f==1:
                message="当前用户："+self.lineEdit_ID.text()
                self.statusBar().showMessage(message)
                # 窗口最大化
                self.showMaximized()
                self.stackedWidget_start.setCurrentIndex(1)
            elif f==-1:
                QMessageBox.critical(self,'ERROR','密码错误')
                # print('密码错误')
                # pass
            else:
                QMessageBox.critical(self, 'ERROR', '账户不存在')
                # print('账户不存在')
                # pass
        else:
            QMessageBox.critical(self, 'ERROR', '数据库连接异常')

    #退出登录
    def on_pushButton_signout_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        # self.lineEdit_ID.setText('')
        self.lineEdit_PWD.setText('')
        self.statusBar().showMessage("欢迎使用")
        # 窗口
        self.showNormal()
        self.stackedWidget_start.setCurrentIndex(0)

    #主页
    def on_pushButton_mainpage_clicked(self):
        self.stackedWidget.setCurrentIndex(0)

    # 按钮一：打开第一个面板
    def on_pushButton_quary_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    # 按钮二：打开第二个面板
    def on_pushButton_updata_clicked(self):
        self.stackedWidget.setCurrentIndex(2)

    # 按钮三：打开第三个面板
    def on_pushButton_analyse_clicked(self):
        self.stackedWidget.setCurrentIndex(3)

    # 按钮四：打开第四个面板
    def on_pushButton_predict_clicked(self):
        self.stackedWidget.setCurrentIndex(4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('F:\project2021\GUI\image\logo.jpg'))
    the_mainwindow = FirstMainWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())
