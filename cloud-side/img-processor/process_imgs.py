import paho.mqtt.client as mqtt
import boto3
import uuid
import os
import io



aws_region = 'us-east-1'
aws_id = os.environ.get('AWS_ID')
aws_key = os.environ.get('AWS_SECRET')

LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"

s3 = boto3.client('s3', region_name = aws_region, aws_access_key_id=aws_id, aws_secret_access_key=aws_key)
response = s3.list_buckets()

print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')

bucket_name = 'hw2bucket-cs'

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

count = 0
def on_message(client,userdata, msg):
    global count
    print("recieved a message")
    try:
        img = msg.payload
        s3.upload_fileobj(io.BytesIO(img), bucket_name, "imgfile"+str(count))
        count += 1
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
