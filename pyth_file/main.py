#import modules
from typing import Optional
from PySide6 import QtCore, QtGui, QtWidgets
import PySide6.QtCore
import PySide6.QtWidgets
import sys

#import Splash screen
from ui_splash_screen import Ui_SplashScreen

#IMPORT MAIN WINDOW UI
from ui_main_window import Ui_MainWindow

from pyth_file.ui_take_sample_screen import Ui_TakeSample

#global
COUNTER = 0

# Create a new class for the "Take Sample" window
class TakeSampleWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        # Create an instance of the Ui_TakeSample class
        self.ui = Ui_TakeSample()
        self.ui.setupUi(self) 

        

#MAIN WINDOW
class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    # Connect the "Take Sample" button click event to open the new window
        self.ui.take_sample_btn.clicked.connect(self.show_take_sample_window)
                        


   


#splash Screen
class SplashScreen(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)



        #remove titile bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #set app logo
        pixmap = QtGui.QPixmap("logo.png")
        self.ui.log_img.setPixmap(pixmap)
        self.ui.log_img.setScaledContents(True)
        self.ui.log_img.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)

        #hide background
        self.ui.background.setMaximumHeight(0)

        #SET INITIOLS STATUS
        self.ui.status.setText("Loading..")

        #Initialize animation
        self.logo_animation()
        self.description_animation()
        self.start_animation()

        #qtimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        #time in milisecond
        self.timer.start(35)

        #change status
        QtCore.QTimer.singleShot(2500, lambda: self.ui.status.setText("Loading Data...."))
        QtCore.QTimer.singleShot(4500, lambda: self.ui.status.setText("Loading App...."))
        QtCore.QTimer.singleShot(6500, lambda: self.ui.status.setText("Starting App...."))


    #animate app logo
    def logo_animation(self):
        opacity_effect = QtWidgets.QGraphicsOpacityEffect(self.ui.log_img)
        self.ui.log_img.setGraphicsEffect(opacity_effect)

        self.logo_opacity_animation = QtCore.QPropertyAnimation(
            opacity_effect, b'opacity', duration=1500, startValue=0, endValue=1
        )
        self.logo_opacity_animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)
        self.logo_opacity_animation.start()  


    #animate app description
    # ////////////////////////////////
    def description_animation(self):
        opacity_effect = QtWidgets.QGraphicsOpacityEffect(self.ui.background)
        self.ui.background.setGraphicsEffect(opacity_effect)

        geometry_animation = QtCore.QPropertyAnimation(
            self.ui.background,
            b'maximumHeight',
            duration = 1000,
            startValue = 0,
            endValue = 228, 
        )  
        geometry_animation.setEasingCurve(QtCore.QEasingCurve.InOutCubic)

        opacity_animation = QtCore.QPropertyAnimation(
            opacity_effect, b'opacity', duration=500, startValue= 0, endValue= 1
        )

        self.description_animation = QtCore.QParallelAnimationGroup(self.ui.background)
        self.description_animation.addAnimation(geometry_animation)
        self.description_animation.addAnimation(opacity_animation)
        
    
    
    #start animation
    def start_animation(self):
        self.anim_group = QtCore.QSequentialAnimationGroup(self)
        self.anim_group.addAnimation(self.logo_opacity_animation)
        self.anim_group.addAnimation(self.description_animation)
        self.anim_group.start()  


    #progress function
    def progress(self):
        global COUNTER

        #set value to progressbar
        self.ui.progressBar.setValue(COUNTER)
        self.ui.percentage.setText(f"{int(COUNTER)}%")

        #CLOSE SPLASH SCREEN AND OPEN APP
        if COUNTER > 100:
            #STOP TIMER
            self.timer.stop()

            #SHOW MAIN WINDOW
            self.main = MyMainWindow()
            self.main.show()

            #CLOSE SPLASH SCREEN
            self.close()

        #INCREASE COUNTER
        COUNTER += 0.5


if __name__== "__main__":
    app = QtWidgets.QApplication([])
    window = SplashScreen()
    window.show()
    sys.exit(app.exec_())