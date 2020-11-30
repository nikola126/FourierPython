# IMPORTS
import matplotlib.pyplot as plt
import numpy as np
from spectrogram import *
from radix2_fft import *

from reading import read_wav
from main_menu import gui_menu


def console_main():
    print("Calculates and plots the spectrogram of a .wav file")
    # Get File Name
    file_name = input("Enter .wav file name (without extension):")
    file_name = file_name + ".wav"
    data, fs, length = read_wav(file_name)

    # SIGNAL PLOT
    user_choice = input("Plot signal? [y/n]")
    if user_choice == 'y':
        time = np.linspace(0., length, data.shape[0])
        plt.figure(1)
        plt.plot(time, data)
        plt.xlabel("Time [s]")
        plt.ylabel("Amplitude")
        plt.grid('both')
        plt.show()

    # SPECTROGRAM
    user_window_choice = input("Enter type of window (Hamming,Hann,Blackman):")
    user_window_size = int(input("Enter window size (power of 2)(1024):"))
    spectrogram_data = spectrogram(data, fs, user_window_choice, user_window_size)


def gui_main():
    gui_menu()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gui_main()
