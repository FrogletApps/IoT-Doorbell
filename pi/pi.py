######################################################
#                   Import Libraries                 #
######################################################

from bluezero import microbit
from picamera import PiCamera
from sense_hat import SenseHat

import os
import requests
import secret
import socket
import time

######################################################
#                   Define Variables                 #
######################################################

sense = SenseHat()
sense.set_rotation(90) #Make the image the right way up for being mounted on a door

picturePath = '/home/pi/image.jpg'

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
mbX = [
    0b10001,
    0b01010,
    0b00100,
    0b01010,
    0b10001]

#Microbit Bluetooth connected icon
mbHappyFace = [
    0b00000,
    0b01010,
    0b00000,
    0b10001,
    0b01110]

#Microbit Bluetooth disconnected icon
mbSadFace = [
    0b00000,
    0b01010,
    0b00000,
    0b01110,
    0b10001]

#Microbit button pressed icon
mbTick = [
    0b00001,
    0b00010,
    0b10100,
    0b01000,
    0b00000]

#Sense HAT display arrays
#255 is the max value but this is very bright!
R = [120,0,0]       #Red
G = [0,120,0]       #Green
B = [0,0,120]       #Blue - use this for Bluetooth related stuff
W = [120,120,120]   #White - use this for WiFi related stuff
N = [0,0,0]         #Off


#Pi Bluetooth connected icon
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

#Pi Bluetooth disconnected icon
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

######################################################
#                   Define Functions                 #
######################################################

#A function for sending notifications over Telegram
def sendNotification(message):
    print(message)
    #response = 
    requests.get(mPart1 + 'sendMessage' + chatID + '&parse_mode=Markdown&text=' + message)
    #print (response.json())

#A function for sending pictures over Telegram
def sendPicture(picture):
    url = mPart1 + "sendPhoto"
    files = {'photo': open(picturePath, 'rb')}
    data = {'chat_id' : secret.tgChatID()}
    #response = 
    requests.post(url, files=files, data=data)
    #print (response.json())

#Connect Bluetooth Low Energy
def connectBLE():
    sense.set_pixels(piSadFace)
    ubit.connect()
    sense.set_pixels(piHappyFace)
    sendNotification("I'm connected up and ready to go!")

#Run button listening code
def doorbell():
    connectBLE()
    testInternet()
    while True:
        if ubit.button_a > 0 or ubit.button_b > 0:
            try:
                sendNotification("There's someone at the door!")
                ubit.pixels = mbTick
                sense.set_pixels(piTick)
            except:
                print("No internet connection (message failed)")
            
            camera = PiCamera()
            #camera.start_preview()
            #time.sleep(1)
            camera.capture(picturePath)
            #camera.stop_preview()
            picture = open(picturePath, 'rb')
            #Close the camera
            camera.close()
            try:
                sendPicture(picture)
            except:
                print("No internet connection (picture failed)")

            #Wait for 2 seconds
            time.sleep(2)

            #Go back to waiting state
            ubit.pixels = mbHappyFace
            sense.set_pixels(piHappyFace)


#def disconnectBLE():
#    ubit.disconnect()
#    sense.clear()

#Test the internet connection 
def testInternet():
    try:
        #Test to see if we can connect to the telegram API
        socket.create_connection(("api.telegram.org", 80))
        return True
    except OSError:
        pass
    noInternet()
    return False

#Display error if no internet
def noInternet():
    sense.set_pixels(piNoWifi)

######################################################
#                    Call Functions                  #
######################################################

#Run the program
doorbell()