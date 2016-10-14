import RPi.GPIO as GPIO
import time
import signal
import sys

"""
def exit_handler(signal, frame):


  print("\nExit")
  servo.stop()
  GPIO.cleanup()
  sys.exit(0)
"""
#signal.signal(signal.SIGINT, exit_handler)

def control_servo(gpio_out,degree):
    GPIO.setmode(GPIO.BCM)

    #gpio_out = 18
    GPIO.setup(gpio_out, GPIO.OUT)
    servo = GPIO.PWM(gpio_out, 50) #50Hz

    servo.start(0.0)


    servo.ChangeDutyCycle(degree)
    print(degree)


if __name__ == '__main__':
    control_servo(18,3)
    time.sleep(5)
    control_servo(18,12)
    time.sleep(5)
    control_servo(18,8)
    GPIO.cleanup()
    sys.exit(0)

