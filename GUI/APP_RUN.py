import sys
import Start_Window
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('logo.ico'))
    mainWindow = Start_Window.Ui_MainWindow()
    mainWindow.show()
    sys.exit(app.exec())