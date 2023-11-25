# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'take_sample_screen.ui'
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
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(604, 584)
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
        self.sample1_frame_1 = QFrame(self.centralwidget)
        self.sample1_frame_1.setObjectName(u"sample1_frame_1")
        self.sample1_frame_1.setFrameShape(QFrame.StyledPanel)
        self.sample1_frame_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sample1_frame_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sample1_label = QLabel(self.sample1_frame_1)
        self.sample1_label.setObjectName(u"sample1_label")
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(18)
        font.setBold(True)
        self.sample1_label.setFont(font)
        self.sample1_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.sample1_label)

        self.taking_sample_1_btn = QPushButton(self.sample1_frame_1)
        self.taking_sample_1_btn.setObjectName(u"taking_sample_1_btn")
        self.taking_sample_1_btn.setStyleSheet(u"	QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.taking_sample_1_btn)

        self.sample1_popup = QLabel(self.sample1_frame_1)
        self.sample1_popup.setObjectName(u"sample1_popup")

        self.verticalLayout_2.addWidget(self.sample1_popup)

        self.progressBar = QProgressBar(self.sample1_frame_1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #CD96CD;\n"
"    width: 10px;\n"
"    margin: 0.5px;\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)


        self.verticalLayout.addWidget(self.sample1_frame_1)

        self.sample_frame_2 = QFrame(self.centralwidget)
        self.sample_frame_2.setObjectName(u"sample_frame_2")
        self.sample_frame_2.setFrameShape(QFrame.StyledPanel)
        self.sample_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sample_frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sample2_label = QLabel(self.sample_frame_2)
        self.sample2_label.setObjectName(u"sample2_label")
        self.sample2_label.setFont(font)
        self.sample2_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.sample2_label)

        self.taking_sample_2_btn = QPushButton(self.sample_frame_2)
        self.taking_sample_2_btn.setObjectName(u"taking_sample_2_btn")
        self.taking_sample_2_btn.setStyleSheet(u"	QPushButton {\n"
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

        self.verticalLayout_3.addWidget(self.taking_sample_2_btn)

        self.sample2_popup = QLabel(self.sample_frame_2)
        self.sample2_popup.setObjectName(u"sample2_popup")

        self.verticalLayout_3.addWidget(self.sample2_popup)

        self.progressBar_2 = QProgressBar(self.sample_frame_2)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: #CD96CD;\n"
"    width: 10px;\n"
"    margin: 0.5px;\n"
"}")
        self.progressBar_2.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar_2)


        self.verticalLayout.addWidget(self.sample_frame_2)

        self.graph_frame_3 = QFrame(self.centralwidget)
        self.graph_frame_3.setObjectName(u"graph_frame_3")
        self.graph_frame_3.setFrameShape(QFrame.StyledPanel)
        self.graph_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.graph_frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graph_view_btn = QPushButton(self.graph_frame_3)
        self.graph_view_btn.setObjectName(u"graph_view_btn")
        self.graph_view_btn.setStyleSheet(u"	QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.graph_view_btn)

        self.backButton = QPushButton(self.graph_frame_3)
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

        self.horizontalLayout.addWidget(self.backButton)


        self.verticalLayout.addWidget(self.graph_frame_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sample1_label.setText(QCoreApplication.translate("MainWindow", u"You should take 20 samples", None))
        self.taking_sample_1_btn.setText(QCoreApplication.translate("MainWindow", u"Start Taking Sample Type 1", None))
        self.sample1_popup.setText("")
        self.sample2_label.setText(QCoreApplication.translate("MainWindow", u"You should take 20 samples ", None))
        self.taking_sample_2_btn.setText(QCoreApplication.translate("MainWindow", u"Start Taking Samples Type 2", None))
        self.sample2_popup.setText("")
        self.graph_view_btn.setText(QCoreApplication.translate("MainWindow", u"View the Graph", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

