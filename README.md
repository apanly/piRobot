#目标
* 开发一个全智能的语音识别机器人,期望安装在树莓派上，然后控制家里的家电，并且可以控制linux内核的笔记本等设备识别指令集

#开发语言
* python

#依赖包
* pyaudio
* wave
* Internet connection

#Todolist

* 多线程,网络模型如下:有一个栈专门用于接受音频,有很多个子线程从栈中抢取音频指令,对于阻塞的指令可能需要特殊处理,例如播放音乐
* tts 将stt的指令转化为mp3内容
* 搜索指令集需要分类(可以借助dbpedia)，例如人物，音乐，学习，编程手册等等
* 语音识别本地化，Julius speech recogition是一个开源的项目
* 利用树莓派嵌入式的优势，然后开发控制tv，空调等指令

#参考文档如下

* [Linux音频编程指南](http://www.ibm.com/developerworks/cn/linux/l-audio/index.html)
* [python pyaudio doc](http://people.csail.mit.edu/hubert/pyaudio/#docs)
* [Gordons Projects](https://projects.drogon.net/raspberry-pi/wiringpi/)
* [text to speach](http://translate.google.com/translate_tts?q=%E6%AC%A2%E8%BF%8E%E5%85%89%E4%B8%B4%E4%B8%83%E5%93%A5%E7%9A%84%E5%8D%9A%E5%AE%A2&tl=zh-CN)
