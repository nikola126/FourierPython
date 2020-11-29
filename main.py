# IMPORTS
import matplotlib.pyplot as plt
import numpy as np
from window import *

from reading import read_wav

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Get File Name
    # file_name = input("Enter file name (without extension):")
    # file_name = file_name + ".wav"
    # data, fs, length = read_wav(file_name)
    data, fs, length = read_wav("short_birds.wav")

    # SIGNAL PLOT
    # TODO Plot function
    time = np.linspace(0., length, data.shape[0])
    plt.figure(1)
    plt.plot(time, data)
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid('both')
    plt.show()

    window_array = hamming_window(1024)
    plt.figure(2)
    plt.plot(window_array)
    plt.grid('both')
    window_array = hanning_window(1024)
    plt.plot(window_array)
    window_array = blackman_window(1024)
    plt.plot(window_array)
    plt.show()

    # TODO FT Function
    # TODO Spectrogram function
