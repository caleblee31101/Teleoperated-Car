import serial
import time
import string
import pynmea2

class Gps:
    def __init__(self):
        port = "/dev/ttyS0"
        self.ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        #dataout = pynmea2.NMEAStreamReader()
    def getPosition(self):
        loops = 0
        while True:
            loops = loops + 1
            newdata = self.ser.readline()
            string = str(newdata, "UTF-8")
            if "$GPRMC" in string:
                newmsg = pynmea2.parse(string)
                return newmsg.latitude, newmsg.longitude
            if loops > 100:
                return 0, 0
