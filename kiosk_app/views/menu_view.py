import os
import pymysql
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QLabel, QVBoxLayout, QFrame, QPushButton, \
    QScrollArea, QWidget, QGroupBox, QGridLayout, QStackedWidget


# Database Class
class database:
    def __init__(self):
        self.connection = pymysql.connect(
            host="34.101.167.101",
            user="dev",
            password="12345678x@X",
            database="kioskapp",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def fetch_categories(self):
        self.cursor.execute("SELECT ID, Name, ImageURL FROM Category")
        return self.cursor.fetchall()

    def fetch_itemsall(self):
        query = """
        SELECT fi.ID 
              ,fi.Name 
              ,fi.IsBestSeller 
              ,fh.Price 
              ,CAST(IF(pfi.FoodItemID IS NOT NULL, IF(p.IsPercent, fh.Price*(1-(p.Discount/100)), fh.Price - p.Discount), fh.Price) AS UNSIGNED) AS DiscountedPrice 
              ,fi.ImageURL
              ,pfi.PromotionID
        FROM fooditem fi 
        INNER JOIN fooditem_history fh
            ON fi.ID = fh.FoodItemId
        LEFT JOIN promotionfooditem pfi
            ON fi.ID = pfi.FoodItemID
        LEFT JOIN promotion p
            ON p.ID = pfi.PromotionID
        WHERE fi.IsFulltime = True
        AND fh.IsEffective = True 
        UNION
        SELECT fi.ID
            ,fi.Name
            ,fi.IsBestSeller
            ,fh.Price
            ,CAST(IF(pfi.FoodItemID IS NOT NULL, IF(p.IsPercent, fh.Price*(1-(p.Discount/100)), fh.Price - p.Discount), fh.Price) AS UNSIGNED) AS DiscountedPrice
            ,fi.ImageURL
            ,pfi.PromotionID 
        FROM fooditem fi 
        INNER JOIN fooditem_history fh
            ON fi.id = fh.FoodItemId
        LEFT JOIN promotionfooditem pfi
            ON fi.ID = pfi.FoodItemID
        LEFT JOIN promotion p
            ON p.ID = pfi.PromotionID
        WHERE fi.IsFulltime = False 
        AND fh.IsEffective = True
        AND fi.Days LIKE CONCAT('%',CAST(WEEKDAY(current_timestamp) AS CHAR),'%')
        AND current_time BETWEEN AvailableStartTime AND AvailableEndTime;
        """
        # print(query)
        self.cursor.execute(query)
        return self.cursor.fetchall()


    # truyen vao category_id de lay cac sp thuoc category_id do
    def fetch_items(self, category_id):
        query = f"""
        SELECT fi.ID 
              ,fi.Name 
              ,fi.IsBestSeller 
              ,fh.Price 
              ,CAST(IF(pfi.FoodItemID IS NOT NULL, IF(p.IsPercent, fh.Price*(1-(p.Discount/100)), fh.Price - p.Discount), fh.Price) AS UNSIGNED) AS DiscountedPrice,
            fi.ImageURL, pfi.PromotionID
        FROM fooditem fi
        INNER JOIN fooditem_history fh 
            ON fi.ID = fh.FoodItemId
        LEFT JOIN promotionfooditem pfi 
            ON fi.ID = pfi.FoodItemID
        LEFT JOIN promotion p 
            ON p.ID = pfi.PromotionID
        WHERE fi.IsFulltime = True 
        AND fh.IsEffective = True 
        AND fi.CategoryID = {category_id}
        UNION
        SELECT fi.ID
            ,fi.Name
            ,fi.IsBestSeller
            ,fh.Price,
            CAST(IF(pfi.FoodItemID IS NOT NULL, IF(p.IsPercent, 
            fh.Price * (1 - (p.Discount / 100)), fh.Price - p.Discount), 
            fh.Price) AS UNSIGNED) AS DiscountedPrice,
            fi.ImageURL, pfi.PromotionID
        FROM fooditem fi
        INNER JOIN fooditem_history fh 
            ON fi.ID = fh.FoodItemId
        LEFT JOIN promotionfooditem pfi 
            ON fi.ID = pfi.FoodItemID
        LEFT JOIN promotion p 
            ON p.ID = pfi.PromotionID
        WHERE fi.IsFulltime = False AND fh.IsEffective = True
        AND fi.Days LIKE CONCAT('%', CAST(WEEKDAY(CURRENT_TIMESTAMP) AS CHAR), '%')
        AND current_time BETWEEN AvailableStartTime AND AvailableEndTime
        AND fi.CategoryID = {category_id};
        """
        # print(query)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


# Category Frame
class CategoryFrame(QFrame):
    def __init__(self, image_path, name, category_id, MainWindow):
        super().__init__()
        self.main_window = MainWindow  # khi bấm vào frame sẽ kích hoạt mainwindow
        self.category_id = category_id  # lấy category_id để load những sp có cùng category_id
        self.setMaximumSize(100, 116)
        self.setStyleSheet("background-color: #f0f0f0")

        self.layout_categoryFrame = QVBoxLayout(self)
        self.layout_categoryFrame.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.img_category = QLabel(self)
        self.img_category.setMaximumSize(90, 90)
        self.img_category.setPixmap(QtGui.QPixmap(image_path))
        self.img_category.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.img_category.setScaledContents(True)
        self.layout_categoryFrame.addWidget(self.img_category)

        self.name_category = QLabel(name)
        self.name_category.setFont(QtGui.QFont("Segoe UI", 10, QtGui.QFont.Weight.Bold))
        self.name_category.setStyleSheet("color: #BD1906;")
        self.name_category.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout_categoryFrame.addWidget(self.name_category)

    # xử lý sự kiện khi có click vào categoryFrame
    def mousePressEvent(self, event):
        print(f"Category ID clicked: {self.category_id}")
        self.main_window.load_items(self.name_category.text(), self.category_id)  # lấy tên của category và id
        super().mousePressEvent(event)


class ProductFrame(QFrame):
    def __init__(self, image_path, price, name, is_bestseller):
        super().__init__()
        self.current_path = os.getcwd()
        self.setFixedSize(130, 200)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;
                border: 2px solid rgba(0, 0, 0, 0.2);
            }
            QLabel {
                border: none;
                background: transparent;
                color: #000000
            }
        """)

        # LAYOUT PRODUCTFRAME
        layout_ProductFrame = QVBoxLayout(self)
        layout_ProductFrame.setContentsMargins(5, 5, 5, 5)
        # layout_ProductFrame.setSpacing(0)

        # Hình ảnh sp
        self.img_product = QLabel()
        self.img_product.setFixedSize(110, 110)
        self.img_product.setPixmap(QtGui.QPixmap(image_path))
        self.img_product.setScaledContents(True)
        layout_ProductFrame.addWidget(self.img_product, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.price_product = QLabel(price)
        self.price_product.setFont(QtGui.QFont("Segoe UI", 10))
        self.price_product.setWordWrap(True)
        self.price_product.setStyleSheet("color: #000000")
        layout_ProductFrame.addWidget(self.price_product, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.name_product = QLabel(name)
        self.name_product.setFont(QtGui.QFont("Segoe UI", 10, QtGui.QFont.Weight.Bold))
        self.name_product.setWordWrap(True)
        self.name_product.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if is_bestseller:
            # layout icon + tên sp
            self.layout_ProductName = QHBoxLayout()
            # self.layout_ProductName.setContentsMargins(0, 0, 0, 0)
            self.layout_ProductName.setSpacing(5)
            layout_ProductFrame.addLayout(self.layout_ProductName)

            # hình ảnh icon
            self.img_bestseller = QLabel()
            self.img_bestseller.setFixedSize(30, 30)
            self.img_bestseller.setPixmap(QtGui.QPixmap(f"{self.current_path}/../resources/images/bestseller.png"))
            self.img_bestseller.setScaledContents(True)

            # thêm icon và tên vào layout
            self.layout_ProductName.addWidget(self.img_bestseller)
            self.layout_ProductName.addWidget(self.name_product)

        else:
            layout_ProductFrame.addWidget(self.name_product, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)


class Button(QPushButton):
    def __init__(self, name, icon_path):
        super().__init__()
        self.setText(name)
        self.setIcon(QtGui.QIcon(icon_path))
        self.setIconSize(QtCore.QSize(30, 30))
        self.setFlat(True)  # bỏ viền ở ngoài của nút
        self.setFont(QtGui.QFont("Segoe UI", 14, QtGui.QFont.Weight.Bold))
        self.setStyleSheet("""
                    QPushButton {
                        background-color: #bd1906;
                        color: #ffffff;
                        padding: 5px;
                        border-radius: 0px;
                    }
                    QPushButton:pressed {
                        background-color:#a61505;
                    }
                """)
class groupbox(QGroupBox):
    def __init__(self, category_name):
        super().__init__()
        self.setTitle(category_name)
        self.setFont(QtGui.QFont("Segoe UI", 14, QtGui.QFont.Weight.Bold))
        self.setStyleSheet("color: #bd1906;")
        self.setMinimumSize(QtCore.QSize(317, 635))
        # layout
        self.layout_groupbox = QVBoxLayout(self)
        # vùng cuộn
        self.scroll_product = QScrollArea()
        self.scroll_product.setWidgetResizable(True)
        self.layout_groupbox.addWidget(self.scroll_product)
        # widget trong vùng cuộn
        self.scroll_widget = QWidget()
        self.scroll_product.setWidget(self.scroll_widget)
        # gridlayout trong widget
        self.gridlayout = QGridLayout(self.scroll_widget)
        self.gridlayout.setSpacing(10)
        self.gridlayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

    def add_product(self, product, row, col):
        self.gridlayout.addWidget(product, row, col)

    def delete_product(self):
        while self.gridlayout.count() != 0:
            item = self.gridlayout.takeAt(0).widget()  # lấy widget ở vị trí đầu tiên của gridlayout
            item.setParent(None)


# Main UI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.db = database()
        self.current_path = os.getcwd()
        MainWindow.resize(478, 850)

        # widget trung tâm
        self.centralwidget = QWidget(parent=MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # LAYOUT CHÍNH, gồm 3 phần
        self.verticalLayout = QVBoxLayout(self.centralwidget)

        # BANNER
        self.label_banner = QLabel(parent=self.centralwidget)
        self.label_banner.setMinimumSize(478, 150)
        self.label_banner.setPixmap(
            QtGui.QPixmap(f"{self.current_path}/../resources/images/quang-cao-la-gi-peakads.png"))
        self.label_banner.setScaledContents(True)
        self.verticalLayout.addWidget(self.label_banner)

        # KHUNG CONTENT (frame menu + groupbox)
        self.frame_chung = QFrame(parent=self.centralwidget)
        self.frame_chung.setStyleSheet("background-color: #ffffff;")
        self.verticalLayout.addWidget(self.frame_chung)
        # layout
        self.layout_content = QHBoxLayout(self.frame_chung)

        # FRAME MENU (tiêu đề + nội dung)
        self.frame_menu = QFrame(self.centralwidget)
        self.frame_menu.setMaximumSize(125, 635)
        self.layout_content.addWidget(self.frame_menu)
        # layout
        self.layout_menu = QVBoxLayout(self.frame_menu)

        # tiêu đề
        self.menu_header = QLabel("Menu")
        self.menu_header.setFont(QtGui.QFont("Segoe UI", 14, QtGui.QFont.Weight.Bold))
        self.menu_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.menu_header.setStyleSheet("background-color: #bd1906; color: #ffffff; border-radius: 5px;")
        self.layout_menu.addWidget(self.menu_header)

        # nội dung
        self.frame_typeMenu = QFrame(self.centralwidget)
        self.frame_typeMenu.setMaximumSize(116, 585)
        # vùng cuộn
        self.scroll_menu = QScrollArea(self.frame_typeMenu)
        self.scroll_menu.setWidgetResizable(True)
        self.layout_menu.addWidget(self.scroll_menu)

        # tạo widget chứa nội dung cuộn -> chèn thêm layout
        self.widget_scroll = QWidget()
        self.scroll_menu.setWidget(self.widget_scroll)  # nhớ chú ý
        # layout chứa category
        self.layout_category = QVBoxLayout(self.widget_scroll)
        self.layout_category.setContentsMargins(0, 10, 0, 10)
        self.layout_category.setSpacing(10)
        self.layout_category.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # GROUPBOX
        self.groupbox_item = groupbox("Tất cả món")
        self.layout_content.addWidget(self.groupbox_item)

        categories = self.load_categories()
        if len(categories) > 0:
            self.load_items(None)

        # LAYOUT CHỨA 2 NÚT
        self.layout_2button = QtWidgets.QHBoxLayout()
        self.verticalLayout.addLayout(self.layout_2button)

        # nút trang chủ
        self.pushButton_home = Button("Trang chủ", f"{self.current_path}/../resources/images/home.png")
        self.layout_2button.addWidget(self.pushButton_home)
        # nút giỏ hàng
        self.pushButton_shoppingcart = Button("Giỏ hàng", f"{self.current_path}/../resources/images/shopping_cart.png")
        self.layout_2button.addWidget(self.pushButton_shoppingcart)

    def load_categories(self):
        categories = self.db.fetch_categories()  # lấy danh sách của các category (ImageURL, Name, ID)
        for category in categories:
            category = CategoryFrame(category["ImageURL"], category["Name"], category["ID"], self)
            self.layout_category.addWidget(category)
        return categories

    def load_items(self, category_name, category_id=None):
        self.groupbox_item.delete_product()
        if category_id:
            self.groupbox_item.setTitle(category_name)
            items = self.db.fetch_items(category_id)
        else:
            items = self.db.fetch_itemsall()
        row, col = 0, 0
        for item in items:
            item = ProductFrame(item["ImageURL"], str(item["DiscountedPrice"]), item["Name"], item["IsBestSeller"])
            self.groupbox_item.add_product(item, row, col)
            col += 1
            if col == 2:
                col = 0
                row += 1
class MainWindow_Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow

    def show(self):
        self.MainWindow.show()


app = QApplication([])
window = MainWindow_Ext()
window.setupUi(QMainWindow())
window.show()
app.exec()



