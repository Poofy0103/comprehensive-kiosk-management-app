import sys
from PyQt6 import QtWidgets

from common.sql_func import Database
from kiosk_app.controllers.MiniGameFullViewEx import MiniGameFullEx
from kiosk_app.views.FeedbacKhachhangView import MainWindow
from kiosk_app.models.Order import Order
from kiosk_app.models.SharedDataModel import SharedDataModel
from kiosk_app.views.GeneralView import GeneralView
from kiosk_app.views.CustomStackedWidget import CustomStackedWidget


class FeedbackKhachhangEx(MainWindow):
    def __init__(self, mainStackedWidget: CustomStackedWidget, sharedData: SharedDataModel, db: Database):
        super().__init__()  # Kế thừa từ FeedbackKhachhang.MainWindow
        self.sharedData = sharedData
        self.db = db
        self.mainStackedWidget = mainStackedWidget

        print(f"{self.sharedData.order.id}")
        # **Sử dụng frame chung từ GeneralView nhưng đặt kích thước = 0**
        general_view = GeneralView()  # Tạo instance
        self.frame_ngang = general_view.frame_ngang  # Truy cập thuộc tính
        self.frame_ngang.setFixedSize(0, 0)

        # **Sử dụng label hình ảnh từ GeneralView**
        self.image_label = general_view.label_image

        # **Khởi tạo các biến khác**
        self.current_rating = 0
        self.feedback_buttons = []
        self.is_submitting = False
        self.setup_connections()

    def setup_connections(self):
        if hasattr(self, 'stars'):
            for i in range(len(self.stars)):
                self.stars[i].mousePressEvent = self.create_rating_handler(i + 1)

        try:
            self.submit_button.clicked.disconnect()
        except TypeError:
            pass

        self.submit_button.clicked.connect(self.submit_feedback)

    def create_rating_handler(self, rating):
        def handler(event):
            self.set_rating(rating)
        return handler

    def set_rating(self, rating):
        self.current_rating = rating

        # Cập nhật hiển thị sao
        if hasattr(self, 'stars'):
            for i, star in enumerate(self.stars):
                star.setText("⭐" if i < rating else "☆")
                star.setStyleSheet(
                    "font-size: 22pt; color: gold;" if i < rating else "font-size: 22pt; color: black;"
                )

        # Cập nhật nhãn đánh giá
        if hasattr(self, 'rating_label'):
            self.rating_label.setText("Tốt" if rating >= 4 else "Tệ")
            self.rating_label.setStyleSheet("font-size: 10pt; font-weight: bold; color: gray;")

        # Xóa hết các lựa chọn phản hồi trước đó
        for button in self.feedback_buttons:
            self.feedback_grid.removeWidget(button)
            button.deleteLater()
            button = None
        self.feedback_buttons = []

        # Cập nhật lại danh sách các nút phản hồi phù hợp với số sao
        self.update_feedback_buttons(rating)

    def update_feedback_buttons(self, rating):
        feedback_texts = self.feedback_texts_positive if rating >= 4 else self.feedback_texts_negative
        for i, text in enumerate(feedback_texts):
            button = QtWidgets.QPushButton(text)
            button.setCheckable(True)
            button.setStyleSheet("background-color: solid lightgray; color: black")
            button.clicked.connect(lambda checked, btn=button: self.toggle_feedback_button(btn))
            self.feedback_grid.addWidget(button, i // 2, i % 2)
            self.feedback_buttons.append(button)

    def toggle_feedback_button(self, button):
        if button.isChecked():
            button.setStyleSheet("background-color: green; color: blue;")
        else:
            button.setStyleSheet("background-color: solid lightgray; color: black")

    def submit_feedback(self):
        if self.is_submitting:
            return

        self.is_submitting = True

        if not hasattr(self.sharedData, 'order') or not hasattr(self.sharedData.order, 'id'):
            QtWidgets.QMessageBox.critical(self, "Lỗi", "ID đơn hàng không hợp lệ!")
            self.is_submitting = False
            return

        order_id = self.sharedData.order.id

        if not isinstance(order_id, int):
            QtWidgets.QMessageBox.critical(self, "Lỗi", "ID đơn hàng không hợp lệ!")
            self.is_submitting = False
            return

        if self.current_rating == 0:
            QtWidgets.QMessageBox.critical(self, "Lỗi", "Vui lòng chọn số sao trước khi gửi đánh giá!")
            self.is_submitting = False
            return

        selected_reasons = [btn.text() for btn in self.feedback_buttons if btn.isChecked()]

        if self.db.update_customer_feedback(order_id, self.current_rating, selected_reasons):
            msg_box = QtWidgets.QMessageBox(self)
            msg_box.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg_box.setWindowTitle("Cửa hàng Kiosk")
            msg_box.setText("Cảm ơn bạn đã đánh giá!")
            msg_box.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)

            # Đợi người dùng bấm OK rồi mới chuyển màn hình
            if msg_box.exec() == QtWidgets.QMessageBox.StandardButton.Ok:
                self.open_minigame_view()
                self.sharedData.reset_data()
        else:
            QtWidgets.QMessageBox.critical(self, "Lỗi", "Không thể lưu đánh giá. Vui lòng thử lại!")
        self.is_submitting = False

    def open_minigame_view(self):
        minigameView = MiniGameFullEx(self.mainStackedWidget, self.sharedData, self.db)
        self.mainStackedWidget.change_screen(minigameView, self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainStackedWidget = QtWidgets.QStackedWidget()

    sharedData = SharedDataModel()
    sharedData.order = Order()
    sharedData.order.ID = 3  # Cho bất kỳ giá trị nào để test thử
    db = Database("34.101.167.101", "dev", "12345678x@X", "kioskapp")

    # Bây giờ có thể gọi FeedbackKhachhangEx mà không bị lỗi
    window = FeedbackKhachhangEx(mainStackedWidget, sharedData, db)
    window.show()
    sys.exit(app.exec())