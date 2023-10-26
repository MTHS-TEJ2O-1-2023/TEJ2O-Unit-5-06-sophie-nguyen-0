"""
Created by: sophie
Created on: Oct 2023
This module is a Micro:bit MicroPython program detects distance with sonar
"""

from microbit import *
from machine import time_pulse_us


display.show(Image.GHOST)

# choose pins
trig = pin1
echo = pin2

# setup
trig.write_digital(0)
echo.read_digital()

while True:
    if button_a.is_pressed():
        # output
        trig.write_digital(1)
        trig.write_digital(0)

        # Measure the echo pulse
        micros = time_pulse_us(echo, 1)
        t_echo = micros / 1000000

        # calculate distance to cm
        dist_cm = (t_echo / 2) * 34300
        display.scroll(str(int(dist_cm)))

        sleep(300)
