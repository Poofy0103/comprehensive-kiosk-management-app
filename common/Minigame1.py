import os

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Hộp Quà May Mắn")
        MainWindow.setFixedSize(398, 708)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Đặt nền trắng cho toàn bộ giao diện
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget.setStyleSheet("background-color: white;")

        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Ảnh tiêu đề
        self.label_image = QtWidgets.QLabel()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "..", "kiosk_app", "resources", "images", "img_bannerminigame.png")
        pixmap = QtGui.QPixmap(image_path)
        self.label_image.setPixmap(pixmap)
        self.label_image.setScaledContents(True)
        self.label_image.setFixedHeight(150) #Size cho ảnh minigame
        main_layout.addWidget(self.label_image)

        # Tiêu đề chính
        # Layout chứa nút và tiêu đề
        button_layout1 = QtWidgets.QHBoxLayout()

        # Nút quay lại
        self.button_back = QtWidgets.QPushButton()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, "..", "kiosk_app", "resources", "images", "img_backbutton.png")
        self.button_back.setIcon(QtGui.QIcon(icon_path))
        self.button_back.setIconSize(QtCore.QSize(30, 30))
        button_layout1.addWidget(self.button_back)

        # khoảng trống giữa nút và tiêu đề
        spacer = QtWidgets.QSpacerItem(5, 5, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        button_layout1.addItem(spacer)

        # Tiêu đề chính
        self.label_title = QtWidgets.QLabel("Hộp Quà May Mắn")
        self.label_title.setStyleSheet("font-size: 20px; font-weight: bold; color: black;")
        self.label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)  # Căn giữa theo chiều dọc
        self.label_title.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        button_layout1.addWidget(self.label_title)

        main_layout.addLayout(button_layout1)

        # grid_ Layout chứa 6 hộp quà
        grid_layout = QtWidgets.QGridLayout()
        grid_layout.setSpacing(20)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(base_dir, "..", "kiosk_app", "resources", "images", "img_hopqua.png")

        # 8 hộp quà
        for i in range(8):
            button = QtWidgets.QPushButton()
            button.setFixedSize(100, 100)
            button.setIcon(QtGui.QIcon(icon_path))
            button.setIconSize(QtCore.QSize(80, 80)) # kích thước hộp quà nhỏ hơn button
            grid_layout.addWidget(button, i // 2, i % 2)

        main_layout.addLayout(grid_layout)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())