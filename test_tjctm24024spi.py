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


from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


import time
from sys import stdout
from TJCTM24024SPI import TJCTM24024SPI
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI

"""COnnection"""
DC = 27
RST = 22
IRQ = 23
PORT = 0


"""Elements of vertical interface"""
HEAD_V_POS      = (0,       240,    240,    40)
KEY_L_POS       = (0,       280,    80,     40)
KEY_V_POS       = (80,      280,    80,     40)
KEY_R_POS       = (160,     280,    80,     40)
HEAD_V_IMG      = (None, None)
KEY_L_IMG       = (None, None)
KEY_V_IMG       = (None, None)
KEY_R_IMG       = (None, None)

"""Elements of horizontal interface"""
HEAD_H_POS      = (240,     0,      80,     120)
KEY_U_POS       = (240,     120,    80,     40)
KEY_H_POS       = (240,     160,    80,     40)
KEY_D_POS       = (240,     200,    80,     40)
HEAD_H_IMG      = (None, None)
KEY_U_IMG       = (None, None)
KEY_H_IMG       = (None, None)
KEY_D_IMG       = (None, None)


ELEMENT_HEAD        = 0
ELEMENT_KEY         = 1

HEAD_COL_LINE       = (255,255,255)
HEAD_COL_FILL       = (255,255,255)
HEAD_COL_TEXT       = (0,0,255)
HEAD_COL_LINE_PR    = (255,255,255)
HEAD_COL_FILL_PR    = (0,255,0)
HEAD_COL_TEXT_PR    = (255,255,255)
HEAD_FONT_TYPE      = '/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf'
HEAD_FONT_SIZE      = 32

KEY_COL_LINE        = (255,255,255)
KEY_COL_FILL        = (0,0,255)
KEY_COL_TEXT        = (255,255,255)
KEY_COL_LINE_PR     = (255,255,255)
KEY_COL_FILL_PR     = (0,255,0)
KEY_COL_TEXT_PR     = (255,255,255)
KEY_FONT_TYPE       = '/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf'
KEY_FONT_SIZE       = 32


HEAD_COLOR          = dict(line=HEAD_COL_LINE, fill=HEAD_COL_FILL, text=HEAD_COL_TEXT, line_pr=HEAD_COL_LINE_PR, fill_pr=HEAD_COL_FILL_PR, text_pr=HEAD_COL_TEXT_PR)
HEAD_FONT           = dict(font=HEAD_FONT_TYPE, size=HEAD_FONT_SIZE)
KEY_COLOR           = dict(line=KEY_COL_LINE, fill=KEY_COL_FILL, text=KEY_COL_TEXT, line_pr=KEY_COL_LINE_PR, fill_pr=KEY_COL_FILL_PR, text_pr=KEY_COL_TEXT_PR)
KEY_FONT            = dict(font=KEY_FONT_TYPE, size=KEY_FONT_SIZE)



#T_KEY_L             = (ELEMENT_KEY, KEY_L_POS, KEY_L_IMG, KEY_COLOR, KEY_FONT)
#T_KEY_H             = (ELEMENT_KEY, KEY_H_POS, KEY_H_IMG, KEY_COLOR, KEY_FONT)
#T_KEY_R             = (ELEMENT_KEY, KEY_R_POS, KEY_R_IMG, KEY_COLOR, KEY_FONT)
#T_KEY_U             = (ELEMENT_KEY, KEY_U_POS, KEY_U_IMG, KEY_COLOR, KEY_FONT)
#T_KEY_V             = (ELEMENT_KEY, KEY_V_POS, KEY_V_IMG, KEY_COLOR, KEY_FONT)
#T_KEY_D             = (ELEMENT_KEY, KEY_D_POS, KEY_D_IMG, KEY_COLOR, KEY_FONT)
#T_HEAD_H            = (ELEMENT_HEAD, HEAD_H_POS, HEAD_H_IMG, HEAD_COLOR, HEAD_FONT)
#T_HEAD_V            = (ELEMENT_HEAD, HEAD_V_POS, HEAD_V_IMG, HEAD_COLOR, HEAD_FONT)



S_HEAD_V            = dict(key=0,  text_v='Voltage',    text_h='Volt',  div=', ',   unit_count=2,   unit=dict([(1,'V'), (2,'%')]))
S_HEAD_C            = dict(key=0,  text_v='Current',    text_h='Curr',  div=', ',   unit_count=2,   unit=dict([(1,'A'), (2,'%')]))
S_HEAD_P            = dict(key=0,  text_v='Power',      text_h='Pwr',   div=', ',   unit_count=2,   unit=dict([(1,'kW'), (2,'%')]))
S_HEAD_E            = dict(key=0,  text_v='Energy',     text_h='Engy',  div=', ',   unit_count=1,   unit=dict([(1,'kW/h')]))
S_HEAD_S            = dict(key=0,  text_v='Sensor',     text_h='Sens',  div='',     unit_count=1,   unit=dict([(1,'')]))
S_HEAD_N            = dict(key=0,  text_v='Net',        text_h='Net',   div='',     unit_count=1,   unit=dict([(1,'')]))
S_HEAD_I            = dict(key=0,  text_v='Info',       text_h='Info',  div='',     unit_count=1,   unit=dict([(1,'')]))

S_KEY_1             = dict(key=1,  text_v='<',          text_h='^',     div='',     unit_count=1,   unit=dict([(1,'')]))
S_KEY_2_V           = dict(key=1,  text_v='',           text_h='',      div='',     unit_count=2,   unit=dict([(1,'%'), (2,'V')]))
S_KEY_2_C           = dict(key=1,  text_v='',           text_h='',      div='',     unit_count=2,   unit=dict([(1,'%'), (2,'I')]))
S_KEY_2_P           = dict(key=1,  text_v='',           text_h='',      div='',     unit_count=2,   unit=dict([(1,'%'), (2,'kW')]))
S_KEY_2_E           = dict(key=1,  text_v='',           text_h='',      div='',     unit_count=1,   unit=dict([(1,'kW/h')]))
S_KEY_2_S           = dict(key=1,  text_v='',           text_h='',      div='',     unit_count=1,   unit=dict([(1,'')]))
S_KEY_2_N           = dict(key=1,  text_v='',           text_h='',      div='',     unit_count=1,   unit=dict([(1,'')]))
S_KEY_2_I           = dict(key=1,  text_v='',           text_h='',      div='',     unit_count=1,   unit=dict([(1,'')]))
S_KEY_3             = dict(key=1,  text_v='>',          text_h='v',     div='',     unit_count=1,   unit=dict([(1,'')]))


P_HEAD              = dict(pos_v=HEAD_V_POS,    pos_h=HEAD_H_POS)
P_KEY_1             = dict(pos_v=KEY_L_POS,     pos_h=KEY_U_POS)
P_KEY_2             = dict(pos_v=KEY_V_POS,     pos_h=KEY_H_POS)
P_KEY_3             = dict(pos_v=KEY_R_POS,     pos_h=KEY_D_POS)

I_HEAD              = dict(color=HEAD_COLOR,    font=HEAD_FONT, img_v=HEAD_V_IMG,   img_h=HEAD_H_IMG)
I_KEY_1             = dict(color=KEY_COLOR,     font=KEY_FONT,  img_v=KEY_L_IMG,    img_h=KEY_U_IMG)
I_KEY_2             = dict(color=KEY_COLOR,     font=KEY_FONT,  img_v=KEY_V_IMG,    img_h=KEY_H_IMG)
I_KEY_3             = dict(color=KEY_COLOR,     font=KEY_FONT,  img_v=KEY_R_IMG,    img_h=KEY_D_IMG)

T_HEAD              = dict([(1,S_HEAD_V),   (2,S_HEAD_C),   (3,S_HEAD_P),   (4,S_HEAD_E),   (5,S_HEAD_S),   (6,S_HEAD_N),   (7,S_HEAD_I)])
T_KEY_1             = dict([(1,S_KEY_1),    (2,S_KEY_1),    (3,S_KEY_1),    (4,S_KEY_1),    (5,S_KEY_1),    (6,S_KEY_1),    (7,S_KEY_1)])
T_KEY_2             = dict([(1,S_KEY_2_V),  (2,S_KEY_2_C),  (3,S_KEY_2_P),  (4,S_KEY_2_E),  (5,S_KEY_2_S),  (6,S_KEY_2_N),  (7,S_KEY_2_I)])
T_KEY_3             = dict([(1,S_KEY_3),    (2,S_KEY_3),    (3,S_KEY_3),    (4,S_KEY_3),    (5,S_KEY_3),    (6,S_KEY_3),    (7,S_KEY_3)])

EL_HEAD             = dict(pos=P_HEAD,  pict=I_HEAD,    text=T_HEAD)
EL_KEY_1            = dict(pos=P_KEY_1, pict=I_KEY_1,   text=T_KEY_1)
EL_KEY_2            = dict(pos=P_KEY_2, pict=I_KEY_2,   text=T_KEY_2)
EL_KEY_3            = dict(pos=P_KEY_3, pict=I_KEY_3,   text=T_KEY_3)


ORIENT_V            = 0
ORIENT_H            = 1
ORIENT_V_INV        = 2
ORIENT_H_INV        = 3



def draw_rotated_text(image, text, pos, angle, font, fill=(255,255,255)):
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
    px = int(pos[0] + (pos[2] - width)/2)
    py = int(pos[1] + (pos[3] - height)/2)
    image.paste(rotated, (px, py), rotated)


def draw_element(screen, orient, mode, view, element, press):
    if (element != None):

        if (view <= element['text'][mode]['unit_count']):
            v = view
        else:
            v = element['text'][mode]['unit_count']

        if ( not press):
            col_line = element['pict']['color']['line']
            col_fill = element['pict']['color']['fill']
            col_text = element['pict']['color']['text']
            img_sel=0
        else:
            col_line = element['pict']['color']['line_pr']
            col_fill = element['pict']['color']['fill_pr']
            col_text = element['pict']['color']['text_pr']
            img_sel=1

        if ((orient == ORIENT_V) or (orient == ORIENT_V_INV)):
            pos = element['pos']['pos_v']           
            img = element['pict']['img_v'][img_sel]
            text1 = element['text'][mode]['text_v'] + element['text'][mode]['div'] + element['text'][mode]['unit'][v]
            text2 = ''
        else:
            pos = element['pos']['pos_h']
            img = element['pict']['img_h'][img_sel]
            if (element['text'][mode]['key'] == 0):
                text1 = element['text'][mode]['text_h']
                text2 = element['text'][mode]['unit'][v]
            else:
                text1 = element['text'][mode]['text_v'] + element['text'][mode]['div'] + element['text'][mode]['unit'][v]
                text2 = ''                

        font_type = element['pict']['font']['font']
        font_size = element['pict']['font']['size']
        font = ImageFont.truetype(font_type, font_size)

        draw.rectangle((pos[0], pos[1], pos[0]+pos[2]-1, pos[1]+pos[3]-1), outline=col_line, fill=col_fill)
        if (text2 == ''):
            draw_rotated_text(screen, text1, pos, 0, font, col_text)
        else:
            p = (pos[0], pos[1]-int(font_size/2), pos[2], pos[3])
            draw_rotated_text(screen, text1, p, 0, font, col_text)
            p = (pos[0], pos[1]+int(font_size/2), pos[2], pos[3])
            draw_rotated_text(screen, text2, p, 0, font, col_text)
            

def is_press_element(element):
    i = disp.isTouch()
    if (i == 1):
        disp.readTouch()
        x = disp.getTouchX()
        y = disp.getTouchY()
        press = False
        print ("i: %s " % i +  "  x: %s " % x + "    y %s" % y)
        if ((orient == ORIENT_V) or (orient == ORIENT_V_INV)):
            pos = element['pos']['pos_v']
            if ((x > pos[0]+10) and (x < pos[0]+pos[2]-10) and (y > pos[1]) and (y < pos[1]+pos[3])):
                press = True
        else:
            pos = element['pos']['pos_h']
            if ((x > pos[0]) and (x < pos[0]+pos[2]) and (y > pos[1]+5) and (y < pos[1]+pos[3]-5)):
                press = True         
        print ("  x1: %s " % pos[0] + "    x2 %s" % (pos[0]+pos[2]) + "  y1: %s " % pos[1] + "    y2 %s" % (pos[1]+pos[3]))
        return press


def draw_screen():
    draw_element(disp.dispBuffer(), orient, mode, view, EL_HEAD, False)
    draw_element(disp.dispBuffer(), orient, mode, view, EL_KEY_1, False)
    draw_element(disp.dispBuffer(), orient, mode, view, EL_KEY_2, False)
    draw_element(disp.dispBuffer(), orient, mode, view, EL_KEY_3, False)
    disp.dispDisplay()
    
                
try:
#    print(EL_HEAD)
    print(EL_HEAD['text'][1]['unit'])        

    disp = TJCTM24024SPI(DC, port=PORT, rst=RST, irq=IRQ)
  
    draw = disp.dispDraw()


#    draw.rectangle((0, 280, 79, 319), outline=(255,255,255), fill=(0,0,255))
#    draw.rectangle((79, 280, 159, 319), outline=(255,255,255), fill=(0,0,255))
#    draw.rectangle((159, 280, 239, 319), outline=(255,255,255), fill=(0,255,0))

#    draw_header(HEADER_H)
    
#    draw_element(HEADER_H,element=ELEMENT_HEADER,text="Current, A")

#    draw_element(KEY_L,element=ELEMENT_KEY,text="<")
#    draw_element(KEY_H,element=ELEMENT_KEY,text="%")
#    draw_element(KEY_R,element=ELEMENT_KEY, text=">")
 

#    draw.line((0, 240, 239, 240), fill=(0,0,255))


    orient=ORIENT_V_INV
    mode=1
    view=1
    
#def draw_element(view, mode, element, press):

    disp.orient = orient




#    disp.dispDisplay()
    

    draw_screen()
    

    print ("Start")
    while True:
        if (is_press_element(EL_KEY_1)):
            mode -= 1
            if (mode == 0):
                mode = 7
            draw_element(disp.dispBuffer(), orient, mode, view, EL_KEY_1, True)
            disp.dispDisplay()
            time.sleep(0.2)
            draw_screen()
        if (is_press_element(EL_KEY_3)):
            mode += 1
            if (mode == 8):
                mode = 1
            draw_element(disp.dispBuffer(), orient, mode, view, EL_KEY_3, True)
            disp.dispDisplay()
            time.sleep(0.2)
            draw_screen()


        if (is_press_element(EL_KEY_2)):
#            orient += 1
#            if (orient == 4):
#                mode = 0
#            disp.orient = orient
            draw_element(disp.dispBuffer(), orient, mode, view, EL_KEY_2, True)
            disp.dispDisplay()
            time.sleep(0.2)
            draw_screen()


#        print ("\rX: %s " % x + " Y: %s" % y + " Z1: %s" % z1 + " Z2: %s" % z2 + " Pressure: %s" % pressure + " Temp0: %s" % temp0 + " Temp1: %s" % temp1 + " VBatt: %s" % vbatt + " Aux: %s" % aux + " SampleTime: %s ms" % duration +"                  ")
#        print ("i: %s " % i +  "  x: %s " % x + "    y %s" % y)
#        stdout.flush ()
except KeyboardInterrupt:
    print ("keyInt")
    print ("\n")
except Exception:
    print ("except")
    raise
