#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from  inputs.microphone import microphone
from  outputs.speaker import aerophone
from  stt.google import google
from ex.exception import NotUnderstoodException
from  actions.command import InstructionSet
from outputs.debug import debug

def main():
    debugInit=debug()
    try:
        WAVPATH="/home/vincent/coding/python/piRobot/output.wav"
        audioInput = microphone(WAVPATH,debugInit)
        audioInput.recordAudio()
        speech_to_text=google(audioInput,debugInit)
        command=speech_to_text.sst_google()
        debugInit.saytxt(command)
        cmd=InstructionSet(command,debugInit)
        cmd.docmd()
        #audioOutput=aerophone(WAVPATH)
        #audioOutput.play()
    except NotUnderstoodException:
        debugInit.saytxt("error")


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    main()