安装注意的地方
================
* 安装pyaduio,遇到以下错误
Searching for pyaudio
Reading http://pypi.python.org/simple/pyaudio/
Reading http://people.csail.mit.edu/hubert/pyaudio/
Best match: pyaudio 0.2.7
Downloading http://people.csail.mit.edu/hubert/pyaudio/packages/pyaudio-0.2.7.tar.gz
Processing pyaudio-0.2.7.tar.gz
Writing /var/folders/vg/98k5hfl52m16wm45ckdx1_5c0000gp/T/easy_install-s1wLkT/PyAudio-0.2.7/setup.cfg
Running PyAudio-0.2.7/setup.py -q bdist_egg --dist-dir /var/folders/vg/98k5hfl52m16wm45ckdx1_5c0000gp/T/easy_install-s1wLkT/PyAudio-0.2.7/egg-dist-tmp-pFDrFR
warning: no files found matching '*.c' under directory 'test'
clang: warning: argument unused during compilation: '-mno-fused-madd'
src/_portaudiomodule.c:29:10: fatal error: 'portaudio.h' file not found
#include "portaudio.h"
         ^
1 error generated.


请安装portaudio即可

* 安装PIL，遇到以下错误(on max os)
clang: warning: argument unused during compilation: '-mno-fused-madd'
_imagingft.c:73:10: fatal error: 'freetype/fterrors.h' file not found
#include <freetype/fterrors.h>
         ^
1 error generated.

解决方案:ln -s /usr/local/include/freetype2 /usr/local/include/freetype