from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from XPT2046 import XPT2046 as XPT
import Adafruit_ILI9341 as ILI
import Adafruit_GPIO.SPI as SPI


TJCTM24024SPI_ORIENTATION_0     = 0
TJCTM24024SPI_ORIENTATION_90    = 1
TJCTM24024SPI_ORIENTATION_180   = 2
TJCTM24024SPI_ORIENTATION_270   = 3


""" 8 bit resolution touch """
TJCTM24024SPI_TOUCH_MIN_X      = 20
TJCTM24024SPI_TOUCH_MAX_X      = 240
TJCTM24024SPI_TOUCH_MIN_Y      = 15
TJCTM24024SPI_TOUCH_MAX_Y      = 230



class TJCTM24024SPI(object):

    def __init__(self, dc, port=0, rst=None, irq=None):
        self._disp = ILI.ILI9341(dc, rst=rst, spi=SPI.SpiDev(port, 0, max_speed_hz=1000000)) 
        self._touch = XPT(irq=irq, spi=SPI.SpiDev(port, 1, max_speed_hz=100000))

        self.orient = TJCTM24024SPI_ORIENTATION_0

        self._disp.begin()
        self._disp.clear((0,0,0))
        self.buffer = Image.new('RGB', (320, 320))
        
        self._touch.setMode8bit
        self._touchX = 0
        self._touchY = 0


    def setOrientation(self, deg=TJCTM24024SPI_ORIENTATION_0):
        self._orientation = deg


    def isTouch(self):
       return self._touch.getIRQ()


    def readTouch(self):
        x = self._touch.readX()
        y = self._touch.readY()
#        print ("  x: %s " % x + "  y %s" % y)
        
        if ((x<TJCTM24024SPI_TOUCH_MIN_X) or (x>TJCTM24024SPI_TOUCH_MAX_X) or (y<TJCTM24024SPI_TOUCH_MIN_Y) or (y>TJCTM24024SPI_TOUCH_MAX_Y)):
            xp = 0
            yp = 0
        else:
            x -= TJCTM24024SPI_TOUCH_MIN_X
            xmax = TJCTM24024SPI_TOUCH_MAX_X - TJCTM24024SPI_TOUCH_MIN_X
            y -= TJCTM24024SPI_TOUCH_MIN_Y
            ymax = TJCTM24024SPI_TOUCH_MAX_Y - TJCTM24024SPI_TOUCH_MIN_Y
            xp = round((ILI.ILI9341_TFTWIDTH-1)*x/xmax)
            yp = round((ILI.ILI9341_TFTHEIGHT-1)*y/ymax)
            if (self.orient == TJCTM24024SPI_ORIENTATION_0):
                xp = ILI.ILI9341_TFTWIDTH - 1 - xp
            elif (self.orient == TJCTM24024SPI_ORIENTATION_90):
                xp = ILI.ILI9341_TFTWIDTH - 1 - xp
                yp = ILI.ILI9341_TFTHEIGHT - 1 - yp
                z = xp
                xp = yp
                yp = z
            elif (self.orient == TJCTM24024SPI_ORIENTATION_180):
                yp = ILI.ILI9341_TFTHEIGHT - 1 - yp
            elif (self.orient == TJCTM24024SPI_ORIENTATION_270):
                z = xp
                xp = yp
                yp = z
        self._touchX = xp
        self._touchY = yp


    def getTouchX(self):
        return self._touchX


    def getTouchY(self):
        return self._touchY


    def dispBegin(self):
        self._disp.begin()

        
    def dispDisplay(self):
        b = self.buffer
        if (self.orient == 0):
            b = b.crop((0,0,240,320))
        elif (self.orient == 1):
            b = b.rotate(90)
            b = b.crop((0,0,240,320))
        elif (self.orient == 2):
            b = b.crop((0,0,240,320))
            b = b.rotate(180)
        elif (self.orient == 3):
            b = b.rotate(90)
            b = b.crop((0,0,240,320))
            b = b.rotate(180)
        self._disp.buffer.paste(b, (0,0))            
        self._disp.display()


    def dispDisplayImage(self, image=None):
        self._disp.display(image)

                
    def dispClear(self, color=(0,0,0)):
        self._disp.clear(color)


    def dispDraw(self):
        return ImageDraw.Draw(self.buffer)

    def dispBuffer(self):
        return self.buffer
        
