import requests
class CCP:
    def __init__(self, ip, username, password):
        self.ip = ip
        data = "username="+ username + "&password=" + password
        r = requests.post(url = "https://" + ip + "/2/system/login", data = data, headers={"content-type":"application/x-www-form-urlencoded"}, verify=False)
        self.cookie = ""
        for cookie in r.cookies:
            self.cookie = cookie.value

    def getIP(self):
        return self.ip

    def getcookie(self):
        return self.cookie