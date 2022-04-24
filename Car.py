import pigpio
import time

class Car:
    def __init__(self, steeringPin, throttlePin)
        self.steeringPin = steeringPin
        self.throttlePin = throttlePin
        pi = pigpio.pi()             # exit script if no connection
        if not pi.connected:
            print("pigpio not initialized properly")
            exit()
        pi.set_mode(steeringPin, pigpio.ALT5) # steering
        pi.set_mode(throttlePin, pigpio.ALT5) # throttle
    def setSteering(pwm):
        pi.set_servo_pulsewidth(steeringPin, pwm)
    def setThrottle(pwm):
        pi.set_servo_pulsewidth(throttlePin, pwm)
    def reset():
        pi.set_servo_pulsewidth(steeringPin, 1500)
        pi.set_servo_pulsewidth(throttlePin, 1500)
    def runDuration(pwm, time):
        pi.set_servo_pulsewidth(steeringPin, pwm)
        time.sleep(time)
        pi.set_servo_pulsewidth(steeringPin, 1500)
