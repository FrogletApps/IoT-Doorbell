from bluezero import microbit
ubit = microbit.Microbit(adapter_addr='B8:27:EB:0B:AA:BE',
                         device_addr='E6:51:A6:1A:37:5B',
                         accelerometer_service=True,
                         button_service=True,
                         led_service=True,
                         magnetometer_service=False,
                         pin_service=False,
                         temperature_service=True)
my_text = 'Hello, world'
ubit.connect()

while my_text is not '':
    ubit.text = my_text
    my_text = input('Enter message: ')

ubit.disconnect()

#From ukbaz.github.io/howto/ubit_workshop.html