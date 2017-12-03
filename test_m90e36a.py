import time
import redis
from M90E36A import M90E36A


def get_init_energy():
    return (0,0,0,0)


def read_meter_u(dev, ind):
    u = dev.meter_u_rms()
    vals.set('meter_u_a_'+ind, u[0], dt)
    vals.set('meter_u_b_'+ind, u[1], dt)
    vals.set('meter_u_c_'+ind, u[2], dt)
    
def read_meter_i(dev, ind):
    i = dev.meter_i_rms()
    vals.set('meter_i_a_'+ind, i[0], dt)
    vals.set('meter_i_b_'+ind, i[1], dt)
    vals.set('meter_i_c_'+ind, i[2], dt)
    vals.set('meter_i_n_'+ind, i[3], dt)
    vals.set('meter_i_total_'+ind, i[4], dt)

# Active Power, kw
def read_meter_pa(dev, ind)
    p = dev.meter_p_a()
    vals.set('meter_pa_a_'+ind, p[0], dt)
    vals.set('meter_pa_b_'+ind, p[1], dt)
    vals.set('meter_pa_c_'+ind, p[2], dt)
    vals.set('meter_pa_total_'+ind, p[3], dt)

# Reactive Power, kvar
def read_meter_pra(dev, ind)
    p = dev.meter_p_ra()
    vals.set('meter_pra_a_'+ind, p[0], dt)
    vals.set('meter_pra_b_'+ind, p[1], dt)
    vals.set('meter_pra_c_'+ind, p[2], dt)
    vals.set('meter_pra_total_'+ind, p[3], dt)

# Apparent Power, kVA
def read_meter_pap(dev, ind)
    p = dev.meter_p_ap()
    vals.set('meter_pap_a_'+ind, p[0], dt)
    vals.set('meter_pap_b_'+ind, p[1], dt)
    vals.set('meter_pap_c_'+ind, p[2], dt)
    vals.set('meter_pap_total_'+ind, p[3], dt)

# Forward Active Energy
def read_meter_efa(dev, ind)
    p = dev.meter_e_fa()
    vals.set('meter_pap_a_'+ind, p[0], dt)
    vals.set('meter_pap_b_'+ind, p[1], dt)
    vals.set('meter_pap_c_'+ind, p[2], dt)
    vals.set('meter_pap_total_'+ind, p[3], dt)





try:

    vals = redis.StrictRedis(host='localhost', port=6379, db=0)

    meter0 = M90E36A(port=2, dev=0, irq=39)
    
    dt = 3

    print ("Meter Start")


    energy = get_init_energy()


    while True:

        read_meter_u(meter0, '0')
        u = meter1.meter_u_rms()
        vals.set('meter_u_a_0', u[0], dt)
        vals.set('meter_u_b_0', u[1], dt)
        vals.set('meter_u_c_0', u[2], dt)
        
        i = meter1.meter_i_rms()
        vals.set('meter_i_a_1', i[0], dt)
        vals.set('meter_i_b_1', i[1], dt)
        vals.set('meter_i_c_1', i[2], dt)
        vals.set('meter_i_n_1', i[3], dt)
        vals.set('meter_i_total', i[4], dt)

        # Active Power, kw
        p = meter1.meter_p_a()
        vals.set('meter_pa_a_1', p[0], dt)
        vals.set('meter_pa_b_1', p[1], dt)
        vals.set('meter_pa_c_1', p[2], dt)
        vals.set('meter_pa_total', p[3], dt)

        # Reactive Power, kvar
        p = meter1.meter_p_ra()
        vals.set('meter_pra_a_1', p[0], dt)
        vals.set('meter_pra_b_1', p[1], dt)
        vals.set('meter_pra_c_1', p[2], dt)
        vals.set('meter_pra_total', p[3], dt)

        # Apparent Power, kVA
        p = meter1.meter_p_ap()
        vals.set('meter_pap_a_1', p[0], dt)
        vals.set('meter_pap_b_1', p[1], dt)
        vals.set('meter_pap_c_1', p[2], dt)
        vals.set('meter_pap_total', p[3], dt)

        freq = meter1.meter_freq()
        vals.set('meter_freq_1', freq, dt)

        temp=meter1.meter_temp()
        vals.set('meter_freq_2', temp, dt)
        time.sleep(1)



except KeyboardInterrupt:
    print ("keyInt")
    print ("\n")
except Exception:
    print ("except")
    raise

