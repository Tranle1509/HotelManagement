from PyQt6.QtWidgets import QApplication, QMainWindow

from ui.MainWindow_NewReservationExt import MainWindow_NewReservationExt

app=QApplication([])
mainwindow=QMainWindow()
myui=(MainWindow_NewReservationExt())
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()