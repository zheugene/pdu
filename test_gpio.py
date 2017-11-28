import RPi.GPIO as GPIO
import time

pin=5
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin,GPIO.GPCLK1)



p.stop()

GPIO.cleanup()
print("End of program")
