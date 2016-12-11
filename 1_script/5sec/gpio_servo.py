import RPi.GPIO as GPIO
import time
import signal
import sys

def exit_handler(signal, frame):

  print("\nExit")
  servo.stop()
  GPIO.cleanup()
  sys.exit(0)

signal.signal(signal.SIGINT, exit_handler)

GPIO.setmode(GPIO.BCM)

gpio_out = 11
GPIO.setup(gpio_out, GPIO.OUT)
servo = GPIO.PWM(gpio_out, 50)

servo.start(0.0)


dc = 0.0
while True:
  for dc in range(2, 12, 1):
    servo.ChangeDutyCycle(dc)
    print("dc = %d" % dc)
    time.sleep(0.5)
  for dc in range(12, 2, -1):
    servo.ChangeDutyCycle(dc)
    print("dc = %d" % dc)
    time.sleep(0.5)

