import os, sys, io
import M5
from M5 import *
from umqtt import *
from hardware import *


mqtt_client = None
username = 'ResistantJs'
password = 'Password Here'

def setup():
  global mqtt_client, username, password

  M5.begin()
  mqtt_client = MQTTClient('testjason',
                           'io.adafruit.com',
                           port=1883,
                           user= username,
                           password= password,
                           keepalive=0)
  
  mqtt_client.connect(clean_session=True)


def loop():
  global mqtt_client
  M5.update()
  if BtnA.wasPressed():
    print("Button Press")
    mqtt_client.publish('ResistantJs/feeds/button-feed', 'Button Press', qos=0)


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
