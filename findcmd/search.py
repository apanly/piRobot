# -*- coding: utf-8 -*-
import jieba
from mapping import codemapping
from convert import codeconvert
txt="空调温度低点"
ret=jieba.cut(txt,cut_all=False)
search=codemapping()
cmdconvert=codeconvert()
cmds=[]
for subword in ret:
    cmds.append(subword)
#找到命令大类
cmdtype='broswer'
tmpindex=0
for cmd in cmds:
    tmptype=search.findBM(cmdconvert.convert(cmd))
    if tmptype:
        cmdtype=tmptype
        del cmds[tmpindex]
        break;
    tmpindex+=1

#找到最终要执行的命令
for cmd in cmds:
    tmp=search.findcmdinfo(cmdtype,cmd)
    if tmp:
        if type(tmp) is dict:
            pass
        break

