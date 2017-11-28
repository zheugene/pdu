# Copyright 2012 Matthew Lowden
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Python proof of concept for interfacing an XPT2046 Touch Screen Controller
# to a Raspberry Pi using SPI (via bit-banged GPIO).

# This sample uses the SPI pins on the Raspberry Pi Expansion header.
# (With the intention that no wiring changes should be required to use SPI
# drivers, rather than bit-banged GPIO).

# More information on Raspberry Pi GPIO can be found here:
# http://elinux.org/RPi_Low-level_peripherals

# This sample code is dependent on the RPi.GPIO library available here:
# http://pypi.python.org/pypi/RPi.GPIO/


import time
from sys import stdout
from XPT2046 import XPT2046
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI


IRQ = None
SPI_PORT = 0
SPI_DEVICE = 1

                
try:
    touch = XPT2046(irq=IRQ, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=500000))
    print ("Start")
    while True:
        startTime = time.time()
        x = touch.readX()
        y = touch.readY()
        z1 = touch.readZ1()
        z2 = touch.readZ2()
        pressure = round(touch.readTouchPressure(),2)
        temp0 = touch.readTemperature0()
        temp1 = touch.readTemperature1()
        vbatt = touch.readBatteryVoltage()
        aux = touch.readAuxiliary()
        duration = round((time.time() - startTime) * 1000, 2)
        print ("\rX: %s " % x + " Y: %s" % y + " Z1: %s" % z1 + " Z2: %s" % z2 + " Pressure: %s" % pressure + " Temp0: %s" % temp0 + " Temp1: %s" % temp1 + " VBatt: %s" % vbatt + " Aux: %s" % aux + " SampleTime: %s ms" % duration +"                  ")
#        print ("\rtemp0: %s " % temp0 + " %s" % temp1)
        stdout.flush ()
except KeyboardInterrupt:
    print ("keyInt")
    print ("\n")
except Exception:
    print ("except")
    raise
