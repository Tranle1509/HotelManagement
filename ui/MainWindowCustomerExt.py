from PyQt6.QtWidgets import QMainWindow

from Test.TestData.TestCustomer_Write import c
from ui.MainWindowCustomer import Ui_MainWindow


class MainWindowCustomerExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

        self.setupSignalAndSlot()
        self.xem_chi_tiet()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        pass
    def xem_chi_tiet(self):
        self.lineEdit_CusCode.setText(str(c.code))
        self.lineEdit_Name.setText(c.name)
        self.lineEdit_Email.setText(c.email)
        self.lineEdit_Identity.setText(str(c.identity))
        self.lineEdit_Phone.setText(str(c.phone))
