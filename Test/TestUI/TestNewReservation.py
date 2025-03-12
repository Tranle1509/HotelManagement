from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.MainWindowManagementEx import MainWindowManagementEx

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowManagementEx()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()