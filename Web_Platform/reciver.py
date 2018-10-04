import paho.mqtt.client as mqtt
import pandas as pd
from numpy  import array
from time import gmtime, strftime


MQTT_SERVER = "localhost"
MQTT_PATH = "test_channel"

def on_connect(client, userdata, flags, rc):
#    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    msg = msg.payload
#    print msg
    write_csv(msg)

def write_csv(msg):
	df=pd.read_csv('read.csv')
	msg=msg.split()
	a = array(msg)
#	print a[0]
	df.loc[df['sensor'] == int(a[0]), 'readings'] = a[1]
	df.loc[df['sensor'] == int(a[0]), 'timestamp'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
	df.to_csv('read.csv', encoding='utf-8', index=False)
	


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)
client.loop_forever()
