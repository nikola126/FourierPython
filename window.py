import numpy as np


def hamming_window(n):
    """
    INPUT:
    n               (length of window)
    OUTPUT:
    window_array    (contains window coefficients of a Hamming window)
    """
    window_array = np.zeros(n, dtype=np.float64)
    for i in range(0, n):
        window_array[i] = 0.54 - 0.46 * np.cos(2 * np.pi * (i / n))
    return window_array


def hanning_window(n):
    """
    INPUT:
    n               (length of window)
    OUTPUT:
    window_array    (contains window coefficients of a Hanning window)
    """
    window_array = np.zeros(n, dtype=np.float64)
    for i in range(0, n):
        window_array[i] = np.sin(np.pi * (i / n)) * np.sin(np.pi * (i / n))
    return window_array


def blackman_window(n):
    """
    INPUT:
    n               (length of window)
    OUTPUT:
    window_array    (contains window coefficients of a Blackman window)
    """
    window_array = np.zeros(n, dtype=np.float64)
    a0 = 0.42
    a1 = 0.5
    a2 = 0.08
    for i in range(0, n):
        window_array[i] = a0 - a1 * np.cos(2 * np.pi * (i / n)) + a2 * np.cos(4 * np.pi * (i / n))
    return window_array
