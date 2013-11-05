import cv2.cv as cv
import time

__all__ = ["take_picture",]
FLAG = False

def on_mouse(event, x, y, flag, param):
    global FLAG
    if event == cv.CV_EVENT_LBUTTONDOWN:
        FLAG = True

def take_picture():
    cv.NamedWindow("camera", 1)
    capture = cv.CaptureFromCAM(0)

    while True:
        img = cv.QueryFrame(capture)
        cv.ShowImage("camera", img)
        cv.SetMouseCallback("camera", on_mouse)
        if cv.WaitKey(10) in [10, 27, 32] or FLAG:
            cv.SaveImage("/tmp/webcam.png", img)
            break
    cv.DestroyAllWindows()
    return open("/tmp/webcam.png", "r").read()
