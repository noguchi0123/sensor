# -- coding: utf-8 -*-
# test/get_temp_10sec.py

import serial
import sys
import time
import datetime
import threading
import RPi.GPIO as GPIO
from GPIO_control import LED, exit_handler, servo

class TestThread(threading.Thread):
    def __init__(self, port_num, filename):
        super(TestThread, self).__init__()
        self.port_num = port_num
        self.filename = filename

    def run(self):
        f = open(self.filename, 'w')
        while True:
            try:
                ser = serial.Serial(self.port_num, 38400, timeout=10)  # 10s-timeout baudrate=38400
                ser.write(b'<RM,>??\r\n')  # send command (CR+LF)
                line = ser.readline()
                now = datetime.datetime.now()
                line = str(now.strftime("%Y/%m/%d %H:%M:%S")) + str(",") + line.decode('utf-8')
                line = line.split(',')

                velocity = float(line[2])
                temp = float(line[5])

                print(self.port_num + '/' +  line[0] + ',' + line[2] + ','
                        + line[3] + ',' + line[4] + ',' + line[5])
                f.write(line[0] + ',' + line[2] + ','
                        + line[3] + ',' + line[4] + ',' + line[5] + "\n")

                time.sleep(5)

            except IndexError:
                print('Index Error occurred')
                pass

def get_data(port_num, filename):
        #f = open('./original_data/data0.csv', 'w')
        f = open(filename, 'w')

        while True:
            try:
                ser = serial.Serial(port_num, 38400, timeout=10)  # 10s-timeout baudrate=38400
                ser.write(b'<RM,>??\r\n')  # send command (CR+LF)
                line = ser.readline()
                #now = datetime.datetime.now()
                #line = str(now.strftime("%Y/%m/%d %H:%M:%S")) + str(",") + line.decode('utf-8')
                line = str(datetime.datetime.now()) + str(",") + line.decode('utf-8')
                line = line.split(',')

                velocity = float(line[2])
                temp = float(line[5])

                #print(str(port_num) + '/' + line[0] + ',' + line[2] + ','
                #        + line[3] + ',' + line[4] + ',' + line[5])
                f.write(line[0] + ',' + line[2] + ','
                        + line[3] + ',' + line[4] + ',' + line[5] + "\n")

#                if temp >= 50.0:
#                    print('too hot')
#                        LED(11, True)
#                else:
#                    print('oh.. cool')
#                    LED(11, False)

                return(temp)
                ser.close()

                time.sleep(5)

            except IndexError:
                pass

def main():
    #all needs to run automatically
    port0 = '/dev/ttyUSB0'
    port1 = '/dev/ttyUSB1'
    port2 = '/dev/ttyUSB2'
    ##
    #th_cl1 = TestThread(port1, './original_data/data1208.csv')
    #th_cl1 = TestThread(port1, './original_data/data1208.csv')

    #th_cl1.start()
    #th_cl2.start()
    t0 = get_data(port0, './original_data/1208/data0.csv')
    t1 = get_data(port1, './original_data/1208/data1.csv')
    t2 = get_data(port2, './original_data/1208/data2.csv')
    print([t0, t1, t2])
    print(min([t0, t1, t2]))

    if (t0 <= t1 and t0 <= t2):
        LED(13, True)
        time.sleep(2)
        LED(13, False)
    elif (t1 <= t2):
        LED(12, True)
        time.sleep(2)
        LED(12, False)
    else:
        LED(11, True)
        time.sleep(2)
        LED(11, False)


    GPIO.cleanup()




if __name__ == '__main__':
    main()
