##arduino.py

import serial
import time

port = '/dev/ttyUSB0'

#ser = serial.Serial(port,38400,timeout=10)

#ser.write('<RM,>??\r\n') #send command (CR+LF)

arduino = serial.Serial('/dev/ttyACM0', 9600)
temp=23
ondo=70

while True:
	arduino.write(chr(temp))
	arduino.write(chr(ondo))
	#ser.write('<RM,>??\r\n') #send command (CR+LF)
