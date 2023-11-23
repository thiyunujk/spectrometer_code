# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newHome1UHdntS.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame, QLabel, QToolTip { border: 2px solid black; border-radius: 3px; padding: 1px; background-color: rgb(0, 61, 90); color: white; }")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(2, 0))
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Open Sans SemiBold"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 180))
        self.frame_3.setSizeIncrement(QSize(0, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.absorbanceBtn = QPushButton(self.frame_3)
        self.absorbanceBtn.setObjectName(u"absorbanceBtn")
        self.absorbanceBtn.setStyleSheet(u"	QPushButton {\n"
"	background-color: #138086;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: black;\n"
"    font: bold 12px;\n"
"    min-width: 3em;\n"
"    padding: 3px;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(100,170,255)\n"
"}")

        self.horizontalLayout.addWidget(self.absorbanceBtn)

        self.TransmissionBtn = QPushButton(self.frame_3)
        self.TransmissionBtn.setObjectName(u"TransmissionBtn")
        self.TransmissionBtn.setStyleSheet(u"	QPushButton {\n"
"	background-color: #138086;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: black;\n"
"    font: bold 12px;\n"
"    min-width: 3em;\n"
"    padding: 3px;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(100,170,255)\n"
"}")

        self.horizontalLayout.addWidget(self.TransmissionBtn)

        self.reflectanceBtn = QPushButton(self.frame_3)
        self.reflectanceBtn.setObjectName(u"reflectanceBtn")
        self.reflectanceBtn.setStyleSheet(u"	QPushButton {\n"
"	background-color: #138086;\n"
"    border-style: outset;\n"
"    border-width: 1px;\n"
"    border-radius: 4px;\n"
"    border-color: black;\n"
"    font: bold 12px;\n"
"    min-width: 3em;\n"
"    padding: 3px;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color:rgb(100,170,255)\n"
"}")

        self.horizontalLayout.addWidget(self.reflectanceBtn)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AI Powerd Spectrometer", None))
        self.absorbanceBtn.setText(QCoreApplication.translate("MainWindow", u"Absorbance", None))
        self.TransmissionBtn.setText(QCoreApplication.translate("MainWindow", u"Transmission", None))
        self.reflectanceBtn.setText(QCoreApplication.translate("MainWindow", u"Reflectance", None))
    # retranslateUi

