from time import sleep, perf_counter
from threading import Thread

from Car import Car
from Gps import Gps
from Imu import Imu

from flask import Flask, render_template, jsonify

app = Flask(__name__)

Car = Car(17,27)
Gps = Gps()
Imu = Imu()

roll = 0
pitch = 0
yaw = 0

def callImu():
    global roll
    global pitch
    global yaw
    while True:
        orientation = Imu.getOrientation()
        roll = orientation[0]
        pitch = orientation[1]
        yaw = orientation[2]
        sleep(0.5)

imuThread = Thread(target=callImu)
imuThread.start()

"""
def task(id):
    print(f'Starting the task {id}...')
    sleep(1)
    print('done')
"""
@app.route("/", methods = ["POST","GET"])
def home():
    """
    if request.method == 'POST':
	return jsonify(
	    
	    
	)
    if request.method == 'GET':
    """
    return render_template("index.html")

@app.route("/getGpsPosition", methods = ["GET"])
def getGpsPosition():
    position = Gps.getPosition()
    return jsonify(
        latitude = position[0],
        longitude = position[1],
    )

@app.route("/getImuOrientation", methods = ["GET"])
def getImuOrientation():
    orientation = Imu.getOrientation()
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
    
