#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from index.browser import Browser
from index.singsongs import SingSongs
from gl import SEARCH
import urllib
class InstructionSet:

    def __init__(self,txt,debug):
        self.txt=txt
        self.debug=debug
        self.setCmdFlag(False)

    def docmd(self):
        if self.getCmdFlag()==False:
            self.debug.saytxt("cmd:browser")
            self.browser()
        if self.getCmdFlag()==False:
            self.debug.saytxt("cmd:terminal")
            self.terminal()
        if self.getCmdFlag()==False:
            self.debug.saytxt("cmd:songs")
            self.singhappy()
        if self.getCmdFlag()==False:
            self.googleSearch()

    def browser(self):
        target=Browser()
        if self.txt.find("谷歌") > -1  or self.txt.find("google")>-1 :
            self.setCmdFlag(True)
            target.docmd("www.google.com.hk")
        elif self.txt.find("百度") > -1:
            self.setCmdFlag(True)
            target.docmd("www.baidu.com")
        elif self.txt.find("新浪") > -1:
            self.setCmdFlag(True)
            target.docmd("www.sina.com.cn")
        elif self.txt.find("火狐") > -1:
            self.setCmdFlag(True)
            target.docmd("ww.echocool.net")


    def terminal(self):
        if self.txt.find("终端") > -1 or self.txt.find("ternimal") > -1 :
            self.setCmdFlag(True)
            os.system("gnome-terminal")

    def singhappy(self):
        target=SingSongs()
        if self.txt.find("首歌")>-1 or self.txt.find("听歌")>-1:
            self.setCmdFlag(True)
            target.docmd()

    def googleSearch(self):
        global  SEARCH
        q=urllib.quote_plus((u'%s'%self.txt).encode('utf8'))
        searchquri=SEARCH%(q,q)
        target=Browser()
        target.docmd(searchquri)

    def setCmdFlag(self,modeFlag):
        self.Flag=modeFlag

    def getCmdFlag(self):
        return self.Flag



