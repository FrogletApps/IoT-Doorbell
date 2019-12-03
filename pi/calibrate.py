from csv import writer
from sense_hat import SenseHat
import time

sense = SenseHat()

def calibrate():
    data = []
    orientation = sense.get_orientation()
    data.append(orientation["yaw"])
    data.append(orientation["pitch"])
    data.append(orientation["roll"])
    
def averageData(allData):
    print(allData)

def writeData():
    with open ('calibate.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

#Collect 10 data samples of door position/orientation
allData = []
for x in range(0, 10):
    allData.append(calibrate())
    time.sleep(1)

averageData(allData)



