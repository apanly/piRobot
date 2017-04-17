申明
===================
项目转移到 [autohome](https://github.com/apanly/autohome),目的是全新重构智能家居系统,是系统更具有扩展性


家居声控系统
==================
# 目标
* 开发一个全智能的语音识别机器人,期望安装在树莓派上，然后控制家里的家电，并且可以控制linux内核的笔记本等设备识别指令集

# 开发语言
* python

# python依赖包(推荐使用easy_install安装依赖)
* requests
* pyzmq
* pyaudio(如若提示portaudio错误，请安装就可以了)
* PIL(Python Imaging Library)
* v4l2capture
* wave
* Internet connection
* gntp
* wolframalpha

# linux依赖包
* growl for linux
* pico2wave
* sudo apt-get install espeak

# 如何使用
* 启动gol(growl on linux) 我编译安装之后路径如下/usr/local/bin/gol
* python startup.py

# 系统架构图
![家居声控系统图](http://www.echocool.net/wp-content/uploads/2013/09/sys.png)

# Todolist
* 静音判断
* 搜索指令集需要分类(可以借助dbpedia)，例如人物，音乐，学习，编程手册等等
* 语音识别本地化，Julius speech recogition是一个开源的项目
* 加入学习模式,例如大耳朵、可可、沪江等网站，可以获取感兴趣的每天开始学习
* 加入新闻机器人的功能，以后看新闻就可以不用那么多网站找了（想法是可以找英文和科技）英文我发现有个拓词和百词斩非常不错
* 命令分类：电视,空调,唱歌,编程,新闻,图片,天气预报(目前就这几类,后面可以添加),先找命令类型，然后执行详细命令 例如电视频道50(分词结果电视频道,50) 电视 先找到电视类别，然后执行频道50

# has done
* 录音功能，最长录音时间5S，如果中间停顿次数多余15次会提前终止此次录音
* stt功能，将上一步的录音通过google api 翻译音频内容
* command功能 根据上一步google api 返回的内容，进行简单指令操作
* 加入Usage命令提示功能
* 实现了 start/stop 命令功能
* 实现了同时只有一个应用程序启动的判断
* 在桌面环境使用growl提示用户
* 使用pico实现了tts->修改成e-speak (例如：espeak -vzh "郭威 我爱你")
* gntp 和 growl 共同结合 给用户有好提示信息
* 多线程,网络模型如下:有一个栈专门用于接受音频,有很多个子线程(或者多个进程)从栈中抢取音频指令,对于阻塞的指令可能需要特殊处理,例如播放音乐
* 利用树莓派嵌入式的优势，然后开发控制tv，空调等指令 --PS:这个已经实现了，请关注红外控制系统[piInfrated](https://github.com/apanly/piInfrated)


# doing
* Yahoo由14个基本大类组成，包括
    Art＆Humanities(艺术与人文)、Business＆Economy(商业与经济)、
    Computers＆Internet(电脑与网际网路/网络)、Education(教育)、
    Entertainment(娱乐)、Government(政府)、Health(健康与医药)、
    News＆Media(新闻与媒体)、Recreation＆Sports(休闲与运动)、
    Reference(参考资料)、Regional(国家与地区)、
    Science(科学)、SocialScience(社会科学)、
    Society＆Culture(社会与文化)
* 静音判断,正在研究vad技术
* 中文文本自动纠错
* 语音识别可以修改成Kaldi(google被墙了)


# 参考文档如下
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
* [语音识别实现方式之一](http://a7b.cn/2013/%E8%AF%AD%E9%9F%B3%E8%AF%86%E5%88%AB/#toc_3)
* [树莓派客厅中央控制](http://www.peiqianhuo.net/?p=28)
* [在Ubuntu的系统下通过串口连接IOIO-OTG](http://www.oschina.net/question/1174645_116717)
* [豆瓣书屋]https://api.douban.com/v2/book/search?q=%E6%B5%AA%E6%BD%AE%E4%B9%8B%E5%B7%85
* [天气查询]http://blog.mynook.info/2012/08/18/weather-com-cn-api.html
* [天气城市id]http://www.xiaoningmeng.com/2012/10/androids-china-weather-city-id-data/
* [浅谈中文文本自动纠错在影视剧搜索中应用与Java实现]http://www.cnblogs.com/wuren/archive/2012/12/21/2828649.html
* [espeak跨平台语音合成器](http://www.oschina.net/p/espeak/)
* [Raspberry Pi创意大荟萃](http://guiquanz.github.io/2013/01/04/projects-of-raspberry-pi/)
* [几个常见的语音交互平台的简介和比较](http://blog.csdn.net/lchunli/article/details/18504799)

# How to Contact
## QQ:36405410
## Email:apanly@163.com


# Copying
### Free use of this software is granted under the terms of the GNU Lesser General Public License (LGPL)
