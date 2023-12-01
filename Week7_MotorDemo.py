from machine import Pin, PWM
from servo import Servo
import time

servo = Servo(pin=2)
while True:
    servo.move(101)
    print("100")
    time.sleep_ms(800)
    servo.move(88)
    print("89")
    time.sleep_ms(800)
