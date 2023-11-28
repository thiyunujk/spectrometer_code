import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import serial
import time
import struct

import random

# Create an empty list
data_list = []

# Generate 2090 random integer values between 390 and 800
for _ in range(2090):
    data_list.append(random.randint(390, 800))

#print(data_list)




num_points_to_read = 2090

# Replace 'COM3' with the appropriate serial port on your system
ser = serial.Serial('COM10', baudrate=115200, timeout=1.0)

# Wait for the Arduino to initialize
time.sleep(2)

ser.reset_input_buffer()
print("Arduino Connected")

try:
    ser.write(b'r')
    print("Sent 'r' to Arduino. Waiting for data...")
except Exception as e:
    print(f'Error: {e}')

data_list = []

while True:
    # Check if data is available
    if ser.in_waiting > 0:
        # Read the data bytes
        data_bytes = ser.read(2 * num_points_to_read)

        # Unpack the data bytes into integers
        data_points = struct.unpack(f'{num_points_to_read}H', data_bytes)

        # Append the data points to the list
        data_list.extend(data_points)

        # Print the data points
        print(data_list)

        # Break the loop after receiving the desired data
        if len(data_list) == num_points_to_read:
            break

print(f"Received {len(data_list)} data points.")

ser.close()
print("Serial port closed.")


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
    

    # Read data from Arduino
    data_array = data_list

    # Plot the scaled data
    fig, ax = plt.subplots()
    canvas = FigureCanvas(fig)
    scale_and_plot_data(data_array, ax)
    plt.show()

if __name__ == "__main__":
    main()