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
    data, fs, length = read_wav("short_birds.wav")

    # SIGNAL PLOT
    # time = np.linspace(0., length, data.shape[0])
    # plt.figure(1)
    # plt.plot(time, data)
    # plt.xlabel("Time [s]")
    # plt.ylabel("Amplitude")
    # plt.grid('both')
    # plt.show()

    # TODO Spectrogram function

    # freq_1 = 50
    # freq_2 = 100
    # freq_3 = 150
    # fs = 2 ** 10
    # t = np.arange(0, 1, 1 / fs)
    # sin1 = t * np.array(2 * np.pi * freq_1)
    # sin2 = t * np.array(2 * np.pi * freq_2)
    # sin3 = t * np.array(2 * np.pi * freq_3)
    # data = np.sin(sin1) + np.sin(sin2) + np.sin(sin3)
    # plt.figure(4)
    # plt.plot(data)
    # plt.show()
    #
    # Fourier_scipy = scipy_fft(test_data)
    # Fourier_radix2 = radix2_fft(test_data)
    # plt.figure(4)
    # plt.plot(abs(Fourier_scipy))
    # plt.plot(abs(Fourier_radix2))
    # plt.grid('both')
    # plt.show()

    sliced_data = data_prep(data, 1024)
    sliced_data = 20 * np.log10(sliced_data)
    sliced_data = np.transpose(sliced_data)
    plt.figure()
    plt.imshow(sliced_data, cmap='gray', origin='lower', extent=[0, (len(data) / fs), 0, fs / 2 / 1000], aspect='auto',
               vmin=-80)
    plt.title('Spectrogram')
    plt.xlabel('Time[s]')
    plt.ylabel('Freq[kHz]')
    plt.colorbar()
    plt.show()
