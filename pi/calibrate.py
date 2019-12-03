from csv import writer
from sense_hat import SenseHat

import csv
import time

sense = SenseHat()

def collectData():
    data = []
    orientation = sense.get_orientation()
    data.append(orientation["yaw"])
    data.append(orientation["pitch"])
    data.append(orientation["roll"])
    print(data)
    return data
    
def averageData(allData):
    yawArray = []
    pitchArray = []
    rollArray = []
    #Iterate through the data and sort it into different arrays (also round to nearest number)
    for group in allData:
        print(group)
        yawArray.append(round(group[0], 0))
        pitchArray.append(round(group[1], 0))
        rollArray.append(round(group[2], 0))

    #Calculate range (adjusting for overflow/underflow)
    yawRange = fixRangeWrap(yawArray)
    if (yawRange == False):
        yawRange = max(yawArray) - min(yawArray)

    pitchRange = fixRangeWrap(pitchArray)
    if (pitchRange == False):
        pitchRange = max(pitchArray) - min(pitchArray)

    rollRange = fixRangeWrap(rollArray)
    if (rollRange == False):
        rollRange = max(rollArray) - min(rollArray)

    #Calculate range
    #yawRange = max(yawArray) - min(yawArray)
    #pitchRange = max(pitchArray) - min(pitchArray)
    #rollRange = max(rollArray) - min(rollArray)

    #Calculate average
    arrayLength = len(allData)
    yawAvg = sum(yawArray)/arrayLength
    pitchAvg = sum(pitchArray)/arrayLength
    rollAvg = sum(rollArray)/arrayLength

    return [[yawAvg, yawRange], [pitchAvg, pitchRange], [rollAvg, rollRange]]

#Fix data when data has gone up from 360 to 0 or gone down from 0 to 360
def fixRangeWrap(dataArray):
    if (min(dataArray) < 90 and max(dataArray) > 270):
        for data in dataArray:
            if data < 90:
                data += 360
    else:
        return False
        

def writeData(data):
    with open ('calibate.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

#Collect x data samples of door position/orientation
def calibrate(x):
    allData = []
    for x in range(0, x):
        print(x)
        allData.append(collectData)
        time.sleep(1)

    print(averageData(allData))

calibrate(10)


