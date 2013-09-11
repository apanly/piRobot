#!/usr/bin/python
# -*- coding: utf-8 -*-
class codemapping:
    def __init__(self):
        mapping={}
        mapping['google']={'type':'browser','cmd':'www.google.com.hk'}
        mapping['谷歌']=mapping['google']
        mapping['baidu']={'type':'browser','cmd':'www.baidu.com'}
        mapping['百度']=mapping['baidu']
        mapping['新浪']={'type':'browser','cmd':'www.sina.com.cn'}
        self.mapping=mapping
    def codetomsg(self,code):
        if code in self.mapping:
            return self.mapping[code]
        else:
            return 'unknown'
        pass
    def msgtocode(self,txt):
        pass
