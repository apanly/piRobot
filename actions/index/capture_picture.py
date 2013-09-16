#!/usr/bin/python
#
# python-v4l2capture
#
# This file is an example on how to capture a picture with
# python-v4l2capture.
#
# 2009, 2010 Fredrik Portstrom
#
# I, the copyright holder of this file, hereby release it into the
# public domain. This applies worldwide. In case this is not legally
# possible: I grant anyone the right to use this work for any
# purpose, without any conditions, unless such conditions are
# required by law.

import Image
import select
import v4l2capture
import time
import traceback
import os
import sys
# Open the video device.
video = v4l2capture.Video_device("/dev/video1")

# Suggest an image size to the device. The device may choose and
# return another size if it doesn't support the suggested one.
size_x, size_y = video.set_format(1280, 1024)

# Create a buffer to store image data in. This must be done before
# calling 'start' if v4l2capture is compiled with libv4l2. Otherwise
# raises IOError.
video.create_buffers(1)

# Send the buffer to the device. Some devices require this to be done
# before calling 'start'.
video.queue_all_buffers()

# Start the device. This lights the LED if it's a camera that has one.
video.start()
# Wait for the device to fill the buffer.
while 1:
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
                    image.save("/home/vincent/opensource/record/image.jpg")
                    print "Saved image.jpg (Size: " + str(size_x) + " x " + str(size_y) + ")"
                except IOError as e:
                    if e.errno == 11:
                        print "error"
                time.sleep(0.03)
        for s in writable:
            pass
        for s in exceptional:
            print " exception condition on ", s.getpeername()
    except:
        traceback.print_exc()
        video.close()
        sys.exit(1)
