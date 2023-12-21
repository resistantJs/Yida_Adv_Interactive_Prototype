import threading

import serial

import time


connected = False

# modify your port name:

port = '/dev/tty.usbmodemUiFlow2_1'

baud = 115200


ser = serial.Serial(port, baud, timeout=0)

print('serial_port =', ser)


# read data from serial port and print it out:

def read_serial(ser):

   while True:

      if(ser.in_waiting > 0):

         line = ser.readline().decode()

         if(line != None):

            print(line)

            #ser.close()

            #sys.exit()  # exits thread only


# create a thread to read serial:

thread = threading.Thread(target=read_serial, args=(ser,))

thread.start()


# simple loop to write something to the serial port:

while True:

   State = "Open"

   print('write to serial..')

   ser.write((State+"\r").encode())

   time.sleep(1)