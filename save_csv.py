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

#ser.write('<RM,>??\r\n') #send command (CR+LF)

now = datetime.datetime.now() # now no setting
count = 0


while True:
        #ser.write('<RM,>??\r\n') #send command (CR+LF)
        #line = ser.readline()
        #split_line = line.split(',') #conma de split
        f = open(argvs[1],"w")
        while True:
                ser.write('<RM,>??\r\n') #send command (CR+LF)
                line = ser.readline()
                print line
                f.write(str(count))
                f.write(",")
                f.write(line)
                #print now
                time.sleep(delay)
                count += delay
        f.close()
ser.close()

