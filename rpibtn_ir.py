#!/usr/bin/env python

# Rodolfo García Peñas (kix) <kix@kix.es>
# Script for Raspberry Pi Infrared Shield
# More info at http://kix.es

import RPi.GPIO as GPIO
import time
import subprocess
import sys
import os

# Get the scripts folder
def get_scripts_folder():
    return os.path.dirname(sys.argv[0]) + "/scripts/"

def select_Button_1(bouncetime):
    subprocess.call(get_scripts_folder() + "button_1.py")

def select_Button_2(bouncetime):
    subprocess.call(get_scripts_folder() + "button_2.py")

def gpio_setup():
    GPIO.setwarnings(False)
    GPIO.setmode (GPIO.BCM)

    GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Button 1
    GPIO.add_event_detect(21, GPIO.FALLING, callback=select_Button_1, bouncetime=500)

    GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP) # Button 2
    GPIO.add_event_detect(22, GPIO.FALLING, callback=select_Button_2, bouncetime=500)
 
gpio_setup()

while True:
    time.sleep(2)
