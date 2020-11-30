from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
from scipy.io import wavfile


def gui_plot_signal(field_filename):
    user_choice = field_filename.get()
    fs, wav_data = wavfile.read(user_choice)

def gui_read_file(field_filename):
    pass


def gui_plot_spectrogram():
    pass