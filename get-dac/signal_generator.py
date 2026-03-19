import math
import time 

def get_sin_wave_amplitude(freq, time):
    return(math.sin(2 * math.pi * freq * time) + 1) / 2

def wait_for_sampling_period(sampling_frequency):
    period = 1.0/sampling_frequency
    time.sleep(period)