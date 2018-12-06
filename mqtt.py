import paho.mqtt.client as paho
import os
from urlparse import urlparse as parse

# Define event callbacks
def on_connect(self, mqttc, obj, rc):
	print("rc: " + str(rc))

def on_message(mqttc, obj, msg):
	print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mqttc, obj, mid):
	print("mid: " + str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
	print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
	print(string)

class MQTT(object):
	def __init__(self, user, password):

		self.mqttc = paho.Client()
		self.user = user
		self.password = password
		# Assign event callbacks
		self.mqttc.on_message = on_message
		self.mqttc.on_connect = on_connect
		self.mqttc.on_publish = on_publish
		self.mqttc.on_subscribe = on_subscribe

		# Parse CLOUDMQTT_URL (or fallback to localhost)
		url_str = os.environ.get('CLOUDMQTT_URL', 'mqtt://m21.cloudmqtt.com')
		url = parse(url_str)
		# Uncomment to enable debug messages
		self.mqttc.on_log = on_log
		# Connect

		if user == None or password == None:
			self.mqttc.username_pw_set("lgvohswk", "VcimBX_iUvkb")
		else:
			self.mqttc.username_pw_set(self.user, self.password)
		self.mqttc.connect("m21.cloudmqtt.com", 11172)

	def publish(self, topic, message):
		self.mqttc.publish(topic, message)
		print("Message published!")

	def subscribe(self, topic):
		self.mqttc.subscribe(topic, 0)
		print("Subscribed to " ,topic, " !")

	def on_receive(self, message_fn):
		self.mqttc.on_message = message_fn

	def loop(self):
		rc = 0
		while rc == 0:
			rc = self.mqttc.loop()
			print("rc: ", str(rc))
