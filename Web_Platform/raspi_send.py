#!/usr/bin/env python

import paho.mqtt.publish as publish
from time import sleep
import RPi.GPIO as GPIO
import time

MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"
GPIO.setmode(GPIO.BCM)
a_pin = 18
b_pin = 23


def discharge():
    GPIO.setup(a_pin, GPIO.IN)
    GPIO.setup(b_pin, GPIO.OUT)
    GPIO.output(b_pin, False)
    time.sleep(0.005)

def charge_time():
    GPIO.setup(b_pin, GPIO.IN)
    GPIO.setup(a_pin, GPIO.OUT)
    count = 0
    GPIO.output(a_pin, True)
    while not GPIO.input(b_pin):
        count = count +1
    return count


def analog_read():
    discharge()
    return charge_time()



while True:
    k=analog_read()
    sleep(5);           # Sleep for a full second before restarting our loop
	
	publish.single(MQTT_PATH, "2"+''+' '+ k, hostname=MQTT_SERVER)	
    



