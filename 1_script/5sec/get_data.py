# -- coding: utf-8 -*-
# test/get_temp_10sec.py

import serial
import sys
import time
import datetime
import threading
from GPIO_control import LED, exit_handler, servo

import wiringpi #to control servo motors through GPIO

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
                line = str(datetime.datetime.now()) + str(",") + line.decode('utf-8')
                line = line.split(',')

                velocity = float(line[2])
                temp = float(line[5])

                print(self.port_num + '/' +  line[0] + ',' + line[2] + ','
                        + line[3] + ',' + line[4] + ',' + line[5])
                f.write(line[0] + ',' + line[2] + ','
                        + line[3] + ',' + line[4] + ',' + line[5] + "\n")

                time.sleep(5)

            except IndexError:
                pass

def main():
    #all needs to run automatically
    port0 = '/dev/ttyUSB0'
    port1 = '/dev/ttyUSB1'
    port2 = '/dev/ttyUSB2'
    ##
    th_cl1 = TestThread(port1, './original_data/data1208.csv')
    th_cl1 = TestThread(port1, './original_data/data1208.csv')

    #th_cl1.start()
    #th_cl2.start()

    f = open('./original_data/data1209.csv', 'w')
    ##
    servo_pin = 18

    param = sys.argv
    set_degree = int(param[1])
    print(set_degree)

    wiringpi.wiringPiSetupGpio()

    wiringpi.pinMode(servo_pin, 2)

    wiringpi.pwmSetMode(0)
    wiringpi.pwmSetRange(1024)
    wiringpi.pwmSetClock(375)


    while True:
        try:
            ser = serial.Serial(port0, 38400, timeout=10)  # 10s-timeout baudrate=38400
            ser.write(b'<RM,>??\r\n')  # send command (CR+LF)
            line = ser.readline()
            line = str(datetime.datetime.now()) + str(",") + line.decode('utf-8')
            line = line.split(',')

            velocity = float(line[2])
            temp = float(line[5])

            print('CPU_temperature' + '/' + line[0] + ',' + line[2] + ','
                    + line[3] + ',' + line[4] + ',' + line[5])
            f.write(line[0] + ',' + line[2] + ','
                    + line[3] + ',' + line[4] + ',' + line[5] + "\n")

            if temp >= 35.0:
#                print('too hot')
                wiringpi.pwmWrite(servo_pin, set_degree + 5)
#                LED(11, True)
            else:
#                print('oh.. cool')
#                move_deg = int (81+41/90*set_degree)

                wiringpi.pwmWrite(servo_pin, set_degree)
#                LED(11, False)

            time.sleep(5)

        except IndexError:
            pass

if __name__ == '__main__':
    main()
