import numpy as np
import time

def get_sin_wave_amplitude(freq, t):
    sin_value = np.sin(2 * np.pi * freq * t)
    shifted = sin_value + 1
    normalized = shifted / 2
    return normalized

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period + 1)