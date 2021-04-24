import sys
from PyQt5.QtWidgets import * #QMainWindow,QApplication,QDesktopWidget,QHBoxLayout,QVBoxLayout,QPushButton,QWidget,QLabel
from PyQt5.QtGui import QIcon,QFont,QPalette,QPixmap,QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import Qt,QRegExp


class FirstMainWindow(QMainWindow):
    def __init__(self,parent=None):
        #super（）调用父类方法
        super(FirstMainWindow,self).__init__(parent)
        #设置主窗口的标题
        self.setWindowTitle('气象分析预测系统')
        #设置主窗口尺寸
        self.resize(500,400)
        #设置状态栏
        self.inistatus()
        #设置标签控件
        self.inilabel()
        #设置图标
        # self.iniUI()

    #定义图标,此方法在苹果系统中无效
    def iniUI(self):
        #setGeometry是相对于父窗体来说的一种对子窗体进行位置设置的方法。
        self.setGeometry(300,300,250,250)#从300，300位置 ，显示一个250*250的窗口
        #设置窗口图标
        self.setWindowIcon(QIcon('GUI/image/logo.jpg'))

    #设置状态栏
    def inistatus(self):
        # 状态栏（窗口下方）
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息', 5000)

    #设置按钮
    def inibutton(self):
        # 添加button
        self.button_1 = QPushButton('退出应用程序')

        # 提示信息
        self.button_1.setToolTip('点此按钮关闭程序')

        # 将信号与槽关联
        self.button_1.clicked.connect(self.onClick_Button)

        # 定义一个水平布局，把按钮加入进去
        layout = QHBoxLayout()
        layout.addWidget(self.button_1)

        # 将上方的水平布局整体加入到框架中
        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        # 将上方的框架加入到窗口中
        self.setCentralWidget(mainFrame)

    #按钮单击事件的方法（自定义的槽）
    def onClick_Button(self):
        sender=self.sender()
        print(sender.text()+'按钮被按下')

        #屏幕坐标系的有关代码。。。。（略）


        #返回应用程序对象
        app=QApplication.instance()
        #关闭应用程序
        app.quit()

    #窗口居中函数
    def center(self):
        # 获取屏幕坐标系
        screen=QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size=self.geometry()
        newleft=(screen.width()-size.width())/2
        newtop=(screen.height()-size.height())/2
        self.move(newleft,newtop)

    #定义label控件
    def inilabel(self):
        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)


        #通过HTML文本设置字体颜色格式等
        label1.setText("<font color=yellow>这是一个文本标签</font>")
        #填充整个屏幕（label1的区域）
        label1.setAutoFillBackground(True)
        #定义一个调色板
        patette=QPalette()
        #设置背景色setColor
        patette.setColor(QPalette.Window,Qt.blue)

        #设置调色板
        label1.setPalette(patette)
        #设置文本对齐方式
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        # 设置文本对齐方式
        label3.setAlignment(Qt.AlignCenter)
        #设置提示
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("GUI/image/logo.jpg"))

        #设置超链接可以用浏览器打开
        label4.setOpenExternalLinks(True)

        label4.setText("<a href='https://www.chenluo.wang/'>label4</a>")
        # 设置文本对齐方式
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')


        #设置垂直布局
        vbox=QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        #绑定事件
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        # self.setLayout(vbox) #QWidget中使用

        # 将上方的水平布局整体加入到框架中
        mainFrame = QWidget()
        mainFrame.setLayout(vbox)
        # 将上方的框架加入到窗口中
        self.setCentralWidget(mainFrame)


    #划过显示提示
    def linkHovered(self):
        print('当鼠标划过label2，触发')
    #鼠标单击标签4时，出发事件
    def linkClicked(self):
        print('当鼠标单击label4时，触发')


#对话框QDialog
class FirstQDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(500,200)
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle('Qlabel与伙伴控件')

        nameLabel=QLabel('&Name',self)
        nameLineEdit=QLineEdit(self)

        #设置输入框没有输入时的默认提示 setPlaceholdrText
        nameLineEdit.setPlaceholderText('id，数字与字母类型')

        #整数校验器 范围 0-9999
        intValidator=QIntValidator(self)
        intValidator.setRange(0,9999)

        #浮点校验器 精度小数点后两位
        doubleValidator=QDoubleValidator(self)
        doubleValidator.setRange(-360,360)
        #标准显示法
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        #显示精度 小数点后两位
        doubleValidator.setDecimals(2)

        #字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator=QRegExpValidator(self)
        validator.setRegExp(reg)

        #设置校验器
        # nameLineEdit.setValidator(intValidator)  #整数
        # nameLineEdit.setValidator(doubleValidator) #浮点数
        nameLineEdit.setValidator(validator) #字符或者数字




        '''
        QLineEdit：
        基本功能：输入单行文本
        高级功能： 
            1.设置回显模式 EchoMode：4种回显模式
                NoEcho = 1
                Normal = 0
                Password = 2
                PasswordEchoOnEdit = 3
            2.校验器，设置输入的类型格式长度等
                
        '''
        #设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel = QLabel('&Password', self)
        passwordLineEdit = QLineEdit(self)

        #设置回显模式
        passwordLineEdit.setEchoMode(2)
        # passwordLineEdit.setEchoMode(QLineEdit.Password) #两种方法

        # 设置伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)

        #设置按钮
        btnOK=QPushButton('&OK')
        btnCancel=QPushButton('&Cancel')



        #设置栅格布局
        mainLayout=QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)#第0行0列
        mainLayout.addWidget(nameLineEdit,0,1,1,2)#第0行1列，占用1行2列

        mainLayout.addWidget(passwordLabel,1,0)
        mainLayout.addWidget(passwordLineEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,0)
        mainLayout.addWidget(btnCancel,2,2)


class DialogDemo(QMainWindow):
    def __init__(self):
        super(DialogDemo,self).__init__()
        self.iniUI()

    def iniUI(self):
        self.setWindowTitle('QDialog案例')
        self.resize(300,200)

        self.button = QPushButton(self)
        self.button.setText('弹出对话框')
        self.button.move(50,50)
        self.button.clicked.connect(self.showDialog)

    def showDialog(self):
        dialog=QDialog()
        button = QPushButton('确定',dialog)
        button.clicked.connect(dialog.close)
        button.move(50,50)
        dialog.setWindowTitle('对话框')
        #以模式状态显示，即窗口弹出时mainwindow的控件不可用
        dialog.setWindowModality(Qt.ApplicationModal)

        dialog.exec()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('GUI/image/logo.jpg'))
    mainWindow = FirstMainWindow()
    mainWindow.center()
    mainWindow.show()

    # mainDialog=FirstQDialog()
    # mainDialog.show()
    sys.exit(app.exec())

    # DialogDemo=DialogDemo()
    # DialogDemo.show()
    # sys.exit(app.exec())
