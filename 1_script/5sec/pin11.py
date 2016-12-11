import RPi.GPIO as GPIO
import time
import signal
import sys

def exit_handler(signal, fname):
	print("\nExit")
	GPIO.cleanup()
	sys.exit(0)
signal.signal(signal.SIGINT, exit_handler)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.output(13, True)
while True:
    GPIO.output(11, True)
    print("ON")
    time.sleep(2)
    GPIO.output(11, False)
    print("OFF")
    time.sleep(2)
    GPIO.output(12, True)
    print("ON12")
    time.sleep(2)
    GPIO.output(12, False)
    print("OFF12")
    time.sleep(2)
