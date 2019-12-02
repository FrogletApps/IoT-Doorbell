from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

def get_sense_data():
    orientation = sense.get_orientation()
    print("Accelerometer")
    print(orientation["yaw"])
    print(orientation["pitch"])
    print(orientation["roll"])
    gyro = sense.get_gyroscope_raw()
    print("Gyro")
    print(gyro["x"])
    print(gyro["y"])
    print(gyro["z"])
    acc = sense.get_accelerometer_raw()
    print("Accel raw")
    print(acc["x"])
    print(acc["y"])
    print(acc["z"])
    print(datetime.now())

while True:
    get_sense_data()