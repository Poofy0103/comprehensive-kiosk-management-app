from common.sql_func import Database
from kiosk_app.controllers.BankFailedViewEx import BankFailedViewEx
from kiosk_app.models.EnumClasses import OrderStatus
from kiosk_app.models.SharedDataModel import SharedDataModel
from PyQt6.QtWidgets import QStackedWidget
from kiosk_app.views.BankCancelDialog import BankCancelDialog
from kiosk_app.views.CustomStackedWidget import CustomStackedWidget


class BankCancelDialogEx(BankCancelDialog):
    def __init__(self, mainStackedWidget: CustomStackedWidget, sharedData: SharedDataModel, db: Database, bankQRViewEx): #Tất cả màn hình đều cần truyền vào 3 biến: mainStackedWidget, sharedData, db
        super().__init__()
        self.mainStackedWidget = mainStackedWidget
        self.sharedData = sharedData
        self.db = db
        self.bankQRViewEx = bankQRViewEx
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    def accept(self):
        super().accept()
        updateQuery = "UPDATE `order` SET Status = %s WHERE ID = %s"
        rows_affected = self.db.do_any_sql(updateQuery, OrderStatus.cancelled.value, self.sharedData.order.id)
        if rows_affected:
            print(f"✅ Successfully updated {rows_affected} row(s).")
        else:
            print("❌ Update failed.")
        self.bankQRViewEx.stop_process()
        bankFailedView = BankFailedViewEx(self.mainStackedWidget, self.sharedData, self.db, "Đã huỷ đơn hàng!", "Bấm xác nhận để quay lại từ đầu.")
        self.mainStackedWidget.change_screen(bankFailedView, self)
        self.sharedData.reset_data()


