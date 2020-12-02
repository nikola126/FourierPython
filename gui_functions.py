from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
from scipy.io import wavfile
from radix2_fft import *
from window import *
from spectrogram import *


def gui_open_file(field_filename, label_info, button_plot_signal,
                  button_plot_spectrogram):
    try:
        signal_name = field_filename.get()
        fs, wav_data = wavfile.read(signal_name)
    except FileNotFoundError:
        label_info.config(text=f"{signal_name} No such file found.")
        return
    except ValueError:
        label_info.config(text=f"{signal_name} is not a valid WAV file.")
        return

    # isolate one channel
    try:
        data = wav_data[:, 0]
    except IndexError:
        data = wav_data
    length = int(len(wav_data) / fs)

    # scaling
    label_info.config(text=f"{signal_name} scaling...")
    max_val = float(np.max(data))
    min_val = float(np.min(data))
    denom = max_val - min_val

    # for i in range(0, len(data)):
    #     normalized_data[i] = 2 * ((data[i] - min_val) / denom) - 1
    normalized_data = np.subtract(data,min_val)
    normalized_data = np.divide(normalized_data,denom)
    normalized_data = np.multiply(normalized_data,2)
    normalized_data = np.subtract(normalized_data,1)


    # change UI if file is opened successfully
    button_plot_signal["state"] = "active"
    button_plot_signal["fg"] = "green"
    button_plot_spectrogram["state"] = "active"
    button_plot_spectrogram["fg"] = "green"
    label_info.config(text=f"{signal_name} read successfully")

    # make data available to other functions
    gui_open_file.fs = fs
    gui_open_file.data = normalized_data
    gui_open_file.length = int(len(wav_data) / fs)
    gui_open_file.signal_name = signal_name


def gui_plot_signal(field_filename, label_info, fig_signal, canvas_signal):
    # get data from other functions
    data = gui_open_file.data
    fs = gui_open_file.fs
    signal_name = gui_open_file.signal_name

    length = int(len(data) / fs)
    time = np.linspace(0., length, data.shape[0])
    # plot signal
    fig_signal.clear()
    fig_signal.add_subplot(111).grid()
    fig_signal.add_subplot(111).plot(time, data)
    fig_signal.suptitle(f"{signal_name} Sample Rate: {fs}Hz Duration: {length}sec")
    axes = fig_signal.gca()
    axes.set_xlabel("Time [s]")
    axes.set_ylabel("Signal Value")
    axes.set_xlim([0, length])
    axes.set_ylim([-1, 1])
    canvas_signal.draw()
    # refresh info label
    label_info.config(text="Plot Complete")


def gui_plot_spectrogram(field_window_type, field_window_size, label_info, fig_spectrogram, canvas_spectrogram):
    # get data from other functions
    data = gui_open_file.data
    fs = gui_open_file.fs
    signal_name = gui_open_file.signal_name

    # get user parameters
    try:
        window_length = int(field_window_size.get())
    except ValueError:
        label_info.config(text="Please provide window length. Default is 1024 points.")
        field_window_size.set(1024)
        return

    window_type = field_window_type.get()
    if window_type == '':
        label_info.config(text="Please provide window type. Default is Hamming window.")
        field_window_type.set(value="Hamming")
        return

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
        # fft_data[row, :] = radix2_fft(sliced_data[row, :])
        fft_data[row, :] = scipy_fft(sliced_data[row, :])
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
