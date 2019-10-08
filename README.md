# Cisco Container Platform node autoscaler

This repository contains the source code for a script which allows you to autoscale CCP clusters based on load average using the CCP API.

## Getting Started

These instructions will get you a copy of the project up and running on your environment.

### Prerequisites

* Credentials to your CCP interface
* Network access to CCP and the cluster worker nodes
* A CCP cluster (version 2) that's up and running
* The private ECDSA key which you configured for node access
* If you're using ACI as your CNI: contracts between the cronjob and CCP (http) / worker nodes (ssh)

### Installing

A step by step walkthrough to get this up and running in your own environment:

1. Clone this GIT repository
2. Change directory to ccp-autoscaler
3. Insert your ECDSA private key into the [private.key](src/private.key) file (edit the file and paste in the key)
4. Build your docker image using the [Dockerfile](Dockerfile) (docker build -t "imagename" .)
5. Push the Docker image to your repository (docker push "imagename")
6. Edit [cron.yaml](cron.yaml) variables (ip, user, pass of your CCP management interface; k8s cluster name; the name you gave your pushed image) to match your setup
7. Apply the cron.yaml file to your cluster (kubectl apply -f cron.yaml)

## How it works

First, the script will contact CCP to get all worker node ip's. Next, it will connect to all worker nodes via SSH to get the load average of the past 5 minutes. 

The script will calculate the load average of the entire cluster (sum of (load nodeX / processor count nodeX) / total nodes in cluster) and contact CCP to scale the nodes up when the load average is above 80% or down when the load average is below 50%.

The project is open source so feel free to adapt the script to fit your own environment.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
