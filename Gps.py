import serial
import time
import string
import pynmea2

class Gps:
    def __init__(self):
        port="/dev/ttyS0"
        ser=serial.Serial(port, baudrate=9600, timeout=0.5)
        dataout = pynmea2.NMEAStreamReader()
    def getGpsData():
        while True:
            newdata=ser.readline()
            string = str(newdata, "UTF-8")
            if "$GPRMC" in string:
                newmsg = pynmea2.parse(string)
                return newmsg.latitude, newmsg.longitude
            
            
