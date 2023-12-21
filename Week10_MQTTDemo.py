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
password = 'aio_FIwi946YNkzlQfsFBe1TRwz1RDJg'
mqtt_timer = 0




def setup():
  global mqtt_client, username, password, adc, adc_val

  M5.begin()
  #mqtt_client = MQTTClient('testjason',
  #                         'io.adafruit.com',
  #                         port=1883,
  #                         user= username,
  #                         password= password,
  #                         keepalive=3000)
  mqtt_client = MQTTClient('test', '0.0.0.0', port=1883, user='ResistantJs', password='JyD189168', keepalive=3000)
  mqtt_client.subscribe('ResistantJs/feeds/button-feed', 'OFF', qos = 0)
  
  mqtt_client.connect(clean_session=True)
  #config adc
  #adc = ADC(Pin(8), atten = ADC.ATTN_11DB)


def loop():
  global mqtt_client, mqtt_timer, adc, adc_val
  M5.update()
  if BtnA.wasPressed():
    print("ON")
    mqtt_client.publish('ResistantJs/feeds/button-feed', 'ON', qos=0)
    mqtt_client.wait_msg()

  
  if BtnA.wasReleased():
    print("OFF")
    mqtt_client.publish('ResistantJs/feeds/button-feed', 'OFF', qos=0)
  #if(time.ticks_ms() > mqtt_timer + 2500):
  #  adc_val = adc.read()
  #  #publish analog value as string message
  #  mqtt_client.publish('ResistantJs/feeds/adc-feed', str(adc_val), qos=0)
  #  print('publish for data')
  #  #update timer
  #  mqtt_timer = time.ticks_ms()

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
