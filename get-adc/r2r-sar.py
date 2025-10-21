import r2r_adc
from matplotlib import pyplot as plt
import time

voltage_values = []
time_values = []
duration = 3.0
adc = r2r_adc.R2R_ADC(3.2)
try:
    begin = time.time()
    while time.time() - begin < duration:
        voltage_values.append(adc.get_sar_voltage())
        time_values.append(time.time() - begin)
    plt.figure(figsize=(10, 6))
    plt.plot(time_values, voltage_values)
    plt.grid()
    plt.show()
finally:
    adc.deinit()