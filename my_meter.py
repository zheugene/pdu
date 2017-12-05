import time
import redis
from M90E36A import M90E36A
from AM2315 import AM2315
import Adafruit_GPIO as GPIO


PIN_SEN_0   = 33
PIN_SEN_1   = 34
PIN_SEN_2   = 35
PIN_KEY_0   = 36
PIN_KEY_1   = 37


def get_init_energy():
    return (0,0,0,0)




def get_value_level(val, name):
    min0 = vals.get('meter_' + name + '_min0')
    min1 = vals.get('meter_' + name + '_min1')
    max0 = vals.get('meter_' + name + '_max0')
    max1 = vals.get('meter_' + name + '_max1')
    l = 0
    if ((min0 != None) & (min1 != None) & (max0 != None) & (max1 != None)):
        if ((val > min0) & (val < max0)):
            l = 0
        elif ((val > min1) & (val < max1)):
            l = 1
        else:
            l = 2
    return l
    

def get_value_p(val, name):
    norm = vals.get('meter_' + name + '_norm')
    p = []
    for v in val:
        if ((norm != None) & (v != None)):
            n = float(norm)
            p.append(float(100-(100*(n-v)/n)))            
        else:
            p.append(None)
    return p



#-------------------------------------------------------------------------------
# Voltage RMS, V
#-------------------------------------------------------------------------------
def read_meter_u_rms(dev, ind, dt):
    v = dev.meter_u_rms()
#    p = get_value_p(v, 'u_rms')
    l0 = get_value_level(v[0], 'u_rms')
    l1 = get_value_level(v[1], 'u_rms')
    l2 = get_value_level(v[2], 'u_rms')
    vals.hset('meter_u_rms_'+ind, 'a', v[0]) 
    vals.hset('meter_u_rms_'+ind, 'b', v[1]) 
    vals.hset('meter_u_rms_'+ind, 'c', v[2]) 
    vals.hset('meter_u_rms_'+ind, 'la', l0) 
    vals.hset('meter_u_rms_'+ind, 'lb', l1) 
    vals.hset('meter_u_rms_'+ind, 'lc', l2) 
    
#-------------------------------------------------------------------------------
# Current RMS, A
#-------------------------------------------------------------------------------
def read_meter_i_rms(dev, ind, dt):
    v = dev.meter_i_rms()
    p = get_value_p(v, 'i_rms_norm')
    l0 = get_value_level(v[0], 'i_rms')
    l1 = get_value_level(v[1], 'i_rms')
    l2 = get_value_level(v[2], 'i_rms')
    l3 = get_value_level(v[3], 'i_n_rms')
    l4 = get_value_level(v[4], 'i_t_rms')
#    vals.set('meter_i_a_'+ind, i[0], dt)
#    vals.set('meter_i_b_'+ind, i[1], dt)
#    vals.set('meter_i_c_'+ind, i[2], dt)
#    vals.set('meter_i_n_'+ind, i[3], dt)
#    vals.set('meter_i_total_'+ind, i[4], dt)
#    vals.set('meter_i_rms_'+ind, ((v[0],l0), (v[1],l1), (v[2],l2), (v[3],l3)), dt)
#    vals.set('meter_it_rms_'+ind, ((v[4],l4)), dt)
#    vals.set('meter_i_rms_p_'+ind, ((p[0],l0), (p[1],l1), (p[2],l2), (p[3],l3)), dt)
#    vals.set('meter_it_rms_p_'+ind, ((p[4],l4)), dt)
    vals.hset('meter_i_rms_'+ind, 'a', v[0]) 
    vals.hset('meter_i_rms_'+ind, 'b', v[1]) 
    vals.hset('meter_i_rms_'+ind, 'c', v[2]) 
    vals.hset('meter_i_rms_'+ind, 'n', v[3]) 
    vals.hset('meter_i_rms_'+ind, 't', v[4]) 
    vals.hset('meter_i_rms_'+ind, 'la', l0) 
    vals.hset('meter_i_rms_'+ind, 'lb', l1) 
    vals.hset('meter_i_rms_'+ind, 'lc', l2) 
    vals.hset('meter_i_rms_'+ind, 'ln', l3) 
    vals.hset('meter_i_rms_'+ind, 'lt', l4) 


#-------------------------------------------------------------------------------
# Active Power, kw
#-------------------------------------------------------------------------------
def read_meter_pa(dev, ind, dt):
    v = dev.meter_p_a()
    l0 = get_value_level(v[0], 'pa')
    l1 = get_value_level(v[1], 'pa')
    l2 = get_value_level(v[2], 'pa')
    l3 = get_value_level(v[3], 'pa_t')
#    vals.set('meter_pa_a_'+ind, p[0], dt)
#    vals.set('meter_pa_b_'+ind, p[1], dt)
#    vals.set('meter_pa_c_'+ind, p[2], dt)
#    vals.set('meter_pa_total_'+ind, p[3], dt)
##    vals.set('meter_pa_'+ind, ((v[0],l0), (v[1],l1), (v[2],l2)), dt)
##    vals.set('meter_pa_t_'+ind, ((v[3],l3)), dt)
    vals.hset('meter_pa_'+ind, 'a', v[0]) 
    vals.hset('meter_pa_'+ind, 'b', v[1]) 
    vals.hset('meter_pa_'+ind, 'c', v[2]) 
    vals.hset('meter_pa_'+ind, 't', v[3]) 
    vals.hset('meter_pa_'+ind, 'la', l0) 
    vals.hset('meter_pa_'+ind, 'lb', l1) 
    vals.hset('meter_pa_'+ind, 'lc', l2) 
    vals.hset('meter_pa_'+ind, 'lt', l3) 


#-------------------------------------------------------------------------------
# Reactive Power, kvar
#-------------------------------------------------------------------------------
def read_meter_pra(dev, ind, dt):
    v = dev.meter_p_ra()
    l0 = get_value_level(v[0], 'pra')
    l1 = get_value_level(v[1], 'pra')
    l2 = get_value_level(v[2], 'pra')
    l3 = get_value_level(v[3], 'pra_t')
#    vals.set('meter_pra_a_'+ind, p[0], dt)
#    vals.set('meter_pra_b_'+ind, p[1], dt)
#    vals.set('meter_pra_c_'+ind, p[2], dt)
#    vals.set('meter_pra_total_'+ind, p[3], dt)
##    vals.set('meter_pra_'+ind, ((v[0],l0), (v[1],l1), (v[2],l2)), dt)
##    vals.set('meter_pra_t_'+ind, ((v[3],l3)), dt)
    vals.hset('meter_pra_'+ind, 'a', v[0]) 
    vals.hset('meter_pra_'+ind, 'b', v[1]) 
    vals.hset('meter_pra_'+ind, 'c', v[2]) 
    vals.hset('meter_pra_'+ind, 't', v[3]) 
    vals.hset('meter_pra_'+ind, 'la', l0) 
    vals.hset('meter_pra_'+ind, 'lb', l1) 
    vals.hset('meter_pra_'+ind, 'lc', l2) 
    vals.hset('meter_pra_'+ind, 'lt', l3) 


#-------------------------------------------------------------------------------
# Apparent Power, kVA
#-------------------------------------------------------------------------------
def read_meter_pap(dev, ind, dt):
    v = dev.meter_p_ap()
    l0 = get_value_level(v[0], 'pap')
    l1 = get_value_level(v[1], 'pap')
    l2 = get_value_level(v[2], 'pap')
    l3 = get_value_level(v[3], 'pap_t')
#    vals.set('meter_pap_a_'+ind, p[0], dt)
#    vals.set('meter_pap_b_'+ind, p[1], dt)
#    vals.set('meter_pap_c_'+ind, p[2], dt)
#    vals.set('meter_pap_total_'+ind, p[3], dt)
##    vals.set('meter_pap_'+ind, ((v[0],l0), (v[1],l1), (v[2],l2)), dt)
##    vals.set('meter_pap_t_'+ind, ((v[3],l3)), dt)
    vals.hset('meter_pap_'+ind, 'a', v[0]) 
    vals.hset('meter_pap_'+ind, 'b', v[1]) 
    vals.hset('meter_pap_'+ind, 'c', v[2]) 
    vals.hset('meter_pap_'+ind, 't', v[3]) 
    vals.hset('meter_pap_'+ind, 'la', l0) 
    vals.hset('meter_pap_'+ind, 'lb', l1) 
    vals.hset('meter_pap_'+ind, 'lc', l2) 
    vals.hset('meter_pap_'+ind, 'lt', l3) 





# Forward Active Energy
def read_meter_efa(dev, ind, dt):
    p = dev.meter_e_fa()
    vals.set('meter_pap_a_'+ind, p[0], dt)
    vals.set('meter_pap_b_'+ind, p[1], dt)
    vals.set('meter_pap_c_'+ind, p[2], dt)
    vals.set('meter_pap_total_'+ind, p[3], dt)

# Frequncy
def read_meter_freq(dev, ind, dt):
    v = dev.meter_freq()
    l = get_value_level(v, 'freq')
    vals.hset('meter_freq_'+ind, 'f', v) 
    vals.hset('meter_freq_'+ind, 'lf', l) 


# Temperature
def read_meter_temp(dev, ind, dt):
    v = dev.meter_temp()
    l = get_value_level(v, 'temp')
    vals.hset('meter_temp_'+ind, 't', v) 
    vals.hset('meter_temp_'+ind, 'lt', l) 




def read_meter_all():
    read_meter_u_rms(meter0, '0', dt)
    read_meter_i_rms(meter0, '0', dt)
    read_meter_pa(meter0, '0', dt)
    read_meter_pra(meter0, '0', dt)
    read_meter_pap(meter0, '0', dt)
    read_meter_freq(meter0, '0', dt)
    read_meter_temp(meter0, '0', dt)




def select_sensor(s = 0):
    mygpio.output(PIN_SEN_0, False)
    mygpio.output(PIN_SEN_1, False)
    mygpio.output(PIN_SEN_2, False)
    if (s == 0):
        mygpio.output(PIN_SEN_0, True)
    elif (s == 1):
        mygpio.output(PIN_SEN_1, True)
    elif (s == 2):
        mygpio.output(PIN_SEN_2, True)



def read_key_all():
    select_sensor(3)
    k0 = mygpio.input(PIN_KEY_0)
    k1 = mygpio.input(PIN_KEY_1)
    if k0:
        vals.hset('sensor', 'key1', 'Off' )
    else:
        vals.hset('sensor', 'key1', 'On')
    if k1:
        vals.hset('sensor', 'key2', 'Off')
    else:
        vals.hset('sensor', 'key2', 'On')



def read_sensor_all():
    select_sensor(0)
    s0 = thsen.read_humidity_temperature()
    select_sensor(1)
    s1 = thsen.read_humidity_temperature()
    select_sensor(2)
    s2 = thsen.read_humidity_temperature()
    if ((s0[0] != None) & (s0[1] != None)):
        vals.hset('sensor', 'h1', s0[0])
        vals.hset('sensor', 't1', s0[1])
    if ((s1[0] != None) & (s1[1] != None)):
        vals.hset('sensor', 'h2', s1[0])
        vals.hset('sensor', 't2', s1[1])
    if ((s2[0] != None) & (s2[1] != None)):
        vals.hset('sensor', 'h3', s2[0])
        vals.hset('sensor', 't3', s2[1])

      

def init_levels():
    # Voltage RMS, V
    vals.set('meter_u_rms_norm','220')
    vals.set('meter_u_rms_min0','210')
    vals.set('meter_u_rms_max0','230')
    vals.set('meter_u_rms_min1','200')
    vals.set('meter_u_rms_max1','240')
    # Current RMS, A
    vals.set('meter_i_rms_norm','16')
    vals.set('meter_i_rms_min0','12')
    vals.set('meter_i_rms_max0','16')
    vals.set('meter_i_rms_min1','14')
    vals.set('meter_i_rms_max1','16')
    # Active Power, kw

    # Reactive Power, kvar

    # Apparent Power, kVA



try:

    vals = redis.StrictRedis(host='localhost', port=6379, db=0)
    meter0 = M90E36A(port=2, dev=0, irq=39)
    thsen = AM2315()
    mygpio = GPIO.get_platform_gpio()    

    mygpio.setup(PIN_SEN_0, GPIO.OUT, GPIO.PUD_OFF)
    mygpio.output(PIN_SEN_0, False)
    mygpio.setup(PIN_SEN_1, GPIO.OUT, GPIO.PUD_OFF)
    mygpio.output(PIN_SEN_1, False)
    mygpio.setup(PIN_SEN_2, GPIO.OUT, GPIO.PUD_OFF)
    mygpio.output(PIN_SEN_2, False)
    mygpio.setup(PIN_KEY_0, GPIO.IN, GPIO.PUD_UP)
    mygpio.setup(PIN_KEY_1, GPIO.IN, GPIO.PUD_UP)
    

    dt = 3
    dts = 6

    print ("Meter Start")


    energy = get_init_energy()

    init_levels()


    while True:
        # 1
        read_sensor_all()
        read_meter_all()
        read_key_all()
        time.sleep(1)
        # 2
        read_meter_all()
        read_key_all()
        time.sleep(1)
        # 3
        read_meter_all()
        read_key_all()
        time.sleep(1)
        # 4
        read_meter_all()
        read_key_all()
        time.sleep(1)

    

except KeyboardInterrupt:
#    print ("keyInt")
#    print ("\n")
    pass
except Exception:
#    print ("except")
    pass
    raise

"""
def read_meter_u_thdn(dev, ind, dt):
    u = dev.meter_u_thdn()
    vals.set('meter_u_a_p_'+ind, u[0], dt)
    vals.set('meter_u_b_p_'+ind, u[1], dt)
    vals.set('meter_u_c_p_'+ind, u[2], dt)

def read_meter_i_thdn(dev, ind, dt):
    i = dev.meter_i_thdn()
    vals.set('meter_i_a_p_'+ind, i[0], dt)
    vals.set('meter_i_b_p_'+ind, i[1], dt)
    vals.set('meter_i_c_p_'+ind, i[2], dt)




"""
