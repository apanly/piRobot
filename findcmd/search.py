# -*- coding: utf-8 -*-
import jieba
from mapping import codemapping
from convert import codeconvert

class vsearch:
    def __init__(self):
        pass
    def search(self,txt):
        ret=jieba.cut(txt,cut_all=False)
        search=codemapping()
        cmdconvert=codeconvert()
        cmds=[]
        for subword in ret:
            cmds.append(subword)
        print "==分词结果=="
        print  ",".join(cmds)
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
        tmpindex=0
        cmdinfo={'guide':'next','data':'default'}
        for cmd in cmds:
            tmp=search.findcmdinfo(cmdtype,cmd)
            if tmp:
                cmdinfo=tmp
                del cmds[tmpindex]
                break
            tmpindex+=1
        #有的可能要在找一次
        commands={}
        if cmdinfo['guide']=='next':
            for cmd in cmds:
                tmp=search.findlastcmdinfo(cmdtype,cmdinfo['data'],cmd)
                if tmp:
                    commands=tmp
                    break
        elif cmdinfo['guide']=="over":
            commands['type']=cmdinfo['type']
            commands['code']=cmdinfo['data']
            commands['kind']=cmdinfo['kind']

        return commands
