from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.MainWindowBookingManagementExt import MainWindowBookingManagementEx

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowBookingManagementEx()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()