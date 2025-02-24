from PyQt6 import QtWidgets, QtGui, QtCore
import sys

class AddTopping(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chi tiết")
        self.resize(398, 708)  # Set size
        self.setupUI()

    def setupUI(self):
        # Set main layout dọc chính cho kiosk
        self.main_layout = QtWidgets.QVBoxLayout(self)

        # Thanh tiêu đề
        self.title_label = QtWidgets.QLabel("Chi tiết")
        self.title_label.setStyleSheet(
            "background-color: #BD1906; color: white; padding: 10px; font-weight: bold; font-family: Arial; font-size: 16px;")
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Label căn giữa
        self.main_layout.addWidget(self.title_label)

        # Chọn size
        self.group_box_size = QtWidgets.QGroupBox("Chọn size")
        self.group_box_size.setStyleSheet("font-weight: bold")
        self.vertical_layout_size = QtWidgets.QHBoxLayout()
        self.size_buttons = []
        sizes = ['S', 't', 'M', 'L', 'XL', 'XXL']  # Danh sách size
        for size in sizes:
            button = QtWidgets.QPushButton(size)
            self.size_buttons.append(button)
            self.vertical_layout_size.addWidget(button)
        self.group_box_size.setLayout(self.vertical_layout_size)
        self.main_layout.addWidget(self.group_box_size)

        # Slider chọn đá
        self.group_box_ice = QtWidgets.QGroupBox("Chọn đá")
        font = QtGui.QFont()
        font.setBold(True)
        self.group_box_ice.setFont(font)
        self.vertical_layout_ice = QtWidgets.QHBoxLayout()
        self.slider_ice = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)  # Slider nằm ngang
        self.slider_ice.setMinimum(0)
        self.slider_ice.setMaximum(100)
        self.slider_ice.setValue(50)  # Giá trị mặc định 50%
        self.slider_label = QtWidgets.QLabel("50%")  # Hiển thị phần trăm thật còn mấy cái trên là đang mặc định
        self.slider_ice.valueChanged.connect(self.update_slider_label)  # Kết nối sự kiện thay đổi
        self.vertical_layout_ice.addWidget(self.slider_ice)
        self.vertical_layout_ice.addWidget(self.slider_label)
        self.group_box_ice.setLayout(self.vertical_layout_ice)
        self.main_layout.addWidget(self.group_box_ice)

        # Radio button chọn mức độ đường
        self.group_box_sugar = QtWidgets.QGroupBox("Anh Trọng có bị gay không")

        self.vertical_layout_sugar = QtWidgets.QVBoxLayout()
        self.sugar_buttons = []
        sugar_levels = ["Không gay", "Có gay", "Ít gay", "Gya vllll", "men"]
        for level in sugar_levels:
            button = QtWidgets.QRadioButton(level)
            self.sugar_buttons.append(button)
            self.vertical_layout_sugar.addWidget(button)
        self.group_box_sugar.setLayout(self.vertical_layout_sugar)
        self.main_layout.addWidget(self.group_box_sugar)

        # GridView cho topping
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setFixedHeight(300)

        self.group_box_topping = QtWidgets.QGroupBox("Chọn topping")
        self.group_box_topping.setStyleSheet("font-weight: bold")

        self.scroll_widget = QtWidgets.QWidget()
        self.grid_layout_topping = QtWidgets.QGridLayout(self.scroll_widget)
        self.topping_buttons = []

        rows = 3 # Số hàng
        cols = 3  # Số cột
        image_path = "D:/Tran-chau-den.jpg"  # Đường dẫn hình ảnh

        for col in range(cols):
            for row in range(rows):
                button = QtWidgets.QCheckBox()
                button.setFixedSize(100, 100)
                pixmap = QtGui.QPixmap(image_path)
                icon = QtGui.QIcon(pixmap)
                button.setIcon(icon)
                button.setIconSize(QtCore.QSize(80, 80))
                self.topping_buttons.append(button)
                self.grid_layout_topping.addWidget(button, row, col)

        self.scroll_widget.setMinimumSize(320, rows * 120)
        self.scroll_widget.setLayout(self.grid_layout_topping)
        self.scroll_area.setWidget(self.scroll_widget)

        self.group_box_topping.setLayout(QtWidgets.QVBoxLayout())
        self.group_box_topping.layout().addWidget(self.scroll_area)
        self.main_layout.addWidget(self.group_box_topping)

        #Hiển thị thanh số lượng
        self.group_box_quantity = QtWidgets.QGroupBox("Số lượng")
        self.group_box_quantity.setStyleSheet("font-weight:bold")
        self.frame_vertical = QtWidgets.QHBoxLayout()

        # Căn phải toàn bộ layout
        self.frame_vertical.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

        # Nút trừ
        self.minus = QtWidgets.QPushButton("-")
        self.minus.setFixedSize(50,50)
        self.minus.setStyleSheet("color: red")

        # Nút cộng
        self.plus = QtWidgets.QPushButton("+")
        self.plus.setFixedSize(50, 50)
        self.plus.setStyleSheet("color: red")

        # Hiển thị số
        self.number = QtWidgets.QLabel("1")
        self.number.setStyleSheet("color: red")

        # Add vào layout ngang
        self.frame_vertical.addWidget(self.minus)
        self.frame_vertical.addWidget(self.number)
        self.frame_vertical.addWidget(self.plus)

        # Add vào group bõ
        self.group_box_quantity.setLayout(self.frame_vertical) #setlayout vì căn khổ cho layout
        self.main_layout.addWidget(self.group_box_quantity)

        # Nút thêm vào giỏ hàng
        self.add_to_cart = QtWidgets.QPushButton("Thêm vào giỏ hàng")
        self.add_to_cart.setMinimumSize(454, 32)
        self.add_to_cart.setIcon(QtGui.QIcon("D:\\avcnro3i9.jpg"))
        self.add_to_cart.setIconSize(QtCore.QSize(24, 24))
        self.add_to_cart.setStyleSheet("background-color: #BD1906; color: white; font-weight: bold")
        self.main_layout.addWidget(self.add_to_cart)

    # hàm hiển thị phần trăm slider
    def update_slider_label(self, value):
        self.slider_label.setText(f"{value}%")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AddTopping()
    window.show()
    sys.exit(app.exec())
