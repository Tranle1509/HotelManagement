from PyQt6.QtWidgets import QMainWindow, QApplication

from ui.AboutUsMainWindowEx import AboutUsMainWindowEx

app=QApplication([])
mainwindow=QMainWindow()

myui=AboutUsMainWindowEx()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()