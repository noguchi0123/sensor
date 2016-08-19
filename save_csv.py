##save_csv.py

#import psycopg2 # python-posgresql connection
import serial #serial communication
import datetime, time # time delay
import sys # to get argv module

argvs = sys.argv # list of hikisuu

delay = int (argvs[3])

#serial settings

#ser = serial.Serial('/dev/ttyUSB0',38400,timeout=10) # 10s-timeout baudrate=38400
ser = serial.Serial(argvs[2],38400,timeout=5) # 10s-timeout baudrate=38400

#ser.write(b'<RM,>??\r\n') #send command (CR+LF)

count = 0


while True:
        f = open(argvs[1],"w")
        while True:
                ser.write(b'<RM,>??\r\n') #send command (CR+LF)
                line=ser.readline()
                line=str(datetime.datetime.now())+str(",")+line.decode('utf-8')
                #line=line.split(',')
                print(line)
		#f.write(str(count)+","+str(line)+str("\r\n"))
                #f.write(str(count))
                #f.write(",")
                f.write(str(line)+str("\n"))
                #print now
                time.sleep(delay)
                #count += delay
        f.close()
ser.close()

