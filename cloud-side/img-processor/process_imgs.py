import paho.mqtt.client as mqtt
import boto3

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces_remote"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

def on_message(client,userdata, msg):
    print("recieved a message")
    try:
        print("message received: ",str(msg.payload.decode("utf-8")))
    # if we wanted to re-publish this message, something like this should work
    # msg = msg.payload
    # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
    except Exception as e:
        print("Unexpected error:", e)

print("creating mqtt client")
local_mqttclient = mqtt.Client()

print("connecting to broker...")
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 600)
local_mqttclient.on_message = on_message



# go into a loop
local_mqttclient.loop_forever()
