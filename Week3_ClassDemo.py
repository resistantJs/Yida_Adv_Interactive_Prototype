import os, sys, io
import M5
from M5 import *
from hardware import *
import time


pin1 = None
pwm1 = None


i = None


def setup():
  global pin1, pwm1

  M5.begin()
  pin1 = Pin(1, mode=Pin.OUT)
  pwm1 = PWM(Pin(1), freq=20000, duty=512)


def loop():
  global pin1, pwm1
  M5.update()
  for i in range(1000):
    pwm1.duty(i)
    time.sleep_ms(1)
  for x in range(1000, 0, -1):
    pwm1.duty(x)
    time.sleep_ms(1)
    


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
