#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from index.browser import Browser
from index.singsongs import SingSongs
class InstructionSet:

    def __init__(self,txt):
        self.txt=txt

    def docmd(self):
        self.browser()
        self.terminal()
        self.singhappy()

    def browser(self):
        target=Browser()
        if self.txt.find("谷歌") > -1 :
            target.docmd("www.google.com.hk")
        elif self.txt.find("google")>-1 :
            target.docmd("www.google.com.hk")
        elif self.txt.find("百度") > -1:
            target.docmd("www.baidu.com")
        elif self.txt.find("新浪") > -1:
            target.docmd("www.sina.com.cn")
        elif self.txt.find("火狐") > -1:
            target.docmd("ww.echocool.net")


    def terminal(self):
        if self.txt.find("终端") > -1 :
            os.system("gnome-terminal")
        if self.txt.find("ternimal") > -1 :
            os.system("gnome-terminal")

    def singhappy(self):
        target=SingSongs()
        target.docmd()


