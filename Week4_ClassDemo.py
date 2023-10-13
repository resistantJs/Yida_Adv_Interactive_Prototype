import os, sys, io
import M5
from M5 import *
from hardware import *
import time


rgb = None
input_pin = None
state = 'green'


def setup():
    global rgb, input_pin

    M5.begin()
    rgb = RGB(io=2, n=30, type = "WS2812")
    input_pin = Pin(39, mode=Pin.IN, pull=Pin.PULL_UP)


def loop():
    global rgb,state
    M5.update()

    if (state == 'green'):
        # if input pin is low change to red state:
        if input_pin.value() == 0 :
            state = 'red'
            print('change to ', state)
            time.sleep(1)
        else:
            # fade in all RGB LEDs green:
            for i in range(100):
                rgb.fill_color(get_color(0,i,0))
                time.sleep_ms(10)
        elif(state == 'red'):
            # if input pin is low change to green state
            if input_pin.value()== 0 :
                state = 'green'
                print('change to ', state)
                time.sleep(1)
            else:
                #chase RGB blue:
                for i in range(30):
                    rgb.set_color(i, get_color(0,0,255))
                    time.sleep_ms(50)
                rgb.fill_color(0xff0000)
                time.sleep_ms(250)
def get_color(r, g, b):
    rgb_color = (r << 16) | (g << 8) | b
    return rgb_color

print('color =', hex(get_color(255, 0, 0)))
print('color =', hex(get_color(0, 255, 0)))

    


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
        


