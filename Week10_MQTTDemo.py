import os, sys, io
import M5
from M5 import *
from umqtt import *
from hardware import *
import time


mqtt_client = None
adc = None
adc_val = None
username = 'ResistantJs'
password = ''
mqtt_timer = 0


def setup():
  global mqtt_client, username, password, adc, adc_val

  M5.begin()
  mqtt_client = MQTTClient('testjason',
                           'io.adafruit.com',
                           port=1883,
                           user= username,
                           password= password,
                           keepalive=3000)
  
  mqtt_client.connect(clean_session=True)
  #config adc
  adc = ADC(Pin(8), atten = ADC.ATTN_11DB)


def loop():
  global mqtt_client, mqtt_timer, adc, adc_val
  M5.update()
  if BtnA.wasPressed():
    print("ON")
    mqtt_client.publish('ResistantJs/feeds/button-feed', 'ON', qos=0)
  
  if BtnA.wasReleased():
    print("OFF")
    mqtt_client.publish('ResistantJs/feeds/button-feed', 'OFF', qos=0)
  if(time.ticks_ms() > mqtt_timer + 2500):
    mqtt_client.publish('ResistantJs/feeds/button-feed', 'waiting', qos=0)
    print('waiting for data')
    #update timer
    mqtt_timer = time.ticks_ms()

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
