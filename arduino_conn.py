##arduino.py

import serial
import time

port = '/dev/ttyUSB0'

#ser = serial.Serial(port,38400,timeout=10)

#ser.write('<RM,>??\r\n') #send command (CR+LF)

arduino = serial.Serial('/dev/ttyACM0', 9600)
temp_low=23
temp_high=70

while True:
	arduino.write(chr(temp_low))
	arduino.write(chr(temp_high))
	#ser.write('<RM,>??\r\n') #send command (CR+LF)
