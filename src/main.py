import sys
import os
from ccp import CCP
from cluster import cluster
from node import node
import logging

ccp = CCP(os.environ['CCPIP'],os.environ['CCPUSER'],os.environ['CCPPASS'])
cluster1 = cluster(os.environ['CLUSTERNAME'],ccp)
ips = cluster1.getworkerips()

totalLoad = 0
for ip in ips:
    workernode = node(ip)
    totalLoad = totalLoad + workernode.getAvgLoad()

loadAvgOverAllNodes = totalLoad / len(ips)
print("Average load over all nodes is " + str(loadAvgOverAllNodes))

if (loadAvgOverAllNodes > 0.8):
    # Load higher than 80% --> scale up
    print("Scaling up...")
    cluster1.scaleupworkernodes()
elif (loadAvgOverAllNodes < 0.5):
    if (cluster1.getnumberofworkernodes() > 1):
        # Load lower than 50% --> scale down
        print("Scaling down...")
        cluster1.scaledownworkernodes()