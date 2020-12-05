#! /bin/ python

import os
class Server (object):
    def __init__(self,ip,hostname):
        self.ip=ip
        self.hostname= hostname
    def set_ip(self,ip):
        self.ip=import ip
    def set_hostname(self,hostname):
        self.hostname=hostname
    def ping(self,ip_addr):
        print("pinging % from %s %" % ip_addr, self.ip, self.hostname)

if __name__== '__main__':
    server= Server('192.168.1.104','localhost')
    server.ping('192.168.1.1')
