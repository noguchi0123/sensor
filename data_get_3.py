# -*- coding: utf-8 -*-
#test/data_get_3.py

import serial
import sys
import datetime
argvs = sys.argv

port = argvs[1]
ser = serial.Serial(port,38400,timeout=10) # 10s-timeout baudrate=38400
ser.write(b'<RM,>??\r\n') #send command (CR+LF)
line = ser.readline()
line = str(datetime.datetime.now()) + str(",") + line.decode('utf-8')
line = line.split(',')
#print(line[0])
#print(line[1])
#print(line[4])
print(line)


