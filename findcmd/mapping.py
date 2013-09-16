#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
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

    #find the best match key
    def findBM(self,txt):
        mapping=self.mapping
        retval=''
        for item in mapping:
             index=txt.find(item)
             if index>-1:
                 retval=item
                 break
        return retval
    def findcmdinfo(self,cmdtype,txt):
        cmds=self.mapping[cmdtype]
        retval={}
        for item in cmds:
            index=txt.find(item)
            if index>-1:
                tmpret=cmds[item]
                if type(tmpret) is dict:
                    retval['data']=item
                    retval['guide']='next'
                else:
                    retval['data']=tmpret
                    retval['guide']='over'
                    retval['type']=self.mapping[cmdtype]['type']
                    retval['kind']=cmdtype
                break;
        return retval
    def findlastcmdinfo(self,cmdtype,skey,txt):
        cmds=self.mapping[cmdtype][skey]
        retval={}
        retval['type']=self.mapping[cmdtype]['type']
        retval['kind']=cmdtype
        for item in cmds:
            index=txt.find(item)
            if index>-1:
                tmpret=cmds[item]
                retval['code']=tmpret
                break
        return retval





