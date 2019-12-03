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
    return data
    
def averageData(allData):
    yawTotal = 0
    pitchTotal = 0
    rollTotal = 0
    for group in allData:
        print(group)
        yawTotal += group[0]
        pitchTotal += group[1]
        rollTotal += group[2]

    arrayLength = len(allData)
    yawAvg = round(yawTotal/arrayLength, 0)
    pitchAvg = round(pitchTotal/arrayLength, 0)
    rollAvg = round(rollTotal/arrayLength, 0)

    return [yawAvg, pitchAvg, rollAvg]



def writeData():
    with open ('calibate.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

#Collect 10 data samples of door position/orientation
allData = []
for x in range(0, 10):
    print(x)
    allData.append(calibrate())
    time.sleep(1)

print(averageData(allData))



