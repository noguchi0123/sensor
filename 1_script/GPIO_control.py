import RPi.GPIO as GPIO
import time
import signal
import sys

def exit_handler(signal, fname):
	print("\nExit")
	GPIO.cleanup()
	sys.exit(0)

def LED(pin, TF):
    signal.signal(signal.SIGINT, exit_handler)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
#    while True:
    GPIO.output(pin, TF)
        # time.sleep(2)
        # GPIO.output(pin, False)
        # time.sleep(2)


def servo(pin, deg):

    signal.signal(signal.SIGINT, exit_handler)
    GPIO.setmode(GPIO.BCM)
    gpio_out = pin
    GPIO.setup(gpio_out, GPIO.OUT)
    servo = GPIO.PWM(gpio_out, 50)

    servo.start(0.0)


    dc = 0.0
#    while True:
    for dc in range(2, deg, 1):
        servo.ChangeDutyCycle(dc)
#        print("dc = %d" % dc)
        time.sleep(0.5)
        """
      for dc in range(12, 2, -1):
        servo.ChangeDutyCycle(dc)
        print("dc = %d" % dc)
        time.sleep(0.5)
        """
