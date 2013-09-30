# -*- coding: utf-8 -*-
#!/usr/bin/python
#coding=utf-8
import socket

class proofreadClient():
    def __init__(self,txt):
        self.txt=txt
    def do(self):
        txt=self.txt
        address = ('127.0.0.1', 10000)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        try:
            s.connect(address)
            s.send("%s\r"%txt)
            result=s.recv(1024)
            if result=="correct":
                return txt
            else:
                return result
        except IOError:
            return txt


# target=proofreadClient("看电视")
# print target.do()