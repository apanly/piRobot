
import os
from outputs.speaker import aerophone
from gl import SPEECHTTS


class picotts:
    def __init__(self,txt):
        self.txt=txt
        self.lang="en-US"

    def onPlayer(self):
        global SPEECHTTS
        os.system('pico2wave -l %s -w %s \"%s\" ' % ( self.lang, SPEECHTTS, self.txt ))
        player=aerophone(SPEECHTTS)
        player.play()



