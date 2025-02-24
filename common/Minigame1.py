from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(478,850)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(-310, 630, 251, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")

        # grid layout
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(130, 30, 301, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # frame
        self.frame_4 = QtWidgets.QFrame(parent=self.gridLayoutWidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.widget = QtWidgets.QWidget(parent=self.frame_4)
        self.widget.setGeometry(QtCore.QRect(0, 160, 301, 351))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")

        # box1
        self.label_box1 = QtWidgets.QLabel(parent=self.widget)
        self.label_box1.setGeometry(QtCore.QRect(40, 20, 81, 81))
        self.label_box1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_box1.setText("")
        self.label_box1.setPixmap(QtGui.QPixmap("D:\\hoccode\\QT Designer\\TEST\\doanktlt\\ui\\../../../../../ktlt_đồ án/hop-qua-vivo-tai-nghe-op-lung-mieng-dan-600x600.jpg"))
        self.label_box1.setScaledContents(True)
        self.label_box1.setObjectName("label_box1")

        #box2
        self.label_box2 = QtWidgets.QLabel(parent=self.widget)
        self.label_box2.setGeometry(QtCore.QRect(180, 20, 81, 81))
        self.label_box2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_box2.setText("")
        self.label_box2.setPixmap(QtGui.QPixmap("D:\\hoccode\\QT Designer\\TEST\\doanktlt\\ui\\../../../../../ktlt_đồ án/hop-qua-vivo-tai-nghe-op-lung-mieng-dan-600x600.jpg"))
        self.label_box2.setScaledContents(True)
        self.label_box2.setObjectName("label_box2")

        #box3
        self.label_box3 = QtWidgets.QLabel(parent=self.widget)
        self.label_box3.setGeometry(QtCore.QRect(40, 130, 81, 81))
        self.label_box3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_box3.setText("")
        self.label_box3.setPixmap(QtGui.QPixmap("D:\\hoccode\\QT Designer\\TEST\\doanktlt\\ui\\../../../../../ktlt_đồ án/hop-qua-vivo-tai-nghe-op-lung-mieng-dan-600x600.jpg"))
        self.label_box3.setScaledContents(True)
        self.label_box3.setObjectName("label_box3")

        #box4
        self.label_box4 = QtWidgets.QLabel(parent=self.widget)
        self.label_box4.setGeometry(QtCore.QRect(180, 130, 81, 81))
        self.label_box4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_box4.setText("")
        self.label_box4.setPixmap(QtGui.QPixmap("D:\\hoccode\\QT Designer\\TEST\\doanktlt\\ui\\../../../../../ktlt_đồ án/hop-qua-vivo-tai-nghe-op-lung-mieng-dan-600x600.jpg"))
        self.label_box4.setScaledContents(True)
        self.label_box4.setObjectName("label_box4")

        #box5
        self.label_box5 = QtWidgets.QLabel(parent=self.widget)
        self.label_box5.setGeometry(QtCore.QRect(40, 240, 81, 81))
        self.label_box5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_box5.setText("")
        self.label_box5.setPixmap(QtGui.QPixmap("D:\\hoccode\\QT Designer\\TEST\\doanktlt\\ui\\../../../../../ktlt_đồ án/hop-qua-vivo-tai-nghe-op-lung-mieng-dan-600x600.jpg"))
        self.label_box5.setScaledContents(True)
        self.label_box5.setObjectName("label_box5")

        #box6
        self.label_box6 = QtWidgets.QLabel(parent=self.widget)
        self.label_box6.setGeometry(QtCore.QRect(180, 240, 81, 81))
        self.label_box6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_box6.setText("")
        self.label_box6.setPixmap(QtGui.QPixmap("D:\\hoccode\\QT Designer\\TEST\\doanktlt\\ui\\../../../../../ktlt_đồ án/hop-qua-vivo-tai-nghe-op-lung-mieng-dan-600x600.jpg"))
        self.label_box6.setScaledContents(True)
        self.label_box6.setObjectName("label_box6")


        self.frame_5 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(0, 129, 301, 31))
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_title = QtWidgets.QLabel(parent=self.frame_5)
        self.label_title.setGeometry(QtCore.QRect(30, 10, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)

        # title
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_11 = QtWidgets.QLabel(parent=self.frame_5)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 21, 16))
        self.label_11.setObjectName("label_11")

        # hình ảnh
        self.label_image = QtWidgets.QLabel(parent=self.frame_4)
        self.label_image.setGeometry(QtCore.QRect(0, 0, 301, 131))
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("D:\\hoccode\\QT Designer\\TEST\\doanktlt\\ui\\../../../../../ktlt_đồ án/subiz-minigame-la-gi-e1704609883891.jpg"))
        self.label_image.setScaledContents(True)
        self.label_image.setObjectName("label_image")


        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1723, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Hộp quà may mắn"))
        self.label_11.setText(_translate("MainWindow", "<"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())