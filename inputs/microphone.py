# -*- coding: utf-8 -*-
import pyaudio
import wave
from array import array

class microphone:

    def __init__(self,savepath,debug):
        self.savepath=savepath
        self.debug=debug

    def getRate(self):
        return 16000

    def silent(self,recorddata):
        return max(array('h', recorddata))<self.slientThreshold()

    def slientThreshold(self):
        return 5000

    def recordAudio(self):
        NUM_SILENT=10
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1 # 0,1
        RECORD_SECONDS=5
        RATE = self.getRate() #采样频率
        WAVE_OUTPUT_FILENAME = self.savepath
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
        self.debug.saytxt("* recording")
        frames = []
        num_silent=0
        longtime=int(RATE / CHUNK * RECORD_SECONDS) # if time is belong 5 ,force stop
        counter=0;
        while 1:
            counter +=1
            data = stream.read(CHUNK)
            frames.append(data)
            silent=self.silent(data)
            if silent:
                num_silent += 1
                self.debug.saytxt("* sleeping")
            else:
                num_silent = 0
                self.debug.saytxt("* active")
            if num_silent>=NUM_SILENT:
                self.debug.saytxt("* sleeping too long")
                break
            if counter>longtime:
                self.debug.saytxt("* record time out")
                break
        self.debug.saytxt("* done recording")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()