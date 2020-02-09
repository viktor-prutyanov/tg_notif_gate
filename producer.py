import requests

class Producer():
    def __init__(self, addr):
        self.addr = addr

    def publish(self, msg):
        payload = {'msg': msg}
        req = requests.get(self.addr, params=payload)

        return req
