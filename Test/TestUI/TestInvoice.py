from PyQt6.QtWidgets import QMainWindow, QApplication

from ui.MainWindowInvoicesEx import MainWindowInvoicesEx

app = QApplication([])
mainwindow = MainWindowInvoicesEx(selected_room_code)  # Không cần khởi tạo QMainWindow riêng
mainwindow.show()  # Gọi trực tiếp show()
app.exec()
