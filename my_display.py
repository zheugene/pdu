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



def get_value(val, dig, dec=0):
    sv = vals.get(val)
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
    

def draw_out_V():
    draw.rectangle(SCR_CONF['pos'], outline=SCR_CONF['line'], fill=SCR_CONF['fill'])
    font = ImageFont.truetype(FONT_H['font'], FONT_H['size'])
    color = FONT_H['color']
    draw_rotated_text(disp.dispBuffer(), "A", POS_H_A, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "B", POS_H_B, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "C", POS_H_C, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "Freq1", POS_H_U, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "Freq2", POS_H_D, 0, font, color, False, False)  
    font = ImageFont.truetype(FONT_T['font'], FONT_T['size'])
    color = FONT_T['color']
    if (view == 1):
        va1 = get_value('meter_ua_1',3)
        vb1 = get_value('meter_ub_1',3)
        vc1 = get_value('meter_uc_1',3)
        va2 = get_value('meter_ua_2',3)
        vb2 = get_value('meter_ub_2',3)
        vc2 = get_value('meter_uc_2',3)
    else:
        va1 = get_value('meter_ua_p_1',3)
        vb1 = get_value('meter_ub_p_1',3)
        vc1 = get_value('meter_uc_p_1',3)
        va2 = get_value('meter_ua_p_2',3)
        vb2 = get_value('meter_ub_p_2',3)
        vc2 = get_value('meter_uc_p_2',3)
    vf1 = get_value('meter_freq_1',2) + ' Hz'
    vf2 = get_value('meter_freq_2',2) + ' Hz'
    draw_rotated_text(disp.dispBuffer(), va1, POS_T_A1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vb1, POS_T_B1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vc1, POS_T_C1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vf1, POS_T_U12, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), va2, POS_T_A2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vb2, POS_T_B2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vc2, POS_T_C2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vf2, POS_T_D12, 0, font, color, False, False)  


def draw_out_C():
    draw.rectangle(SCR_CONF['pos'], outline=SCR_CONF['line'], fill=SCR_CONF['fill'])
    draw.rectangle(SCR_LINE['pos'], outline=SCR_LINE['line'], fill=SCR_LINE['fill'])
    font = ImageFont.truetype(FONT_H['font'], FONT_H['size'])
    color = FONT_H['color']
    draw_rotated_text(disp.dispBuffer(), "A", POS_H_A, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "B", POS_H_B, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "C", POS_H_C, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "N", POS_H_N, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "Total", POS_H_D, 0, font, color, False, False)  
    font = ImageFont.truetype(FONT_T['font'], FONT_T['size'])
    color = FONT_T['color']
    if (view == 1):
        va1 = get_value('meter_ia_1',4,2)
        vb1 = get_value('meter_ib_1',4,2)
        vc1 = get_value('meter_ic_1',4,2)
        vn1 = get_value('meter_in_1',4,2)
        va2 = get_value('meter_ia_2',4,2)
        vb2 = get_value('meter_ib_2',4,2)
        vc2 = get_value('meter_ic_2',4,2)
        vn2 = get_value('meter_in_2',4,2)
        vt = get_value('meter_itotal',4,2)
    else:
        va1 = get_value('meter_ia_p_1',4,2)
        vb1 = get_value('meter_ib_p_1',4,2)
        vc1 = get_value('meter_ic_p_1',4,2)
        vn1 = get_value('meter_in_p_1',4,2)
        va2 = get_value('meter_ia_p_2',4,2)
        vb2 = get_value('meter_ib_p_2',4,2)
        vc2 = get_value('meter_ic_p_2',4,2)
        vn2 = get_value('meter_in_p_2',4,2)
        vt = get_value('meter_itotal_p',4,2)
    draw_rotated_text(disp.dispBuffer(), va1, POS_T_A1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vb1, POS_T_B1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vc1, POS_T_C1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vn1, POS_T_N1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), va2, POS_T_A2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vb2, POS_T_B2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vc2, POS_T_C2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vn2, POS_T_N2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vt, POS_T_D12, 0, font, color, False, False)  

    
def draw_out_P():
    draw.rectangle(SCR_CONF['pos'], outline=SCR_CONF['line'], fill=SCR_CONF['fill'])
    draw.rectangle(SCR_LINE['pos'], outline=SCR_LINE['line'], fill=SCR_LINE['fill'])
    font = ImageFont.truetype(FONT_H['font'], FONT_H['size'])
    color = FONT_H['color']
    draw_rotated_text(disp.dispBuffer(), "A", POS_H_A, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "B", POS_H_B, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "C", POS_H_C, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "N", POS_H_N, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "Total", POS_H_D, 0, font, color, False, False)  
    font = ImageFont.truetype(FONT_T['font'], FONT_T['size'])
    color = FONT_T['color']
    if (view == 1):
        va1 = get_value('meter_pa_1',4,2)
        vb1 = get_value('meter_pb_1',4,2)
        vc1 = get_value('meter_pc_1',4,2)
        vn1 = get_value('meter_pn_1',4,2)
        va2 = get_value('meter_pa_2',4,2)
        vb2 = get_value('meter_pb_2',4,2)
        vc2 = get_value('meter_pc_2',4,2)
        vn2 = get_value('meter_pn_2',4,2)
        vt = get_value('meter_ptotal',4,2)
    else:
        va1 = get_value('meter_pa_p_1',4,2)
        vb1 = get_value('meter_pb_p_1',4,2)
        vc1 = get_value('meter_pc_p_1',4,2)
        vn1 = get_value('meter_pn_p_1',4,2)
        va2 = get_value('meter_pa_p_2',4,2)
        vb2 = get_value('meter_pb_p_2',4,2)
        vc2 = get_value('meter_pc_p_2',4,2)
        vn2 = get_value('meter_pn_p_2',4,2)
        vt = get_value('meter_itotal_p',4,2)
    draw_rotated_text(disp.dispBuffer(), va1, POS_T_A1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vb1, POS_T_B1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vc1, POS_T_C1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vn1, POS_T_N1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), va2, POS_T_A2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vb2, POS_T_B2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vc2, POS_T_C2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vn2, POS_T_N2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vt, POS_T_D12, 0, font, color, False, False)  


def draw_out_E():
    draw.rectangle(SCR_CONF['pos'], outline=SCR_CONF['line'], fill=SCR_CONF['fill'])
    font = ImageFont.truetype(FONT_H['font'], FONT_H['size'])
    color = FONT_H['color']
    draw_rotated_text(disp.dispBuffer(), "A", POS_H_A, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "B", POS_H_B, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "C", POS_H_C, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), "Total", POS_H_D, 0, font, color, False, False)  
    font = ImageFont.truetype(FONT_T['font'], FONT_T['size'])
    color = FONT_T['color']
    if (view == 1):
        va1 = get_value('meter_ea_1',4,2)
        vb1 = get_value('meter_eb_1',4,2)
        vc1 = get_value('meter_ec_1',4,2)
        va2 = get_value('meter_ea_2',4,2)
        vb2 = get_value('meter_eb_2',4,2)
        vc2 = get_value('meter_ec_2',4,2)
        vt = get_value('meter_ptotal',4,2)
    draw_rotated_text(disp.dispBuffer(), va1, POS_T_A1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vb1, POS_T_B1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vc1, POS_T_C1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), va2, POS_T_A2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vb2, POS_T_B2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vc2, POS_T_C2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vt, POS_T_D12, 0, font, color, False, False)  


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
    color = FONT_T['color']
    if (view == 1):
        vt1 = get_value('meter_temp1',4)+chr(0xb0)+"C" 
        vt2 = get_value('meter_temp2',4)+chr(0xb0)+"C"
        vt3 = get_value('meter_temp3',4)+chr(0xb0)+"C"
        vh1 = get_value('meter_hum1',4)+"%"
        vh2 = get_value('meter_hum2',4)+"%"
        vh3 = get_value('meter_hum3',4)+"%"
        vk1 = get_value('meter_key1',4)
        vk2 = get_value('meter_key2',4)
    draw_rotated_text(disp.dispBuffer(), vt1, POS_T_A1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vt2, POS_T_B1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vt3, POS_T_C1, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vh1, POS_T_A2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vh2, POS_T_B2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vh3, POS_T_C2, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vk1, POS_T_U12, 0, font, color, False, False)  
    draw_rotated_text(disp.dispBuffer(), vk2, POS_T_D12, 0, font, color, False, False)  
    

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


                
try:

    vals = redis.StrictRedis(host='localhost', port=6379, db=0)

    disp = TJCTM24024SPI(DC, port=PORT, rst=RST, irq=IRQ)
  
    draw = disp.dispDraw()


    orient=ORIENT_H
    mode=1
    view=2
    
    disp.orient = orient
    

    draw_screen()
    

    print ("Start")


    while True:
        draw_screen()
        if (is_press_element(EL_KEY_1)):
            mode -= 1
            if (mode == 0):
                mode = 7
            view = 1
            draw_element(disp.dispBuffer(), orient, mode, view, EL_KEY_1, True)
            disp.dispDisplay()
            time.sleep(0.2)
            draw_screen()
        if (is_press_element(EL_KEY_3)):
            mode += 1
            if (mode == 8):
                mode = 1
            view = 1
            draw_element(disp.dispBuffer(), orient, mode, view, EL_KEY_3, True)
            disp.dispDisplay()
            time.sleep(0.2)
            draw_screen()

        if (is_press_element(EL_KEY_2)):
            v = EL_KEY_2['text'][mode]['unit_count']
            view += 1
            if (view > v):
                view = 1
            draw_element(disp.dispBuffer(), orient, mode, view, EL_KEY_2, True)
            disp.dispDisplay()
            time.sleep(0.2)
            draw_screen()

except KeyboardInterrupt:
    print ("keyInt")
    print ("\n")
except Exception:
    print ("except")
    raise
