import os
import sys
import time
import smbus

from imusensor.MPU9250 import MPU9250
from imusensor.filters import madgwick

class Imu:
    def __init__(self)
        sensorfusion = madgwick.Madgwick(0.5)
        address = 0x68
        bus = smbus.SMBus(1)
        imu = MPU9250.MPU9250(bus, address)
        imu.begin()
        imu.loadCalibDataFromFile("/home/pi/calib_real4.json")
        def getOrientation():
            currTime = time.time()
            imu.readSensor()
            for i in range(10):
	        newTime = time.time()
	        dt = newTime - currTime
	        currTime = newTime
	        sensorfusion.updateRollPitchYaw(imu.AccelVals[0], imu.AccelVals[1], imu.AccelVals[2], \
                                                imu.GyroVals[0],imu.GyroVals[1], imu.GyroVals[2], \
                                                imu.MagVals[0], imu.MagVals[1], imu.MagVals[2], \
                                                dt)
	    return sensorfusion.roll, sensorfusion.pitch, sensorfusion.yaw
