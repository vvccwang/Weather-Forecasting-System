import sys
from PyQt5.QtWidgets import *  # QMainWindow,QApplication,QDesktopWidget,QHBoxLayout,QVBoxLayout,QPushButton,QWidget,QLabel
from PyQt5.QtGui import QIcon, QFont, QPalette, QPixmap, QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import Qt, QRegExp


class FirstMainWindow(QMainWindow):
    def __init__(self, parent=None):
        # super（）调用父类方法
        super(FirstMainWindow, self).__init__(parent)
        # 设置主窗口的标题
        self.setWindowTitle('css test')
        # 设置主窗口尺寸
        self.resize(500, 400)
        # 设置标签控件
        self.inilabel()

    # 定义图标,此方法在苹果系统中无效
    def iniUI(self):
        # setGeometry是相对于父窗体来说的一种对子窗体进行位置设置的方法。
        self.setGeometry(300, 300, 250, 250)  # 从300，300位置 ，显示一个250*250的窗口
    # 窗口居中函数
    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newleft = (screen.width() - size.width()) / 2
        newtop = (screen.height() - size.height()) / 2
        self.move(newleft, newtop)

    # 定义label控件
    def inilabel(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        # 通过HTML文本设置字体颜色格式等
        label1.setText("这是一个文本标签")
        label1.setStyleSheet(''' 
                            QLabel{
                            color: yellow; 
                            height: 28px; 
                            font-size:40px;
                            background: skyblue; 
                            border-radius: 14px;
                            font-style:italic;
                            font-family:'黑体';}
                        ''')

        # 设置文本对齐方式
        label1.setAlignment(Qt.AlignCenter)

        #设置超链接文本
        label2.setText("<a href='www.baidu.com'><b>注意:</b>这是一个超链接</a>")
        # 设置超链接可以用浏览器打开
        label2.setOpenExternalLinks(True)
        # 设置文本对齐方式
        label2.setAlignment(Qt.AlignCenter)
        label2.setToolTip('这是一个超级链接')

        btn = QPushButton('按钮')
        # 设置按钮格式
        #setStyleSheet(...)语法很大比重来源于html的CSS，但是适用于窗口
        #对于同一个部件，要在同一个setStyleSheet(...)中完全写出来，否则对于该部件来讲，只有最后一个setStyleSheet(...)起作用。
        btn.setStyleSheet(''' 
                            QPushButton
                            {text-align : center;
                            background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #fbc2eb, stop:1 #a6c1ee);
                            font: bold;
                            border-color: grey;
                            border-width: 2px;
                            border-radius: 10px;
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
                            border-width: 2px;
                            border-radius: 10px;
                            padding: 6px;
                            height : 28px;
                            border-style: outset;
                            font-family:'黑体';
                            font : 18px;}
                            QPushButton:hover:!pressed
                            {color:red;}
                        ''')

        # 设置垂直布局
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(btn)

        mainFrame = QWidget()
        mainFrame.setLayout(vbox)
        # 将上方的框架加入到窗口中
        self.setCentralWidget(mainFrame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = FirstMainWindow()
    mainWindow.center()
    mainWindow.show()
    sys.exit(app.exec())
