//This is some test code and is not used in the final project

/* See 
 * http://lancaster-university.github.io/microbit-docs/advanced/ 
 * for docs about using the micro:bit library
*/
#include "MicroBit.h"

//accelerometer stuff
//MicroBitI2C i2c = MicroBitI2C(I2C_SDA0, I2C_SCL0);
//MicroBitAccelerometer accelerometer = MicroBitAccelerometer(i2c);

//MicroBit uBit;
MicroBitMessageBus bus;
MicroBitButton buttonA(MICROBIT_PIN_BUTTON_A, MICROBIT_ID_BUTTON_A);
MicroBitButton buttonB(MICROBIT_PIN_BUTTON_B, MICROBIT_ID_BUTTON_B);
MicroBitDisplay display;

void onAPressed(MicroBitEvent e)
{
    display.print("S");    
}

void onBPressed(MicroBitEvent e)
{
    display.clear();
}

int main()
{
    //uBit.init();
    //Activate BLE
    //new MicroBitButtonService(*uBit.ble);
    
    scheduler_init(bus);

    bus.listen(MICROBIT_ID_BUTTON_A, MICROBIT_BUTTON_EVT_CLICK, onAPressed);
    bus.listen(MICROBIT_ID_BUTTON_B, MICROBIT_BUTTON_EVT_CLICK, onBPressed);

    while(1)
        fiber_sleep(1000);
}
