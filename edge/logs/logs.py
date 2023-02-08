import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)
    
def on_message(client, userdata, msg):
  try:
    print("message received")
    # if we wanted to re-publish this message, something like this should work
    # msg = msg.payload
    # remote_mqttclient.publish(REMOTE_MQTT_TOPIC, payload=msg, qos=0, retain=False)
  except Exception as e:
    print("Unexpected error")
    print(e)

print("initalizing new client")
local_mqttclient = mqtt.Client()

print("connecting...")
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 600)

print("new message:")
local_mqttclient.on_message = on_message

local_mqttclient.loop_forever()
