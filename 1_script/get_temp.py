# -*- coding: utf-8 -*-
#test/get_temp.py

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
#print(line[2])
#print(line[3])
#print(line[4])
#print(line[5])
temp = line[5]

from mymodule import air_parameter
print(mymodule.air_parameter(temp))
#print(line)

#if __name__ == '__main__':
 #   main()
