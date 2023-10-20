import os, sys, io
import M5
from M5 import *
from hardware import *
import time

adc = None
adc_val = None
adc_timer = 0
adc_calib_val = None

def setup():
  global adc, adc_val, adc_calib_val
  M5.begin()
  # configure ADC input on pin G1 with 11dB attenuation:
  adc = ADC(Pin(1), atten=ADC.ATTN_11DB)
  time.sleep_ms(500)
  #set calibration value 100 less than adc_val
  set_calibration(100)

def loop():
  global adc, adc_val, adc_timer, adc_calib_val
  M5.update()
  
  #calibrate sensor when button pressed
  if (BtnA.wasPressed()):
    set_calibration(100) 
      
  #read adc value once every 500ms passed
  if (time.ticks_ms() > adc_timer + 100):
    # read 12-bit analog value (0 - 4095 range):
    adc_val = adc.read()
    #print(adc_val)
    # convert adc_val from 0-4095 range to 
    adc_val_8bit = map_value(adc_val, in_min = 0, in_max = 4095,
                           out_min = 0, out_max = 255)
    print(adc_val_8bit)
    #time.sleep_ms(100)
    #timer instead of sleep
    adc_timer = time.ticks_ms()
    #compare adc_val with adc_calib_val
    if (adc_val < adc_calib_val - 100):
      print('sensor low..')
    else:
      print('sensor high..')
  

def set_calibration(calib):
  global adc_calib_val
  #set calibration value 100 less than adc_val
  adc_calib_val = adc.read() - calib
  print('Set calibration value...', adc_calib_val)
  
# map an input value (v_in) between min/max ranges:
def map_value(in_val, in_min, in_max, out_min, out_max):
  v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
  if (v < out_min): 
    v = out_min 
  elif (v > out_max): 
    v = out_max
  return int(v)

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

