# CircuitPython Timing Gates

## requirements

### libraries

[Adafruit_CircuitPython_IRRemote](https://github.com/adafruit/Adafruit_CircuitPython_IRRemote)

### hardware

[Feather cases](https://learn.adafruit.com/3d-printed-case-for-adafruit-feather/overview)

console_lora_rx:
[Adafruit Feather nRF52840 Express](https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather?view=all)
[Adafruit RFM9x LoRa](https://learn.adafruit.com/radio-featherwing/circuitpython-for-rfm9x-lora)
SMA Edge-Mount connector with 1.6mm spacing - maybe go for flexible mount
[DS3231 Precision RTC FeatherWing](https://www.adafruit.com/product/3028)

eye_ir_tx
[Adafruit Feather M4 Express](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51)
SFH 4544 Osram Opto 950Nm IR LED, 5mm (T-1 3/4)
SMA Edge-Mount connector with 1.6mm spacing

eye_ir_rx_lora_tx
[Adafruit Feather M4 Express](https://learn.adafruit.com/adafruit-feather-m4-express-atsamd51)
[Adafruit RFM9x LoRa](https://learn.adafruit.com/radio-featherwing/circuitpython-for-rfm9x-lora)
Vishay TSOP4838, 38kHz IR Receiver, 950Nm, 45m Range, 2.5V - 5V
or
Vishay TSOP38238, 38kHz IR Receiver, 950Nm, 45m Range, 2.5V - 5V

### Farmtek output

normal
  21.11 (M)

ASCII float
  14.68
  6.971

ASCII fixed
  8.387

### circuitpython IR Tx and Rx

Note that for receiver minimum burst length is 10 cycles with a minimum break of 10 cycles.
@ 38kHz each cycle is 0.027 ms so minimum burst is 0.27 ms

https://learn.adafruit.com/infrared-ir-receive-transmit-circuit-playground-express-circuit-python/ir-from-cpx-to-cpx

but should be able to implement it simply using:

* [pulseio.PulseOut](https://circuitpython.readthedocs.io/en/5.0.x/shared-bindings/pulseio/PulseOut.html)
* [pulseio.PulseIn](https://circuitpython.readthedocs.io/en/5.0.x/shared-bindings/pulseio/PulseIn.html)

## Displays

8 [CircuitPython Display Support Using displayio](https://learn.adafruit.com/circuitpython-display-support-using-displayio/introduction)


## Basic Plan

Four types of components:

* eye_ir_tx: IR transmitter eye - in arena. Use IR led to transmit 38kHz signal indicating battery status to eye_ir_rx_lora_tx once every 5 millisecs.

* eye_ir_rx_lora_tx: 38kHz IR receiver and 900 MHz LoRa transmitter - in arena. Receives the battery status from the eye_ir_tx. Use a flag (999?) to indicate no signal received from eye_ir_tx. Send status packet to console_lora_rx_ble_tx indicating [eye_ID, eye_ir_tx battery status, eye_ir_rx_lora_tx].

* console_lora_rx_ble_tx: 900 MHz LoRa and BLE transmitter - in judges box. Receives status packets from all eye_ir_rx_lora_tx an transmits to app_ble_rx on computer and/or phone. Could also interface with computer via serial cable.

* app_ble_rx: Computer and/or smart phone BLE receiver and user interface app. Receives status packets for all eye pairs. If status of any of pair has a 'no signal' flag then identifies a possible beam break and records time. No signal flag must be persistent for a certain period of time (500 ms?) before beam break is confirmed. Once beam break is confirmed log the time of the break and the eye.Confirmed beam break is used to identify start or finish of round if 'eyes on'. Keep a log of previous n confirmed beam breaks in case judge forgets to turn eyes on, can scroll through log.

## Construction notes
Per ISO 1222:2010,[1] the current tripod screw thread standard for attaching the camera calls for a 1/4-20 UNC[2] or 3/8-16 UNC thread.[3] Most consumer cameras are fitted with 1/4-20 UNC threads.

Documentation:
to make docs
C:\Users\ggoldrick\Projects\cp_timing_gates\c4h_timers\docs>sphinx-apidoc -f -o . ../c4h_timers
C:\Users\ggoldrick\Projects\cp_timing_gates\c4h_timers\docs>make html