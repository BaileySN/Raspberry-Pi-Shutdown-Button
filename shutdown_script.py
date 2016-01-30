#! /usr/bin/env python
# coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import os

#config
#change the GPIO Port number
gpioport=24

sdate = time.strftime("%H:%M:%S")
stime = time.strftime("%Y-%m-%d")
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpioport, GPIO.IN)

def sysshutdown(channel):
	msg="System shutdown GPIO.Low state"
	logpath="/var/log/shutdown.log"
	print("System shutdown")
	f = open(logpath, "a")
	f.write(str(sdate)+";"+str(stime)+";"+str(msg)+";")
	f.close()
	os.system("shutdown -h now")

while True:
	if(GPIO.input(gpioport)):
		sysshutdown("1")
		break
	time.sleep(2)
