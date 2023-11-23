import sys
import typing
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, uic
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from function_modules.communicate_with_arduino import establish_communication
from function_modules.plotting_module import scale_and_plot_data


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('newHome1.ui', self)
    
    # button configuration
        self.absorbanceBtn.clicked.connect(self.goto_Calib_pge)
        self.TransmissionBtn.clicked.connect(self.goto_Calib_pge)
        self.reflectanceBtn.clicked.connect(self.goto_Calib_pge)
        self.reflectanceBtn.clicked.connect(self.communicate_with_arduino)

    def communicate_with_arduino(self):
        response = establish_communication()

        if response is not None:
            data_array = response  
            self.plot_data_on_qgraphicobject(data_array)

            
    def goto_Calib_pge(self):
        self.calib_pge = calibrationmain2()
        self.calib_pge.show()
        self.close()



class calibrationmain2(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("calibrationmain2.ui", self)
        self.tabWidget.setCurrentIndex(0)

    #button configuration
        self.tab1NextBtn.clicked.connect(self.switch_tabs)
        self.tab2NextBtn.clicked.connect(self.switch_tabs2)
        self.finishBtn.clicked.connect(self.goto_graph_home3)

    def switch_tabs(self):
        self.tabWidget.setCurrentIndex(1)  
    
    def switch_tabs2(self):
        self.tabWidget.setCurrentIndex(2) 

    def goto_graph_home3(self):
        self.graph_home = graphHome3()
        self.graph_home.show()
        self.close()



class graphHome3(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("graph_home3.ui",self)

     # button configuration
        self.StartButton.clicked.connect(self.startspectrometer)
        self.takesampleButton.clicked.connect(self.Take_sample_for_ML)
        self.PredictButton.clicked.connect(self.Get_Prediction)

    # Timer for live update (adjust interval as needed)
        self.update_timer = QtCore.QTimer(self)
        self.update_timer.timeout.connect(self.update_plot)
        self.update_timer.start(500)  # Update every 500 milliseconds

    def update_plot(self):
        # Update data_array with new data from Arduino (replace this with your data retrieval logic)
        # Example: self.data_array = get_new_data_from_arduino()
        # For now, let's assume it's a placeholder list
        data_array = [random.randint(0, 900) for _ in range(2090)]

        # Scale and plot the data on the existing QGraphicsView
        scale_and_plot_data(data_array, self.graphHomeqgraphic)
        
    def startspectrometer(self):
        pass

    def Take_sample_for_ML(self):
            self.take_sample_screen = TakeSampleScreen()
            self.take_sample_screen.show()
            self.close()

    def Get_Prediction(self):
        self.get_prediction_screen = GetPredictionScreen()
        self.get_prediction_screen.show()
        self.close()

class TakeSampleScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("take_sample_screen.ui", self)
        self.backButton.clicked.connect(self.show_main_window)
        self.TrainModelBtn.clicked.connect(self.model_train_screen)

        self.sample_count_1 = 0
        self.progress_1 = 0
        self.sample_count_2 = 0
        self.progress_2 = 0
        self.taking_sample_1_btn.clicked.connect(self.take_sample_1)
        self.taking_sample_2_btn.clicked.connect(self.take_sample_2)

        self.timer_1 = QtCore.QTimer(self)
        self.timer_1.timeout.connect(self.clear_popup_1)
        self.timer_1.setInterval(2000)

        self.timer_2 = QtCore.QTimer(self)
        self.timer_2.timeout.connect(self.clear_popup_2)
        self.timer_2.setInterval(2000)
    def take_sample_1(self):

        self.sample_count_1 += 1
        self.sample1_popup.setText(f"Sample {self.sample_count_1} collected")
        self.progress_1 = (self.sample_count_1 / 20) * 100
        self.sample1_progressbar.setValue(int(self.progress_1))

        if self.sample_count_1 >= 20:
            self.sample_count_1 = 0
            self.sample1_popup.setText("All samples collected")
            self.taking_sample_1_btn.setEnabled(False)

        self.timer_1.start()

    def take_sample_2(self):
        self.sample_count_2 += 1
        self.sample2_popup.setText(f"Sample {self.sample_count_2} collected")
        self.progress_2 = (self.sample_count_2 / 20) * 100
        self.sample2_progressbar.setValue(int(self.progress_2))

        if self.sample_count_2 >= 20:
            self.sample_count_2 = 0
            self.sample1_popup.setText("All samples collected")
            self.taking_sample_1_btn.setEnabled(False)

        self.timer_2.start()

    def clear_popup_1(self):
        self.sample1_popup.clear()
        self.timer_1.stop()

    def clear_popup_2(self):
        self.sample2_popup.clear()
        self.timer_2.stop()

    def model_train_screen(self):
        self.graph_screen = ModeltrainScreen()
        self.graph_screen.show()
        self.close()

    def show_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

class GetPredictionScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("prediction_screen.ui", self)
        self.backButton.clicked.connect(self.show_main_window)
        self.take_sample_btn.clicked.connect(self.show_sample_pickup_status)

        # Create and configure the timer
        self.timer_4 = QtCore.QTimer(self)
        self.timer_4.timeout.connect(self.clear_popup_pickup_status)
        self.timer_4.setInterval(3000)

    def show_sample_pickup_status(self):
        # Show the pop-up messages
        self.sample_taken_label.setText("We have successfully \ntaken a sample..")
        self.result_label.setText("Ripe")

        # Restart the timer
        self.timer_4.start()

    def clear_popup_pickup_status(self):
        # Clear the pop-up messages and stop the timer
        self.sample_taken_label.clear()
        self.result_label.clear()
        self.timer_4.stop()

    def show_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

class ModeltrainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("model_training_screen.ui", self)
        self.backButton.clicked.connect(self.show_main_window)
        self.gotoPredictionBtn.clicked.connect(self.Get_Prediction)

        self.timer_3 = QtCore.QTimer(self)
        self.timer_3.timeout.connect(self.show_popup_finished)
        self.timer_3.setInterval(2000)  

        self.timer_3.start()

    def show_popup_finished(self):
        self.model_train_finished.setText("We have finished AI Models' Train.")
        self.timer_3.stop()

    def show_main_window(self):
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()

    def Get_Prediction(self):
        self.get_prediction_screen = GetPredictionScreen()
        self.get_prediction_screen.show()
        self.close()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

 