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
    yawArray = []
    pitchArray = []
    rollArray = []
    #Iterate through the data and sort it into different arrays (also round to nearest number)
    for group in allData:
        print(group)
        yawArray.append(round(group[0], 0))
        pitchArray.append(round(group[1], 0))
        rollArray.append(round(group[2], 0))

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



