#目标
* 开发一个全智能的语音识别机器人,期望安装在树莓派上，然后控制家里的家电，并且可以控制linux内核的笔记本等设备识别指令集

#开发语言
* python

#python依赖包
* pyaudio
* wave
* Internet connection
* gntp

#linux依赖包
* growl for linux

#如何使用
* 启动gol(growl on linux) 我编译安装之后路径如下/usr/local/bin/gol
* python startup.py

#Todolist

* 多线程,网络模型如下:有一个栈专门用于接受音频,有很多个子线程(或者多个进程)从栈中抢取音频指令,对于阻塞的指令可能需要特殊处理,例如播放音乐
* tts 将stt的指令转化为mp3内容
* 静音判断
* gntp 和 growl 共同结合 给用户有好提示信息
* 搜索指令集需要分类(可以借助dbpedia)，例如人物，音乐，学习，编程手册等等
* 语音识别本地化，Julius speech recogition是一个开源的项目
* 利用树莓派嵌入式的优势，然后开发控制tv，空调等指令

#has done
* 录音功能，最长录音时间5S，如果中间停顿次数多余15次会提前终止此次录音
* stt功能，将上一步的录音通过google api 翻译音频内容
* command功能 根据上一步google api 返回的内容，进行简单指令操作
* 加入Usage命令提示功能
* 实现了 start/stop 命令功能
* 实现了同时只有一个应用程序启动的判断

#doing
* Yahoo由14个基本大类组成，包括
    Art＆Humanities(艺术与人文)、Business＆Economy(商业与经济)、
    Computers＆Internet(电脑与网际网路/网络)、Education(教育)、
    Entertainment(娱乐)、Government(政府)、Health(健康与医药)、
    News＆Media(新闻与媒体)、Recreation＆Sports(休闲与运动)、
    Reference(参考资料)、Regional(国家与地区)、
    Science(科学)、SocialScience(社会科学)、
    Society＆Culture(社会与文化)
* 静音判断,正在研究vad技术
* growl的gntp协议

#参考文档如下
* [Linux音频编程指南](http://www.ibm.com/developerworks/cn/linux/l-audio/index.html)
* [python pyaudio doc](http://people.csail.mit.edu/hubert/pyaudio/#docs)
* [Gordons Projects](https://projects.drogon.net/raspberry-pi/wiringpi/)
* [text to speach](http://translate.google.com/translate_tts?q=%E6%AC%A2%E8%BF%8E%E5%85%89%E4%B8%B4%E4%B8%83%E5%93%A5%E7%9A%84%E5%8D%9A%E5%AE%A2&tl=zh-CN)
* 搜索引擎Yahoo的分类体系及性能评价
* [静音判断参考资料](http://ibillxia.github.io/blog/2013/05/22/audio-signal-processing-time-domain-Voice-Activity-Detection/)
* [基于短时能量与过零率的端点检测的matlab分析 ](http://blog.csdn.net/ziyuzhao123/article/details/8932336)
* [Google speech recognition with python](http://campus.albion.edu/squirrel/2012/03/01/google-speech-recognition-with-python/)
* [gntp](https://github.com/kfdm/gntp)
* [Growl For Linux](https://github.com/apanly/growl-for-linux)
