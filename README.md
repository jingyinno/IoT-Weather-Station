# IoT-Weather-Station
Aarhus University - E18 - Internet of Things Technology Project

For this project, we have implemented a weather monitoring station with a Sense Hat sensor that monitors temperature, pressure, humidity and light, which transmits the data captured to a Raspberry Pi 3 that it is connected to. We are using the CloudMQTT server as our cloud service, and the MQTT protocol between Pi to cloud and cloud to clients. For more information, please view the report under [here](https://github.com/jingyinno/IoT-Weather-Station/blob/master/Project%2010%20Report.pdf)

# Setting up

## Prerequisite
 
Text editor - Vim (Any text editor will be sufficient)

`sudo apt-get install vim`

Python 2.7

`Download from https://www.python.org/download/releases/2.7/ for respective OS.`

## Setting up static IP on Raspberry Pi

`This needs to be done for the recent Jessie or later update. /etc/network/interfaces should be left alone. Open browser and enter the router address (192.168.1.1 for most) and check home network to make sure the Raspberry Pi shows up as 'Static'.
For a static IP address on an Ethernet connection:`

`1. sudo vim /etc/dhcpcd.conf`

Type in the following lines on the top of the file (This only applies if the router address is 192.168.1.1, otherwise change accordingly):

`1. interface eth0 static ip_address=192.168.1.XX/24`  
`2. static routers=192.168.1.1`  
`3. static domain_name_servers=192.168.1.1 8.8.8.8`  
`4. sudo reboot`  

## Setting up Sense Hat on Raspberry Pi

`1. sudo apt-get update`  
`2. sudo apt-get upgrade`  
`3. sudo apt-get install sense-hat`  
`4. sudo reboot`  

## Setting up MQTT.paho
`1. pip install paho-mqtt`
