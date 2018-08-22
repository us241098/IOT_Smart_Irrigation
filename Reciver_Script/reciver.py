import paho.mqtt.client as mqtt

MQTT_SERVER = "192.168.43.3"
MQTT_PATH = "test_channel"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(MQTT_PATH)

def on_message(client, userdata, msg):
    msg = msg.payload
    print msg
    write_csv(msg)

def write_csv(msg):
    sensor, value = msg.split('-')
    lines = []

    with open('recived.txt') as f:
        lines = f.read().splitlines()
    lines[int(sensor)] = value
    with open('recived.txt','w') as f:
        for line in lines:
            f.write("%s\n" % line)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, 1883, 60)
client.loop_forever()
