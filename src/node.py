import paramiko
from socket import error as socket_error
import os

class node:
    def __init__(self, ip):
        self.ip = ip
        k = paramiko.ECDSAKey.from_private_key_file("/app/private.key")
        self.c = paramiko.SSHClient()
        self.c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.c.connect( hostname = ip, username = "admin", pkey = k )

    def getAvgLoad(self):
        # get number of processors
        stdin, stdout, stderr = self.c.exec_command("nproc")
        stdin.close()
        noProc = stdout.read().splitlines()[0].decode('ascii')
        
        # get load average of last 5 minutes
        stdin, stdout, stderr = self.c.exec_command("cat /proc/loadavg | cut -d' ' -f2")
        stdin.close()
        loadAvg = stdout.read().splitlines()[0].decode('ascii')

        # divide load average by number of processors
        return float(loadAvg) / float(noProc)