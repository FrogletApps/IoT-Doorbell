######################################################
#                   Import Libraries                 #
######################################################

from bluezero import microbit
from datetime import datetime
from picamera import PiCamera
from sense_hat import SenseHat

import atexit
#import mysql.connector as mariadb
import os
import requests
import secret
import socket
import time

######################################################
#                   Define Variables                 #
######################################################

#Set a flag file so we can tell the script is still running
open("/tmp/doorbellRunning", "w")

sense = SenseHat()
sense.set_rotation(90) #Make the image the right way up for being mounted on a door

#Need to add this string before message text
mPart1 = 'https://api.telegram.org/bot' + secret.tgBotKey() + '/'
chatID = '?chat_id=' + secret.tgChatID()

ubit = microbit.Microbit(adapter_addr='B8:27:EB:0B:AA:BE',
                         device_addr='E6:51:A6:1A:37:5B',
                         accelerometer_service=False,
                         button_service=True,
                         led_service=True,
                         magnetometer_service=False,
                         pin_service=False,
                         temperature_service=False)

#Microbit display arrays
#Microbit Bluetooth connected icon
mbHappyFace = [
    0b00000,
    0b01010,
    0b00000,
    0b10001,
    0b01110
]

#Microbit Bluetooth disconnected icon
mbSadFace = [
    0b00000,
    0b01010,
    0b00000,
    0b01110,
    0b10001
]

#Microbit button pressed icon
mbTick = [
    0b00001,
    0b00010,
    0b10100,
    0b01000,
    0b00000
]

#Sense HAT/Pi display arrays
#255 is the max value but this is very bright!
R = [120,0,0]       #Red
G = [0,120,0]       #Green
B = [0,0,120]       #Blue - use this for Bluetooth related stuff
W = [120,120,120]   #White - use this for WiFi related stuff
N = [0,0,0]         #Off


#Pi happy icon (all connected)
piHappyFace = [
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,B,N,N,B,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,B,N,N,N,N,B,N,
N,N,B,B,B,B,N,N,
N,N,N,N,N,N,N,N
]

#Pi sad icon (disconnected - script terminated)
piSadFace = [
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,B,N,N,B,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,B,B,B,B,N,N,
N,B,N,N,N,N,B,N,
N,N,N,N,N,N,N,N
]

#Pi button on the microbit pressed icon
piTick = [
N,N,N,N,N,N,N,N,
N,N,N,N,N,N,N,N,
N,N,N,N,N,G,G,N,
N,N,N,N,G,G,N,N,
N,G,N,G,G,N,N,N,
N,G,G,G,N,N,N,N,
N,N,G,N,N,N,N,N,
N,N,N,N,N,N,N,N
]

#Pi no internet icon
piNoWifi = [
R,N,N,N,N,N,N,N,
N,R,W,W,W,W,N,N,
N,W,R,N,N,N,W,N,
N,N,N,W,W,N,N,N,
N,N,W,N,R,W,N,N,
N,N,N,N,N,R,N,N,
N,N,N,W,W,N,R,N,
N,N,N,N,N,N,N,R
]

#Pi no bluetooth icon
piNoBT = [
R,N,N,B,N,N,N,N,
N,R,N,B,B,N,N,N,
N,B,R,B,N,B,N,N,
N,N,B,B,B,N,N,N,
N,N,B,B,R,N,N,N,
N,B,N,B,N,B,N,N,
N,N,N,B,B,N,R,N,
N,N,N,B,N,N,N,R
]

######################################################
#                   Define Functions                 #
######################################################

#A function for sending notifications over Telegram
def sendNotification(message):
    try:
        #response = 
        requests.get(mPart1 + 'sendMessage' + chatID + '&parse_mode=Markdown&text=' + message)
        #print (response.json())
    except:
        print("No internet connection (message " + message + " failed)")
        print("Now retry until we get a connection...")
        testInternet(message, 0)
    print(message)


#A function for sending pictures over Telegram
def sendPicture(picturePath):
    url = mPart1 + "sendPhoto"
    files = {'photo': open(picturePath, 'rb')}
    data = {'chat_id' : secret.tgChatID()}
    try:
        #response = 
        requests.post(url, files=files, data=data)
        #print (response.json())
    except:
        print("No internet connection (picture failed)")
        print("Now retry until we get a connection...")
        testInternet(picturePath, 1)
    print("Picture sent")

#Get file path for pictures
def getPicturePath():
    time = datetime.now()
    return '/home/pi/Git/iot-doorbell-pi/webControl/DoorbellPics/'+ time.strftime("%Y-%m-%d %H-%M-%S") +'.jpg'

#Set Pi to show no WiFi, Microbit is sad
def noWiFiDisplay():
    sense.set_pixels(piNoWifi)
    ubit.pixels = mbSadFace

#Set Microbit and Pi to display happy faces
def happyDisplay():
    sense.set_pixels(piHappyFace)
    ubit.pixels = mbHappyFace

#Set both to display sad faces
def sadDisplay():
    sense.set_pixels(piSadFace)
    ubit.pixels = mbSadFace

#Set Microbit and Pi to display a tick (message sent)
def allTick():
    sense.set_pixels(piTick)
    ubit.pixels = mbTick

#Connect Bluetooth Low Energy
#notification false means no notification
def connectBLE(notification):
    sense.set_pixels(piNoBT)
    ubit.connect()
    if notification:
        sendNotification("I'm connected up and ready to go!")
    happyDisplay()

#Run button listening code
def doorbell():
    connectBLE(True)
    while True:
        try:
            buttonA = ubit.button_a
            buttonB = ubit.button_b
        except:
            #If there's some error setting values then attempt to reconnect
            print("Problem reading button, attempting to reconnect")
            connectBLE(False)
            print("I fixed it!")

        if buttonA > 0 or buttonB > 0:
            sendNotification("There's someone at the door!")
            allTick()
            
            picturePath = getPicturePath()
            camera = PiCamera()
            #camera.start_preview()
            #time.sleep(1)
            camera.capture(picturePath)
            #camera.stop_preview()
            #Close the camera
            camera.close()

            sendPicture(picturePath)

            #Wait for 2 seconds
            time.sleep(2)

            #Go back to waiting state
            happyDisplay()

#def disconnectBLE():
#    ubit.disconnect()
#    sense.clear()

#Test the internet connection
#Display error if no internet, wait, then repeat the test
#Once there is a connection then resend the 
#contentType 0 is message, 1 is picture
def testInternet(content, contentType):
    try:
        #Test to see if we can connect to the telegram API
        socket.create_connection(("api.telegram.org", 80))
        sense.clear()
        if contentType == 0:
            sendNotification(content)
        else:
            sendPicture(content)
        return True
    except OSError:
        pass
    noWiFiDisplay()
    time.sleep(5)
    testInternet(content, contentType)

    return False

def exit_handler():
    print('Quitting pi.py')
    sadDisplay()
    os.remove("/tmp/doorbellRunning") 

######################################################
#                    Call Functions                  #
######################################################

#Check for the script ending
atexit.register(exit_handler)

#Run the program
doorbell()