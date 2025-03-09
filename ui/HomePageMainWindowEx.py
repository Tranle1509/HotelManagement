from PyQt6.QtWidgets import QMainWindow

from ui.HomePageMainWindow import Ui_MainWindow
from ui.LoginMainWindowEx import LoginMainWindowEx
from ui.MainWindowBookingManagementExt import MainWindowRoomManagementEx
from ui.NewReservationMainWindowExt import MainWindow_NewReservationExt


class HomePageMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonNext.clicked.connect(self.process_next)
        self.pushButtonBack.clicked.connect(self.process_back)
    def process_next(self):
        self.MainWindow.close()#close login window
        self.mainwindow = QMainWindow()
        self.myui = MainWindow_NewReservationExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
    def process_back(self):
        self.MainWindow.close()  # close login window
        self.mainwindow = QMainWindow()
        self.myui = LoginMainWindowEx()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
