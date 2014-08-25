__author__ = 'vincent'
import os
import random
import urllib2
import urllib
import json
class SingSongs:
    def docmd(self):
        print  os.getpid()
        os.system("mplayer  %s"%self.douban())
        return
    def douban(self):
        songrui=''
        f = urllib2.urlopen("http://douban.fm/j/mine/playlist?type=n&channel=1")
        res = f.read()
        f.close()
        doubansongs = json.loads(res)['song']
        if doubansongs:
            for item in doubansongs:
                songrui=item['url']
                if songrui:
                    break
        return songrui


if __name__=="__main__":
    target=SingSongs()
    target.docmd()

