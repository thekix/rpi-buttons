#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import subprocess
import sys
import os

# Get the scripts folder
def get_scripts_folder():
    return os.path.dirname(sys.argv[0]) + "/scripts/"

def select_o_Button(bouncetime):
    subprocess.call(get_scripts_folder() + "button_o.py")

def select_s_Button(bouncetime):
    subprocess.call(get_scripts_folder() + "button_s.py")

def select_t_Button(bouncetime):
    subprocess.call(get_scripts_folder() + "button_t.py")

def select_x_Button(bouncetime):
    subprocess.call(get_scripts_folder() + "button_x.py")

def select_u_Button(bouncetime):
    subprocess.call(get_scripts_folder() + "button_u.py")

def select_d_Button(bouncetime):
    subprocess.call(get_scripts_folder() + "button_d.py")

def gpio_setup():
    GPIO.setwarnings(False)
    GPIO.setmode (GPIO.BCM)

    GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP) # o - Circle Button
    GPIO.setup(22, GPIO.IN, pull_up_down = GPIO.PUD_UP) # s - Square button
    GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP) # t - Triangle Button
    GPIO.setup( 5, GPIO.IN, pull_up_down = GPIO.PUD_UP) # x - X Button
    GPIO.setup( 4, GPIO.IN, pull_up_down = GPIO.PUD_UP) # u - Up button
    GPIO.setup(17, GPIO.IN, pull_up_down = GPIO.PUD_UP) # d - Down button

    GPIO.add_event_detect(23, GPIO.FALLING, callback=select_o_Button, bouncetime=500)
    GPIO.add_event_detect(22, GPIO.FALLING, callback=select_s_Button, bouncetime=500)
    GPIO.add_event_detect(24, GPIO.FALLING, callback=select_t_Button, bouncetime=500)
    GPIO.add_event_detect( 5, GPIO.FALLING, callback=select_x_Button, bouncetime=500)  
    GPIO.add_event_detect( 4, GPIO.FALLING, callback=select_u_Button, bouncetime=500)
    GPIO.add_event_detect(17, GPIO.FALLING, callback=select_d_Button, bouncetime=500)

gpio_setup()

while True:
    time.sleep(2)
