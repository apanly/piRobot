# -*- coding: utf-8 -*-
import jieba
from mapping import codemapping
from convert import codeconvert
txt="空调温度低点"
ret=jieba.cut(txt,cut_all=False)
search=codemapping()
cmdconvert=codeconvert()
for cmd in ret:
    search.findBM(cmdconvert.convert(cmd))