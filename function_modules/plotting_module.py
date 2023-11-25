import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from arduino_communication import ArduinoCommunication

def scale_and_plot_data(data_array, canvas):
    # Define the desired x-axis range
    x_min = 300
    x_max = 900

    # Calculate the scaling factor for the x-axis
    scaling_factor_x = (x_max - x_min) / (len(data_array) - 1)

    # Calculate the number of original data points per scaled x-axis point
    data_points_per_x_point = round(1 / scaling_factor_x)

    # Map the indices to the x-axis range
    x_values = [x_min + i * scaling_factor_x for i in range(len(data_array))]

    # Scale the y-axis values between 0 and 1
    y_values = [(value - min(data_array)) / (max(data_array) - min(data_array)) for value in data_array]

    # Plot the original data on the provided canvas
    canvas.plot(x_values, y_values, label='Sensor Data')
    canvas.set_xlabel('X Axis Label')
    canvas.set_ylabel('Y Axis Label (Scaled)')
    canvas.legend()
    canvas.figure.canvas.draw()

def main():
    # Create an instance of ArduinoCommunication
    arduino_comm = ArduinoCommunication()

    # Read data from Arduino
    data_array = arduino_comm.read_data()

    # Plot the scaled data
    fig, ax = plt.subplots()
    canvas = FigureCanvas(fig)
    scale_and_plot_data(data_array, ax)
    plt.show()

if __name__ == "__main__":
    main()
