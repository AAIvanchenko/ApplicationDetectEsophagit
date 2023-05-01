# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QVBoxLayout,
    QWidget)

from widgets.CamWidget import CamWidget
from widgets.CustomSlideMenu import CustomSlideMenu
import data.resourse_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(923, 653)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(12)
        self.header.setFont(font1)
        self.header.setStyleSheet(u"background-color: rgb(197, 238, 244);")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 5, 0, 0)
        self.menuButton = QPushButton(self.header)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(13)
        self.menuButton.setFont(font2)
        self.menuButton.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(86, 120, 121)\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icon/icon/menu.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(32, 32))
        self.menuButton.setFlat(True)

        self.horizontalLayout_4.addWidget(self.menuButton)

        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(0, 20))
        font3 = QFont()
        font3.setPointSize(17)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout.addWidget(self.header)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setStyleSheet(u"background-color: rgb(234, 234, 234);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(197, 238, 244);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.menu = CustomSlideMenu(self.frame)
        self.menu.setObjectName(u"menu")
        self.menu.setEnabled(True)
        self.menu.setStyleSheet(u"background-color: rgb(197, 238, 244);")
        self.verticalLayout_3 = QVBoxLayout(self.menu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.video = QPushButton(self.menu)
        self.video.setObjectName(u"video")
        self.video.setEnabled(True)
        self.video.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(86, 120, 121)\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/upload.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.video.setIcon(icon1)
        self.video.setIconSize(QSize(32, 32))
        self.video.setFlat(True)

        self.verticalLayout_3.addWidget(self.video)

        self.camera = QPushButton(self.menu)
        self.camera.setObjectName(u"camera")
        self.camera.setEnabled(True)
        self.camera.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(86, 120, 121)\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/camer.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.camera.setIcon(icon2)
        self.camera.setIconSize(QSize(32, 32))
        self.camera.setFlat(True)

        self.verticalLayout_3.addWidget(self.camera)

        self.predict = QPushButton(self.menu)
        self.predict.setObjectName(u"predict")
        self.predict.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(86, 120, 121)\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/clipboard.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.predict.setIcon(icon3)
        self.predict.setIconSize(QSize(32, 32))
        self.predict.setFlat(True)

        self.verticalLayout_3.addWidget(self.predict)

        self.verticalSpacer = QSpacerItem(13, 307, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.settings = QPushButton(self.menu)
        self.settings.setObjectName(u"settings")
        self.settings.setEnabled(True)
        self.settings.setStyleSheet(u"QPushButton:pressed {\n"
"	background-color: rgb(86, 120, 121)\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/setting.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.settings.setIcon(icon4)
        self.settings.setIconSize(QSize(32, 32))
        self.settings.setFlat(True)

        self.verticalLayout_3.addWidget(self.settings)


        self.horizontalLayout_5.addWidget(self.menu)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setKerning(False)
        self.stackedWidget.setFont(font4)
        self.stackedWidget.setTabletTracking(False)
        self.stackedWidget.setLineWidth(1)
        self.page_0 = QWidget()
        self.page_0.setObjectName(u"page_0")
        sizePolicy.setHeightForWidth(self.page_0.sizePolicy().hasHeightForWidth())
        self.page_0.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.page_0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.page_0)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setPointSize(20)
        font5.setBold(False)
        self.label_4.setFont(font5)

        self.verticalLayout_2.addWidget(self.label_4)

        self.progressBar = QProgressBar(self.page_0)
        self.progressBar.setObjectName(u"progressBar")
        font6 = QFont()
        font6.setPointSize(20)
        self.progressBar.setFont(font6)
        self.progressBar.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.progressBar.setValue(50)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.stackedWidget.addWidget(self.page_0)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        sizePolicy.setHeightForWidth(self.page_1.sizePolicy().hasHeightForWidth())
        self.page_1.setSizePolicy(sizePolicy)
        font7 = QFont()
        font7.setKerning(True)
        self.page_1.setFont(font7)
        self.verticalLayout_4 = QVBoxLayout(self.page_1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.webcamera = CamWidget(self.page_1)
        self.webcamera.setObjectName(u"webcamera")

        self.verticalLayout_4.addWidget(self.webcamera)

        self.pushButton = QPushButton(self.page_1)
        self.pushButton.setObjectName(u"pushButton")
        font8 = QFont()
        font8.setBold(True)
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  20px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.pushButton)

        self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.page_3.sizePolicy().hasHeightForWidth())
        self.page_3.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.page_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)

        self.verticalLayout_5.addWidget(self.label_2)

        self.save_result = QPushButton(self.page_3)
        self.save_result.setObjectName(u"save_result")
        self.save_result.setFont(font8)
        self.save_result.setStyleSheet(u"QPushButton {\n"
"    border-radius:  10px;\n"
"    background-color:  rgb(37, 37, 37);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  20px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(118, 118, 118);\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.save_result)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.menuButton.setText(QCoreApplication.translate("MainWindow", u" \u041c\u0435\u043d\u044e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435 Eso", None))
        self.video.setText("")
        self.camera.setText("")
        self.predict.setText("")
        self.settings.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0435\u043b\u044c \u043f\u0440\u0435\u0434\u0441\u043a\u0430\u0437\u044b\u0432\u0430\u0435\u0442 \u043f\u043e\u0434\u043e\u0436\u0434\u0438\u0442\u0435...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.save_result.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
    # retranslateUi

