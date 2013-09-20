#!/usr/bin/python
# -*- coding: utf-8 -*-
import Image
import select
import v4l2capture
import time
import traceback
import sys,pygame
from gl import PICPATH

class camera:
    def __init__(self):
        self.flag=True
    def do(self):
        size = width, height = 1280,1024
        speed = [2, 2]
        # Open the video device.
        video = v4l2capture.Video_device("/dev/video1")
        size_x, size_y = video.set_format(1280,1024)
        video.create_buffers(1)
        video.queue_all_buffers()
        video.start()
        pygame.init()
        pygame.display.set_caption('视频拍照')
        screen = pygame.display.set_mode(size)
        while self.flag:
            try:
                readable , writable , exceptional =select.select([video,], [], [])
                if not (readable or writable or exceptional) :
                    print "Time out ! "
                    break;
                for s in readable :
                    if s is video:
                        try:
                            image_data = video.read_and_queue()
                            image = Image.fromstring("RGB", (size_x, size_y), image_data)
                            image.save(PICPATH+"image.bmp")
                            print "Saved image.jpg (Size: " + str(size_x) + " x " + str(size_y) + ")"
                            #加载图像
                            pyimage = pygame.image.load(PICPATH+"image.bmp")
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    break
                            #传送画面
                            screen.blit(pyimage, speed)
                            #显示图像
                            pygame.display.flip()
                        except IOError as e:
                            if e.errno == 11:
                                print "error"
                        time.sleep(0.01)
                for s in writable:
                    pass
                for s in exceptional:
                    print " exception condition on ", s.getpeername()
            except:
                traceback.print_exc()
                video.close()
                sys.exit(1)
    def stop(self):
        self.flag=False