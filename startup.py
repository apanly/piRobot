#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys 
reload(sys) 
sys.setdefaultencoding('utf-8')

from  inputs.microphone import microphone
from  outputs.speaker import aerophone
from  stt.google import google
from ex.exception import NotUnderstoodException

from  actions.command import InstructionSet

def main():

	try:

		WAVPATH="/home/vincent/coding/python/piRobot/output.wav"

		audioInput = microphone(WAVPATH)

		audioInput.recordAudio()

		#exit()

		speech_to_text=google(audioInput)

		command=speech_to_text.sst_google()

		cmd=InstructionSet(command)


		#audioOutput=aerophone(WAVPATH)

		#audioOutput.play()

	except NotUnderstoodException:

		print("error")


if __name__ == "__main__":

	main()