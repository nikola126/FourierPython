import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
from gui_functions import *


def stop_all(root):
    root.quit()  # stops mainloop
    root.destroy()
    return 1


def gui_menu():
    root = Tk()
    root.configure(background='#EEEEEE')
    root.geometry("1620x620")
    root.title("WAV Spectrogram")
    root.resizable(False, False)

    # Add UI elements
    label_info = Label(root, text="", font=('Arial', 12))
    label_choice_filename = Label(root, text="File name", font=('Arial', 12), width=10, anchor='w')
    label_choice_window_type = Label(root, text="Window type", font=('Arial', 12), width=10, anchor='w')
    label_choice_window_size = Label(root, text="Window size", font=('Arial', 12), width=10, anchor='w')

    input_filename = StringVar(root)

    choices_window_size = [256, 512, 1024, 2048]
    dropdown_window_size = ttk.Combobox(root, width=12, state="readonly", values=choices_window_size,
                                        font=("Courier", 15, 'bold'))
    choices_window_type = ["Hamming", "Hanning", "Blackman"]
    dropdown_window_type = ttk.Combobox(root, width=12, state="readonly", values=choices_window_type,
                                        font=("Courier", 15, 'bold'))

    field_filename = Entry(root, textvariable=input_filename, font=('Courier', 15, 'bold'), width=14)

    button_plot_signal = Button(root, text="Plot Signal", fg="green", width=18, height=1,
                                command=lambda: gui_plot_signal(field_filename, label_info, fig_signal, canvas_signal))
    button_plot_spectrogram = Button(root, text="Plot Spectrogram", fg="green", width=18, height=1,
                                     command=lambda: gui_plot_spectrogram(dropdown_window_type, dropdown_window_size,
                                                                          label_info, fig_spectrogram,
                                                                          canvas_spectrogram))
    button_read_file = Button(root, text="Open WAV", fg="blue", width=18, height=1,
                              command=lambda: gui_open_file(field_filename, label_info, button_plot_signal,
                                                            button_plot_spectrogram))
    button_quit = Button(root, text="Quit", fg="red", font=('Courier', 13, 'bold'), width=15, height=1,
                         command=lambda: stop_all(root))
    button_plot_signal["state"] = "disabled"
    button_plot_spectrogram["state"] = "disabled"

    # Signal Plot
    fig_signal = Figure(figsize=(8, 4), dpi=100)
    fig_signal.add_subplot(111).grid()
    fig_signal.suptitle('Signal')
    canvas_signal = FigureCanvasTkAgg(fig_signal, master=root)
    axes = fig_signal.gca()
    canvas_signal.draw()
    toolbar_frame_signal = Frame(master=root)
    toolbar = NavigationToolbar2Tk(canvas_signal, toolbar_frame_signal)

    # Spectrogram Plot
    fig_spectrogram = Figure(figsize=(8, 4), dpi=100)
    fig_spectrogram.add_subplot(111).grid()
    fig_spectrogram.suptitle('Spectrogram')
    canvas_spectrogram = FigureCanvasTkAgg(fig_spectrogram, master=root)
    axes = fig_spectrogram.gca()
    canvas_spectrogram.draw()
    toolbar_frame_spectrogram = Frame(master=root)
    toolbar = NavigationToolbar2Tk(canvas_spectrogram, toolbar_frame_spectrogram)

    # Align UI elements
    # Plots
    canvas_signal.get_tk_widget().grid(row=0, column=0, columnspan=6, rowspan=10, padx=5, pady=5)
    toolbar_frame_signal.grid(row=11, column=0, columnspan=3, rowspan=2, sticky='w')
    canvas_spectrogram.get_tk_widget().grid(row=0, column=7, columnspan=6, rowspan=10, padx=5, pady=5)
    toolbar_frame_spectrogram.grid(row=11, column=7, columnspan=3, rowspan=2, sticky='w')
    # Labels and Buttons
    label_info.grid(row=13, column=0, padx=1, pady=1, columnspan=6)
    label_info.configure(anchor="center")
    label_choice_filename.grid(row=14, column=0, pady=2)
    label_choice_window_size.grid(row=15, column=0, pady=2, columnspan=1)
    label_choice_window_type.grid(row=16, column=0, pady=2, columnspan=1)
    field_filename.grid(row=14, column=1, pady=2)
    dropdown_window_size.grid(row=15, column=1, pady=2)
    dropdown_window_type.grid(row=16, column=1, pady=2)
    button_read_file.grid(row=14, column=2, pady=2)
    button_plot_signal.grid(row=15, column=2, pady=2)
    button_plot_spectrogram.grid(row=16, column=2, pady=2)
    button_quit.grid(row=17, column=0, columnspan=1, pady=2)

    root.mainloop()
    return 0
