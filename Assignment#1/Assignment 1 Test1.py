# change RGB LED colors with digital input and time using state logic
# 4 states are implemented as shown:
# 'START'  -> turns on RGB green
# 'OPEN'   -> pulsate RGB blue
# 'CLOSED' -> fade in RGB yellow if digital input is closed
# 'FINISH' -> fade in RGB red 5 seconds after 'CLOSED' state
#             fade out RGB to black after 2 seconds

import os, sys, io
import M5
from M5 import *
from hardware import *
import time

rgb = None
state = 'START'
state_timer = 0
count = 0
touched = False
x = None

def setup():
  global pin1, pin2, rgb, darkSlide_pin, count_pin
  M5.begin()
  
  # custom RGB setting using pin G35 (M5 AtomS3 built-in LED):
  rgb = RGB(io=35, n=1, type="SK6812")
  
  # custom RGB setting using pin G2 (M5 AtomS3 bottom connector) and 10 LEDs:
  #rgb = RGB(io=2, n=10, type="SK6812")
  
  # initialize pin G41 (M5 AtomS3 built-in button) as input:
  #darkSlide_pin = Pin(41)
  
  # initialize pin G39 (M5 PortABC Extension red connector) as input:
  darkSlide_pin = Pin(39, mode=Pin.IN, pull=Pin.PULL_UP)
  count_pin = Pin(1, mode=Pin.IN, pull=Pin.PULL_UP)
  
  # turn on RGB green and wait 2 seconds:
  if (state == 'START'):
    print('start with RGB White..')
    rgb.fill_color(get_color(255, 255, 255))
    time.sleep(2)  
    check_input()

def loop():
  global state, state_timer, count, touched, count_pin
  M5.update()
  if BtnA.wasClicked():
    print("Clicked, Error! Reset Count")
    count = 0
  #State Actions
  if (state == 'Closed'):
    print('Lights Green')
    rgb.fill_color(get_color(0, 255, 0))
    time.sleep_ms(20)
    if(count == 39):
        print('Film Out, reset count')
        count = 0
    check_input()
    
  elif (state == 'Open'):
    print('Flash Red')
    Flash(0xff0000)
    check_input()
    #check if touched(count++) and left, 
    if(count_pin.value()):
        #NOTHING Happend
        print('count: ' ,count)
        if(touched):
          print('left')
          touched = False
    else:
        if(touched == False):
          print('touched')
          count += 1
          print('count: ' , count)
          touched = True
            
  if(count == 39):
      print('Count = 39, Film READY, Close Darkslide and get film')
      print('Flash Blue')
      #if Open, keep flashing blue untill Closed
      if(state == 'Open'):
          Flash(0x3366ff)
          check_input()

    
    #  check_input()

# check input pin and change state to 'OPEN' or 'CLOSED'
def check_input():
  global state, state_timer, darkSlide_pin
  
  if (darkSlide_pin.value()):
      if(state != 'Open'):
          print('Dark Slide Out, Loading, NOT Safe to Open')
      state = 'Open'
  else:
      if(state != 'Closed'):
          print('Safe to Open')
      state = 'Closed'
      # save current time in milliseconds:
      state_timer = time.ticks_ms()
      
  #if (input_pin.value() == 0):
  #  if(state != 'CLOSED'):
  #    print('change to CLOSED')
  #  state = 'CLOSED'
  #  # save current time in milliseconds:
  #  state_timer = time.ticks_ms()
  #else:
  #  if(state != 'OPEN'):
  #    print('change to OPEN')
  #  state = 'OPEN'
    
    
def Flash(x):
  global rgb
  
  rgb.fill_color(x)
  time.sleep_ms(50)
  rgb.fill_color(x)  
  time.sleep_ms(50)
  
# convert separate r, g, b values to one rgb_color value:  
def get_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

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

