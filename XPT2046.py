
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI



# Constants for interacting with display registers.
XPT2046_StartBit        = 0b10000000
XPT2046_X_POSITION      = 0b01010000
XPT2046_Y_POSITION      = 0b00010000
XPT2046_Z1_POSITION     = 0b00110000
XPT2046_Z2_POSITION     = 0b01000000
XPT2046_TEMPERATURE_0   = 0b00000000
XPT2046_TEMPERATURE_1   = 0b01110000
XPT2046_BATTERY_VOLTAGE = 0b00100000
XPT2046_AUXILIARY       = 0b01100000
XPT2046_8_BIT           = 0b00001100
XPT2046_12_BIT          = 0b00000100

    
                
class XPT2046(object):
    """Representation of an XPT2046 touch panel."""

    def __init__(self, spi, irq=None, gpio=None):
        """Create an instance of the touch panel using SPI communication.  Must
        provide the GPIO pin number for the SPI driver.  Can optionally provide
        the GPIO pin number for the interrupt pin as the irq parameter."""
        self._irq = irq
        self._spi = spi
        self._gpio = gpio
        if self._gpio is None:
            self._gpio = GPIO.get_platform_gpio()
        # Setup interrupt as input (if provided).
        if irq is not None:
            self._gpio.setup(irq, GPIO.IN)
        # Set SPI to mode 0, MSB first.
        spi.set_mode(0)
        spi.set_bit_order(SPI.MSBFIRST)
        spi.set_clock_hz(100000)
               
        self._ConversionSelect = XPT2046_8_BIT

    def setMode(self, conversionSelect):
        self._ConversionSelect = conversionSelect
    
    def makeControlByte(self, channelSelect):
        # @@TODO Other elements in control byte.
        return XPT2046_StartBit | channelSelect | self._ConversionSelect
    
    def readValue(self, channelSelect):
        controlByte = self.makeControlByte(channelSelect)
        #msg = bytearray(1)
        msg=[controlByte]
        msg.append(0)
        msg.append(0)
        #msg[0] = controlByte
        ans = bytearray()
        ans = self._spi.transfer(msg)
#        print(controlByte," ",ans[1]," ",ans[2])

#        ans = bytearray(3)
#        ans[0]=msg[0]
#        ans[1]=msg[1]
#        ans[2]=msg[2]
        
        
        responseValue = 0
        
        if self._ConversionSelect == XPT2046_12_BIT:
#            responseData = self._SPIManager.SPIReceive(12)
            responseValue = (ans[1] << 4) | (ans[2] >> 4) 
        else:
#            responseData = self._SPIManager.SPIReceive(8)
            responseValue = (ans[1] << 1) | (ans[2] >> 7)
                            
        return responseValue
        
        
    def readX(self):
        return self.readValue(XPT2046_X_POSITION)
        
    def readY(self):
        return self.readValue(XPT2046_Y_POSITION)
        
    def readZ1(self):
        return self.readValue(XPT2046_Z1_POSITION)
    
    def readZ2(self):
        return self.readValue(XPT2046_Z2_POSITION)

    def readBatteryVoltage(self):
        return self.readValue(XPT2046_BATTERY_VOLTAGE)

    def readTemperature0(self):
        return self.readValue(XPT2046_TEMPERATURE_0)

    def readTemperature1(self):
        return self.readValue(XPT2046_TEMPERATURE_1)

    def readAuxiliary(self):
        return self.readValue(XPT2046_AUXILIARY)

    def readTouchPressure(self):
        # Formula (option 1) according to the datasheet (12bit conversion)
        # RTouch = RX-Plate.(XPosition/4096).((Z1/Z2)-1)
        # Not sure of the correct value of RX-Plate.
        # Assuming the ratio is sufficient.
        # Empirically this function seems to yield a values in the range of 0.4
        # for a firm touch, and 1.75 for a light touch.

        x = self.readX();
        z1 = self.readZ1();
        z2 = self.readZ2();
        
        # Avoid division by zero exception
        if (z1 == 0) :
            z1 = 1
        
        xDivisor = 4096;
        if (self._ConversionSelect == XPT2046_8_BIT) :
            xDivisor = 256;

        result = ( x / xDivisor) * (( z2 / z1) - 1);
        return result;

    def getIRQ(self):
        irq = 0
        if (self._gpio.is_low(self._irq)):
            irq = 1
        return irq

    def setMode8bit(self):
        self.setMode(XPT2046_8_BIT)
        
    def setMode12bit(self):
        self.setMode(XPT2046_12_BIT)
        
