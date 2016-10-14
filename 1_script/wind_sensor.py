def conn_sensor(filename, delay):
  f = open(filename, 'w')
  ser.write(b'<RM,>??\r\n') #send command (CR+LF)
  line=ser.readline()
  line=str(datetime.datetime.now())+str(",")+line.decode('utf-8')
  li_line=line.split(',')
  return li_line[5] #show temperature
  print(line)
  f.write(str(line)+str("\n"))
  time.sleep(delay)
  f.close()
  ser.close()
