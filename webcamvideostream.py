import cv2
from threading import Thread
import time
import numpy as np

class WebcamVideoStream:
    def __init__(self, src = 0):
        print("init camera")
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        time.sleep(2.0)
        self.t = None
        print("init finished")
        
    def start(self):
        self.stopped = False
        if self.t is None:
            print("start thread")
            self.t = Thread(target=self.update, args=())
            self.t.daemon = True
            self.t.start()
        return self
            
    def update(self):
        print("read")
        while True:
            if self.stopped:
                return # returns nothing to terminate loop
            (self.grabbed, self.frame) = self.stream.read()
    
    def read(self):
        return self.frame
    
    def stop(self):
        self.stopped = True

