"""Courses4Horses Showjumping Timing Gates.

Hardware:
    * `Adafruit Feather nRF52840 express <https://learn.adafruit.com/introducing-the-adafruit-nrf52840-feather>`_
    * `Adafruit 2.4" TFT FeatherWing <https://learn.adafruit.com/adafruit-2-4-tft-touch-screen-featherwing/overview>`_
    * `SPDT Mini Power Switch <https://core-electronics.com.au/spdt-mini-power-switch.html>`_
    * `Polymer Lithium Ion Battery (LiPo) 3.7V 1100mAh <https://core-electronics.com.au/polymer-lithium-ion-battery-1000mah-38458.html>`_

Ports:
    * A1: IR_LED - Red Battery Level Indicator LED (BAT_LED)
    * A2: IR_SIG - IR signal receiver 
    * A3: BAT_LED - IR transmission LED (ir_tx) or Green signal indicator LED (ir_rx)
    * D5: SD_CS - SD card chip select
    * D6: RAD_IRQ - radio interrupt request TODO Move this
    * D6: TS_CS - touchscreen chip select
    * D9: TFT_CS - TFT display chip select
    * D10: TFT_DC - TFT display data/command
    * D11: RAD_CS - radio chip select
    * D12: RAD_RST - radio reset

"""
import board
import neopixel


class Timer(object):
    """Timing gates base class.

    Attributes:
        _BAT: the battery voltage monitor pin
        _PIN_LIST: a list of named pins for the board
        debug: A boolean indicating whether debugging
    """
    def __init__(self, debug=False):
        """its the init :P."""
        from analogio import AnalogIn

        self._BAT = AnalogIn(board.VOLTAGE_MONITOR)
        self._PIN_LIST = dir(board)
        self.debug = debug
        # self.NeoPixPin = board.NEOPIXEL

        #turn off the neopixel
        # NeoPix = neopixel.NeoPixel(board.NEOPIXEL,1)
        # NeoPix.brightness = 0
        neopixel.NeoPixel(board.NEOPIXEL,1).brightness = 0


        if self.debug:
            print('C4H base class initialised')

    def get_pins(self):
        """Returns a list of the board's defined io pins."""
        return self._PIN_LIST

    def get_volts(self, precision = 1):
        """Battery voltage.

        Keyword Arguments:
            precision {int} -- number of decimal places (default: {1})

        Returns:
            float -- voltage to 'precision' decimal places
        """

        volts = self._BAT.value * 3.3 * 2 / 65536
        volts = round(volts, precision)
        if self.debug: print('bat volts: {}'.format(volts))
        return volts

class Console(Timer):
    """Judge/Timer's  console.
    
    Touch screen
    900 MHz Radio transceiver
    SD Card

    Attributes:
    """

    def __init__(self, **kwargs):
        """ initialise the console."""
        super().__init__(**kwargs)
        
        if self.debug: print('Console initialised')

class Eye(Timer):
    """Eye base class.

    Attributes:
        _IR_LED: the IR transmission LED for eye_ir_tx or signal led for ir_rx
        _BAT_LED: battery status LED. Blinks faster as bat level drops
        _bat_status: integer indicating battery status. 0 in fully charged, 1 if ok, 2 if needs recharging

    """
    def __init__(self, **kwargs):
        """initialise the eye super class."""
        super().__init__(**kwargs)
        import pulseio

        # DUTY_FULL = 2**16 - 1 # 100% duty cycle
        # DUTY_HALF = 2**15 - 1 # 50% duty cycle

        # self._BAT_LED = pulseio.PWMOut(board.A3, frequency=1, duty_cycle=2**15 - 1, variable_frequency=True)
        # self._IR_LED = pulseio.PWMOut(board.A1, frequency=38000, duty_cycle=0)
        self._BAT_LED = pulseio.PWMOut(board.A1, frequency=1, duty_cycle=2**15 - 1, variable_frequency=True)
        self._IR_LED = pulseio.PWMOut(board.A3, frequency=38000, duty_cycle=0)
        self._bat_status = 3
        self.update_bat_status()
        
        if self.debug: print('Eye initialised')


    def update_bat_status(self):
        """updates the battery status depending on voltage."""
        volts = self.get_volts()
        if volts > 3.7:
            self._bat_status = 0

        elif volts > 3.5:
            self._bat_status = 1
        else:
            self._bat_status = 2

        self._update_BAT_LED()

    
    def _update_BAT_LED(self):
        """changes the BAT_LED so flashes faster as v decreases."""
        self._BAT_LED.frequency =  1 << self._bat_status
        if self.debug: print('BAT LED freq: {}'.format(1 << self._bat_status))
        
 
class Eye_IR_TX(Eye):
    """IR transmitter eye.

    Attributes:
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs) #freq for IR transmission

        # continuous transmission TODO send bat status instead
        self.send_pulses(off=0)
        
        if self.debug:
            print('IR_TX initialised')
            print('IR LED duty cycle {}'.format(self._IR_LED.duty_cycle))

    def send_pulses(self, on=1000, off=1000, num=1):
        """sends a series of identical IR pulses.

        Keyword Arguments:
            on {int} -- length of the on signal in micros (default: {1000})
            off {int} -- length of the off signal in micros. 0 = continuous (default: {1000})
            num {int} -- number of pulses to send (default: {1})
        """
        if not off: # continuous
            self._IR_LED.duty_cycle = 2**15 # 50% duty cycle
        else:
            pass # TODO implement pulses





class Eye_IR_RX(Eye):
    """IR receiver eye.

    Attributes:
        _IR_SIG: IR signal receiver
        _ir_sig_status: Boolean to indicate whether signal is being received.
            note pin is pulled up so status is True when pin value if False.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        import digitalio
        self._IR_SIG = digitalio.DigitalInOut(board.A2)
        self._IR_SIG.direction = digitalio.Direction.INPUT
        self._ir_sig_status = not self._IR_SIG.value # see note in docstring
        self.update()
        if self.debug: print('IR_RX initialised')

    def update(self):
        """Update the IR receiver signal status."""
        self._ir_sig_status = not self._IR_SIG.value #pulled up so False when signal received
        self._IR_LED.duty_cycle = ((2**16)-1)*self._ir_sig_status

