'''eye_ir_tx C4H IR transmitter eye.

Transmitter eye sends a constant IR signal @ 38kHz
Uses LED to indicate battery status

Hardware:
* [Adafruit Feather M4 express](https://www.adafruit.com/product/3857)
* [SFH 4544 Osram Opto 950Nm IR LED](https://au.rs-online.com/web/p/ir-leds/8108247)
* [Green LED 5mm](https://core-electronics.com.au/led-green-with-resistor-5mm-25-pack.html)
* [Red LED 5mm](https://core-electronics.com.au/led-red-with-resistor-5mm-25-pack.html)
* [SPDT Mini Power Switch](https://core-electronics.com.au/spdt-mini-power-switch.html)
* [Polymer Lithium Ion Battery (LiPo) 3.7V 1100mAh](https://core-electronics.com.au/polymer-lithium-ion-battery-1000mah-38458.html)

'''
DEBUG = False
import time

if DEBUG: print('main started')

from c4h_timers import Eye_IR_RX

eye = Eye_IR_RX(debug=DEBUG)

if DEBUG:
    print(eye.get_pins())
    print(eye.get_volts())

while True:
    eye.update()
    if DEBUG:
        print(eye.get_volts())
        time.sleep(1)