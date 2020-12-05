import numpy as np
from scipy.fft import fft


def fft_scipy(data):
    """
    Uses the FFT algorithm from the SciPy library
    :param data: wav data vector
    :return: NumPy array of fft values
    """
    Fourier = fft(data)

    # calculate absolute value
    Fourier = abs(Fourier)
    # cut half values
    half_index = int(len(Fourier) / 2)
    Fourier = Fourier[0:half_index]
    return Fourier


def fft_radix2(data):
    """
    Uses a recursive radix2 FFT algorithm
    :param data: wav data vector
    :return: NumPy array of fft values
    """
    Fourier = fft_radix2_alg(data)

    # calculate absolute value
    Fourier = abs(Fourier)
    # cut half values
    half_index = int(len(Fourier) / 2)
    Fourier = Fourier[0:half_index]
    return Fourier


def fft_radix2_alg(data):
    """
    Recursive radix2 FFT algorithm
    :param data: wav data vector
    :return: NumPy array of fft values
    """
    N = len(data)
    if N == 1:
        Xdft = data
    else:
        # in MATLAB
        # W = exp(-2 * pi * j / N). ^ (0: (N / 2) - 1);

        # exponential = np.exp(-2 * np.pi * (0 + 1j) / N)
        exponential = np.exp(-2j * np.pi / N)
        if N == 2:
            N_array = np.array([0])
        else:
            N_array = np.arange(0, (N / 2))
        W = np.power(exponential, N_array)

        # recursive calls
        # in MATLAB
        # XE = fftrecur(x(1: 2: (N - 1)));
        XE = fft_radix2_alg(data[0:N:2])
        # XO = fftrecur(x(2:2: N));
        XO = fft_radix2_alg(data[1:N:2])

        temp = np.multiply(W, XO)
        Xdft = np.concatenate((XE + temp, XE - temp), axis=0)
    return Xdft