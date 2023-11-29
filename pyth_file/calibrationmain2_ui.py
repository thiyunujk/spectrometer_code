# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calibrationmain2ydrKPb.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpinBox, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 324)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.tab1.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.tab1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.tab1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 191, 261))
        self.frame.setStyleSheet(u"QFrame, QLabel, QToolTip {\n"
"    border: 2px solid black;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    background-color:rgb(0, 61, 90) ;\n"
"	color: white;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 20, 141, 41))
        font = QFont()
        font.setFamilies([u"Tw Cen MT"])
        font.setPointSize(13)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 60, 141, 41))
        font1 = QFont()
        font1.setFamilies([u"Tw Cen MT"])
        font1.setPointSize(13)
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 120, 191, 41))
        font2 = QFont()
        font2.setFamilies([u"Tw Cen MT"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_8.setFont(font2)
        self.storeNowBtn = QPushButton(self.frame)
        self.storeNowBtn.setObjectName(u"storeNowBtn")
        self.storeNowBtn.setGeometry(QRect(0, 160, 75, 24))
        self.storeNowBtn.setStyleSheet(u"	QPushButton {\n"
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
        self.tab1NextBtn = QPushButton(self.frame)
        self.tab1NextBtn.setObjectName(u"tab1NextBtn")
        self.tab1NextBtn.setGeometry(QRect(100, 230, 75, 24))
        self.tab1NextBtn.setStyleSheet(u"	QPushButton {\n"
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
        self.spinBox_3 = QSpinBox(self.frame)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(150, 30, 42, 22))
        self.spinBox_4 = QSpinBox(self.frame)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setGeometry(QRect(150, 70, 42, 22))
        self.Tab1graphicsView = QGraphicsView(self.frame_2)
        self.Tab1graphicsView.setObjectName(u"Tab1graphicsView")
        self.Tab1graphicsView.setGeometry(QRect(190, 0, 251, 261))

        self.horizontalLayout.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tab1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout = QGridLayout(self.tab_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_5 = QFrame(self.tab_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.Tab2graphicsView_live = QGraphicsView(self.frame_5)
        self.Tab2graphicsView_live.setObjectName(u"Tab2graphicsView_live")
        self.Tab2graphicsView_live.setGeometry(QRect(0, 20, 321, 101))
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 171, 16))
        font3 = QFont()
        font3.setFamilies([u"Tw Cen MT"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.label_10.setFont(font3)

        self.gridLayout.addWidget(self.frame_5, 0, 1, 1, 1)

        self.frame_6 = QFrame(self.tab_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.Tab2graphicsView_ref = QGraphicsView(self.frame_6)
        self.Tab2graphicsView_ref.setObjectName(u"Tab2graphicsView_ref")
        self.Tab2graphicsView_ref.setGeometry(QRect(0, 20, 441, 101))
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 0, 271, 21))
        self.label_11.setFont(font3)
        self.tab2NextBtn = QPushButton(self.frame_6)
        self.tab2NextBtn.setObjectName(u"tab2NextBtn")
        self.tab2NextBtn.setGeometry(QRect(360, 0, 75, 21))
        self.tab2NextBtn.setStyleSheet(u"	QPushButton {\n"
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

        self.gridLayout.addWidget(self.frame_6, 1, 0, 1, 2)

        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QSize(120, 0))
        self.frame_4.setStyleSheet(u"QFrame, QLabel, QToolTip {\n"
"    border: 2px solid black;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    background-color:rgb(0, 61, 90) ;\n"
"	color: white;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 10, 121, 21))
        font4 = QFont()
        font4.setFamilies([u"Tw Cen MT"])
        font4.setPointSize(12)
        self.label_9.setFont(font4)
        self.whiteRefBtn = QPushButton(self.frame_4)
        self.whiteRefBtn.setObjectName(u"whiteRefBtn")
        self.whiteRefBtn.setGeometry(QRect(10, 33, 91, 81))
        font5 = QFont()
        font5.setPointSize(15)
        self.whiteRefBtn.setFont(font5)
        self.whiteRefBtn.setIconSize(QSize(11, 11))

        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_7 = QFrame(self.tab_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 0, 201, 16))
        self.label_13.setFont(font3)
        self.Tab3graphicsView_live = QGraphicsView(self.frame_7)
        self.Tab3graphicsView_live.setObjectName(u"Tab3graphicsView_live")
        self.Tab3graphicsView_live.setGeometry(QRect(0, 20, 321, 101))

        self.gridLayout_2.addWidget(self.frame_7, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.tab_3)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QSize(120, 0))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 0, 120, 127))
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QSize(120, 0))
        self.frame_9.setStyleSheet(u"QFrame, QLabel, QToolTip {\n"
"    border: 2px solid black;\n"
"    border-radius: 4px;\n"
"    padding: 2px;\n"
"    background-color:rgb(0, 61, 90) ;\n"
"	color: white;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 10, 121, 21))
        self.label_12.setFont(font4)
        self.darkrefBtn = QPushButton(self.frame_9)
        self.darkrefBtn.setObjectName(u"darkrefBtn")
        self.darkrefBtn.setGeometry(QRect(10, 33, 91, 81))
        font6 = QFont()
        font6.setPointSize(16)
        self.darkrefBtn.setFont(font6)
        self.darkrefBtn.setIconSize(QSize(18, 18))

        self.gridLayout_2.addWidget(self.frame_3, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.tab_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 0, 301, 21))
        self.label_14.setFont(font3)
        self.Tab3graphicsView_ref = QGraphicsView(self.frame_8)
        self.Tab3graphicsView_ref.setObjectName(u"Tab3graphicsView_ref")
        self.Tab3graphicsView_ref.setGeometry(QRect(0, 20, 441, 101))
        self.finishBtn = QPushButton(self.frame_8)
        self.finishBtn.setObjectName(u"finishBtn")
        self.finishBtn.setGeometry(QRect(360, 0, 75, 21))
        self.finishBtn.setStyleSheet(u"	QPushButton {\n"
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

        self.gridLayout_2.addWidget(self.frame_8, 1, 0, 1, 2)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Scans to average :", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Boxcar width :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"No dark specrum stored", None))
        self.storeNowBtn.setText(QCoreApplication.translate("MainWindow", u"Store now", None))
        self.tab1NextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Live Acquistion", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Reference spectrum preview", None))
        self.tab2NextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Store Reference", None))
        self.whiteRefBtn.setText(QCoreApplication.translate("MainWindow", u"white ref", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Live Acquistion", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Store Reference", None))
        self.darkrefBtn.setText(QCoreApplication.translate("MainWindow", u"Dark Ref", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Reference spectrum preview", None))
        self.finishBtn.setText(QCoreApplication.translate("MainWindow", u"Finish", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 3", None))
    # retranslateUi

