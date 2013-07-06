# -*- coding: utf-8 -*-
import pyaudio
import wave

from array import array
from outputs.debug import  debug

class microphone:

	def __init__(self,savepath):
		self.savepath=savepath

	def getRate(self):
		return 16000

	def silent(self,recorddata):
		return max(array('h', recorddata))<self.slientThreshold()

	def slientThreshold(self):
		return 5000

	def recordAudio(self):
		NUM_SILENT=15
		CHUNK = 1024
		FORMAT = pyaudio.paInt16
		CHANNELS = 1 # 0,1
		RATE = self.getRate() #采样频率
		RECORD_SECONDS = 5
		WAVE_OUTPUT_FILENAME = self.savepath

		p = pyaudio.PyAudio()

		stream = p.open(format=FORMAT,
		                channels=CHANNELS,
		                rate=RATE,
		                input=True,
		                frames_per_buffer=CHUNK)

		debugtarget=debug()
		debugtarget.saytxt("* recording")

		frames = []
		num_silent=0
		while 1:
			#for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		    data = stream.read(CHUNK)
		    frames.append(data)
		    silent=self.silent(data)
		    if silent:
		    	num_silent += 1
		    	debugtarget.saytxt("* sleeping")
		    else:
		    	num_silent = 0
		    	debugtarget.saytxt("* active")

		    if num_silent>=NUM_SILENT:
		    	break


		debugtarget.saytxt("* done recording")

		stream.stop_stream()
		stream.close()
		p.terminate()

		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
		wf.close()