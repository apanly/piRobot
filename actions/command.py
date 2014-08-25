#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from index.infrate import innerInfrated
from index.ppt import  innerppt
from tts.picotts import picotts
from proofread.javaproofread import proofreadClient
#from index.cam import camera

class InstructionSet:

    def __init__(self,txt,debug):
        self.txt=txt
        self.debug=debug
        self.pico=picotts("welcome to google world")

    def docmd(self):
        print self.txt
        self.pico.onPlayer()
        prooftarget=proofreadClient(self.txt)
        result=prooftarget.do()
        commands=result.split(",")
        cmdtype=commands[3]
        cmddetail=commands[2]
        if cmdtype=="tv":
            self.dotvair(cmddetail)
        elif cmdtype=="air":
            self.dotvair(cmddetail)
        elif cmdtype=="ppt":
            self.doppt(cmddetail)
        #测试照相功能
        #camtarget=camera()
        #camtarget.do()

    def dotvair(self,command):
        target=innerInfrated()
        target.gogo(command)
    def doppt(self,command):
        target=innerppt()
        target.gogo(command)





