from PyQt6.QtWidgets import QMainWindow

from ui.AboutUsMainWindow import Ui_MainWindow
from ui.HomePageMainWindowEx import HomePageMainWindowEx


class AboutUsMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonBack.clicked.connect(self.process_back)

    def process_back(self):
        self.MainWindow.close()#close login window
        self.mainwindow = QMainWindow()
        self.myui = HomePageMainWindowEx()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
