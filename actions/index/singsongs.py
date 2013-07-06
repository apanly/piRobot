__author__ = 'vincent'
import os
import random
class SingSongs:
    def docmd(self):
        MUSICROOT="/home/vincent/Music/"
        allsongs=[]
        for filename in os.listdir(MUSICROOT):
            allsongs.append(MUSICROOT+filename)
        os.system("mplayer  %s"%random.choice(allsongs)) #allsongs[random.randint(0, len(allsongs)-1)]
        return

