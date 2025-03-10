from PyQt6.QtWidgets import QMainWindow

from ui.HomePageMainWindow import Ui_MainWindow


class HomePageMainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogIn.clicked.connect(self.process_login)
        self.pushButtonAboutUs.clicked.connect(self.process_about)
    def process_login(self):
        from ui.LoginMainWindowEx import LoginMainWindowEx

        self.MainWindow.close()#close login window
        self.mainwindow = QMainWindow()
        self.myui = LoginMainWindowEx()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()

    def process_about(self):
        from ui.AboutUsMainWindowEx import AboutUsMainWindowEx

        self.MainWindow.close()  # close login window
        self.mainwindow = QMainWindow()
        self.myui = AboutUsMainWindowEx()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()

