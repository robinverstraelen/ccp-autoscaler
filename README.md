# Cisco Container Platform node autoscaler

This repository contains the source code for a script which allows you to autoscale CCP clusters based on load average using the CCP API.

## Getting Started

These instructions will get you a copy of the project up and running on your environment.

### Prerequisites

* Credentials to your CCP interface
* Network access to CCP and the cluster worker nodes
* A CCP cluster (version 2) that's up and running
* The private key ECDSAKEY which you configured for node access
* Contracts between the cronjob and CCP (http) / worker nodes (ssh)

### Installing

A step by step walkthrough to get this up and running in your own environment:

1. Insert your ECDSAKEY private key into the [private.key](src/private.key) file
2. Build your docker image using the [Dockerfile](Dockerfile)
3. Push the Docker image to your repository
4. Edit [cron.yaml](cron.yaml) variables to match your setup
5. Apply the cron.yaml file to your cluster

## How it works

First, the script will contact CCP to get all worker node ip's. Next, it will connect to all worker nodes via SSH to get the load average of the past 5 minutes. 

The script will calculate the load average of the entire cluster (sum of (load nodeX / processor count nodeX) / total nodes in cluster) and contact CCP to scale the nodes up when the load average is above 80% or down when the load average is below 50%.

The project is open source so feel free to adapt the script to fit your own environment.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details