from scipy.io import wavfile
import numpy as np


def read_wav(file_name):
    """
    INPUT:
    filename.wav
    OUTPUT:
    data    (one channel signal values)
    fs      (sample rate)
    length  (length of the array)

    normalizes data
    """
    fs, wav_data = wavfile.read(file_name)

    # isolate one channel
    try:
        data = wav_data[:,0]
    except IndexError:
        data = wav_data
    length = int(len(wav_data) / fs)

    # scaling
    max_val = max(data)
    min_val = min(data)
    print(f"Max data:{max_val} Min data:{min_val}")

    normalized_data = np.zeros(len(wav_data))
    #print(normalized_data.shape)
    for i in range(0,len(wav_data)):
        normalized_data[i] = (data[i]-min_val)/(max_val-min_val)

    print("Sample Rate:", fs)
    print("Data points:", len(data))

    return normalized_data, fs, length
