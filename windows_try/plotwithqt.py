import serial
import matplotlib.pyplot as plt
import time
import struct

num_points_to_read = 2090

# Replace 'COM3' with the appropriate serial port on your system
ser = serial.Serial('COM3', baudrate=115200, timeout=1.0)

# Wait for the Arduino to initialize
time.sleep(5)

ser.reset_input_buffer()
print("Arduino Connected")

try:
    ser.write(b'c')
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

# Define data points
sensor_data = data_list

# Set graph limits
x_min = 0
x_max = len(sensor_data) - 1
y_min = 0
y_max = max(sensor_data) + 10

# Create the plot
fig, ax = plt.subplots()

# Set x-axis
ax.set_xlim(x_min, x_max)
ax.set_xlabel('Data Point')

# Set y-axis
ax.set_ylim(y_min, y_max)
ax.set_ylabel('Sensor Reading')

# Plot data points
ax.plot(sensor_data, marker='o', linestyle='-')

# Add title
plt.title('Sensor Data')

# Show the plot
plt.show()

