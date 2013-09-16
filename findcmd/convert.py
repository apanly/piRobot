#!/usr/bin/python
# -*- coding: utf-8 -*-

class codeconvert:
    def __init__(self):
        mapping={}
        mapping[u'电视']="tv"
        mapping[u'空调']="air"
        mapping[u'电灯']="light"
        mapping[u'浏览器']="broswer"
        mapping[u'天气预报']="weather"
        mapping[u'天气']="weather"
        self.mapping=mapping
    def convert(self,txt):
        mapping=self.mapping
        if txt in mapping:
            return mapping[txt]
        else:
            return txt
