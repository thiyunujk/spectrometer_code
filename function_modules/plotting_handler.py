# function_modules/plotting_handler.py
from function_modules.plotting_module import scale_and_plot_data

class PlottingHandler:
    def __init__(self, qgraphicsobject):
        self.qgraphicsobject = qgraphicsobject

    def plot_data_on_qgraphicobject(self, data_array):
        # Modify the following line based on how your QGraphicsObject handles plotting
        self.qgraphicsobject.plot_data(data_array)
