# data_communication.py
import struct

def read_data(data):
    my_list = []  # Initialize an empty list outside the function

    def send_request():
        data.write(b'r')

    def read_data_from_arduino():
        nonlocal my_list
        my_list.clear()  # Clear the list before adding new data
        num_points_to_read = 2090
        send_request()
        data_bytes = data.read(2 * num_points_to_read)
        data_list = struct.unpack(f'{num_points_to_read}H', data_bytes)
        my_list.extend(data_list)

        # Print the received data list in the console
        print(my_list)
        #print("Length of Data List:", len(my_list))

    def communicate_with_arduino():
        try:
            send_request()
            #print("Sent 'r' to Arduino. Waiting for data...")
            read_data_from_arduino()
        except Exception as e:
            print(f'Error: {e}')

    # Function to handle the "Plot Data" button click event
    communicate_with_arduino()


