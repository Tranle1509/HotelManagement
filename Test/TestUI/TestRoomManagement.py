from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.MainWindowRoomManagementEx import MainWindowRoomManagementEx

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowRoomManagementEx()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()