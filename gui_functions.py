from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
from scipy.io import wavfile
from radix2_fft import *
from window import *
from spectrogram import *


def gui_plot_signal(field_filename, label_info, fig_signal, canvas_signal):
    # try to open file
    signal_name = field_filename.get()
    fs, wav_data = wavfile.read(signal_name)
    # TODO add try except if a file can't be opened

    # isolate one channel
    try:
        data = wav_data[:, 0]
    except IndexError:
        data = wav_data
    length = int(len(wav_data) / fs)
    time = np.linspace(0., length, data.shape[0])

    # scaling
    max_val = float(np.max(data))
    min_val = float(np.min(data))
    denom = max_val - min_val
    #
    normalized_data = np.zeros(len(wav_data), dtype=np.float64)
    for i in range(0, len(data)):
        normalized_data[i] = 2 * ((data[i] - min_val) / denom) - 1
        # normalized_data[i] = data[i]

    # refresh info label
    label_info.config(text="File read successfully")
    # plot signal
    fig_signal.clear()
    fig_signal.add_subplot(111).grid()
    fig_signal.add_subplot(111).plot(time, normalized_data)
    fig_signal.suptitle(f"{signal_name} Sample Rate: {fs}Hz Duration: {length}sec")
    axes = fig_signal.gca()
    axes.set_xlabel("Time [s]")
    axes.set_ylabel("Signal Value")
    axes.set_xlim([0, length])
    axes.set_ylim([-1, 1])
    canvas_signal.draw()

    # make data available to other functions
    gui_plot_signal.fs = fs
    gui_plot_signal.data = normalized_data
    gui_plot_signal.length = length
    gui_plot_signal.signal_name = signal_name


def gui_plot_spectrogram(field_window_type, field_window_size, label_info, fig_spectrogram, canvas_spectrogram):
    # get data from Plot Signal function
    fs = gui_plot_signal.fs
    data = gui_plot_signal.data
    length = gui_plot_signal.length
    signal_name = gui_plot_signal.signal_name

    # get user parameters
    #TODO Add falling menu
    window_type = field_window_type.get()
    window_length = int(field_window_size.get())

    # divide data in slices
    slice_length = window_length
    slices = int(len(data) / window_length)
    # if there is leftover data, increase slices by one
    if slices > int(np.floor(slices)):
        slices = int(np.floor(slices)) + 1

    sliced_data = np.ones((slices, slice_length))

    # populate reshaped array
    idx = 0
    for row in range(0, slices):
        for col in range(0, slice_length):
            if idx >= len(data):
                sliced_data[row, col] = 0
            else:
                sliced_data[row, col] = data[idx]
            idx = idx + 1

    # calculate window parameters
    if window_type == "hamming" or "Hamming":
        window = hamming_window(window_length)
    elif window_type == "hann" or "Hann":
        window = hanning_window(window_length)
    elif window_type == "blackman" or "Blackman" or "blackmann" or "Blackmann":
        window = blackman_window(window_length)
    else:
        window = hamming_window(window_length)

    # apply windowing
    for row in range(0, slices):
        sliced_data[row, :] = np.multiply(sliced_data[row, :], window)

    # calculate FFT of each row
    label_info.config(text="Calculating FFT...")
    fft_data = np.zeros((slices, int(window_length / 2)))
    for row in range(0, slices):
        fft_data[row, :] = radix2_fft(sliced_data[row, :])
        # fft_data[row, :] = scipy_fft(sliced_data[row, :])
        # progress
        if row == int(slices * (1 / 4)):
            label_info.config(text="FFT 25% Complete")
        elif row == int(slices * (1 / 2)):
            label_info.config(text="FFT 50% Complete")
        elif row == int(slices * (3 / 4)):
            label_info.config(text="FFT 75% Complete")
    label_info.config(text="FFT Calculation complete.")

    fft_data = 20 * np.log10(fft_data)
    fft_data = np.transpose(fft_data)
    label_info.config(text="All done.")

    # plot signal
    fig_spectrogram.clear()
    fig_spectrogram.add_subplot(111).grid()
    fig_spectrogram.add_subplot(111).imshow(fft_data, cmap='gray', origin='lower',
                                            extent=[0, (len(data) / fs), 0, fs / 2 / 1000],
                                            aspect='auto', vmin=-50)
    axes = fig_spectrogram.gca()
    fig_spectrogram.suptitle(f"{signal_name} Spectrogram")
    axes.set_xlabel("Time [s]")
    axes.set_ylabel("Frequency [kHz]")
    canvas_spectrogram.draw()
