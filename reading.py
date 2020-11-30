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
        data = wav_data[:, 0]
    except IndexError:
        data = wav_data
    length = int(len(wav_data) / fs)

    # scaling
    max_val = float(np.max(data))
    min_val = float(np.min(data))
    denom = max_val - min_val
    #
    normalized_data = np.zeros(len(wav_data), dtype=np.float64)
    print("Normalizing...")
    for i in range(0, len(data)):
        normalized_data[i] = 2 * ((data[i] - min_val) / denom) - 1
        #normalized_data[i] = data[i]
    print("Normalizing Complete")

    print("Sample Rate:", fs)
    print("Data points:", len(data))

    return normalized_data, fs, length
