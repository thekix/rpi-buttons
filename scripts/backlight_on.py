#!/usr/bin/env python
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT) 
GPIO.output(27,GPIO.HIGH)
