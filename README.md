# 251_hw2


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
1. necessary installs, clone repo, cd into correct 

```
kubectl apply -f mosquitto-deployment.yaml
kubectl apply -f mosquittoService.yaml
kubectl apply -f forwarder-deployment.yaml
kubectl apply -f camera-deployment.yaml
```


