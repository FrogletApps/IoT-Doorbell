import time
from bluezero import microbit
from sense_hat import SenseHat
from picamera import PiCamera

import secret
import os
import requests

sense = SenseHat()

#Need to add this string before message text
preMessage = 'https://api.telegram.org/bot' + secret.tgBotKey() + '/sendMessage?chat_id=' + secret.tgChatID() + '&parse_mode=Markdown&text='

#A function for sending notifications
def sendNotification(message):
    requests.get(preMessage + message)

ubit = microbit.Microbit(adapter_addr='B8:27:EB:0B:AA:BE',
                         device_addr='E6:51:A6:1A:37:5B',
                         accelerometer_service=False,
                         button_service=True,
                         led_service=True,
                         magnetometer_service=False,
                         pin_service=False,
                         temperature_service=False)

looping = True

#Microbit display arrays
mbX = [
    0b10001,
    0b01010,
    0b00100,
    0b01010,
    0b10001]

#Currently used as Bluetooth connected icon
mbHappyFace = [
    0b00000,
    0b01010,
    0b00000,
    0b10001,
    0b01110]

#Currently used as Bluetooth disconnected icon
mbSadFace = [
    0b00000,
    0b01010,
    0b00000,
    0b01110,
    0b10001]

mbTick = [
    0b00001,
    0b01010,
    0b10100,
    0b01000,
    0b00001]

mbBellLeft = [
    0b00100,
    0b01100,
    0b11100,
    0b01100,
    0b10100]

mbBellCentre = [
    0b00100,
    0b01110,
    0b01110,
    0b11111,
    0b00100]

mbBellRight = [
    0b00100,
    0b01110,
    0b00111,
    0b00110,
    0b00101]

#Sense HAT display arrays
#255 is the max value but this is very bright!
R = [120,0,0]  #Red
G = [0,120,0]  #Green
B = [0,0,120]  #Blue - use this for Bluetooth related stuff
N = [0,0,0]    #Off


#Currently used as Bluetooth connected icon
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

#Currently used as Bluetooth disconnected icon
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

sense.set_pixels(piSadFace)
ubit.connect()
sense.set_pixels(piHappyFace)
sendNotification("I'm connected up and ready to go!")
print('Connected... Press a button to select mode')

while looping:
    if ubit.button_a > 0 and ubit.button_b > 0:
        looping = False
    elif ubit.button_a > 0 or ubit.button_b > 0:
        mode = 1
        ubit.pixels = mbTick
        sense.set_pixels(piTick)
        print('A button was pressed')
        time.sleep(2)

    ubit.pixels = mbHappyFace
    sense.set_pixels(piHappyFace)

ubit.disconnect()
sense.clear()