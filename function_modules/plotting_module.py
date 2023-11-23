# function_modules/plotting_module.py
import matplotlib.pyplot as plt

def scale_and_plot_data(data_array):
    # Define the desired x-axis range
    x_min = 300
    x_max = 900

    # Calculate the scaling factor for the x-axis
    scaling_factor_x = (x_max - x_min) / (len(data_array) - 1)

    # Calculate the number of original data points per scaled x-axis point
    data_points_per_x_point = round(1 / scaling_factor_x)

    # Map the indices to the x-axis range
    x_values = [x_min + i * scaling_factor_x for i in range(len(data_array))]

    # Group the original data points based on the scaled x-axis intervals
    grouped_data = [data_array[i:i+data_points_per_x_point] for i in range(0, len(data_array), data_points_per_x_point)]

    # Calculate the average for each interval
    averaged_data = [sum(group) / len(group) for group in grouped_data]

    # Plot the averaged data
    plt.plot(x_values[:len(averaged_data)], averaged_data, label='Averaged Sensor Data')
    plt.xlabel('X Axis Label')
    plt.ylabel('Y Axis Label (Averaged)')
    plt.legend()
    plt.show()

