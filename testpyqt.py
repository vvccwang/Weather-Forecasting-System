import sys
import test_main1
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow


if __name__ == '__main__':

    app=QApplication(sys.argv)
    # w=QWidget()
    # w.resize(1000, 500)
    # #     移动窗口
    # w.move(300, 300)
    # w.setWindowTitle('test1_window')
    # w.show()
    # #     循环扫描在窗口事件，进入程序主循环；
    # #     通过exit函数安全结束
    # sys.exit(app.exec())

    login_page = QMainWindow()
    login_ui=test_main1.Ui_MainWindow()
    # 向主窗口添加控件
    login_ui.setupUi(login_page)
    login_page.show()
    sys.exit(app.exec())






