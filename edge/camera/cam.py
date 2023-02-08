import numpy as np
import cv2
import paho.mqtt.client as mqtt


LOCAL_MQTT_HOST="mosquitto-service"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="faces"

def on_connect_local(client, userdata, flags, rc):
    print("connected to local broker with rc: " + str(rc))
    client.subscribe(LOCAL_MQTT_TOPIC)

local_mqttclient = mqtt.Client()
local_mqttclient.loop_start()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)


# the index depends on your camera setup and which one is your USB camera.
# you may need to change to 1 or 2 depending on your machine.
cap = cv2.VideoCapture(0) # with macOS and an iphone, this might be your iphone camera
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
    	cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    	
    	face_img = gray[y:y+h, x:x+w]
    	rc, png = cv2.imencode('.png', face_img)
    	msg = png.tobytes() 
    	
    	# publish the face
    	try:
    	    print("sending face img to local mqtt")
    	    local_mqttclient.publish(LOCAL_MQTT_TOPIC, msg, qos=0, retain=False)
    	except Exception as e:
    	    print("Unexpected error")
    	    print(e)

    # Display the resulting frame
    cv2.imshow('Video', frame)
    	
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
