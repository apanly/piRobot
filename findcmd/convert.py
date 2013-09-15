#!/usr/bin/python
# -*- coding: utf-8 -*-

class codeconvert:
    def __init__(self):
        mapping={}
        mapping['电视']="tv"
        mapping['空调']="air"
        mapping['电灯']="light"
        mapping['浏览器']="broswer"
        mapping['天气']="weather"
        self.mapping=mapping
    def convert(self,txt):
        mapping=self.mapping
        if '电视' in mapping:
            print 1
            return mapping[u''+txt]
        else:
            print 3
            return txt
