from PyQt6 import QtCore, QtGui, QtWidgets


class general_ui(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478, 850)

        # widget trung tâm
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # layout chính (dọc), gồm 3 phần
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0) # các khoảng cách xung quanh
        self.verticalLayout.setSpacing(0) # khoảng cách giữa 2 cái

        # label hình ảnh
        self.label_image = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_image.setObjectName("label_image")
        self.label_image.setMinimumSize(478, 150)
        self.label_image.setPixmap(QtGui.QPixmap("C:/Users/ADMIN/Downloads/quang-cao-la-gi-peakads.jpg"))
        self.label_image.setScaledContents(True)
        self.verticalLayout.addWidget(self.label_image)

        # thanh ngang
        self.frame_ngang = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_ngang.setObjectName("frame_ngang")
        self.frame_ngang.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_ngang.setMinimumSize(QtCore.QSize(478, 50))

        # tạo layout ngang để chứa nút và spacer
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_ngang)

        # nút quay lại
        self.pushButton_back = QtWidgets.QPushButton("Quay lại", self.frame_ngang)
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_back.setIcon(QtGui.QIcon("C:/Users/ADMIN/Downloads/icon/3994376_arrow_back_left_navigation_previous_icon.png"))
        self.pushButton_back.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_back.setFlat(True) # bỏ viền ở ngoài của nút
        self.pushButton_back.setFont(QtGui.QFont("Segoe UI", 12, QtGui.QFont.Weight.Bold))
        self.horizontalLayout.addWidget(self.pushButton_back)

        # spacer
        spacerItem = QtWidgets.QSpacerItem(349, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.verticalLayout.addWidget(self.frame_ngang) # thêm layout ngang vào layout chính


        # tạo khung chung chứa nội dung
        self.frame_chung = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_chung.setObjectName("frame_chung")
        self.frame_chung.setStyleSheet("background-color: rgb(189, 25, 6);")
        self.frame_chung.setMinimumSize(QtCore.QSize(478, 650))
        self.verticalLayout.addWidget(self.frame_chung)

        # thiết lập các ngôn ngữ và kết nối các slot
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # thiết lập văn bản cho các widget
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_back.setText(_translate("MainWindow", "Quay lại"))
