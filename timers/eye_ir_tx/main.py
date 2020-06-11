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

Ports:
A1      IR_LED - Red Battery Level Indicator LED (BAT_LED)
A2      IR_SIG - IR signal receiver 
A3      BAT_LED - IR transmission LED (ir_tx) or Green signal indicator LED (ir_rx)
D5      SD_CS - SD card chip select
D6      RAD_IRQ - radio interrupt request TODO Move this
D6      TS_CS - touchscreen chip select
D9      TFT_CS - TFT display chip select
D10     TFT_DC - TFT display data/command
D11     RAD_CS - radio chip select
D12     RAD_RST - radio reset
'''
DEBUG = True
import time

if DEBUG: print('main started')

from c4h_timers import Eye_IR_TX

eye = Eye_IR_TX(debug=DEBUG)

if DEBUG:
    print(eye.get_pins())
    print(eye.get_volts())

while True:
    if DEBUG:
        eye.update_bat_status()
        print(eye._IR_LED.duty_cycle, eye._IR_LED.frequency)
        time.sleep(1)

