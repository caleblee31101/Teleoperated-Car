from time import sleep, perf_counter
from threading import Thread

from Car import Car
from Gps import Gps
from Imu import Imu
from webcamvideostream import WebcamVideoStream
import cv2

from flask import Flask, render_template, jsonify, Response, request, redirect, url_for

app = Flask(__name__)

car = Car(17,27)
car.reset()
gps = Gps()
imu = Imu()
webcam = WebcamVideoStream()


#carThread = Thread(target=car.run)

roll = 0
pitch = 0
yaw = 0

def callImu():
    global roll
    global pitch
    global yaw
    while True:
        orientation = imu.getOrientation()
        roll = orientation[0]
        pitch = orientation[1]
        yaw = orientation[2]
        sleep(0.5)
        
imuThread = Thread(target=callImu)
imuThread.start()

@app.route("/")
def home():
    return render_template("index.html")

def gen(camera):
    while True:
        if camera.stopped:
            break
        frame = camera.read()
        ret, jpeg = cv2.imencode('.jpg',frame)
        if jpeg is not None:
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n\r\n')
        else:
            print("frame is none")
        sleep(0.1)

@app.route("/postCarMovement", methods = ["POST"])
def postCarMovement():

    movement = request.json
    steeringPwm = int(movement["steeringPwm"])
    throttlePwm = int(movement["throttlePwm"])
    seconds = int(movement["seconds"])
    
    car.run(steeringPwm, throttlePwm, seconds)
    return "", 201

@app.route("/getGpsPosition", methods = ["GET"])
def getGpsPosition():
    position = gps.getPosition()
    return jsonify(
        latitude = position[0],
        longitude = position[1],
    )

@app.route("/getImuOrientation", methods = ["GET"])
def getImuOrientation():
    orientation = imu.getOrientation()
    return jsonify(
        r = roll,
        p = pitch,
        y = yaw,
    )
    """
    return jsonify(
        roll = orientation[0],
        pitch = orientation[1],
        yaw = orientation[2],
    )
    """

@app.route('/postStopCamera', methods = ["POST"])
def postStopCamera():
    global webcam
    webcam.stop()
    return "", 200

@app.route('/postStartCamera', methods = ["POST"])
def postStartCamera():
    global webcam
    webcam.start()
    return "", 200

@app.route('/video_feed')
def video_feed():
    global webcam
    return Response(gen(webcam.start()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True)
