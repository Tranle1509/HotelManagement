from ui.MainWindowRoomManagement import Ui_MainWindow


class MainWindowRoomManagementEx(Ui_MainWindow):
    def __init__(self):
        self.dc = Dataconnector()
        self.categories=self.dc.get_all_categories()
        self.products=self.dc.get_all_products()
        self.selected_cate=None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        pass