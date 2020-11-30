import numpy as np
from window import *
from radix2_fft import *
import matplotlib.pyplot as plt


def spectrogram(data, fs, window_type, window_length):
    """
    :param data: wav data vector
    :param fs: sample rate of wav data
    :param window_type: type of desired window (Hamming, Hanning, Blackman)
    :param window_length: length of desired window (must be a power of 2)
    :returns: spectrogram and Numpy data array
    """
    # divide data in slices
    slice_length = window_length
    slices = int(len(data) / window_length)
    # if there is leftover data, increase slices by one
    if slices > int(np.floor(slices)):
        slices = int(np.floor(slices)) + 1

    sliced_data = np.ones((slices, slice_length))

    print(f"Data with length {len(data)} has been divided in an array with size {sliced_data.shape}")

    # populate reshaped array
    idx = 0
    for row in range(0, slices):
        for col in range(0, slice_length):
            if idx >= len(data):
                sliced_data[row, col] = 0
            else:
                sliced_data[row, col] = data[idx]
            idx = idx + 1

    print("Windowing...", end="")
    # calculate window parameters
    if window_type == "hamming" or "Hamming":
        window = hamming_window(window_length)
    elif window_type == "hann" or "Hann":
        window = hanning_window(window_length)
    elif window_type == "blackman" or "Blackman":
        window = blackman_window(window_length)
    else:
        window = hamming_window(window_length)

    # apply windowing
    for row in range(0, slices):
        sliced_data[row, :] = np.multiply(sliced_data[row, :], window)
    print("Windowing complete.")

    # calculate FFT of each row
    print("Calculating FFT...")
    fft_data = np.zeros((slices, int(window_length / 2)))
    for row in range(0, slices):
        fft_data[row, :] = radix2_fft(sliced_data[row, :])
        # fft_data[row, :] = scipy_fft(sliced_data[row, :])
        # progress
        if row == int(slices * (1 / 4)):
            print("FFT 25% Complete")
        elif row == int(slices * (1 / 2)):
            print("FFT 50% Complete")
        elif row == int(slices * (3 / 4)):
            print("FFT 75% Complete")
    print("FFT Calculation complete.")

    fft_data = 20 * np.log10(fft_data)
    fft_data = np.transpose(fft_data)
    plt.figure()
    plt.imshow(fft_data, cmap='gray', origin='lower',
               extent=[0, (len(data) / fs), 0, fs / 2 / 1000],
               aspect='auto', vmin=-80)
    plt.title('Spectrogram')
    plt.xlabel('Time [s]')
    plt.ylabel('Freq [kHz]')
    plt.colorbar()
    plt.show()

    return fft_data
