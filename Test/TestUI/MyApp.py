from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.MainWindowCustomerExt import MainWindowCustomerExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowCustomerExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()