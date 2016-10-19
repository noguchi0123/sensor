# -*- coding: utf-8 -*-
# test/get_temp_10sec.py


def main():
    import serial
    import sys
    import time
    import datetime
    from GPIO_control import LED, exit_handler, servo
    argvs = sys.argv

    port = '/dev/ttyUSB0'

    while True:
        try:
            ser = serial.Serial(port, 38400, timeout=10)  # 10s-timeout baudrate=38400
            ser.write(b'<RM,>??\r\n')  # send command (CR+LF)
            line = ser.readline()
            line = str(datetime.datetime.now()) + str(",") + line.decode('utf-8')
            line = line.split(',')
            print(line[0])
            print('velocity:'+line[2])
            velocity = float(line[2])
            print('temperature:'+line[5])
            temp = float(line[5])

            from mymodule import get_air_parameter, volumetric_flow_rate
            print(get_air_parameter(temp))
            #print('specific_heat:')
            sh = get_air_parameter(temp, 'sh')
            #print(sh)
            #print('density:')
            d = get_air_parameter(temp, 'd')
            #print(d)
            hc = get_air_parameter(temp, 'hc')
            #print('heat_conductivity: ' + str(hc))

            # print(volumetric_flow_rate(v_wind=velocity,hole_area=0.001125))
            volume = volumetric_flow_rate(v_wind=velocity, hole_area=0.001125)*1
            print('volume is ' + str(volume))

            from mymodule import get_heat_air
            heat = get_heat_air(specific_heat=sh, density=d, volume=volume, temp_target=70, temp_now=temp)
            print('generated heat is ' + str(heat))
            print("----------------------------------------end-----------------------------------------")

            time.sleep(10)


        except IndexError:
            print("----------------------------------------error-----------------------------------------")
            print("Index ERROR occured")
            print("----------------------------------------error-----------------------------------------")
        if velocity > 0.035:
            print("so speeeedy")
            LED(11)

if __name__ == '__main__':
    main()
