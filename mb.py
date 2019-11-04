#From ukbaz.github.io/howto/ubit_workshop.html

import time
from bluezero import microbit

ubit = microbit.Microbit(adapter_addr='B8:27:EB:0B:AA:BE',
                         device_addr='E6:51:A6:1A:37:5B',
                         accelerometer_service=True,
                         button_service=True,
                         led_service=True,
                         magnetometer_service=False,
                         pin_service=False,
                         temperature_service=True)

looping = True

ledX = [
    0b10001,
    0b01010,
    0b00100,
    0b01010,
    0b10001]

#Currently used as Bluetooth connected icon
ledHappyFace = [
    0b00000,
    0b01010,
    0b00000,
    0b10001,
    0b01110]

#Currently used as Bluetooth disconnected icon
ledSadFace = [
    0b00000,
    0b01010,
    0b00000,
    0b01110,
    0b10001]

ledBellLeft = [
    0b00100,
    0b01100,
    0b11100,
    0b01100,
    0b10100]

ledBellCentre = [
    0b00100,
    0b01110,
    0b01110,
    0b11111,
    0b00100]

ledBellRight = [
    0b00100,
    0b01110,
    0b00111,
    0b00110,
    0b00101]



ubit.connect()
print('Connected... Press a button to select mode')
mode = 0
while looping:
    if ubit.button_a > 0 and ubit.button_b > 0:
        mode = 3
        ubit.pixels = ledX
        time.sleep(1)
    elif ubit.button_b > 0:
        mode = 2
        ubit.pixels = ledSadFace
        time.sleep(1)
    elif ubit.button_a > 0:
        mode = 1
        ubit.pixels = ledHappyFace
        time.sleep(1)

    if mode == 1:
        x, y, z = ubit.accelerometer
        if z < 0:
            print('Face up')
        else:
            print('Face down')
        time.sleep(0.5)
    elif mode == 2:
        print('Temperature:', ubit.temperature)
        time.sleep(0.5)
    elif mode == 3:
        looping = False
        print('Exiting')

ubit.disconnect()