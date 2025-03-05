from PyQt6.QtWidgets import QMainWindow

from ui.HomePageMainWindow import Ui_MainWindow
from ui.MainWindowRoomManagementEx import MainWindowRoomManagementEx


class HomePageMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonRoom.clicked.connect(self.process_room)
        #self.pushButtonBooking.clicked.connect(self.process_booking)
    def process_room(self):
        self.MainWindow.close()#close login window
        self.mainwindow = QMainWindow()
        self.myui = MainWindowRoomManagementEx()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
