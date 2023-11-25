# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pick_model.ui'
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
        MainWindow.resize(571, 568)
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
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Open Sans Condensed ExtraBold"])
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"	QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_4, 4, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"	QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_2, 2, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Open Sans Condensed ExtraBold"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"	QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"	QPushButton {\n"
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

        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.backButton = QPushButton(self.frame_2)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setStyleSheet(u"	QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.backButton)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Model 3", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Model 4", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Select Model 4", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Select Model 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Model 1", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Select Model 1", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Select Model 3", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Model2", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

