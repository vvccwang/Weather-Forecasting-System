import sys
import Start_Window
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('F:\project2021\GUI\image\logo.jpg'))
    the_mainwindow = Start_Window.FirstMainWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())