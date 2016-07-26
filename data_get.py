import serial
ser = serial.Serial('/dev/ttyUSB0',38400,timeout=10) # 10s-timeout baudrate=38400
ser.write('<RM,>??\r\n') #send command (CR+LF)
line = ser.readline()
split_line = line.split(',')
print split_line 
print split_line[0]
print split_line[2]
print split_line[3]
print split_line[4]
print int (float(split_line[4]))
