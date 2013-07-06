import pyaudio
import wave
import sys

class aerophone:
	def __init__(self,filepath):
		self.filepath=filepath


	def play(self):

		print("* speaker")

		CHUNK = 1024

		wf = wave.open(self.filepath, 'rb')

		p = pyaudio.PyAudio()

		stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
		                channels=wf.getnchannels(),
		                rate=wf.getframerate(),
		                output=True)

		data = wf.readframes(CHUNK)

		while data != '':
		    stream.write(data)
		    data = wf.readframes(CHUNK)

		stream.stop_stream()
		stream.close()

		p.terminate()