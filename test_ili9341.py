# -*- coding: utf-8 -*-
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import Adafruit_ILI9341 as TFT
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI


# Raspberry Pi configuration.
DC = 27
RST = 22
SPI_PORT = 0
SPI_DEVICE = 0       

# BeagleBone Black configuration.
# DC = 'P9_15'
# RST = 'P9_12'
# SPI_PORT = 0
# SPI_DEVICE = 0

# Create TFT LCD display class.
disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=6400000))

# Initialize display.
disp.begin()

# Clear the display to a red background.
# Can pass any tuple of red, green, blue values (from 0 to 255 each).
disp.clear((255, 255, 255))

# Alternatively can clear to a black screen by calling:
# disp.clear()

# Get a PIL Draw object to start drawing on the display buffer.
draw = disp.draw()

# blue 0,0,255
# green 0,255,0
# red 255,0,0

# Draw a purple rectangle with yellow outline.
#draw.rectangle((0, 0, 239, 219), outline=(0,0,255), fill=(255,255,255))
#draw.rectangle((0, 220, 239, 269), outline=(0,0,255), fill=(255,255,255))
draw.rectangle((0, 270, 79, 319), outline=(255,255,255), fill=(0,0,255))
draw.rectangle((79, 270, 159, 319), outline=(255,255,255), fill=(0,0,255))
draw.rectangle((159, 270, 239, 319), outline=(255,255,255), fill=(0,255,0))

# Draw a white X.
draw.line((0, 220, 239, 220), fill=(0,0,255))
#draw.line((0, 268, 239, 268), fill=(0,0,255))
#draw.line((79, 270, 79, 319), fill=(255,255,255))
#draw.line((159, 270, 159, 319), fill=(255,255,255))


# Draw a cyan triangle with a black outline.
#draw.polygon([(10, 275), (110, 240), (110, 310)], outline=(0,0,0), fill=(0,255,255))

# Load default font.
#font = ImageFont.load_default()


# Alternatively load a TTF font.
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf', 32)
font1 = ImageFont.truetype('/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf', 50)


# Define a function to create rotated text.  Unfortunately PIL doesn't have good
# native support for rotated fonts, but this function can be used to make a
# text image and rotate it so it's easy to paste in the buffer.
def draw_rotated_text(image, text, position, angle, font, fill=(255,255,255)):
    # Get rendered font width and height.
    draw = ImageDraw.Draw(image)
    width, height = draw.textsize(text, font=font)
    # Create a new image with transparent background to store the text.
    textimage = Image.new('RGBA', (width, height), (0,0,0,0))
    # Render the text.
    textdraw = ImageDraw.Draw(textimage)
    textdraw.text((0,0), text, font=font, fill=fill)
    # Rotate the text image.
    rotated = textimage.rotate(angle, expand=1)
    # Paste the text into the image, using it as a mask for transparency.
    image.paste(rotated, position, rotated)

# Write two lines of white text on the buffer, rotated 90 degrees counter clockwise.
draw_rotated_text(disp.buffer, 'Current, A', (50, 225), 0, font, fill=(0,0,255))
draw_rotated_text(disp.buffer, '<', (30, 275), 00, font, fill=(255,255,255))
draw_rotated_text(disp.buffer, '%', (110, 275), 00, font, fill=(255,255,255))
draw_rotated_text(disp.buffer, '>', (190, 275), 00, font, fill=(255,255,255))



draw_rotated_text(disp.buffer, 'A   10  11', (5, 0), 00, font1, fill=(0,0,255))
draw_rotated_text(disp.buffer, 'B   12  14', (5, 50), 00, font1, fill=(255,0,0))
draw_rotated_text(disp.buffer, 'C   15  10', (5, 100), 00, font1, fill=(0,0,255))
draw_rotated_text(disp.buffer, 'N   37  35', (5, 150), 00, font1, fill=(0,0,255))



# Write buffer to display hardware, must be called to make things visible on the
# display!
disp.display()


print('ok')
