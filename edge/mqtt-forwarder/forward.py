import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"


REMOTE_MQTT_HOST="18.208.207.209"
REMOTE_MQTT_PORT=30272
REMOTE_MQTT_TOPIC="faces"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)
    
def on_connect_remote(client, userdata, flags, rc):
    print("connected to remote broker with rc: " + str(rc))
    client.subscribe(REMOTE_MQTT_TOPIC)
    
def on_message(client, userdata, msg):
  try:
    print("message received")
    # if we wanted to re-publish this message, something like this should work
    msg = msg.payload
    remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except Exception as e:
    print("Unexpected error")
    print(e)
    
    
print("initalizing new local client")
local_mqttclient = mqtt.Client()

print("connecting to local instance...")
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)

print("initalizing remote client")
remote_mqttclient = mqtt.Client()

print("connecting to remote instance...")
remote_mqttclient.on_connect = on_connect_remote
remote_mqttclient.connect(REMOTE_MQTT_HOST, REMOTE_MQTT_PORT, 60)
#remote_mqttclient.publish(REMOTE_MQTT_TOPIC, "Hello cloud")

print("publishing message to remote broker")
local_mqttclient.on_message = on_message


local_mqttclient.loop_forever()


