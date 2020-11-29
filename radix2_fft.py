import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt


def scipy_fft(data):
    # sample_data = np.arange(1, 1024, 1)
    y = fft(data)
    y = np.abs(y)
    y = y[1:int(np.floor(len(y) / 2))]

    plt.figure()
    plt.plot(y)
    plt.show()


def radix2_fft(data):
    Fourier = fftrecur(data)
    # print(f"Length of Fourier: {len(Fourier)}")
    return Fourier


def fftrecur(data):
    N = len(data)
    print(f"N = {N}")
    if N == 1:
        # print("end is here")
        Xdft = data
    else:
        # print("recursive call, sending two arrays")
        # in MATLAB
        # W = exp(-2 * pi * j / N). ^ (0: (N / 2) - 1);
        exponential = np.exp(-2 * np.pi * (0 + 1j) / N)
        N_array = np.array([0, N / 2])
        W = np.multiply(exponential, N_array)

        # in MATLAB
        # XE = fftrecur(x(1: 2: (N - 1)));
        to_XE = data[0:N:2]
        # XO = fftrecur(x(2:2: N));
        to_XO = data[1:N:2]

        # print(f"Data({len(data)}):\n{data}\nTo XE({len(to_XE)}):\n{to_XE}\nTo XO({len(to_XO)}):\n{to_XO}")
        # recursive calls
        XE = fftrecur(to_XE)
        XO = fftrecur(to_XO)

        temp = np.multiply(W, XO)
        #temp = temp[1]
        print(f"This is temp:\n{temp}\nThis is XE:\n{XE}")
        Xdft = np.array([XE+temp, XE-temp])
        print(f"This is Xdft: {Xdft}")
    return Xdft
