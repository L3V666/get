import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequence = 10
sampling_frequence = 1000

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.15)
    
    while True:
        dac.set_voltage(sg.get_sin_wave_amplitude(amplitude, time))
    
finally:
    dac.deinit()