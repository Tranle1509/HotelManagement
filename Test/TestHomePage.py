from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.HomePageMainWindowEx import HomePageMainWindowEx

app=QApplication([])
mainwindow=QMainWindow()
myui=HomePageMainWindowEx()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()