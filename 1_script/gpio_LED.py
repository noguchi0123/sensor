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
while True:
    GPIO.output(11, True)
    time.sleep(3)
    GPIO.output(11, False)
    time.sleep(3)
    GPIO.output(12, True)
    time.sleep(3)
    GPIO.output(12, False)
    time.sleep(3)
    GPIO.output(13, True)
    time.sleep(3)
    GPIO.output(13, False)
    time.sleep(3)
    GPIO.output(15, True)
    time.sleep(3)
    GPIO.output(15, False)
    time.sleep(3)
