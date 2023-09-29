import os, sys, io
import M5
from M5 import *
from hardware import *
import time


pin1 = None


def setup():
  global pin1

  M5.begin()
  pin1 = Pin(1, mode=Pin.OUT)


def loop():
  global pin1
  M5.update()
  if BtnA.isPressed():
    pin1.on()
  else:
    pin1.off()
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
