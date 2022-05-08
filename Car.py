import pigpio
import time

class Car:
    def __init__(self, steeringPin, throttlePin):
        self.steeringPin = steeringPin
        self.throttlePin = throttlePin
        self.pi = pigpio.pi()             # exit script if no connection
        if not self.pi.connected:
            print("pigpio not initialized properly")
            exit()
        self.pi.set_mode(self.steeringPin, pigpio.ALT5) # steering
        self.pi.set_mode(self.throttlePin, pigpio.ALT5) # throttle
        
    def setSteering(self, pwm):
        self.pi.set_servo_pulsewidth(self.steeringPin, pwm)
        
    def setThrottle(self, pwm):
        self.pi.set_servo_pulsewidth(self.throttlePin, pwm)
        
    def reset(self):
        self.pi.set_servo_pulsewidth(self.steeringPin, 1500)
        self.pi.set_servo_pulsewidth(self.throttlePin, 1500)
        
    def runDuration(self, pwm, seconds):
        self.pi.set_servo_pulsewidth(self.steeringPin, pwm)
        self.isRunning
        time.sleep(seconds)
        self.pi.set_servo_pulsewidth(self.steeringPin, 1500)

        
