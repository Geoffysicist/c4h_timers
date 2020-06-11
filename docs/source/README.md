# Courses4Horses Timers

Affordable, open-source timers for equestrian events

## Motivation
Timing equipment for equestrian events is often expensive and beyond the financial resources of small clubs. This project aims to provide code and hardware assemblage instructions so clubs can make their own timing gear using off-the-shelf components and some 3D printing.

## software
This project is build using the [CircuitPython libraries](https://circuitpython.org/)

## hardware
There are 4 hardware components to this project:
* the main console (console_lora_rx) - this is the brains which receives and processes the signals from the eye_ir_rx_lora_tx units and can also interface with a computer 
* the transmitter eyes (eye_ir_tx) - these units send an ir signal to the eye_ir_rx_lora_tx units. Breaking this transmission beam is used to time each round.
* the receiver eyes (eye_ir_rx_lora_tx) - these units recieve the ir transmission from the eye_ir_tx units and send data to the console_lora_rx

### console_lora_rx
[Feather cases](https://learn.adafruit.com/3d-printed-case-for-adafruit-feather/overview)

[Adafruit Feather nRF52840 Express](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather?view=all)
[Adafruit RFM9x LoRa](https://learn.adafruit.com/radio-featherwing/circuitpython-for-rfm9x-lora)
SMA Edge-Mount connector with 1.6mm spacing - maybe go for flexible mount
[DS3231 Precision RTC FeatherWing](https://www.adafruit.com/product/3028)

### eye_ir_tx
[Adafruit Feather M4 Express](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51)
SFH 4544 Osram Opto 950Nm IR LED, 5mm (T-1 3/4)
SMA Edge-Mount connector with 1.6mm spacing

### eye_ir_rx_lora_tx
[Adafruit Feather M4 Express](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51)
[Adafruit RFM9x LoRa](https://learn.adafruit.com/radio-featherwing/circuitpython-for-rfm9x-lora)
Vishay TSOP4838, 38kHz IR Receiver, 950Nm, 45m Range, 2.5V - 5V
or
Vishay TSOP38238, 38kHz IR Receiver, 950Nm, 45m Range, 2.5V - 5V

### TODO
