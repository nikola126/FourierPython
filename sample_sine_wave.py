import numpy as np


def create_sine_wave_data():
    """
    :return: creates a period of sine signal, composed of 3 sine waves with different frequencies
    """
    freq_1 = 50
    freq_2 = 100
    freq_3 = 150
    fs = 2 ** 10
    t = np.arange(0, 1, 1 / fs)
    sin1 = t * np.array(2 * np.pi * freq_1)
    sin2 = t * np.array(2 * np.pi * freq_2)
    sin3 = t * np.array(2 * np.pi * freq_3)
    data = np.sin(sin1) + np.sin(sin2) + np.sin(sin3)

    return data
