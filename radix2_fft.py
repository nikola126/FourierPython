import numpy as np
from scipy.fft import fft


def scipy_fft(data):
    y = fft(data)
    return y


def radix2_fft(data):
    Fourier = fftrecur(data)

    # calculate absolute value
    Fourier = abs(Fourier)
    # Fourier = abs(Fourier)
    # and cut half values
    half_index = int(len(Fourier)/2)
    Fourier = Fourier[0:half_index]

    return Fourier


def fftrecur(data):
    N = len(data)
    if N == 1:
        Xdft = data
    else:
        # in MATLAB
        # W = exp(-2 * pi * j / N). ^ (0: (N / 2) - 1);

        exponential = np.exp(-2 * np.pi * (0 + 1j) / N)
        if N == 2:
            N_array = np.array([0])
        else:
            N_array = np.arange(0, ((N / 2)))
        W = np.power(exponential, N_array)

        # in MATLAB
        # XE = fftrecur(x(1: 2: (N - 1)));
        to_XE = data[0:N:2]
        # XO = fftrecur(x(2:2: N));
        to_XO = data[1:N:2]

        # recursive calls
        XE = fftrecur(to_XE)
        XO = fftrecur(to_XO)

        temp = np.multiply(W, XO)
        Xdft = np.concatenate((XE + temp, XE - temp), axis=0)
    return Xdft
