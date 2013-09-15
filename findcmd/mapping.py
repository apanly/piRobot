#!/usr/bin/python
# -*- coding: utf-8 -*-
class codemapping:
    def __init__(self):
        self.mapping={}
        self.inittv()
        self.initair()
        self.initlight()
        self.initweath()
        self.initbroser()
    def inittv(self):
        mapping=self.mapping
        if 'tv' not in mapping:
            mapping['tv']={"声音":{"大":40,"小":41},"关":42,"开":43,"type":'infrated'}
    def initair(self):
        mapping=self.mapping
        if 'air' not in mapping:
            mapping['air']={"关":42,"开":43,"温度":{"高":44,"低":45},"type":'infrated'}
    def initlight(self):
        mapping=self.mapping
        if 'light' not in mapping:
            mapping['light']={"关":42,"开":43,"type":'infrated'}
    def initweath(self):
        mapping=self.mapping
        if 'weather' not in mapping:
            mapping['weather']={'今天':'onedayweather',"现在":'liveweather','type':'api'}
    def initbroser(self):
        mapping=self.mapping
        if 'broswer' not in mapping:
            mapping['broswer']={'google':'www.google.com.hk',"百度":'www.baidu.com','新浪':'www.sina.com.cn','type':'api'}

    #find the best match
    def findBM(self,txt):
        print "============="
        print txt
        mapping=self.mapping
        for item in mapping:
            print item
