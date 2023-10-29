from machine import Pin, PWM
from servo import Servo
import time

servo = Servo(pin=7)
servo.move(-90)
