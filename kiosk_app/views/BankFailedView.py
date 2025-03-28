from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QSpacerItem, QSizePolicy
from PyQt6 import QtWidgets
import os


class BankFailedWidget(QtWidgets.QWidget): #Thiết kế dưới dạng QWidget để thêm vào frame chung của màn hình chung
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.current_path = os.getcwd()
        self.setupMainWindow()
        self.setupContentSection()
        # self.setupStyleSheet()

    def setupMainWindow(self):
        self.count = 300
        self.setObjectName("MainWindow")
        self.resize(478, 592)
        self.setStyleSheet("background-color: #BD1906; font-family: Montserrat; font-size: 15px;")
        self.setFixedSize(478, 592)
        self.mainVLayout = QtWidgets.QVBoxLayout(self)
        self.mainVLayout.setObjectName("mainVLayout")
        self.mainVLayout.setContentsMargins(26, 64, 26, 64)
        self.redFrame = QtWidgets.QFrame(self)
        self.redFrame.setStyleSheet("background-color: #BD1906;")
        self.mainVLayout.addWidget(self.redFrame)
        self.setLayout(self.mainVLayout)

    def setupContentSection(self):
        self.whiteFrame = QtWidgets.QFrame(self)
        self.whiteFrame.setStyleSheet("background-color: white; border-radius: 15px;")

        self.contentVLayout = QtWidgets.QVBoxLayout(self)
        self.contentVLayout.setObjectName("verticalLayout")
        self.contentVLayout.setSpacing(11)
        upperLowerSpacer = QSpacerItem(40, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        middleSpacer = QSpacerItem(40, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.failedIcon = QtWidgets.QLabel(self)
        self.failedIcon.setPixmap(QPixmap("kiosk_app/resources/images/ic_failed.png"))
        self.failedIcon.setObjectName("failedIcon")
        self.failedIcon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.notificationTitle = QtWidgets.QLabel(self)
        self.notificationTitle.setObjectName("notificationTitle")
        self.notificationTitle.setText("Thanh toán thất bại!")
        self.notificationTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.notificationTitle.setStyleSheet("font-weight: 700;")
        self.instructionSubtitle = QtWidgets.QLabel(self)
        self.instructionSubtitle.setObjectName("instructionSubtitle")
        self.instructionSubtitle.setText("Vui lòng kiểm tra lại.")
        self.instructionSubtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.confirmButtonHLayout = QtWidgets.QHBoxLayout(self)
        self.confirmButtonHLayout.setObjectName("confirmButtonHLayout")
        self.confirmButton = QtWidgets.QPushButton(self)
        self.confirmButton.setMinimumHeight(35)
        self.confirmButton.setMaximumWidth(287)
        self.confirmButton.setObjectName("confirmButton")
        self.confirmButton.setText("Xác nhận")
        self.confirmButton.setStyleSheet("background-color: #BD1906; border-radius: 15px; color: white; font-weight: 700;")
        confirmButtonSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.confirmButtonHLayout.addSpacerItem(confirmButtonSpacer)
        self.confirmButtonHLayout.addWidget(self.confirmButton)
        self.confirmButtonHLayout.addSpacerItem(confirmButtonSpacer)

        self.contentVLayout.addSpacerItem(upperLowerSpacer)
        self.contentVLayout.addWidget(self.failedIcon)
        self.contentVLayout.addWidget(self.notificationTitle)
        self.contentVLayout.addWidget(self.instructionSubtitle)
        self.contentVLayout.addSpacerItem(middleSpacer)
        self.contentVLayout.addLayout(self.confirmButtonHLayout)
        self.contentVLayout.addSpacerItem(upperLowerSpacer)
        self.whiteFrame.setLayout(self.contentVLayout)
        self.whiteFrameVLayout = QtWidgets.QVBoxLayout(self)
        self.whiteFrameVLayout.setObjectName("whiteFrameVLayout")
        self.whiteFrameVLayout.addWidget(self.whiteFrame)
        self.redFrame.setLayout(self.whiteFrameVLayout)


if __name__ == '__main__':
    app=QApplication([])
    myWindow= BankFailedWidget()
    myWindow.show()
    app.exec()