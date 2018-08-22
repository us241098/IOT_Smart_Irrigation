#!/usr/bin/env python

import paho.mqtt.publish as publish
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
INPUT_PIN_1 = 4
GPIO.setup(INPUT_PIN_1, GPIO.IN)
INPUT_PIN_1 = 21
GPIO.setup(INPUT_PIN_2, GPIO.IN)

MQTT_SERVER = "192.168.43.3"
MQTT_PATH = "test_channel"

while True:
    if (GPIO.input(INPUT_PIN_1) == True): # Physically read the pin now
        publish.single(MQTT_PATH, "0-1", hostname=MQTT_SERVER)
    else:
        publish.single(MQTT_PATH, "0-0", hostname=MQTT_SERVER)

    if (GPIO.input(INPUT_PIN_2) == True): # Physically read the pin now
        publish.single(MQTT_PATH, "1-1", hostname=MQTT_SERVER)
    else:
        publish.single(MQTT_PATH, "1-0", hostname=MQTT_SERVER)

    sleep(5);           # Sleep for a full second before restarting our loop
