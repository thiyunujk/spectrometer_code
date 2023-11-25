# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(648, 503)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QFrame, QLabel, QToolTip {\n"
"    border: 2px solid black;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    background-color:rgb(0, 61, 90) ;\n"
"	color: white;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.home_frame = QFrame(self.frame)
        self.home_frame.setObjectName(u"home_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home_frame.sizePolicy().hasHeightForWidth())
        self.home_frame.setSizePolicy(sizePolicy)
        self.home_frame.setMinimumSize(QSize(0, 0))
        self.home_frame.setMaximumSize(QSize(16777215, 80))
        self.home_frame.setFrameShape(QFrame.StyledPanel)
        self.home_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.home_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Home_label = QLabel(self.home_frame)
        self.Home_label.setObjectName(u"Home_label")
        self.Home_label.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(31)
        font.setBold(True)
        self.Home_label.setFont(font)
        self.Home_label.setScaledContents(False)
        self.Home_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Home_label)


        self.verticalLayout_2.addWidget(self.home_frame)

        self.btn_frame = QFrame(self.frame)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setStyleSheet(u"QPushbutton{background-color: #138086;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}")
        self.btn_frame.setFrameShape(QFrame.StyledPanel)
        self.btn_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.btn_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.quit_btn = QPushButton(self.btn_frame)
        self.quit_btn.setObjectName(u"quit_btn")
        self.quit_btn.setStyleSheet(u"QPushButton {\n"
"	background-color: #138086;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 20px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(100,170,255)\n"
"}")

        self.gridLayout.addWidget(self.quit_btn, 2, 1, 1, 1)

        self.get_prediction_btn = QPushButton(self.btn_frame)
        self.get_prediction_btn.setObjectName(u"get_prediction_btn")
        self.get_prediction_btn.setStyleSheet(u"	QPushButton {\n"
"	background-color: #138086;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 20px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(100,170,255)\n"
"}")

        self.gridLayout.addWidget(self.get_prediction_btn, 1, 1, 1, 1)

        self.take_sample_btn = QPushButton(self.btn_frame)
        self.take_sample_btn.setObjectName(u"take_sample_btn")
        self.take_sample_btn.setStyleSheet(u"	QPushButton {\n"
"	background-color: #138086;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 20px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(100,170,255)\n"
"}")

        self.gridLayout.addWidget(self.take_sample_btn, 0, 0, 1, 1)

        self.train_model_btn = QPushButton(self.btn_frame)
        self.train_model_btn.setObjectName(u"train_model_btn")
        self.train_model_btn.setStyleSheet(u"	QPushButton {\n"
"	background-color: #138086;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 20px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(100,170,255)\n"
"}")

        self.gridLayout.addWidget(self.train_model_btn, 0, 1, 1, 1)

        self.calibrate_btn = QPushButton(self.btn_frame)
        self.calibrate_btn.setObjectName(u"calibrate_btn")
        self.calibrate_btn.setStyleSheet(u"	QPushButton {\n"
"	background-color: #138086;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 20px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(100,170,255)\n"
"}")

        self.gridLayout.addWidget(self.calibrate_btn, 1, 0, 1, 1)

        self.pick_a_model_btn = QPushButton(self.btn_frame)
        self.pick_a_model_btn.setObjectName(u"pick_a_model_btn")
        self.pick_a_model_btn.setStyleSheet(u"	QPushButton {\n"
"	background-color: #138086;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 20px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(100,170,255)\n"
"}")

        self.gridLayout.addWidget(self.pick_a_model_btn, 2, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.btn_frame)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Home_label.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.quit_btn.setText(QCoreApplication.translate("MainWindow", u"Quit ", None))
        self.get_prediction_btn.setText(QCoreApplication.translate("MainWindow", u"Get Prediction", None))
        self.take_sample_btn.setText(QCoreApplication.translate("MainWindow", u"Take Sample", None))
        self.train_model_btn.setText(QCoreApplication.translate("MainWindow", u"Train The Model", None))
        self.calibrate_btn.setText(QCoreApplication.translate("MainWindow", u"Calibrate the Spectrometer", None))
        self.pick_a_model_btn.setText(QCoreApplication.translate("MainWindow", u"Pick a Model", None))
    # retranslateUi

