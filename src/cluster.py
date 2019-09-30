import requests
import json
class cluster:

    def __init__(self, name, ccp):
        self.name = name
        self.ccp = ccp

        # get cluster config
        r = requests.get(url = "https://" + ccp.getIP() + "/2/clusters/" + name + "/", headers={"X-Auth-Token":ccp.getcookie()}, verify=False)

        self.config = r.json()
        self.uuid = self.getclusteruuid()

    def updateconfig(self):
        r = requests.get(url = "https://" + self.ccp.getIP() + "/2/clusters/" + self.name + "/", headers={"X-Auth-Token":self.ccp.getcookie()}, verify=False)
        self.config = r.json

    def getclusteruuid(self):
        return self.config['uuid']

    def getnumberofworkernodes(self):
        return self.config['workers']

    def scaleupworkernodes(self):
        currentNodes = self.getnumberofworkernodes()
        data = '{ "workers": ' + str(currentNodes + 1) + ' }'
        requests.patch(url = "https://" + self.ccp.getIP() + "/2/clusters/" + self.uuid + "/", data = data, headers={"X-Auth-Token":self.ccp.getcookie(), "Content-Type": "application/json"}, verify=False)

    def scaledownworkernodes(self):
        currentNodes = self.getnumberofworkernodes()
        if (currentNodes > 1):
            data = '{ "workers": ' + str(currentNodes - 1) + ' }'
            requests.patch(url = "https://" + self.ccp.getIP() + "/2/clusters/" + self.uuid + "/", data = data, headers={"X-Auth-Token":self.ccp.getcookie(), "Content-Type": "application/json"}, verify=False)
    
    def getworkerips(self):
        ips = []
        for node in self.config['nodes']:
            if not node['is_master']:
                ips.append(node['public_ip'])
        return ips