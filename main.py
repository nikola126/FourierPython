# IMPORTS
import matplotlib.pyplot as plt
import numpy as np
from window import *
from data_prep import *
from radix2_fft import *

from reading import read_wav

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Get File Name
    # file_name = input("Enter file name (without extension):")
    # file_name = file_name + ".wav"
    # data, fs, length = read_wav(file_name)
    #data, fs, length = read_wav("short_birds.wav")

    # SIGNAL PLOT
    # time = np.linspace(0., length, data.shape[0])
    # plt.figure(1)
    # plt.plot(time, data)
    # plt.xlabel("Time [s]")
    # plt.ylabel("Amplitude")
    # plt.grid('both')
    # plt.show()
    #
    # window_array = hamming_window(1024)
    # plt.figure(2)
    # plt.plot(window_array)
    # plt.grid('both')
    # window_array = hanning_window(1024)
    # plt.plot(window_array)
    # window_array = blackman_window(1024)
    # plt.plot(window_array)
    # plt.show()

    # TODO FT Function
    # TODO Spectrogram function

    #windowed = data_prep(data,1024)
    # plt.figure(3)
    # plt.plot(windowed)
    # plt.show()

    #scipy_fft()

    freq_1 = 1
    freq_2 = 2
    freq_3 = 3
    fs = 2**4
    t = np.arange(0,1,1/fs)
    sin1 = t * np.array(2*np.pi*freq_1)
    sin2 = t * np.array(2*np.pi*freq_2)
    sin3 = t * np.array(2*np.pi*freq_3)
    test_data = np.sin(sin1) + np.sin(sin2) + np.sin(sin3)
    # plt.figure(4)
    # plt.plot(test_data)
    # plt.show()
    # plt.close()

    #scipy_fft(test_data)
    test_data = np.array([1,2,3,4])
    print(test_data)
    Fourier = radix2_fft(test_data)
    #print(Fourier)
    print(abs(Fourier))

    plt.figure(4)
    plt.plot(abs(Fourier))
    plt.grid('both')
    plt.show()