# communicate_with_arduino.py
import serial
from serial.tools import list_ports

def find_arduino_port():
    for port in list_ports.comports():
        if "Arduino" in port.description:
            return port.device
    return None

def establish_communication():
    arduino_port = find_arduino_port()

    if arduino_port is not None:
        try:
            with serial.Serial(arduino_port, 9600, timeout=1) as ser:
                ser.write(b'r')  # Send 'r' to trigger Arduino

                # Read the series of integers from Arduino
                data = ser.readline().decode().strip()
                data_array = list(map(int, data.split(',')))

                return data_array

        except serial.SerialException as e:
            print("Error:", e)
            return None
    else:
        print("Arduino not found. Check the connection.")
        return None
