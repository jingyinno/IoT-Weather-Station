#!/usr/bin/python
from sense_hat import SenseHat
from mqtt import MQTT
import time
import sys
sense = SenseHat()
mqtt = MQTT("lgvohswk", "VcimBX_iUvkb")
sense.clear()
try:
    while True:
        temp = sense.get_temperature()
        temp = round (temp, 1)
        print("Temperature C", temp)
        mqtt.publish("temperature", temp)
        #sense.show_message(str(temp))

        humidity = sense.get_humidity()
        humidity = round (humidity,1)
        print("Humidity", humidity)
        mqtt.publish("humidity", humidity)

        pressure = sense.get_pressure()
        pressure = round (pressure,1)
        print("Pressure", pressure)
        mqtt.publish("pressure", pressure)

        time.sleep(1)
except KeyboardInterrupt:
    pass
