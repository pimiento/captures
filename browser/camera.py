# -*- coding: utf-8 -*-
import os
import time
import tempfile
import cv2.cv as cv

__all__ = ["take_picture",]
FLAG = False

def take_picture():
    cv.NamedWindow("camera", 1)
    capture = cv.CaptureFromCAM(0)
    tempdir = tempfile.gettempdir()
    filename = os.path.join(tempdir, "webcam.png")

    while True:
        img = cv.QueryFrame(capture)
        cv.ShowImage("camera", img)
        if cv.WaitKey(10) in [10, 27, 32] or FLAG:
            cv.SaveImage(filename, img)
            break
    time.sleep(5)
    cv.DestroyAllWindows()
    return open(filename, "r").read()
