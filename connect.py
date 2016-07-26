##connect.py

import psycopg2 # python-posgresql connection
import serial #serial communication
import datetime, time # time delay

conn = psycopg2.connect(
	host='kurihara.west.sd.keio.ac.jp',
	database='datacenter',
	port=5432,
	user='kpj',
	password='znh1sge'
) # DB setting

#serial settings
ser = serial.Serial('/dev/ttyUSB0',38400,timeout=10) # 10s-timeout baudrate=38400

ser.write('<RM,>??\r\n') #send command (CR+LF)

now = datetime.datetime.now() # now no setting
while True:
	ser.write('<RM,>??\r\n') #send command (CR+LF)
	line = ser.readline()
	split_line = line.split(',') #conma de split


	cur = conn.cursor()
	print now
	cur.execute("INSERT INTO server.anemometer (speed, direction, wind, temp, date) VALUES (%s, %s, %s, %s, %s)",(float (split_line[1]),int (split_line[2]),int (split_line[3]),float (split_line[4]),now))

	#cur.execute("INSERT INTO server.anemometer (speed, direction, wind, temp, date) VALUES (%s, %s, %s, %s, %s)",(1,22,303,4443,23:45:12))
	conn.commit()

	time.sleep(1200)	
	cur.close()
conn.close()
