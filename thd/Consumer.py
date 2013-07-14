
import threading
import time
from  stt.google import google
from  actions.command import InstructionSet
from gl import queue
import os
class Consumer(threading.Thread):
    def __init__(self,debugInit):
        threading.Thread.__init__(self)
        self.debug=debugInit

    def run(self):
        global  queue
        while 1:
            if queue.qsize()>0 :
                wavpath=queue.get()
                self.debug.saytxt("comsumer file:%s"%wavpath)
                speech_to_text=google(wavpath,self.debug)
                command=speech_to_text.sst_google()
                os.remove(wavpath)
                if command:
                    self.debug.saytxt(command)
                    cmd=InstructionSet(command,self.debug)
                    cmd.docmd()
                else:
                    self.debug.saytxt("Sorry, I couldn't understand what you said")
            else :
                self.debug.saytxt('Time:%s/n' %(time.ctime()))
                time.sleep(5)

