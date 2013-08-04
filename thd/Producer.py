import threading
from inputs.microphone import microphone
from gl import queue
from gl import WAVPATH
import time
import os
class Producer(threading.Thread):
    def __init__(self,debugInit):
        threading.Thread.__init__(self)
        self.debug=debugInit

    def run(self):
        global  queue
        global  WAVPATH
        while 1:
            timestamps=int(time.time());
            wavefilepath=WAVPATH+"output%d.wav"%timestamps
            audioInput = microphone(wavefilepath,self.debug)
            audioInput.recordAudio()
            if audioInput.getSleepFLag() == 0:
                os.remove(wavefilepath)
            else:
                self.debug.saytxt("producter file:%s"%wavefilepath)
                queue.put(wavefilepath)
            time.sleep(5)

