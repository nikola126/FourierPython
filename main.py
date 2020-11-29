# IMPORTS
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

from reading import read_wav

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Get File Name
    file_name = input("Enter file name (without extension):")
    file_name = file_name + ".wav"
    data, fs, length = read_wav(file_name)

    # SIGNAL PLOT
    time = np.linspace(0., length, data.shape[0])
    #time.reshape([1,len(time)])

    # # TODO Plot function
    plt.figure(1)
    plt.plot(time, data)

    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid('both')
    plt.show()

    # TODO FT Function
    # TODO Window function
    # TODO Spectrogram function