##control_servo.py

import serial #serial communication
import datetime, time # time delay
import sys # to get argv module
from servo_motor import cont_servo
argvs = sys.argv # list of hikisuu

delay = int (argvs[3])

#serial settings

ser = serial.Serial(argvs[2],38400,timeout=5) # 10s-timeout baudrate=38400

#ser.write(b'<RM,>??\r\n') #send command (CR+LF)

count = 0


while True:
        f = open(argvs[1],"w")
        while True:
                ser.write(b'<RM,>??\r\n') #send command (CR+LF)
                line=ser.readline()
                line=str(datetime.datetime.now())+str(",")+line.decode('utf-8')
                li_line=line.split(',')
                try:
                        print(li_line[5]) #show Temperature measured by the sensor

                        if (float(li_line[5])>=40.0):
                                print("hoge")
                                cont_servo()
                except IndexError:
                        print("out of range")
                print(line)
                f.write(str(line)+str("\n"))
                #print now
                time.sleep(delay)
                #count += delay
        f.close()
ser.close()

