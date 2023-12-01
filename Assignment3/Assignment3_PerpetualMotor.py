import os, sys, io
import M5
from M5 import *
from hardware import *
from machine import Pin, PWM
from servo import Servo
import time

adcl = None
adcl_val = None
adcr = None
adcr_val = None
servo = None

def setup():
  global adcl, adcl_val, adcr, adcr_val,servo
  M5.begin()
  # configure ADC input on pin G1 with 11dB attenuation:
  adcl = ADC(Pin(7), atten=ADC.ATTN_11DB)
  adcr = ADC(Pin(8), atten=ADC.ATTN_11DB)
  
  servo = Servo(pin=2)

def loop():
  global adcl, adcl_val, adcr, adcr_val,servo
  M5.update()
  # read 12-bit analog value (0 - 4095 range):
  adcl_val = adcl.read()
  adcr_val = adcr.read()
  if adcl_val > 200:
    print("left hit",adcl_val)
    servo.move(88)
    print("88 Go Right")
    time.sleep_ms(800)
  if adcr_val > 200:
    print("right hit", adcr_val)
    servo.move(101)
    print("101 Go Left")
    time.sleep_ms(800)
  servo.move(90)
  

  # convert adc_val from 0-4095 range to 
  #adc_val_8bit = map_value(adc_val, in_min = 0, in_max = 4095,
  #                         out_min = 0, out_max = 255)
  #print(adc_val_8bit)
  time.sleep_ms(1)
  
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

