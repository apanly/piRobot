#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import atexit
import signal
from ex.exception import NotUnderstoodException
from outputs.debug import debug
from thd.Consumer import  Consumer
from thd.Producer import Producer
from customnotify.gntpnotify import gntpnotify
from gl import PIDLOG
global PIDLOG
def Usage():
    helpContent='Usage:  python startup.py start/stop/restart'
    print helpContent
    exit()
#为了防止并发加入PID文件
def writePID():
    fd=os.open(PIDLOG,os.O_CREAT|os.O_EXCL|os.O_RDWR)
    os.write(fd,"%s" % str(os.getpid()))
    os.close(fd)
#删除本应用程序的PID
def deletePID():
    try:
        os.remove(PIDLOG)
    except:
        pass

def main():
    atexit.register(lambda:deletePID())
    writePID()
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
        tList = []
        producerTarget=Producer(debugInit)
        tList.append(producerTarget)
        for i in range(5):
            consumerTarget=Consumer(debugInit)
            tList.append(consumerTarget)
        for t in tList:
            t.setDaemon(1)
            t.start()
    except NotUnderstoodException:
        debugInit.saytxt("error")
    #Controller+C也可以终止程序
    while True:
        try:
            sys.stdin.read()
        except KeyboardInterrupt:
            stop()


def stop():
    if os.path.exists(PIDLOG):
        fd=open(PIDLOG)
        pid=int(fd.readline())
        fd.close()
        try:
            deletePID()
            os.kill(pid,signal.SIGTERM)
        except:
            raise SystemExit('1:收到终止命令,退出程序')
    raise SystemExit('2:收到终止命令,退出程序')

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sys.path.append(".")#加入默认的扫描路径
    params=sys.argv
    if len(params)<2:
        Usage()
    else:
        #signal.signal(signal.SIGINT,stop) #当按下Ctrl+C 终止进程
        #signal.signal(signal.SIGKILL,stop) #kill
        #signal.signal(signal.SIGTERM,stop)
        if params[1]=="start":
            if os.path.exists(PIDLOG):
                print("Program is running")
                Usage()
            else:
                main()
        elif params[1]=="stop":
            stop()
        elif params[1]=="restart":
            pass