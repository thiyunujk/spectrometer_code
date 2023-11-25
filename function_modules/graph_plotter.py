from PyQt5.QtWidgets import QGraphicsScene
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class GraphPlotter:
    def __init__(self, graphics_view):
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.graphics_view = graphics_view
        self.scene = QGraphicsScene()
        self.scene.addWidget(self.canvas)
        self.graphics_view.setScene(self.scene)

    def plot_data(self, data_array):
        if data_array is not None:
            ax = self.figure.add_subplot(111)
            ax.clear()  # Clear the previous plot, if any
            ax.plot(data_array, label='Sensor Data')
            ax.set_xlabel('X Axis Label')
            ax.set_ylabel('Y Axis Label (Scaled)')
            ax.legend()
            self.canvas.draw()
