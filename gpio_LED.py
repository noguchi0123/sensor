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
while True:
    GPIO.output(11, True)
    time.sleep(2)
    GPIO.output(11, False)
    time.sleep(2)
