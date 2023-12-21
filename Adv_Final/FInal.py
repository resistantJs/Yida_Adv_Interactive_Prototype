import os, sys, io
import M5
from M5 import *
from hardware import *
import time

rgb38 = None
uart0 = None


def setup():
  global rgb38, uart0

  M5.begin()
  rgb38 = RGB(io=38, n=30, type="WS2812")
  #uart0.init(baudrate=115200, bits=8, parity=None, stop=1, tx=9, rx=10, rts=-1, cts=-1, txbuf=256, rxbuf=256, timeout=0, timeout_char=0, invert=0, flow=0)
  uart0 = UART(
      0,
      baudrate=115200,
      bits=8,
      parity=None,
      #stop=1, tx=9, rx=10, rts=-1, cts=-1,
      #txbuf=256, rxbuf=256, timeout=0, timeout_char=0, invert=0, flow=0
  )


def loop():
  global rgb38, uart0
  M5.update()
  
  #for i in range(1, 31):
  #  rgb38.set_color(i, 0x6600cc)
  #  rgb38.set_color(i-1, 000000)
  uart0.write('hello M5')
  time.sleep_ms(500)
  print(uart0.read())
  time.sleep_ms(500)


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
