#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.append(".")

from ex.exception import NotUnderstoodException

from outputs.debug import debug
from thd.Consumer import  Consumer
from thd.Producer import Producer
from customnotify.gntpnotify import gntpnotify
def main():
    debugInit=debug()
    '''
     如果用户是桌面系统,就可以提示用户信息
    '''
    #gntptarget=gntpnotify()
    #gntptarget.ownnotify()
    '''
    目前准备是1个生产者 5个消费者的模型
    '''
    try:
        producerTarget=Producer(debugInit)
        producerTarget.start()
        for i in range(5):
            consumerTarget=Consumer(debugInit)
            consumerTarget.start()
        #consumerTarget.join()
        #producerTarget.join()
        #for i in range(1,2):
        #    target=Consumer(debugInit)
        #    target.start()
        #audioOutput=aerophone(WAVPATH)
        #audioOutput.play()
    except NotUnderstoodException:
        debugInit.saytxt("error")

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()