import serial
import struct
import time
import os

class ArduinoCommunication:
    def __init__(self, port=None, baudrate=115200):
        # Detect the operating system and set the default port accordingly
        if port is None:
            self.port = self.detect_port()
        else:
            self.port = port

        self.data = serial.Serial(self.port, baudrate, timeout=1.0)
        time.sleep(2)
        self.data.reset_input_buffer()

    def read_data(self):
        try:
            self.send_request()
            # Wait for a moment to allow Arduino to process the request
            time.sleep(0.1)
            data_bytes = self.data.read(2 * 2090)
            data_list = struct.unpack('2090H', data_bytes)
            return list(data_list)
        except Exception as e:
            print(f'Error: {e}')
            return []

    def send_request(self):
        self.data.write(b'r')

    @staticmethod
    def detect_port():
        # Detect the operating system and set the default port accordingly
        if os.name == 'posix':  # Linux
            return '/dev/ttyACM0'
        elif os.name == 'nt':  # Windows
            return 'COM3'
        else:
            raise OSError("Unsupported operating system")

# Example usage:
arduino_comm = ArduinoCommunication()
data_result = arduino_comm.read_data()
print("Received Data List:", data_result)
print("Length of Data List:", len(data_result))
