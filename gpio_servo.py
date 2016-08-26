import RPi.GPIO as GPIO
import time
import signal
import sys

def exit_handler(signal, frame):
  
  #Ctrl+Cが押されたときにデバイスを初期状態

  print("\nExit")
  servo.stop()
  GPIO.cleanup()
  sys.exit(0)

# 終了処理用のシグナルハンドラを準備
signal.signal(signal.SIGINT, exit_handler)

GPIO.setmode(GPIO.BCM)

# GPIO 11番を使用 (PWM 0)
gpio_out = 11
GPIO.setup(gpio_out, GPIO.OUT)
# 20ms / 50Hzに設定らしい
servo = GPIO.PWM(gpio_out, 50)

# 初期化
servo.start(0.0)

# ChangeDutyCycleに渡す値は 0.0 <= dc <= 100.0
# のはずだがなぜか2から12の間で動作している

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

