#目标
* 开发一个全智能的语音识别机器人,期望安装在树莓派上，然后控制家里的家电，并且可以控制linux内核的笔记本等设备识别指令集
#依赖包
* pyaudio
* wave
* Internet connection
#Todolist
* 多线程,网络模型如下:有一个栈专门用于接受音频,有很多个子线程从栈中抢取音频指令,对于阻塞的指令可能需要特殊处理,例如播放音乐
* 搜索指令集需要分类，例如人物，音乐，学习，编程手册等等
* 语音识别本地化，Julius speech recogition是一个开源的项目
* 利用树莓派嵌入式的优势，然后开发控制tv，空调等指令
#参考文档如下
* [Linux音频编程指南](http://www.ibm.com/developerworks/cn/linux/l-audio/index.html)
* [python pyaudio doc](http://people.csail.mit.edu/hubert/pyaudio/#docs)
