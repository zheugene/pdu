# -*- coding: cp1251 -*-

import Adafruit_GPIO as GPIO
import Adafruit_GPIO.SPI as SPI



# Status and Special Register
ADDR_SoftReset      = 0x00    #W Software Reset
ADDR_SysStatus0     = 0x01    #R/C System Status 0
ADDR_SysStatus1     = 0x02    #R/C System Status 1
ADDR_FuncEn0        = 0x03    #R/W Function Enable 0
ADDR_FuncEn1        = 0x04    #R/W Function Enable 1
ADDR_ZXConfig       = 0x07    #R/W Zero-Crossing Configuration Configuration of ZX0/1/2 pins’ source
ADDR_SagTh          = 0x08    #R/W Voltage Sag Threshold
ADDR_PhaseLossTh    = 0x09    #R/W Voltage Phase Losing Threshold Similar to Voltage Sag Threshold register
ADDR_INWarnTh0      = 0x0A    #R/W Threshold for calculated (Ia + Ib +Ic) N line rms current Check SysStatus0/1 register
ADDR_INWarnTh1      = 0x0B    #R/W Threshold for sampled (from ADC) N line rms current Check SysStatus0/1 register
ADDR_THDNUTh        = 0x0C    #R/W Voltage THD Warning Threshold Check SysStatus0/1 register
ADDR_THDNITh        = 0x0D    #R/W Current THD Warning Threshold Check SysStatus0/1 register
ADDR_DMACtrl        = 0x0E    #R/W DMA Mode Interface Control DMA mode interface control
ADDR_LastSPIData    = 0x0F    #R Last Read/ Write SPI Value Refer to 4.2.2 Reliability Enhancement Feature

# Low Power Mode Register
ADDR_DetectCtrl     = 0x10    #R/W Current Detect Control
ADDR_DetectTh1      = 0x11    #R/W Channel 1 current threshold in Detection mode
ADDR_DetectTh2      = 0x12    #R/W Channel 2 current threshold in Detection mode
ADDR_DetectTh3      = 0x13    #R/W Channel 3 current threshold in Detection mode
ADDR_PMoffsetA      = 0x14    #R/W Ioffset for phase A in Partial Measurement mode
ADDR_PMoffsetB      = 0x15    #R/W Ioffset for phase B in Partial Measurement mode
ADDR_PMoffsetC      = 0x16    #R/W Ioffset for phase C in Partial Measurement mode
ADDR_PMPGA          = 0x17    #R/W PGAgain Configuration in Partial Measurement mode
ADDR_PMIrmsA        = 0x18    #R Irms for phase A in Partial Measurement mode
ADDR_PMIrmsB        = 0x19    #R Irms for phase B in Partial Measurement mode
ADDR_PMIrmsC        = 0x1A    #R Irms for phase C in Partial Measurement mode
ADDR_PMConfig       = 0x1B    #R/W Measure configuration in Partial Measurement mode
ADDR_PMAvgSamples   = 0x1C    #R/W Number of 8K samples to be averaged in RMS/mean computation
ADDR_PMIrmsLSB      = 0x1D    #R LSB bits of PMRrms[A/B/C] It returns MSB of the mean measurement data in Mean value test

# Configuration Registers
ADDR_ConfigStart    = 0x30    #R/W Calibration Start Command
ADDR_PLconstH       = 0x31    #R/W High Word of PL_Constant
ADDR_PLconstL       = 0x32    #R/W Low Word of PL_Constant
ADDR_MMode0         = 0x33    #R/W Metering method configuration
ADDR_MMode1         = 0x34    #R/W PGA gain configuration
ADDR_PstartTh       = 0x35    #R/W Active Startup Power Threshold
ADDR_QstartTh       = 0x36    #R/W Reactive Startup Power Threshold
ADDR_SstartTh       = 0x37    #R/W Apparent Startup Power Threshold
ADDR_PphaseTh       = 0x38    #R/W Startup Power Threshold (Active E nergy Accumulation)
ADDR_QphaseTh       = 0x39    #R/W Startup Power Threshold (ReActive E nergy Accumulation)
ADDR_SphaseTh       = 0x3A    #R/W Startup Power Threshold (Apparent E nergy Accumulation)
ADDR_CS0            = 0x3B    #R/W Checksum 0

# Calibration Registers
ADDR_CalStart       = 0x40    #R/W Calibration Start Command
ADDR_PoffsetA       = 0x41    #R/W Phase A Active Power Offset
ADDR_QoffsetA       = 0x42    #R/W Phase A Reactive Power Offset
ADDR_PoffsetB       = 0x43    #R/W Phase B Active Power Offset
ADDR_QoffsetB       = 0x44    #R/W Phase B Reactive Power Offset
ADDR_PoffsetC       = 0x45    #R/W Phase C Active Power Offset
ADDR_QoffsetC       = 0x46    #R/W Phase C Reactive Power Offset
ADDR_GainA          = 0x47    #R/W Phase A calibration gain
ADDR_PhiA           = 0x48    #R/W Phase A calibration phase angle
ADDR_GainB          = 0x49    #R/W Phase B calibration gain
ADDR_PhiB           = 0x4A    #R/W Phase B calibration phase angle
ADDR_GainC          = 0x4B    #R/W Phase C calibration gain
ADDR_PhiC           = 0x4C    #R/W Phase C calibration phase angle
ADDR_CS1            = 0x4D    #R/W Checksum 1

# Fundamental/ Harmonic Energy Calibration registers
ADDR_HarmStart      = 0x50    #R/W Harmonic Calibration Startup Command
ADDR_PoffsetAF      = 0x51    #R/W Phase A Fundamental Active Power Offset
ADDR_PoffsetBF      = 0x52    #R/W Phase B Fundamental Active Power Offset
ADDR_PoffsetCF      = 0x53    #R/W Phase C Fundamental Active Power Offset
ADDR_PgainAF        = 0x54    #R/W Phase A Fundamental Active Power Gain
ADDR_PgainBF        = 0x55    #R/W Phase B Fundamental Active Power Gain
ADDR_PgainCF        = 0x56    #R/W Phase C Fundamental Active Power Gain
ADDR_CS2            = 0x57    #R/W Checksum 2

# Measurement Calibration
ADDR_AdjStart       = 0x60    #R/W Measurement Calibration Startup Command
ADDR_UgainA         = 0x61    #R/W Phase A Voltage RMS Gain
ADDR_IgainA         = 0x62    #R/W Phase A Current RMS Gain
ADDR_UoffsetA       = 0x63    #R/W Phase A Voltage RMS Offset
ADDR_IoffsetA       = 0x64    #R/W Phase A Current RMS Offset
ADDR_UgainB         = 0x65    #R/W Phase B Voltage RMS Gain
ADDR_IgainB         = 0x66    #R/W Phase B Current RMS Gain
ADDR_UoffsetB       = 0x67    #R/W Phase B Voltage RMS Offset
ADDR_IoffsetB       = 0x68    #R/W Phase B Current RMS Offset
ADDR_UgainC         = 0x69    #R/W Phase C Voltage RMS Gain
ADDR_IgainC         = 0x6A    #R/W Phase C Current RMS Gain
ADDR_UoffsetC       = 0x6B    #R/W Phase C Voltage RMS Offset
ADDR_IoffsetC       = 0x6C    #R/W Phase C Current RMS Offset
ADDR_IgainN         = 0x6D    #R/W Sampled N line Current RMS Gain
ADDR_IoffsetN       = 0x6E    #R/W Sampled N line Current RMS Offset
ADDR_CS3            = 0x6F    #R/W Checksum 3

# Energy Register
ADDR_APenergyT      = 0x80    #R/C Total Forward Active Energy
ADDR_APenergyA      = 0x81    #R/C Phase A Forward Active Energy
ADDR_APenergyB      = 0x82    #R/C Phase B Forward Active Energy
ADDR_APenergyC      = 0x83    #R/C Phase C Forward Active Energy
ADDR_ANenergyT      = 0x84    #R/C Total Reverse Active Energy
ADDR_ANenergyA      = 0x85    #R/C Phase A Reverse Active Energy
ADDR_ANenergyB      = 0x86    #R/C Phase B Reverse Active Energy
ADDR_ANenergyC      = 0x87    #R/C Phase C Reverse Active Energy
ADDR_RPenergyT      = 0x88    #R/C Total Forward Reactive Energy
ADDR_RPenergyA      = 0x89    #R/C Phase A Forward Reactive Energy
ADDR_RPenergyB      = 0x8A    #R/C Phase B Forward Reactive Energy
ADDR_RPenergyC      = 0x8B    #R/C Phase C Forward Reactive Energy
ADDR_RNenergyT      = 0x8C    #R/C Total Reverse Reactive Energy
ADDR_RNenergyA      = 0x8D    #R/C Phase A Reverse Reactive Energy
ADDR_RNenergyB      = 0x8E    #R/C Phase B Reverse Reactive Energy
ADDR_RNenergyC      = 0x8F    #R/C Phase C Reverse Reactive Energy
ADDR_SAenergyT      = 0x90    #R/C Total (Arithmetic Sum) Apparent Energy
ADDR_SenergyA       = 0x91    #R/C Phase A Apparent Energy
ADDR_SenergyB       = 0x92    #R/C Phase B Apparent Energy
ADDR_SenergyC       = 0x93    #R/C Phase C Apparent Energy
ADDR_SVenergyT      = 0x94    #R/C (Vector Sum) Total Apparent Energy
ADDR_EnStatus0      = 0x95    #R Metering Status 0
ADDR_EnStatus1      = 0x96    #R Metering Status 1
ADDR_SVmeanT        = 0x98    #R (Vector Sum) Total Apparent Power
ADDR_SVmeanTLSB     = 0x99    #R LSB of (Vector Sum) Total Apparent Power

# Fundamental / Harmonic Energy Register
ADDR_APenergyTF     = 0xA0    #R/C Total Forward Active Fundamental Energy
ADDR_APenergyAF     = 0xA1    #R/C Phase A Forward Active Fundamental Energy
ADDR_APenergyBF     = 0xA2    #R/C Phase B Forward Active Fundamental Energy
ADDR_APenergyCF     = 0xA3    #R/C Phase C Forward Active Fundamental Energy
ADDR_ANenergyTF     = 0xA4    #R/C Total Reverse Active Fundamental Energy
ADDR_ANenergyAF     = 0xA5    #R/C Phase A Reverse Active Fundamental Energy
ADDR_ANenergyBF     = 0xA6    #R/C Phase B Reverse Active Fundamental Energy
ADDR_ANenergyCF     = 0xA7    #R/C Phase C Reverse Active Fundamental Energy
ADDR_APenergyTH     = 0xA8    #R/C Total Forward Active Harmonic Energy
ADDR_APenergyAH     = 0xA9    #R/C Phase A Forward Active Harmonic Energy
ADDR_APenergyBH     = 0xAA    #R/C Phase B Forward Active Harmonic Energy
ADDR_APenergyCH     = 0xAB    #R/C Phase C Forward Active Harmonic Energy
ADDR_ANenergyTH     = 0xAC    #R/C Total Reverse Active Harmonic Energy
ADDR_ANenergyAH     = 0xAD    #R/C Phase A Reverse Active Harmonic Energy
ADDR_ANenergyBH     = 0xAE    #R/C Phase B Reverse Active Harmonic Energy
ADDR_ANenergyCH     = 0xAF    #R/C Phase C Reverse Active Harmonic Energy

# Power and Power Factor Registers
ADDR_PmeanT         = 0xB0    #R Total (all-phase-sum) Active Power
ADDR_PmeanA         = 0xB1    #R Phase A Active Power
ADDR_PmeanB         = 0xB2    #R Phase B Active Power
ADDR_PmeanC         = 0xB3    #R Phase C Active Power
ADDR_QmeanT         = 0xB4    #R Total (all-phase-sum) Reactive Power
ADDR_QmeanA         = 0xB5    #R Phase A Reactive Power
ADDR_QmeanB         = 0xB6    #R Phase B Reactive Power
ADDR_QmeanC         = 0xB7    #R Phase C Reactive Power
ADDR_SAmeanT        = 0xB8    #R Total (Arithmetic Sum) apparent power
ADDR_SmeanA         = 0xB9    #R phase A apparent power
ADDR_SmeanB         = 0xBA    #R phase B apparent power
ADDR_SmeanC         = 0xBB    #R phase C apparent power
ADDR_PFmeanT        = 0xBC    #R Total power factor
ADDR_PFmeanA        = 0xBD    #R phase A power factor
ADDR_PFmeanB        = 0xBE    #R phase B power factor
ADDR_PFmeanC        = 0xBF    #R phase C power factor
ADDR_PmeanTLSB      = 0xC0    #R Lower word of Total (all-phase-sum) Active Power
ADDR_PmeanALSB      = 0xC1    #R Lower word of Phase A Active Power
ADDR_PmeanBLSB      = 0xC2    #R Lower word of Phase B Active Power
ADDR_PmeanCLSB      = 0xC3    #R Lower word of Phase C Active Power
ADDR_QmeanTLSB      = 0xC4    #R Lower word of Total (all-phase-sum) Reactive Power
ADDR_QmeanALSB      = 0xC5    #R Lower word of Phase A Reactive Power
ADDR_QmeanBLSB      = 0xC6    #R Lower word of Phase B Reactive Power
ADDR_QmeanCLSB      = 0xC7    #R Lower word of Phase C Reactive Power
ADDR_SAmeanTLSB     = 0xC8    #R Lower word of Total (Arithmetic Sum) apparent power
ADDR_SmeanALSB      = 0xC9    #R Lower word of phase A apparent power
ADDR_SmeanBLSB      = 0xCA    #R Lower word of phase B apparent power
ADDR_SmeanCLSB      = 0xCB    #R Lower word of phase C apparent power

# Fundamental / Harmonic Power and Voltage / Current RMS Registers
ADDR_PmeanTF        = 0xD0    #R Total active fundamental power
ADDR_PmeanAF        = 0xD1    #R phase A active fundamental power
ADDR_PmeanBF        = 0xD2    #R phase B active fundamental power
ADDR_PmeanCF        = 0xD3    #R phase C active fundamental power
ADDR_PmeanTH        = 0xD4    #R Total active harmonic power
ADDR_PmeanAH        = 0xD5    #R phase A active harmonic power
ADDR_PmeanBH        = 0xD6    #R phase B active harmonic power
ADDR_PmeanCH        = 0xD7    #R phase C active harmonic power
ADDR_IrmsN1         = 0xD8    #R N Line Sampled current RMS
ADDR_UrmsA          = 0xD9    #R phase A voltage RMS
ADDR_UrmsB          = 0xDA    #R phase B voltage RMS
ADDR_UrmsC          = 0xDB    #R phase C voltage RMS
ADDR_IrmsN0         = 0xDC    #R N Line calculated current RMS
ADDR_IrmsA          = 0xDD    #R phase A current RMS
ADDR_IrmsB          = 0xDE    #R phase B current RMS
ADDR_IrmsC          = 0xDF    #R phase C current RMS
ADDR_PmeanTFLSB     = 0xE0    #R Lower word of Total active fundamental Power
ADDR_PmeanAFLSB     = 0xE1    #R Lower word of phase A active fundamental Power
ADDR_PmeanBFLSB     = 0xE2    #R Lower word of phase B active fundamental Power
ADDR_PmeanCFLSB     = 0xE3    #R Lower word of phase C active fundamental Power
ADDR_PmeanTHLSB     = 0xE4    #R Lower word of Total active harmonic Power
ADDR_PmeanAHLSB     = 0xE5    #R Lower word of phase A active harmonic Power
ADDR_PmeanBHLSB     = 0xE6    #R Lower word of phase B active harmonic Power
ADDR_PmeanCHLSB     = 0xE7    #R Lower word of phase C active harmonic Power
ADDR_UrmsALSB       = 0xE9    #R Lower word of phase A voltage RMS
ADDR_UrmsBLSB       = 0xEA    #R Lower word of phase B voltage RMS
ADDR_UrmsCLSB       = 0xEB    #R Lower word of phase C voltage RMS
ADDR_IrmsALSB       = 0xED    #R Lower word of phase A current RMS
ADDR_IrmsBLSB       = 0xEE    #R Lower word of phase B current RMS
ADDR_IrmsCLSB       = 0xEF    #R Lower word of phase C current RMS

# THD+N, Frequency, Angle and Temperature Registers
ADDR_THDNUA         = 0xF1    #R phase A voltage THD+N
ADDR_THDNUB         = 0xF2    #R phase B voltage THD+N
ADDR_THDNUC         = 0xF3    #R phase C voltage THD+N
ADDR_THDNIA         = 0xF5    #R phase A current THD+N
ADDR_THDNIB         = 0xF6    #R phase B current THD+N
ADDR_THDNIC         = 0xF7    #R phase C current THD+N
ADDR_Freq           = 0xF8    #R Frequency
ADDR_PangleA        = 0xF9    #R phase A mean phase angle
ADDR_PangleB        = 0xFA    #R phase B mean phase angle
ADDR_PangleC        = 0xFB    #R phase C mean phase angle
ADDR_Temp           = 0xFC    #R Measured temperature
ADDR_UangleA        = 0xFD    #R phase A voltage phase angle
ADDR_UangleB        = 0xFE    #R phase B voltage phase angle
ADDR_UangleC        = 0xFF    #R phase C voltage phase angle

# Harmonic Fourier Analysis Registers
# 100H ~ 1BFH R
# 1D0H ~ 1D1H R/W



# 01H SysStatus0
b_CS0Err            = 14
b_CS1Err            = 12
b_CS2Err            = 10
b_CS3Err            = 8
b_URevWn            = 7
b_IRevWn            = 6
b_SagWarn           = 3
b_PhaseLoseWn       = 2


# 02H SysStatus1
b_INOv1             = 15
b_INOv0             = 14
b_THDUOv            = 11
b_THDIOv            = 10
b_DFTDone           = 9
b_ReqQchgT          = 7
b_ReqQchgA          = 6
b_ReqQchgB          = 5
b_ReqQchgC          = 4
b_ReqPchgT          = 3
b_ReqPchgA          = 2
b_ReqPchgB          = 1
b_ReqPchgC          = 0


# 03H FuncEn0
b_CS2ErrEn          = 10
b_URevWnEn          = 7
b_IRevWnEn          = 6
b_SagWnEn           = 3
b_PhaseLoseWnRn     = 2


# 04H FuncEn1
b_INOv1En           = 15
b_INOv0En           = 14
b_THDUOvEn          = 11
b_THDIOvEn          = 10
b_DFTDone           = 9
b_ReqQchgTEn        = 7
b_ReqQchgAEn        = 6
b_ReqQchgBEn        = 5
b_ReqQchgCEn        = 4
b_ReqPchgTEn        = 3
b_ReqPchgAEn        = 2
b_ReqPchgBEn        = 1
b_ReqPchgCEn        = 0


"""
# 07H ZXConfig
b_ZX2Src            = 13
b_ZX1Src            = 10
b_ZX0Src            = 7
    v_ZXSrc_Ua          = 0x00
    v_ZXSrc_Ub          = 0x01
    v_ZXSrc_Uc          = 0x02
    v_ZXSrc_0_3         = 0x03
    v_ZXSrc_Ia          = 0x04
    v_ZXSrc_Ib          = 0x05
    v_ZXSrc_Ic          = 0x06
    v_ZXSrc_0_7         = 0x07
b_ZX2Con            = 5
b_ZX1Con            = 3
b_ZX0Con            = 1
    v_ZXCon_pos_zc      = 0x00
    v_ZXCon_neg_zc      = 0x01
    v_ZXCon_all_zc      = 0x02
    v_ZXCon_no_zc       = 0x03
b_ZXdis             = 0
    v_ZXdis_enable      = 0x00
    v_ZXdis_disable     = 0x01


# 11H DetectTh1
b_CalCode1N         = 8
b_CalCode1P         = 0


# 12H DetectTh2
b_CalCode2N         = 8
b_CalCode2P         = 0


# 13H DetectTh3
b_CalCode3N         = 8
b_CalCode3P         = 0
"""







# MMode0
b_I1I3Swap          = 13
b_Freq60Hz          = 12
b_HPFOff            = 11
b_didtEn            = 10
b_001LSB            = 9
b_3P3W              = 8
b_CF2varh           = 7
b_CF2ESV            = 6
b_ABSEnQ            = 4
b_ABSEnP            = 3
b_EnPA              = 2
b_EnPB              = 1
b_EnPC              = 0

#MMode1
b_DPGA_GAIN         = 14
v_DPGA_GAIN_1       = 0x00
v_DPGA_GAIN_2       = 0x01
v_DPGA_GAIN_4       = 0x02
v_DPGA_GAIN_8       = 0x03
b_PGA_GAIN_I1       = 0
b_PGA_GAIN_I2       = 0
b_PGA_GAIN_I3       = 0
b_PGA_GAIN_I4       = 0
b_PGA_GAIN_V1       = 0
b_PGA_GAIN_V2       = 0
b_PGA_GAIN_V3       = 0
v_PGA_GAIN_1        = 0x00
v_PGA_GAIN_2        = 0x01
v_PGA_GAIN_4        = 0x02
    


START_COM_INIT      = 0x6886
START_COM_EDIT      = 0x5678
START_COM_EXEC      = 0x8765



def lo_byte(word):
    return (word & 0xFF)


def hi_byte(word):
    return ((word >> 8) & 0xFF)






class M90E36A(object):

    def __init__ (self, port=2, dev=0, irq=None, gpio=None):
        self._irq = irq
        self._spi = SPI.SpiDev(port, dev, max_speed_hz=100000)
        self._gpio = gpio
        if self._gpio is None:
            self._gpio = GPIO.get_platform_gpio()
        # Set interrupt as input
        if irq is not None:
            self._gpio.setup(irq, GPIO.IN)
        # Set SPI to mode 0, MSB first
        self._spi.set_mode(0)
        self._spi.set_bit_order(SPI.MSBFIRST)
        self._spi.set_clock_hz(100000)

        self.soft_reset()
        self.configuration_registers_init()        



    def getIRQ(self):
        irq = 0
        if (self._gpio.is_low(self._irq)):
            irq = 1
        return irq


    def write_word(self, addr, word):
        msg = [hi_byte(addr) & 0x7F]
        msg.append(lo_byte(addr))
        msg.append(hi_byte(word))
        msg.append(lo_byte(word))
        self._spi.transfer(msg)
        return


    def read_word(self, addr):
        msg = [hi_byte(addr) | 0x80]
        msg.append(lo_byte(addr))
        msg.append(0)
        msg.append(0)
        ans = bytearray()
        ans = self._spi.transfer(msg)
        return (ans[2] * 0x100 + ans[3])


    def calc_checksum(self, arr, count):
        h = 0
        l = 0
        for n in xrange(0, count):
            l = l + ((arr[n] >> 8) & 0xFF) + (arr[n] & 0xFF)
            h = h ^ ((arr[n] >> 8) & 0xFF) ^ (arr[n] & 0xFF)
        l %= 0x100
        return ((h << 8) | l)









#-------------------------------------------------------------------------------
# Energy register LSB configuration for all energy registers
#-------------------------------------------------------------------------------
# 33H MMode0
#-------------------------------------------------------------------------------
    def get_cf_conf(self):
        if ((self.read_word(ADDR_MMode0) & (1<<b_001LSB)) == 0):
            x = 0.1
        else:
            x = 0.01
        return x



#-------------------------------------------------------------------------------
# Software Reset
#-------------------------------------------------------------------------------
# 00H SoftReset
#-------------------------------------------------------------------------------
    def soft_reset(self):
        self.write_word(ADDR_SoftReset, 0x789A)
    


















#-------------------------------------------------------------------------------
# Configuration Registers
#-------------------------------------------------------------------------------
# Addr  Register    Type    Functional Description                  Power-on Value
# 30H   ConfigStart R/W     Calibration Start Command               6886H
# 31H   PLconstH    R/W     High Word of PL_Constant                0861H
# 32H   PLconstL    R/W     Low Word of PL_Constant                 C468H
# 33H   MMode0      R/W     HPF/Integrator On/off, CF and all-phase
#                           energy computation configuration        0087H
# 34H   MMode1      R/W     PGA gain configuration                  0000H
# 35H   PstartTh    R/W     Active Startup Power Threshold          0000H
#                               16 bit unsigned integer,
#                               Unit: 0.00032 Watt              
# 36H   QstartTh    R/W     Reactive Startup Power Threshold        0000H
#                               16 bit unsigned integer,
#                               Unit: 0.00032 var       
# 37H   SstartTh    R/W     Apparent Startup Power Threshold        0000H
#                               16 bit unsigned integer,
#                               Unit: 0.00032 VA            
# 38H   PphaseTh    R/W     Startup power threshold (for |P|+|Q| of
#                           a phase) for any phase participating
#                           Active E nergy Accumulation. Common for
#                           phase A/ B/C.                           0000H
#                               16 bit unsigned integer,
#                               Unit: 0.00032 Watt/var
# 39H   QphaseTh    R/W     Startup power threshold (for |P|+|Q| of
#                           a phase) for any phase participating
#                           ReActive Energy Accumulation. Common
#                           for phase A/B/C.                        0000H
#                               16bit unsigned integer,
#                               Unit: 0.00032 Watt/var
# 3AH   SphaseTh    RW      Startup power threshold (for |P|+|Q| of
#                           a phase) for any phase participating
#                           Apparent Energy Accumulation. Common
#                           for phase A/B/C.                        0000H
#                               16 bit unsigned integer,
#                               Unit: 0.00032 Watt/var
# 3BH   CS0         R/W     Checksum 0                              421CH
#-------------------------------------------------------------------------------
    def configuration_registers(self, arr):
        # Phase A
        # Checksum
        self.write_word(ADDR_CS0, self.calc_checksum(arr, 10))
#-------------------------------------------------------------------------------
# Configuration Registers Read Checksum
#-------------------------------------------------------------------------------
    def configuration_registers_r_cs(self):
        return self.read_word(ADDR_CS0)
#-------------------------------------------------------------------------------
# Configuration Registers Read StartCommand
#-------------------------------------------------------------------------------
    def configuration_registers_r_sc(self):
        return self.read_word(ADDR_ConfigStart)
#-------------------------------------------------------------------------------
# Configuration Registers Read StartCommand
#-------------------------------------------------------------------------------
    def configuration_registers_init(self):
        self.write_word(ADDR_ConfigStart, START_COM_EDIT)
        self.write_word(ADDR_MMode1,0b0000000001010101)
        arr = []
        for addr in xrange(ADDR_ConfigStart+1, ADDR_CS0):
            arr.append(self.read_word(addr))
        cs = self.calc_checksum(arr, 10)
        self.write_word(ADDR_CS0, cs)
        self.write_word(ADDR_ConfigStart, START_COM_EXEC)
#        print(arr)
#        print(cs)
#        print(self.read_word(ADDR_CS0))
       


#-------------------------------------------------------------------------------
# Fundamental/Harmonic Energy Calibration
#-------------------------------------------------------------------------------
# Addr  Register    Type    Functional Description                  Power-on Value
# 40H   CalStart    R/W     Calibration Start Command               6886H
# 41H   PoffsetA    R/W     Phase A Active Power Offset             0000H
# 42H   QoffsetA    R/W     Phase A Reactive Power Offset           0000H
# 43H   PoffsetB    R/W     Phase B Active Power Offset             0000H
# 44H   QoffsetB    R/W     Phase B Reactive Power Offset           0000H
# 45H   PoffsetC    R/W     Phase C Active Power Offset             0000H
# 46H   QoffsetC    R/W     Phase C Reactive Power Offset           0000H
# 47H   GainA       R/W     Phase A Act/React Energy calibr. gain   0000H
# 48H   PhiA        R/W     Phase A calibration phase angle         0000H
# 49H   GainB       R/W     Phase B Act/React Energy calibr. gain   0000H
# 4AH   PhiB        R/W     Phase B calibration phase angle         0000H
# 4BH   GainC       R/W     Phase C Act/React Energy calibr. gain   0000H
# 4CH   PhiC        R/W     Phase C calibration phase angle         0000H
# 4DH   CS1         R/W     Checksum 1                              0000H
# Poffset*, Poffset* - Signed 16-bit integer
# Gain* - Signed integer. Actual power gain = (1+ Gain)
# Phi* -
#   Bit     Name            Description
#   15      DelayV          0: Delay Cycles are applied to current channel. (default)
#                           1: Delay Cycles are applied to voltage channel.
#   14:10                   Reserved.
#   9:0     DelayCycles     Unit is 2.048MHz cycle. It is an unsigned 10 bit integer.
#-------------------------------------------------------------------------------
    def calibration_energy(self, arr):
        # Phase A
        self.write_word(ADDR_PoffsetA,   arr[1])     # Active Power Offset 
        self.write_word(ADDR_QoffsetA,   arr[2])     # Reactive Power Offset 
        self.write_word(ADDR_GainA,      arr[7])     # Active/Reactive Energy calibration gain
        self.write_word(ADDR_PhiA,       arr[8])     # Calibration phase angle 
        # Phase B
        self.write_word(ADDR_PoffsetB,   arr[3])     # Active Power Offset 
        self.write_word(ADDR_QoffsetB,   arr[4])     # Reactive Power Offset
        self.write_word(ADDR_GainB,      arr[9])     # Active/Reactive Energy calibration gain 
        self.write_word(ADDR_PhiB,       arr[10])    # Calibration phase angle 
        # Phase C
        self.write_word(ADDR_PoffsetC,   arr[4])     # Active Power Offset 
        self.write_word(ADDR_QoffsetC,   arr[5])     # Reactive Power Offset
        self.write_word(ADDR_GainC,      arr[11])    # Active/Reactive Energy calibration gain 
        self.write_word(ADDR_PhiC,       arr[12])    # Calibration phase angle 
        # Checksum
        self.write_word(ADDR_CS1, self.calc_checksum(arr, 12))
#-------------------------------------------------------------------------------
# Energy Calibration Read Checksum
#-------------------------------------------------------------------------------
    def calibration_energy_r_cs(self):
        return self.read_word(ADDR_CS1)
#-------------------------------------------------------------------------------
# Energy Calibration Read Start Command
#-------------------------------------------------------------------------------
    def calibration_energy_r_sc(self):
        return self.read_word(ADDR_CalStart)



#-------------------------------------------------------------------------------
# Fundamental/Harmonic Energy Calibration
#-------------------------------------------------------------------------------
# Addr  Register    Type    Functional Description                  Power-on Value
# 50H   HarmStart   R/W     Harmonic Calibration Startup Command    6886H
# 51H   PoffsetAF   R/W     Phase A Fundamental Active Power Offset 0000H
# 52H   PoffsetBF   R/W     Phase B Fundamental Active Power Offset 0000H
# 53H   PoffsetCF   R/W     Phase C Fundamental Active Power Offset 0000H
# 54H   PgainAF     R/W     Phase A Fundamental Active Power Gain   0000H
# 55H   PgainBF     R/W     Phase B Fundamental Active Power Gain   0000H
# 56H   PgainCF     R/W     Phase C Fundamental Active Power Gain   0000H
# 57H   CS2         R/W     Checksum 2                              0000H
#-------------------------------------------------------------------------------
    def calibration_energy_fh(self, arr):
        # Phase A
        self.write_word(ADDR_PoffsetAF,      arr[1])     # Fundamental Active Power Offset
        self.write_word(ADDR_PgainAF,        arr[4])     # Fundamental Active Power Gain             
        # Phase B
        self.write_word(ADDR_PoffsetBF,      arr[2])     # Fundamental Active Power Offset
        self.write_word(ADDR_PgainBF,        arr[5])     # Fundamental Active Power Gain             
        # Phase C
        self.write_word(ADDR_PoffsetCF,      arr[3])     # Fundamental Active Power Offset
        self.write_word(ADDR_PgainCF,        arr[6])     # Fundamental Active Power Gain             
        # Checksum
        self.write_word(ADDR_CS2, self.calc_checksum(arr, 6))
#-------------------------------------------------------------------------------
# Fundamental/Harmonic Energy Calibration Read Checksum
#-------------------------------------------------------------------------------
    def calibration_energy_fh_r_cs(self):
        return self.read_word(ADDR_CS2)
#-------------------------------------------------------------------------------
# Fundamental/Harmonic Energy Calibration Read Start Command
#-------------------------------------------------------------------------------
    def calibration_energy_fh_r_sc(self):
        return self.read_word(ADDR_HarmStart)



#-------------------------------------------------------------------------------
# Measurement Calibration
#-------------------------------------------------------------------------------
# Addr  Register    Type    Functional Description                  Power-on Value
# 60H   AdjStart    R/W     Measurement Calibration Startup Command 6886H
# 61H   UgainA      R/W     Phase A Voltage RMS Gain                CE40H
# 62H   IgainA      R/W     Phase A Current RMS Gain                7530H
# 63H   UoffsetA    R/W     Phase A Voltage RMS Offset              0000H
# 64H   IoffsetA    R/W     Phase A Current RMS Offset              0000H
# 65H   UgainB      R/W     Phase B Voltage RMS Gain                CE40H
# 66H   IgainB      R/W     Phase B Current RMS Gain                7530H
# 67H   UoffsetB    R/W     Phase B Voltage RMS Offset              0000H
# 68H   IoffsetB    R/W     Phase B Current RMS Offset              0000H
# 69H   UgainC      R/W     Phase C Voltage RMS Gain                CE40H
# 6AH   IgainC      R/W     Phase C Current RMS Gain                7530H
# 6BH   UoffsetC    R/W     Phase C Voltage RMS Offset              0000H
# 6CH   IoffsetC    R/W     Phase C Current RMS Offset              0000H
# 6DH   IgainN      R/W     Sampled N line Current RMS Gain         7530H
# 6EH   IoffsetN    R/W     Sampled N line Current RMS Offset       0000H
# 6FH   CS3         R/W     Checksum 3                              8EBEH
# 0xCE40 = 52800
# 0x7530 = 30000
#-------------------------------------------------------------------------------
    def calibration_meter(self, arr):
        # Phase A
        self.write_word(ADDR_UgainA,     arr[1])     # Voltage RMS Gain
        self.write_word(ADDR_IgainA,     arr[2])     # Current RMS Gain             
        self.write_word(ADDR_UoffsetA,   arr[3])     # Voltage RMS Offset
        self.write_word(ADDR_IoffsetA,   arr[4])     # Current RMS Offset
        # Phase B
        self.write_word(ADDR_UgainB,     arr[5])     # Voltage RMS Gain
        self.write_word(ADDR_IgainB,     arr[6])     # Current RMS Gain             
        self.write_word(ADDR_UoffsetB,   arr[7])     # Voltage RMS Offset
        self.write_word(ADDR_IoffsetB,   arr[8])     # Current RMS Offset
        # Phase C
        self.write_word(ADDR_UgainC,     arr[9])     # Voltage RMS Gain
        self.write_word(ADDR_IgainC,     arr[10])    # Current RMS Gain             
        self.write_word(ADDR_UoffsetC,   arr[11])    # Voltage RMS Offset
        self.write_word(ADDR_IoffsetC,   arr[12])    # Current RMS Offset
        # Sampled N Line
        self.write_word(ADDR_IgainN,     arr[13])    # Voltage RMS Gain
        self.write_word(ADDR_IoffsetN,   arr[14])    # Voltage RMS Offset
        # Checksum
        self.self.write_word(ADDR_CS3, self.calc_checksum(arr, 14))
#-------------------------------------------------------------------------------
# Measurement Calibration Read Checksum
#-------------------------------------------------------------------------------
    def calibration_meter_r_cs(self):
        return self.read_word(ADDR_CS3)
#-------------------------------------------------------------------------------
# Measurement Calibration Read Start Command
#-------------------------------------------------------------------------------
    def calibration_meter_r_sc(self):
        return self.read_word(ADDR_AdjStart)



#-------------------------------------------------------------------------------
# Metering Status 0 and 1
#-------------------------------------------------------------------------------
# 95H EnStatus0
# Type: Read
# Default Value: F000H
# Bit   Name            Description
# 15    TQNoload        all-phase-sum reactive power no-load condition detected.
# 14    TPNoload        all-phase-sum active power no-load condition detected.
# 13    TASNoload       all-phase-sum apparent power no-load condition detected.
# 12    TVSNoload       all-phase-sum vectored sum apparent active power no-load condition detected.
# 11-4                  Reserved.
# 3     CF4RevFlag      CF4/CF3/CF2/CF1 Forward/Reverse Flag – reflect the direction of the current CF pulse.
# 2     CF3RevFlag          0: Forward (default)
# 1     CF2RevFlag          1: Reverse
# 0     CF1RevFlag
#-------------------------------------------------------------------------------
# 96H EnStatus1
# Type: Read
# Default Value: 0000H
# Bit   Name            Description
# 15-7                  Reserved.
# 6     SagPhaseA       These bits indicate whether there is voltage sag on phase A, B or C respectively.
# 5     SagPhaseB           0: no voltage sag (default)
# 4     SagPhaseC           1: voltage sag
# 3                     Reserved.
# 2     PhaseLossA      These bits indicate whether there is a phase loss in Phase A/B/C.
# 1     PhaseLossB          0: no phase loss (default)
# 0     PhaseLossC          1: phase loss.
#-------------------------------------------------------------------------------
    def meter_status(self):
        s0 = self.read_word(ADDR_EnStatus0)
        s1 = self.read_word(ADDR_EnStatus0)
        return (s0, s1)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Forward Active Energy
#-------------------------------------------------------------------------------
# 80H-83H APenergyT, APenergyA, APenergyB, APenergyC
# Type: Read/Clear
# Resolution is 0.1CF/0.01CF.
# 0.01CF/0.1CF setting is defined by the 001LSB bit (b9, MMode0).
# Cleared after read.
#-------------------------------------------------------------------------------
    def meter_e_fa(self):
        x = get_cf_conf()
        a = self.read_word(ADDR_APenergyA)*x
        b = self.read_word(ADDR_APenergyB)*x
        c = self.read_word(ADDR_APenergyC)*x 
        t = self.read_word(ADDR_APenergyT)*x      # Total
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Reverse Active Energy
#-------------------------------------------------------------------------------
# 84H-87H ANenergyT, ANenergyA, ANenergyB, ANenergyC
# Type: Read/Clear
# Resolution is 0.1CF/0.01CF.
# 0.01CF/0.1CF setting is defined by the 001LSB bit (b9, MMode0).
# Cleared after read.
#-------------------------------------------------------------------------------
    def meter_e_ra(self):
        x = get_cf_conf()
        a = self.read_word(ADDR_ANenergyA)*x
        b = self.read_word(ADDR_ANenergyB)*x
        c = self.read_word(ADDR_ANenergyC)*x 
        t = self.read_word(ADDR_ANenergyT)*x     # Total
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Forward Reactive Energy
#-------------------------------------------------------------------------------
# 88H-8BH RPenergyT, RPenergyA, RPenergyB, RPenergyC
# Type: Read/Clear
# Resolution is 0.1CF/0.01CF.
# 0.01CF/0.1CF setting is defined by the 001LSB bit (b9, MMode0).
# Cleared after read.
#-------------------------------------------------------------------------------
    def meter_e_fr(self):
        x = get_cf_conf()
        a = self.read_word(ADDR_RPenergyA)*x
        b = self.read_word(ADDR_RPenergyB)*x
        c = self.read_word(ADDR_RPenergyC)*x 
        t = self.read_word(ADDR_RPenergyT)*x     # Total
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Reverse Reactive Energy
#-------------------------------------------------------------------------------
# 8CH-8FH RNenergyT, RNenergyA, RNenergyB, RNenergyC
# Type: Read/Clear
# Resolution is 0.1CF/0.01CF.
# 0.01CF/0.1CF setting is defined by the 001LSB bit (b9, MMode0).
# Cleared after read.
#-------------------------------------------------------------------------------
    def meter_e_rr(self):
        x = get_cf_conf()
        a = self.read_word(ADDR_RNenergyA)*x
        b = self.read_word(ADDR_RNenergyB)*x
        c = self.read_word(ADDR_RNenergyC)*x 
        t = self.read_word(ADDR_RNenergyT)*x     # Total
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Apparent Energy
#-------------------------------------------------------------------------------
# 90H-94H SAenergyT, SenergyA, SenergyB, SenergyC, SVenergyT
# Type: Read/Clear
# Resolution is 0.1CF/0.01CF.
# 0.01CF/0.1CF setting is defined by the 001LSB bit (b9, MMode0).
# Cleared after read.
#-------------------------------------------------------------------------------
    def meter_e_a(self):
        x = get_cf_conf()
        a = self.read_word(ADDR_SenergyA)*x
        b = self.read_word(ADDR_SenergyB)*x
        c = self.read_word(ADDR_SenergyC)*x 
        ta = self.read_word(ADDR_SAenergyT)*x    # Total (Arithmetic Sum) 
        tv = self.read_word(ADDR_SVenergyT)*x    # Total (Vector Sum)
        return (a, b, c, ta, tv)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Forward Active Fundamental Energy
#-------------------------------------------------------------------------------
# A0H-A3H APenergyTF, APenergyAF, APenergyBF, APenergyCF
# Type: Read/Clear
# Resolution is 0.1CF/0.01CF.
# 0.01CF/0.1CF setting is defined by the 001LSB bit (b9, MMode0).
# Cleared after read.
#-------------------------------------------------------------------------------
    def meter_e_faf(self):
        x = get_cf_conf()
        a = self.read_word(ADDR_APenergyAF)*x
        b = self.read_word(ADDR_APenergyBF)*x
        c = self.read_word(ADDR_APenergyCF)*x 
        t = self.read_word(ADDR_APenergyTF)*x    # Total
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Reverse Active Fundamental Energy
#-------------------------------------------------------------------------------
# A4H-A7H ANenergyTF, ANenergyAF, ANenergyBF, ANenergyCF
# Type: Read/Clear
# Resolution is 0.1CF/0.01CF.
# 0.01CF/0.1CF setting is defined by the 001LSB bit (b9, MMode0).
# Cleared after read.
#-------------------------------------------------------------------------------
    def meter_e_raf(self):
        x = get_cf_conf()
        a = self.read_word(ADDR_ANenergyAF)*x
        b = self.read_word(ADDR_ANenergyBF)*x
        c = self.read_word(ADDR_ANenergyCF)*x 
        t = self.read_word(ADDR_ANenergyTF)*x    # Total
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Forward Active Harmonic Energy
#-------------------------------------------------------------------------------
# A8H-ABH APenergyTH, APenergyAH, APenergyBH, APenergyCH
# Type: Read/Clear
# Resolution is 0.1CF/0.01CF.
# 0.01CF/0.1CF setting is defined by the 001LSB bit (b9, MMode0).
# Cleared after read.
#-------------------------------------------------------------------------------
    def meter_e_fah(self):
        x = get_cf_conf()
        a = self.read_word(ADDR_APenergyAH)*x
        b = self.read_word(ADDR_APenergyBH)*x
        c = self.read_word(ADDR_APenergyCH)*x 
        t = self.read_word(ADDR_APenergyTH)*x    # Total
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Reverse Active Harmonic Energy
#-------------------------------------------------------------------------------
# ACH-AFH ANenergyTH, ANenergyAH, ANenergyBH, ANenergyCH
# Type: Read/Clear
# Resolution is 0.1CF/0.01CF.
# 0.01CF/0.1CF setting is defined by the 001LSB bit (b9, MMode0).
# Cleared after read.
#-------------------------------------------------------------------------------
    def meter_e_rah(self):
        x = get_cf_conf()
        a = self.read_word(ADDR_ANenergyAH)*x
        b = self.read_word(ADDR_ANenergyBH)*x
        c = self.read_word(ADDR_ANenergyCH)*x 
        t = self.read_word(ADDR_ANenergyTH)*x    # Total
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Active Power
#-------------------------------------------------------------------------------
# B0H-B3H PmeanT, PmeanA, PmeanB, PmeanC
# C0H-C3H PmeanTLBS, PmeanALBS, PmeanBLBS, PmeanCLBS
# Type: Read
# Pmean* - Complement, MSB as the sign bit XX.XXX kW
#   1LSB corresponds to
#       1 Watt for phase A/B/C
#       4 Watt for Total (all-phase-sum)
# Pmean*LBS - Lower word of Active Powers.
#   1LLSB corresponds to
#       1/256 Watt for phase A/B/C
#       4/256 Watt for Total (all-phase-sum)
#   All the lower 8 bits of this register is always zero.
#   Only the higher 8 bits of these registers are valid.
#   In this document, LLSB means bit 8 of the lower register
#-------------------------------------------------------------------------------
    def meter_p_a(self):
        a = float(self.read_word(ADDR_PmeanA))      # ADDR_PmeanALSB not use
        b = float(self.read_word(ADDR_PmeanB))      # ADDR_PmeanBLSB not use
        c = float(self.read_word(ADDR_PmeanC))      # ADDR_PmeanCLSB not use
        t = float(self.read_word(ADDR_PmeanT))*4    # Total (all-phase-sum)     # ADDR_PmeanTLSB not use  
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Reactive Power
#-------------------------------------------------------------------------------
# B4H-B7H QmeanT, QmeanA, QmeanB, QmeanC
# C4H-C7H QmeanTLBS, QmeanALBS, QmeanBLBS, QmeanCLBS
# Type: Read
# Qmean* - Complement, MSB as the sign bit XX.XXX kvar
#   1LSB corresponds to
#       1 var for phase A/B/C
#       4 var for Total (all-phase-sum)
# Qmean*LBS - Lower word of Active Powers.
#   1LLSB corresponds to
#       1/256 var for phase A/B/C
#       4/256 var for Total (all-phase-sum)
#   All the lower 8 bits of this register is always zero.
#   Only the higher 8 bits of these registers are valid.
#   In this document, LLSB means bit 8 of the lower register
#-------------------------------------------------------------------------------
    def meter_p_ra(self):
        a = float(self.read_word(ADDR_QmeanA))      # ADDR_QmeanALSB not use
        b = float(self.read_word(ADDR_QmeanB))      # ADDR_QmeanBLSB not use
        c = float(self.read_word(ADDR_QmeanC))      # ADDR_QmeanCLSB not use 
        t = float(self.read_word(ADDR_QmeanT))*4    # Total (all-phase-sum)     # ADDR_QmeanTLSB not use     
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Apparent Power
#-------------------------------------------------------------------------------
# B8H-BBH SAmeanT, SmeanA, SmeanB, SmeanC
# C8H-CBH SAmeanTLBS, SmeanALBS, SmeanBLBS, SmeanCLBS
# Type: Read
# SAmean*, Smean - Complement, MSB is always '0'; XX.XXX kVA
#   1LSB corresponds to
#       1 var for phase A/B/C
#       4 var for Total (all-phase-sum)
# SAmean*LBS, Smean*LBS - Lower word of Active Powers.
#   1LLSB corresponds to
#       1/256 VA for phase A/B/C
#       4/256 VA for Total (all-phase-sum)
#   All the lower 8 bits of this register is always zero.
#   Only the higher 8 bits of these registers are valid.
#   In this document, LLSB means bit 8 of the lower register
#-------------------------------------------------------------------------------
# 98H-99H ADDR_SVmeanT, ADDR_SVmeanTLSB 
# Type: Read
# SVmeanT - Complement, MSB is always '0'; XX.XXX kVA
# SVmeanTLSB - LSB of SVmeanT. Unit/LSB is 4/65536 VA
#-------------------------------------------------------------------------------
    def meter_p_ap(self):
        a = float(self.read_word(ADDR_SmeanA))      # ADDR_SmeanALSB not use
        b = float(self.read_word(ADDR_SmeanB))      # ADDR_SmeanBLSB not use
        c = float(self.read_word(ADDR_SmeanC))      # ADDR_SmeanCLSB not use
        ta = float(self.read_word(ADDR_SAmeanT))*4  # Total (Arithmetic Sum)    # ADDR_SAmeanTLSB not use    
        tv = float(self.read_word(ADDR_SVmeanT))*4  # Total (Vector Sum)        # ADDR_SVmeanTLSB not use  
        return (a, b, c, ta, tv)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Total Power Factor
#-------------------------------------------------------------------------------
# BCH-BFH PFmeanT, PFmeanA, PFmeanB, PFmeanC
# Type: Read
# PFmean* - Complement, MSB as the sign bit, 1LSB is 0.001; X.XXX
#   Range from -1.000 to +1.000
#-------------------------------------------------------------------------------
    def meter_tpf(self):
        a = float(self.read_word(ADDR_PFmeanA)) / 1000
        b = float(self.read_word(ADDR_PFmeanB)) / 1000
        c = float(self.read_word(ADDR_PFmeanC)) / 1000
        t = float(self.read_word(ADDR_PFmeanT)) / 1000      # Total  
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Active Fundamental Power
#-------------------------------------------------------------------------------
# D0H-E3H PmeanTF, PmeanAF, PmeanBF, PmeanCF
# E0H-E3H PmeanTFLBS, PmeanAFLBS, PmeanBFLBS, PmeanCFLBS
# Type: Read
# Pmean*F - Complement, 16-bit integer with unit of 1 Watt or 4 Watt.
#   1LSB corresponds to
#       1 Watt for phase A/B/C
#       4 Watt for Total (all-phase-sum)
# Pmean*FLBS - Lower word of Active Powers.
#   1LLSB corresponds to
#       1/256 Watt for phase A/B/C
#       4/256 Watt for Total (all-phase-sum)
#   All the lower 8 bits of this register is always zero.
#   Only the higher 8 bits of these registers are valid.
#   In this document, LLSB means bit 8 of the lower register
#-------------------------------------------------------------------------------
    def meter_p_af(self):
        a = float(self.read_word(ADDR_PmeanAF))     # ADDR_PmeanAFLBS not use
        b = float(self.read_word(ADDR_PmeanBF))     # ADDR_PmeanBFLBS not use
        c = float(self.read_word(ADDR_PmeanCF))     # ADDR_PmeanCFLBS not use 
        t = float(self.read_word(ADDR_PmeanTF))*4   # Total     # ADDR_PmeanTFLBS not use
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Active Harmonic Power
#-------------------------------------------------------------------------------
# D4H-E7H PmeanTH, PmeanAH, PmeanBH, PmeanCH
# E4H-E7H PmeanTHLBS, PmeanAHLBS, PmeanBFHBS, PmeanCHLBS
# Type: Read
# Pmean*H - Complement, 16-bit integer with unit of 1 Watt or 4 Watt.
#   1LSB corresponds to
#       1 Watt for phase A/B/C
#       4 Watt for Total (all-phase-sum)
# Pmean*HLBS - Lower word of Active Powers.
#   1LLSB corresponds to
#       1/256 Watt for phase A/B/C
#       4/256 Watt for Total (all-phase-sum)
#   All the lower 8 bits of this register is always zero.
#   Only the higher 8 bits of these registers are valid.
#   In this document, LLSB means bit 8 of the lower register
#-------------------------------------------------------------------------------
    def meter_p_ah(self):
        a = float(self.read_word(ADDR_PmeanAH))     # ADDR_PmeanAHLBS not use
        b = float(self.read_word(ADDR_PmeanBH))     # ADDR_PmeanBHLBS not use
        c = float(self.read_word(ADDR_PmeanCH))     # ADDR_PmeanCHLBS not use
        t = float(self.read_word(ADDR_PmeanTH))*4   # Total     # ADDR_PmeanTHLBS not use
        return (a, b, c, t)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Voltage RMS
#-------------------------------------------------------------------------------
# D9H-DBH UrmsA, UrmsB, UrmsC
# E9H-EBH UrmsALBS, UrmsBLBS, UrmsCLBS
# Type: Read
# Urms*
#   1LSB corresponds to 0.01 V
# Urms*LBS
#   Lower word of registers 
#   1LLSB corresponds to 0.01/256 V
#   All the lower 8 bits of this register is always zero.
#   Only the higher 8 bits of these registers are valid.
#   In this document, LLSB means bit 8 of the lower register
#-------------------------------------------------------------------------------
    def meter_u_rms(self):
        a = float(self.read_word(ADDR_UrmsA)) / 100      # ADDR_UrmsALBS not use
        b = float(self.read_word(ADDR_UrmsB)) / 100      # ADDR_UrmsBLBS not use
        c = float(self.read_word(ADDR_UrmsC)) / 100      # ADDR_UrmsCLBS not use
        return (a, b, c)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Current RMS
#-------------------------------------------------------------------------------
# D8H IrmsN1 - N Line Sampled current RMS
# Type: Read
#-------------------------------------------------------------------------------
# DCH IrmsN0 - N Line Calculated current RMS
# Type: Read
#-------------------------------------------------------------------------------
# DDH-DFH IrmsA, IrmsB, IrmsC
# Type: Read
# Irms* - Unsigned 16-bit integer with unit of 0.001A
#   1LSB corresponds to 0.001 A
# Irms*LBS
#   Lower word of registers 
#   1LLSB corresponds to 0.001/256 A
#   All the lower 8 bits of this register is always zero.
#   Only the higher 8 bits of these registers are valid.
#   In this document, LLSB means bit 8 of the lower register
#-------------------------------------------------------------------------------
    def meter_i_rms(self):
        a = float(self.read_word(ADDR_IrmsA)) / 1000       # ADDR_IrmsALBS not use
        b = float(self.read_word(ADDR_IrmsB)) / 1000      # ADDR_IrmsBLBS not use
        c = float(self.read_word(ADDR_IrmsC)) / 1000      # ADDR_IrmsCLBS not use
        n = float(self.read_word(ADDR_IrmsN1)) / 1000
        nc = float(self.read_word(ADDR_IrmsN0)) / 1000    
        return (a, b, c, n, nc)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Voltage THD+N
#-------------------------------------------------------------------------------
# F1H-F3H THDNUA, THDNUB, THDNUC
# Type: Read
#   1LSB corresponds to 0.01 %
#-------------------------------------------------------------------------------
    def meter_u_thdn(self):
        a = float(self.read_word(ADDR_THDNUA)) / 100
        b = float(self.read_word(ADDR_THDNUB)) / 100
        c = float(self.read_word(ADDR_THDNUC)) / 100
        return (a, b, c)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Current THD+N
#-------------------------------------------------------------------------------
# F5H-F7H THDNIA, THDNIB, THDNIC
# Type: Read
#   1LSB corresponds to 0.01 %
#-------------------------------------------------------------------------------
    def meter_i_thdn(self):
        a = float(self.read_word(ADDR_THDNIA)) / 100
        b = float(self.read_word(ADDR_THDNIB)) / 100
        c = float(self.read_word(ADDR_THDNIC)) / 100
        return (a, b, c)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Frequency
#-------------------------------------------------------------------------------
# F8H Freq
# Type: Read
# 1LSB corresponds to 0.01 Hz
#-------------------------------------------------------------------------------
    def meter_freq(self):
        f = float(self.read_word(ADDR_Freq)) / 100
        return f
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Mean Phase Angle
#-------------------------------------------------------------------------------
# F9H-FBH PAngleA, PAngleB, PAngleC
# Type: Read
# Signed, MSB as the sign bit
# 1LSB corresponds to 0.1-degree, -180.0°~+180.0°   
#-------------------------------------------------------------------------------
    def meter_p_angle(self):
        a = float(self.read_word(ADDR_PangleA)) / 10
        b = float(self.read_word(ADDR_PangleB)) / 10
        c = float(self.read_word(ADDR_PangleB)) / 10 
        return (a, b, c)
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Temperature
#-------------------------------------------------------------------------------
# FCH Temp
# Type: Read
# 1LSB corresponds to 1 °C
# Signed, MSB as the sign bit
#-------------------------------------------------------------------------------
    def meter_temp(self):
        t = self.read_word(ADDR_Temp)
        return t
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
# Voltage Phase Angle
#-------------------------------------------------------------------------------
# FDH-FFH UAngleA, UAngleB, UAngleC
# Type: Read
# UAngle - Always '0'
# UAngleB, UAngleC - Signed, MSB as the sign bit
#   Take phase A voltage as base voltage
#   1LSB corresponds to 0.1 degree, -180.0°~+180.0°    
#-------------------------------------------------------------------------------
    def meter_u_angle(self):
        a = float(self.read_word(ADDR_PangleA)) / 10       
        b = self.read_word(ADDR_PangleB)
        if ((b and 0x8000) == 0):
            b = float(b) / 10
        else:
            b = 0 - (float(b & 0x7FFF) / 10)
        c = self.read_word(ADDR_PangleB) 
        if ((c and 0x8000) == 0):
            c = float(c) / 10
        else:
            c = 0 - (float(c & 0x7FFF) / 10)
        return (a, b, c)
#-------------------------------------------------------------------------------






