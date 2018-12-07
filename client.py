import paho.mqtt.client as paho
import os
import time
import getopt
import sys
from mqtt import MQTT

def usage():
    print("usage: " + sys.argv[0] + "-u user -s topics")

topic_list = user = password = None
try:
    opts, args = getopt.getopt(sys.argv[1:], 'u:p:s:a:')
except getopt.GetoptError as err:
    usage()
    sys.exit(2)

for o, a in opts:
    if o == '-s':
        topic_list = a.split(",")
    elif o == '-u':
        user = a
    elif o == '-p':
        password = a
    else:
        assert False, "unhandled option"

if topic_list is None:
    print("Client not subscribed to any topics!")
    usage()
    sys.exit(2)

mqttc = MQTT(user, password)

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if msg.topic == "temperature":
    	with open("temperature.txt", "a") as file:
            print("Writing into temperature.txt")
            file.write(msg.payload)
            file.write("\n")
            file.close()
    elif msg.topic == "humidity":
    	with open("humidity.txt", "a") as file:
            print("Writing into humidity.txt")
            file.write(msg.payload)
            file.write("\n")
            file.close()
    elif msg.topic == "pressure":
    	with open("pressure.txt", "a") as file:
            print("Writing into pressure.txt")
            file.write(msg.payload)
            file.write("\n")
            file.close()
    else:
    	print("Not a valid topic")

# Publish a message - Client is connected
mqttc.publish(user, "Getting started ...")
mqttc.on_receive(on_message)
localtime = time.asctime(time.localtime(time.time()))

for topic in topic_list:
    mqttc.subscribe(topic)
    # Continue the network loop, exit when an error occurs
    with open(topic + ".txt", "a") as file:
        header = "-------------- Data for " + topic + ": " + localtime + " --------------"
        file.write(header)
        file.write("\n")

mqttc.loop()

# rc = 0
# while rc == 0:
#     print(str(rc))
#    rc = mqttc.loop()
#print("rc: " + str(rc))