# 251_hw2

**Links to s3 Bucket Images** :
https://hw2bucket-cs.s3.amazonaws.com/imgfile1
https://hw2bucket-cs.s3.amazonaws.com/imgfile2
https://hw2bucket-cs.s3.amazonaws.com/imgfile3
https://hw2bucket-cs.s3.amazonaws.com/imgfile4
https://hw2bucket-cs.s3.amazonaws.com/imgfile5
https://hw2bucket-cs.s3.amazonaws.com/imgfile6
https://hw2bucket-cs.s3.amazonaws.com/imgfile7
https://hw2bucket-cs.s3.amazonaws.com/imgfile8
https://hw2bucket-cs.s3.amazonaws.com/imgfile9


### MQTT Details
I chose to use the deault value (0) for the QoS becasue it provided the functionality necessary--the sender (edge) did not need acknowldegment of reciept of the message because I could see the client recieving the messages. The message did not need to be stored and re-transmitted by the sender. Additionally, I used the same mqtt topic name to reduce complexity.

### Steps to run:

Aws ec2 instance:
1. start instance, install docker and kubernets using instructions from week 1 homework
2. clone repo, cd into directory
2. run the following commands:

```
kubectl apply -f mosquitto-deployment.yaml
kubectl apply -f mosquittoService.yaml
kubectl apply -f processor-deployment.yaml
```

Edge vm:
1. necessary installs (docker, k8s), clone repo, cd into correct directory
2. check public IP and mosquitto service port and update forward.py

```
kubectl apply -f mosquitto-deployment.yaml
kubectl apply -f mosquittoService.yaml
kubectl apply -f forwarder-deployment.yaml
kubectl apply -f camera-deployment.yaml
```


