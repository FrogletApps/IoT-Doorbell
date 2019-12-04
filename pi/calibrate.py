from sense_hat import SenseHat

import argparse
import csv
import time

sense = SenseHat()

#Parse command line arguments
#doorPos=True is open, doorPos=False is closed
parser = argparse.ArgumentParser()
parser.add_argument("doorPos")
args = parser.parse_args()

#Set argument to variable
doorPosition = bool(args.doorPos)

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

    #Recalculate arrays (adjusting for overflow/underflow, and assuming no massive fluctuations)
    yawArray = fixData(yawArray)
    pitchRange = fixData(pitchArray)
    rollRange = fixData(rollArray)

    #Calculate range
    yawRange = max(yawArray) - min(yawArray)
    pitchRange = max(pitchArray) - min(pitchArray)
    rollRange = max(rollArray) - min(rollArray)

    #Calculate average
    arrayLength = len(allData)
    yawAvg = sum(yawArray)/arrayLength
    pitchAvg = sum(pitchArray)/arrayLength
    rollAvg = sum(rollArray)/arrayLength

    return [[yawAvg, yawRange], [pitchAvg, pitchRange], [rollAvg, rollRange]]

#Fix data when data has gone up from 360 to 0 or gone down from 0 to 360
def fixData(dataArray):
    if (min(dataArray) < 90 and max(dataArray) > 270):
        #Fix it by adding 360 to the small values so all values are in the same range
        for i in range(len(dataArray)):
            if dataArray[i] < 90:
                dataArray[i] += 360
    return dataArray
        

def writeData(data):
    with open ('calibate.csv', mode='r') as file:
        readFile = csv.DictReader(file)
        for row in readFile:
            
#Collect x data samples of door position/orientation
def calibrate(x):
    allData = []
    for x in range(0, x):
        print(x)
        allData.append(collectData())
        time.sleep(1)

    print(averageData(allData))

calibrate(10)


