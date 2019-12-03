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
        pitchTotal += group[2]

    arrayLength = len(allData)
    yawAvg = yawTotal/arrayLength
    pitchAvg = pitchTotal/arrayLength
    rollAvg = rollTotal/arrayLength

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



