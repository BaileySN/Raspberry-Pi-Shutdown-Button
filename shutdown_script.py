#! /usr/bin/env python
# coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)

def sysshutdown(channel):
	msg = "System shutdown GPIO.Low"
	print("System shutdown")
	os.system("date >>/var/log/shutdown.log")
	os.system("echo "+msg+" >>/var/log/shutdown.log")
	os.system("shutdown -h now")

while True:
	if(GPIO.input(24)):
		sysshutdown("1")
		break
	time.sleep(2)
