# Yida_Adv_Interactive_Prototype
Files for Advance Interactive Prototype class
+ Week2: Button press on atom s3lite to trigger light connect to pin1 with a `270ohm` resistor
+ Week3: The same light on `pin 1` dims up and dims down


# Wire Diagram
![Wire Diagram](../main/img/Diagram.jpg)
# My Demo Code for Week 3 HW:
```
import os, sys, io
import M5
from M5 import *
import time
from hardware import *


pin1 = None
pin2 = None
rgb = None


x = None
Count = None

# Describe this function...
def Flash(x):
  global Count, pin1, pin2, rgb
  time.sleep_ms(50)
  rgb.fill_color(x)
  time.sleep_ms(50)
  rgb.fill_color(x)


def setup():
  global pin1, pin2, rgb, x, Count

  M5.begin()
  pin1 = Pin(1, mode=Pin.IN)
  pin2 = Pin(2, mode=Pin.IN)
  rgb = RGB()


def loop():
  global pin1, pin2, rgb, x, Count
  M5.update()
  if pin1.value():
    print('Dark Slide In, Safe to Open')
    rgb.fill_color(0x33ff33)
    if Count == 39:
      print('Film Taken, reset count')
      Count = 0
  else:
    print('Dark Slide Out, Loading, NOT Safe to Open')
    print('Flash Red')
    Flash(0xff0000)
    if pin2.value():
      print('Each Cycle Count ++')
      Count = (Count if isinstance(Count, (int, float)) else 0) + 1
    if Count == 39:
      print('Count Reach 39, film ready')
      print('Flash Blue')
      while not (pin1.value()) == 1:
        Flash(0x3366ff)
  if BtnA.wasClicked():
    print('Throw error, Reset Count')
    Count = 0
  time.sleep_ms(50)


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

```

# Tasks
- [x] Flow Diagram
- [x] Code(Need Testing)
- [ ] Physical Prototype
- [ ] Test One

