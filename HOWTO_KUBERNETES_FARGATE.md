# How to configure your Kubernetes Fargate Cluster

In order to create the k8s cluster:

## Configure the tools

* Install AWSCLI: https://linuxhint.com/install_aws_cli_ubuntu/
* Configure AWSCLI
```
aws configure
```
* Install Kubectl: https://kubernetes.io/es/docs/tasks/tools/install-kubectl/
* Install eksctl: https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html

## Create the cluster
```
eksctl create cluster -f rodo-eks.yaml
```
IMPORTANT: I had to use an already existing VPC (see config)

## Deploy your first app
```
kubectl apply -f api.yaml
```

## Give permissions 

* Your node has 2 IP addresses: a public and a private
* You could use the private when connecting internally
* Go to the node security group and add the inbound rule for nodePort and IP addresses or security groups that you want to use
* For SDM you might want to assign tags to the created nodes (ec2 instances)

## Deploy DB

https://kubernetes.io/docs/tasks/run-application/run-single-instance-stateful-application/

# Some learnings

* You cannot use persistent volumes in fargate clusters
* You cannot use affinityNode rules in fargate, better to use externalIp for the service

