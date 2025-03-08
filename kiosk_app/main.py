from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from dotenv import load_dotenv

from common.sql_func import Database
from kiosk_app.controllers.DineSelectViewEx import DineSelectViewEx
from kiosk_app.controllers.KioskMenuViewEx import KioskMenuViewEx
from kiosk_app.controllers.OrderControllerEx import OrderControllerEx
from kiosk_app.models.SharedDataModel import SharedDataModel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #Load file môi trường
        load_dotenv(dotenv_path='.env')

        #Tạo widget chồng để tích hợp nhiều màn hình trên cùng 1 cửa sổ
        self.setWindowTitle('Kiosk Application')
        self.resize(478, 850)
        self.mainStackedWidget = QStackedWidget()
        self.setCentralWidget(self.mainStackedWidget)

        #Khởi tạo các class dùng chung 1 lần duy nhất
        self.sharedData = SharedDataModel()
        self.db = Database()

        #Khởi tạo các màn hình cố định của app (menu, chọn hình thức phục vụ...)
        self.dineSelectView = DineSelectViewEx(self.mainStackedWidget, self.sharedData, self.db)
        self.menuView = KioskMenuViewEx(self.mainStackedWidget, self.sharedData, self.db)
        self.cartView = OrderControllerEx(self.mainStackedWidget, self.sharedData, self.db) # CHECK GIÙM EM


        #Thêm các màn hình theo thứ tự
        self.mainStackedWidget.addWidget(self.menuView)
        self.mainStackedWidget.addWidget(self.dineSelectView)


        #Đặt màn hình đầu tiên
        self.mainStackedWidget.setCurrentWidget(self.menuView)

        #Kết nối màn hình-> CHECK GIÙM EM
        self.menuView.kioskMenuWidget.pushButton_shoppingcart.clicked.connect(self.show_cartView)
    def show_cartView(self):
        self.mainStackedWidget.setCurrentWidget(self.cartView)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
