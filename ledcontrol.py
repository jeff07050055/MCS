#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import requests
import sys
import http.client as http
import urllib
import json

# Set the LED PIN
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)

deviceId = "DEURqOut"
deviceKey = "5so6ld7ois0SBmii"

def get_to_mcs():
	host = "http://api.mediatek.com"
	endpoint = "/mcs/v2/devices/" + deviceId + "/datachannels/LEDcontrol/datapoints"
	url = host + endpoint
	headers = {"Content-type": "application/json", "deviceKey": deviceKey}
	r = requests.get(url,headers = headers)
	value = (r.json()["dataChannels"][0]["dataPoints"][0]["values"]["value"])
	return value

# Receive the Data from MCS
while(True):
	if(get_to_mcs() == 1):
		print("LED turning on.")
		GPIO.output(24,GPIO.HIGH)
		time.sleep(0.5)
	elif(get_to_mcs() == 0):
		print("LED turning off.")
		GPIO.output(24,GPIO.LOW)
		time.sleep(0.5)
