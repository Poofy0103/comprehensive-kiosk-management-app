from PyQt6 import QtCore, QtGui, QtWidgets

class UI_noluck(QtWidgets.QDialog):
    """Cửa sổ hiển thị kết quả mở hộp quà --- không trúng gì hết"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Kết Quả")
        self.setFixedSize(398, 708)
        self.setStyleSheet("background-color: white;")

        # Layout chính
        layout = QtWidgets.QVBoxLayout(self)

        # Hình ảnh minigame phần no luck
        self.label_image_main = QtWidgets.QLabel(self)
        self.label_image_main.setPixmap(QtGui.QPixmap("D:/ktlt_đồ án/minigame-choi-vui-trung-lon-01590979733.jpg"))
        self.label_image_main.setFixedHeight(150)
        self.label_image_main.setScaledContents(True)
        self.label_image_main.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_image_main)

        # Spacer để căn giữa ảnh "Better Luck Next Time"
        layout.addStretch(1)

        # Ảnh chúc may mắn lần sau (Better Luck Next Time)
        self.label_image_noluck = QtWidgets.QLabel(self)
        pixmap = QtGui.QPixmap(
            r"D:\hoccode\QT Designer\TEST\doanktlt\anh\pngtree-better-luck-next-time-setback-fail-png-image_10561842.png")
        self.label_image_noluck.setPixmap(pixmap)
        self.label_image_noluck.setScaledContents(True)
        self.label_image_noluck.setFixedSize(250, 150)  # Điều chỉnh kích thước ảnh
        self.label_image_noluck.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        # Layout ngang để căn giữa ảnh
        image_layout = QtWidgets.QHBoxLayout()
        image_layout.addStretch(1)
        image_layout.addWidget(self.label_image_noluck)
        image_layout.addStretch(1)
        layout.addLayout(image_layout)

        # Label chúc may mắn lần sau
        self.label_lucknext = QtWidgets.QLabel("Chúc bạn may mắn lần sau!", self)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_lucknext.setFont(font)
        self.label_lucknext.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label_lucknext)

        # Spacer để đẩy hai button xuống góc dưới
        layout.addStretch(1)

        # Layout ngang chứa hai button
        button_layout = QtWidgets.QVBoxLayout()

        self.pushButton_gotocart = QtWidgets.QPushButton("Đi tới giỏ hàng", self)
        self.pushButton_gotocart.setStyleSheet("background-color: red; color: white; font-weight: bold; font-size: 15px")
        self.pushButton_gotocart.setFixedSize(150, 40)
        self.pushButton_gotocart.clicked.connect(self.accept)

        self.pushButton_back = QtWidgets.QPushButton("Bỏ qua", self)
        self.pushButton_back.setStyleSheet("background-color: red; color: white; font-weight: bold; font-size: 15px")
        self.pushButton_back.setFixedSize(150, 40)
        self.pushButton_back.clicked.connect(self.reject)

        button_layout.addWidget(self.pushButton_gotocart, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        button_layout.addWidget(self.pushButton_back, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        layout.addLayout(button_layout)

# Khởi chạy ứng dụng
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = UI_noluck()
    window.show()
    sys.exit(app.exec())
