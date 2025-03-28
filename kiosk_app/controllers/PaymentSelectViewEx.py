from common.sql_func import Database
from kiosk_app.controllers.CashSuccessViewEx import CashSuccessViewEx
import kiosk_app.controllers.OrderSummaryViewEx as OrderSummaryViewEx
from kiosk_app.models.EnumClasses import PaymentMethod
from kiosk_app.views import PaymentSelectView, GeneralView
from kiosk_app.controllers import BankQRViewEx
from PyQt6.QtWidgets import QVBoxLayout
from kiosk_app.models.SharedDataModel import SharedDataModel
from kiosk_app.views.CustomStackedWidget import CustomStackedWidget


class PaymentSelectViewEx(GeneralView.GeneralView): #Kế thừa màn hình chung
    def __init__(self, mainStackedWidget: CustomStackedWidget, sharedData: SharedDataModel, db: Database): #Tất cả màn hình đều cần truyền vào 3 biến: mainStackedWidget, sharedData, db
        super().__init__()
        self.sharedData = sharedData
        self.db = db
        self.mainStackedWidget = mainStackedWidget
        self.paymentSelectWidget = PaymentSelectView.PaymentSelectWidget()
        self.paymentVLayout = QVBoxLayout(self.frame_chung) #Add màn hình hiện tại vào frame chung
        self.paymentVLayout.addWidget(self.paymentSelectWidget)
        self.paymentVLayout.setContentsMargins(0, 0, 0, 0)
        self.paymentSelectWidget.left_section.clicked.connect(self.choose_cash)
        self.paymentSelectWidget.right_section.clicked.connect(self.choose_bank)
        self.pushButton_back.clicked.connect(lambda: self.mainStackedWidget.change_screen(OrderSummaryViewEx.OrderSummaryViewEx(self.mainStackedWidget, self.sharedData, self.db), self))

    def choose_bank(self):
        """Sau khi chọn ngân hàng, app thực hiện các tác vụ sau:
        - Cập nhật paymentMethod là bank
        - Thực hiện các câu insert vào db để thêm đơn hàng
        - Chuyển sang màn hình QR
        - Huỷ màn hình hiện tại"""
        self.sharedData.order.paymentMethod = PaymentMethod.bank
        self.db.submit_order_transaction(self.sharedData.order)
        bankQRView = BankQRViewEx.BankQRViewEx(self.mainStackedWidget, self.sharedData, self.db)
        self.mainStackedWidget.change_screen(bankQRView, self, timer_hidden=True)


    def choose_cash(self):
        """Sau khi chọn ngân hàng, app thực hiện các tác vụ sau:
        - Cập nhật paymentMethod là cash
        - Thực hiện các câu insert vào db để thêm đơn hàng
        - Reset data của app (chỉ để test, thực tế bước này sẽ thực hiện sau khi KH feedback)
        - Chuyển sang màn hình thông báo đặt hàng thành công.
        - Huỷ màn hình hiện tại"""
        self.sharedData.order.paymentMethod = PaymentMethod.cash
        self.db.submit_order_transaction(self.sharedData.order)
        cashSuccessView = CashSuccessViewEx(self.mainStackedWidget, self.sharedData, self.db)
        cashSuccessView.frame_ngang.setFixedHeight(0)
        self.mainStackedWidget.change_screen(cashSuccessView, self)


