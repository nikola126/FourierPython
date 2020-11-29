import numpy as np
from window import *


def data_prep(data, window_length):
    """
    :param data: data vector
    :param window_length: length of desired window (default: Hamming)
    :return: data shaped after window
    """
    slice_length = window_length

    # calculate window parameters
    window = hamming_window(window_length)

    # divide data in slices
    slices = len(data) / window_length
    # if there is leftover data, increase slices by one
    if slices > int(np.floor(slices)):
        slices = int(np.floor(slices)) + 1

    sliced_data = np.ones((slices, slice_length))

    print(f"Data with length {len(data)} has been divided in an array with size {sliced_data.shape}")
    print(f"{slices * slice_length} > {len(data)}")

    # populate reshaped array
    idx = 0
    for row in range(0, slices):
        for col in range(0, slice_length):
            if idx >= len(data):
                sliced_data[row, col] = 0
            else:
                sliced_data[row, col] = data[idx]
            idx = idx + 1

    # calculate FFT of each slice

    return 1
