# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


import time
from sys import stdout
from TJCTM24024SPI import TJCTM24024SPI
import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import redis

from my_display_conf import *
#from my_value_list import *


PIN_LED_G   = 30
PIN_LED_R   = 31
PIN_BEEP    = 32





def get_str_value(sv, dig, dec=0):
    if (sv == None):
        sres = '-'
    else:
        sres = ''
        if (dec == 0):
            for char in sv:
                if (char == '.'):
                    break
                sres += char
        else:
            n = 0
            for char in sv:
                n += 1
                if (n > dig):
                    break
                if ((char == '.') and (n == dig)):
                    break
                sres += char
    return sres



def get_value(val, dig, dec=0):
    sv = vals.get(val)
    return get_str_value(sv, dig, dec)

def get_val_lev(name, key, dig, dec=0):
    sv = vals.hget(name, key)
    l = vals.hget(name, 'l'+key)
    if (l == None):
        l = 0
    return get_str_value(sv, dig, dec), int(l)
    
def get_arr_val_lev(name, lsdev, lskey, dig, dec=0):
    av = []
    al = []
    for dev in lsdev:
        v = []
        l = []
        for key in lskey:
            v.append(vals.hget(name + dev, key))
            l.append(vals.hget(name + dev, 'l' + key))
        av.append(v)
        al.append(l)
    return av, al 



def get_value_list(name, dig, dec=0):
    lsval = vals.get(name)
    s = []
    for v in lsval:
        print(v + ' ')
        s.append(get_str_value(v[0], dig, dec=0))
    print('/n')
    return s


def draw_rotated_text(image, text, pos, angle, font, fill=(255,255,255), center_h=True, center_v=True):
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
    if (center_h):
        px = int(pos[0] + (pos[2] - width)/2)
    else:
        px = pos[0]
    if (center_v):
        py = int(pos[1] + (pos[3] - height)/2)
    else:
        py = pos[1]
    py = int(py - height/10)
    image.paste(rotated, (px, py), rotated)


def draw_element(screen, orient, mode, view, element, press):
    if (element != None):

        v_cnt = element['text'][mode]['unit_count']
        v = view
        if (v > v_cnt):
            v = 1

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

        if ((element['text'][mode]['key'] == 2) and (v_cnt == 1)):
            draw.rectangle((pos[0], pos[1], pos[0]+pos[2]-1, pos[1]+pos[3]-1), outline=col_line, fill=col_line)
        else:
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
    draw_out_data()
    disp.dispDisplay()




def block_draw_text(buf, arrtext, arrlevel, arru, arrpos, font, dig, dec=0):  
    ldev = len(arrtext)
    color = [FONT_T['color'], (255,255,0), (255,0,0)]
    pos = 0
#    print(arrtext, arrlevel,arrpos)
    for i in xrange(ldev):
        litem = len(arrtext[i])
        for j in xrange(litem):
            if (arrlevel[i][j] == None):
                c = 0
            else:
                c = int(arrlevel[i][j])
            if (arrtext[i][j] == None):
                text = None
            else:
                text = arrtext[i][j]
#                try
#                except Exception:
#                    c = 0
#                raise
            text = get_str_value(text, dig, dec) + str(arru[pos])
            draw_rotated_text(buf, text, arrpos[pos], 0, font, color[c], False, False)        
            pos += 1

            

def draw_out_V():
    draw.rectangle(SCR_CONF['pos'], outline=SCR_CONF['line'], fill=SCR_CONF['fill'])
    font = ImageFont.truetype(FONT_H['font'], FONT_H['size'])
    color = FONT_H['color']
    draw_rotated_text(disp.dispBuffer(), "A", POS_H_A, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "B", POS_H_B, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "C", POS_H_C, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "Freq", POS_H_U, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "Temp", POS_H_D, 0, font, color, False, False)  
    font = ImageFont.truetype(FONT_T['font'], FONT_T['size'])
    color = [FONT_T['color'], (255,255,0), (255,0,0)]
    if (view == 1):
        v, l = get_arr_val_lev('meter_u_rms_', ('0'), ('a', 'b', 'c'), 3)
    vf, lf = get_arr_val_lev('meter_freq_', ('0'), ('f'), 3)
    vt, lt = get_arr_val_lev('meter_temp_', ('0'), ('t'), 3)

#    vf0 = get_value('meter_freq_0',2) + ' Hz'
#    vt0 = get_value('meter_temp_0',2) + chr(0xb0) + 'C'
    pos = [POS_T_A1, POS_T_B1, POS_T_C1]
    u = ['', '', '', '', '', '', '']
    block_draw_text(disp.dispBuffer(), v, l, u, pos, font, 3)
    u = ['Hz']
    block_draw_text(disp.dispBuffer(), vf, lf, u, [POS_T_U12], font, 3)
    u = [chr(0xb0)+'C'] 
    block_draw_text(disp.dispBuffer(), vt, lt, u, [POS_T_D12], font, 3)
#    draw_rotated_text(disp.dispBuffer(), vf0, POS_T_U12, 0, font, color[0], False, False)  
#    draw_rotated_text(disp.dispBuffer(), vt0, POS_T_D12, 0, font, color[0], False, False)  


def draw_out_C():
    draw.rectangle(SCR_CONF['pos'], outline=SCR_CONF['line'], fill=SCR_CONF['fill'])
#    draw.rectangle(SCR_LINE['pos'], outline=SCR_LINE['line'], fill=SCR_LINE['fill'])
    font = ImageFont.truetype(FONT_H['font'], FONT_H['size'])
    color = FONT_H['color']
    draw_rotated_text(disp.dispBuffer(), "A", POS_H_A, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "B", POS_H_B, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "C", POS_H_C, 0, font, color, False, False)  
#    draw_rotated_text(disp.dispBuffer(), "N", POS_H_N, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "Total", POS_H_D, 0, font, color, False, False)  
    font = ImageFont.truetype(FONT_T['font'], FONT_T['size'])
    color = [FONT_T['color'], (255,255,0), (255,0,0)]
    if (view == 1):
        v, l = get_arr_val_lev('meter_i_rms_', ('0','1'), ('a', 'b', 'c'), 3)
        vt, lt = get_arr_val_lev('meter_i_rms_total', (''), ('t'), 3)
    else:
        v, l = get_arr_val_lev('meter_i_rms_p_', ('0','1'), ('a', 'b', 'c'), 3)
        vt, lt = get_arr_val_lev('meter_i_rms_p_total', (''), ('t'), 3)
    pos = [POS_T_A1, POS_T_B1, POS_T_C1, POS_T_A2, POS_T_B2, POS_T_C2]
    u = ['', '', '', '', '', '', '']
    block_draw_text(disp.dispBuffer(), v, l, u, pos, font, 4, 3)
    block_draw_text(disp.dispBuffer(), vt, lt, u, [POS_T_D12], font, 4, 3)

    
def draw_out_P():
    draw.rectangle(SCR_CONF['pos'], outline=SCR_CONF['line'], fill=SCR_CONF['fill'])
#    draw.rectangle(SCR_LINE['pos'], outline=SCR_LINE['line'], fill=SCR_LINE['fill'])
    font = ImageFont.truetype(FONT_H['font'], FONT_H['size'])
    color = FONT_H['color']
    draw_rotated_text(disp.dispBuffer(), "A", POS_H_A, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "B", POS_H_B, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "C", POS_H_C, 0, font, color, False, False)  
#    draw_rotated_text(disp.dispBuffer(), "N", POS_H_N, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "Total", POS_H_D, 0, font, color, False, False)  
    font = ImageFont.truetype(FONT_T['font'], FONT_T['size'])
    color = [FONT_T['color'], (255,255,0), (255,0,0)]
    if (view == 1):
        v, l = get_arr_val_lev('meter_pa_', ('0','1'), ('a', 'b', 'c'), 3)
        vt, lt = get_arr_val_lev('meter_pa_total', (''), ('t'), 3)
    elif (view == 2):
        v, l = get_arr_val_lev('meter_pra_', ('0','1'), ('a', 'b', 'c'), 3)
        vt, lt = get_arr_val_lev('meter_pra_total', (''), ('t'), 3)
    elif (view == 3):
        v, l = get_arr_val_lev('meter_pap_', ('0','1'), ('a', 'b', 'c'), 3)
        vt, lt = get_arr_val_lev('meter_pap_total', (''), ('t'), 3)
    pos = [POS_T_A1, POS_T_B1, POS_T_C1, POS_T_A2, POS_T_B2, POS_T_C2]
    u = ['', '', '', '', '', '', '']
    block_draw_text(disp.dispBuffer(), v, l, u, pos, font, 3)
    block_draw_text(disp.dispBuffer(), vt, lt, u, [POS_T_D12], font, 3)


def draw_out_E():
    draw.rectangle(SCR_CONF['pos'], outline=SCR_CONF['line'], fill=SCR_CONF['fill'])
    font = ImageFont.truetype(FONT_H['font'], FONT_H['size'])
    color = FONT_H['color']
    draw_rotated_text(disp.dispBuffer(), "A", POS_H_A, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "B", POS_H_B, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "C", POS_H_C, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "Total", POS_H_D, 0, font, color, False, False)  
    font = ImageFont.truetype(FONT_T['font'], FONT_T['size'])
    color = [FONT_T['color'], (255,255,0), (255,0,0)]
    if (view == 1):
        v, l = get_arr_val_lev('meter_e_', ('0','1'), ('a', 'b', 'c'), 3)
        vt, lt = get_arr_val_lev('meter_e_total', (''), ('t'), 3)
    pos = [POS_T_A1, POS_T_B1, POS_T_C1, POS_T_A2, POS_T_B2, POS_T_C2]
    u = ['', '', '', '', '', '', '']
    block_draw_text(disp.dispBuffer(), v, l, u, pos, font, 3)
    block_draw_text(disp.dispBuffer(), vt, lt, u, [POS_T_D12], font, 3)


def draw_out_S():
    draw.rectangle(SCR_CONF['pos'], outline=SCR_CONF['line'], fill=SCR_CONF['fill'])
    font = ImageFont.truetype(FONT_H['font'], FONT_H['size'])
    color = FONT_H['color']
    draw_rotated_text(disp.dispBuffer(), "1", POS_H_A, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "2", POS_H_B, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "3", POS_H_C, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "KEY1", POS_H_U, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "KEY2", POS_H_D, 0, font, color, False, False)  
    font = ImageFont.truetype(FONT_T['font'], FONT_T['size'])
    color = [FONT_T['color'], (255,255,0), (255,0,0)]
    if (view == 1):
        v, l = get_arr_val_lev('senso', ('r'), ('t1', 't1', 't3', 'h1', 'h2', 'h3', 'key1', 'key2'), 3)
    pos = [POS_T_A1, POS_T_B1, POS_T_C1, POS_T_A2, POS_T_B2, POS_T_C2, POS_T_U12, POS_T_D12]
    u = [chr(0xb0)+'C', chr(0xb0)+'C', chr(0xb0)+'C', '%', '%', '%', '', '']
    block_draw_text(disp.dispBuffer(), v, l, u, pos, font, 3)
    

def draw_out_N():
    draw.rectangle(SCR_CONF['pos'], outline=SCR_CONF['line'], fill=SCR_CONF['fill'])
    font = ImageFont.truetype(FONT_H['font'], FONT_H['size'])
    color = FONT_H['color']


def draw_out_I():
    draw.rectangle(SCR_CONF['pos'], outline=SCR_CONF['line'], fill=SCR_CONF['fill'])
    font = ImageFont.truetype(FONT_H['font'], FONT_H['size'])
    color = FONT_H['color']


def draw_out_data():
    if (mode == 1):
        draw_out_V()
    elif (mode == 2):
        draw_out_C()
    elif (mode == 3):
        draw_out_P()
    elif (mode == 4):
        draw_out_E()
    elif (mode == 5):
        draw_out_S()
    elif (mode == 6):
        draw_out_N()
    elif (mode == 7):
        draw_out_I()



def beep_on():
    mygpio.output(PIN_BEEP, True)

def beep_off():
    mygpio.output(PIN_BEEP, False)

def beep_1():
    beep_on()
    time.sleep(0.002)
    beep_off()


def led_off():
    mygpio.output(PIN_LED_G, False)
    mygpio.output(PIN_LED_R, False)

def led_on_green():
    mygpio.output(PIN_LED_G, True)
    mygpio.output(PIN_LED_R, False)
    
def led_on_red():
    mygpio.output(PIN_LED_G, False)
    mygpio.output(PIN_LED_R, True)
                
def led_on_yellow():
    mygpio.output(PIN_LED_G, True)
    mygpio.output(PIN_LED_R, True)


try:

    vals = redis.StrictRedis(host='localhost', port=6379, db=0)
    disp = TJCTM24024SPI(DC, port=PORT, rst=RST, irq=IRQ)
    draw = disp.dispDraw()
    mygpio = GPIO.GPIO.get_platform_gpio()

    mygpio.setup(PIN_LED_G, GPIO.OUT, GPIO.PUD_OFF)
    mygpio.setup(PIN_LED_R, GPIO.OUT, GPIO.PUD_OFF)
    mygpio.setup(PIN_BEEP, GPIO.OUT, GPIO.PUD_OFF)
    mygpio.output(PIN_LED_G, False)
    mygpio.output(PIN_LED_R, False)
    mygpio.output(PIN_BEEP, False)

    orient=ORIENT_H
    mode=1
    view=1
    
    disp.orient = orient

    
#    draw_screen()
#    print ("Start")

    while True:
        draw_screen()
        if (is_press_element(EL_KEY_1)):
            mode -= 1
            if (mode == 0):
                mode = 7
            view = 1
            draw_element(disp.dispBuffer(), orient, mode, view, EL_KEY_1, True)
            disp.dispDisplay()
            beep_1()
            time.sleep(0.2)
            draw_screen()
        if (is_press_element(EL_KEY_3)):
            mode += 1
            if (mode == 8):
                mode = 1
            view = 1
            draw_element(disp.dispBuffer(), orient, mode, view, EL_KEY_3, True)
            disp.dispDisplay()
            beep_1()
            time.sleep(0.2)
            draw_screen()

        if (is_press_element(EL_KEY_2)):
            v = EL_KEY_2['text'][mode]['unit_count']
            view += 1
            if (view > v):
                view = 1
            draw_element(disp.dispBuffer(), orient, mode, view, EL_KEY_2, True)
            disp.dispDisplay()
            beep_1()
            time.sleep(0.2)
            draw_screen()

except KeyboardInterrupt:
    print ("keyInt")
    print ("\n")
except Exception:
    print ("except")
    raise
