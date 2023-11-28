import serial
import time
import struct

num_points_to_read = 2090

# Replace 'COM3' with the appropriate serial port on your system
ser = serial.Serial('COM3', baudrate=115200, timeout=1.0)

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
