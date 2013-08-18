# -*- coding: utf-8 -*-
from Queue import Queue
import os
queue = Queue() #用于当作存放用户音频的队列，后面的处理线程从这个队列取数据
# Temporaries files
CACHEFOLDER = os.getenv('HOME') + '/.cache/piRobot/'
if not os.path.exists(CACHEFOLDER):
    os.makedirs(CACHEFOLDER)

WAVPATH="/home/vincent/coding/python/piRobot/" #用于指定录音文件存放在什么地方

SEARCH="https://www.google.com.hk/search?newwindow=1\&safe=active\&hl=en\&site=webhp\&source=hp\&q=%s&oq=%s"

PIDLOG="%spiRobot.pid"%CACHEFOLDER

SPEECHTTS="%spicotts.wav"%CACHEFOLDER

DOUBANFM="http://douban.fm/j/mine/playlist?type=n&channel=1"
