import os
import sys
import time
import smbus

from imusensor.MPU9250 import MPU9250
from imusensor.filters import madgwick

class Imu:
    def __init__(self):
        self.sensorfusion = madgwick.Madgwick(0.5)
        address = 0x68
        bus = smbus.SMBus(1)
        self.imu = MPU9250.MPU9250(bus, address)
        self.imu.begin()
        # self.imu.loadCalibDataFromFile("/home/dietpi/calib_real4.json")
    def getOrientation(self):
        currTime = time.time()
        self.imu.readSensor()
        for i in range(10):
            newTime = time.time()
            dt = newTime - currTime
            currTime = newTime
            self.sensorfusion.updateRollPitchYaw(self.imu.AccelVals[0], self.imu.AccelVals[1], self.imu.AccelVals[2], \
                                                 self.imu.GyroVals[0],self.imu.GyroVals[1], self.imu.GyroVals[2], \
                                                 self.imu.MagVals[0], self.imu.MagVals[1], self.imu.MagVals[2], \
                                                 dt)
        return self.sensorfusion.roll, self.sensorfusion.pitch, self.sensorfusion.yaw
