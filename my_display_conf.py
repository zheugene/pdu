# -*- coding: utf-8 -*-

"""Connection"""
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
HEAD_H_POS      = (240,     0,      80,     75)
KEY_U_POS       = (240,     75,     80,     55)
KEY_H_POS       = (240,     130,    80,     55)
KEY_D_POS       = (240,     185,    80,     55)
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


S_HEAD_V            = dict(key=0,  text_v='Voltage',    text_h='Volt',  div=', ',   unit_count=2,   unit=dict([(1,'V'), (2,'%')]))
S_HEAD_C            = dict(key=0,  text_v='Current',    text_h='Curr',  div=', ',   unit_count=2,   unit=dict([(1,'A'), (2,'%')]))
S_HEAD_P            = dict(key=0,  text_v='Power',      text_h='Pwr',   div=', ',   unit_count=2,   unit=dict([(1,'kW'), (2,'%')]))
S_HEAD_E            = dict(key=0,  text_v='Energy',     text_h='Engy',  div=', ',   unit_count=1,   unit=dict([(1,'kW/h')]))
S_HEAD_S            = dict(key=0,  text_v='Sensor',     text_h='Sens',  div='',     unit_count=1,   unit=dict([(1,'')]))
S_HEAD_N            = dict(key=0,  text_v='Net',        text_h='Net',   div='',     unit_count=1,   unit=dict([(1,'')]))
S_HEAD_I            = dict(key=0,  text_v='Info',       text_h='Info',  div='',     unit_count=1,   unit=dict([(1,'')]))

S_KEY_1             = dict(key=1,  text_v='<',          text_h='^',     div='',     unit_count=1,   unit=dict([(1,'')]))
S_KEY_2_V           = dict(key=2,  text_v='',           text_h='',      div='',     unit_count=2,   unit=dict([(1,'%'), (2,'V')]))
S_KEY_2_C           = dict(key=2,  text_v='',           text_h='',      div='',     unit_count=2,   unit=dict([(1,'%'), (2,'A')]))
S_KEY_2_P           = dict(key=2,  text_v='',           text_h='',      div='',     unit_count=2,   unit=dict([(1,'%'), (2,'kW')]))
S_KEY_2_E           = dict(key=2,  text_v='',           text_h='',      div='',     unit_count=1,   unit=dict([(1,'')]))
S_KEY_2_S           = dict(key=2,  text_v='',           text_h='',      div='',     unit_count=1,   unit=dict([(1,'')]))
S_KEY_2_N           = dict(key=2,  text_v='',           text_h='',      div='',     unit_count=1,   unit=dict([(1,'')]))
S_KEY_2_I           = dict(key=2,  text_v='',           text_h='',      div='',     unit_count=1,   unit=dict([(1,'')]))
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




SCR_CONF            = dict(pos=(0, 0, 239, 239), fill=(0,0,0), line=(0,0,0))
SCR_LINE            = dict(pos=(0, 135, 239, 135), fill=(0,0,255), line=(0,0,255))

POS_H_A             = (0,0)
POS_H_B             = (0,45)
POS_H_C             = (0,90)
POS_H_N             = (0,135)
POS_H_U             = (0,150)
POS_H_D             = (0,195)

POS_T_A1            = (45,0)
POS_T_B1            = (45,45)
POS_T_C1            = (45,90)
POS_T_N1            = (45,135)
POS_T_U1            = (45,150)
POS_T_D1            = (45,195)

POS_T_A2            = (150,0)
POS_T_B2            = (150,45)
POS_T_C2            = (150,90)
POS_T_N2            = (150,135)
POS_T_U2            = (150,150)
POS_T_D2            = (150,195)

POS_T_N12           = (120,135)
POS_T_U12           = (120,150)
POS_T_D12           = (120,195)

FONT_H              = dict(color=(0,0,255), color_err=(255,0,0), font='/usr/share/fonts/truetype/roboto/Roboto-Light.ttf', size=40)
FONT_T              = dict(color=(255,255,255), color_err=(255,0,0), font='/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf', size=40)

