from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
import numpy as np
from gui_functions import *


def gui_function_caller(function, root):
    # Hides the main menu and returns it after user presses Quit
    root.withdraw()
    function()
    # Recover Main Menu
    root.update()
    root.deiconify()


def stop_all(root):
    root.quit()  # stops mainloop
    root.destroy()
    return 1


def restart(root):
    root.withdraw()
    gui_menu()
    root.quit()  # stops mainloop
    root.destroy()
    return 0


def gui_menu():
    root = Tk()
    root.geometry("1600x600")
    root.title("WAV Spectrogram")
    root.resizable(False, False)

    # Add UI elements
    label_info = Label(root, text="Info here", font=('Arial', 12))
    label_choice_filename = Label(root, text="File name", font=('Arial', 12), width=10, anchor='w')
    # TODO Dropdown menus
    label_choice_window_type = Label(root, text="Window type", font=('Arial', 12), width=10, anchor='w')
    label_choice_window_size = Label(root, text="Window size", font=('Arial', 12), width=10, anchor='w')

    input_filename = StringVar(root)
    input_window_type = StringVar(root)
    input_window_size = StringVar(root)

    field_filename = Entry(root, textvariable=input_filename, font=('Courier', 15, 'bold'), width=14)
    field_window_type = Entry(root, textvariable=input_window_type, font=('Courier', 15, 'bold'), width=14)
    field_window_size = Entry(root, textvariable=input_window_size, font=('Courier', 15, 'bold'), width=14)

    plot_signal_button = Button(root, text="Read and plot", fg="green", width=18, height=1,
                                command=lambda: gui_plot_signal(field_filename, label_info, fig_signal, canvas_signal))
    plot_spectrogram_button = Button(root, text="Plot Spectrogram", fg="green", width=18, height=1,
                                     command=lambda: gui_plot_spectrogram(field_window_type, field_window_size,
                                                                          label_info, fig_spectrogram,
                                                                          canvas_spectrogram))
    quit_button = Button(root, text="Quit", fg="red", width=15, height=1, command=lambda: stop_all(root))

    # Align UI elements
    label_info.grid(row=17, column=0, padx=10, pady=5, columnspan=10)
    label_info.configure(anchor="center")
    label_choice_filename.grid(row=18, column=0, pady=3)
    label_choice_window_size.grid(row=19, column=0, pady=3, columnspan=1)
    label_choice_window_type.grid(row=20, column=0, pady=3, columnspan=1)
    field_filename.grid(row=18, column=1)
    field_window_size.grid(row=19, column=1)
    field_window_type.grid(row=20, column=1)
    plot_signal_button.grid(row=18, column=2, pady=3)
    plot_spectrogram_button.grid(row=19, column=2, pady=3)
    quit_button.grid(row=20, column=2, pady=3)

    # Signal Plot
    fig_signal = Figure(figsize=(8, 4), dpi=100)
    fig_signal.add_subplot(111).grid()
    fig_signal.suptitle('Signal')
    canvas_signal = FigureCanvasTkAgg(fig_signal, master=root)
    canvas_signal.get_tk_widget().grid(row=0, column=0, columnspan=6, rowspan=10)
    axes = fig_signal.gca()
    canvas_signal.draw()
    toolbar_frame_signal = Frame(master=root)
    toolbar_frame_signal.grid(row=15, column=0, columnspan=3, rowspan=2)
    toolbar = NavigationToolbar2Tk(canvas_signal, toolbar_frame_signal)

    # Spectrogram Plot
    fig_spectrogram = Figure(figsize=(8, 4), dpi=100)
    fig_spectrogram.add_subplot(111).grid()
    fig_spectrogram.suptitle('Spectrogram')
    canvas_spectrogram = FigureCanvasTkAgg(fig_spectrogram, master=root)
    canvas_spectrogram.get_tk_widget().grid(row=0, column=7, columnspan=6, rowspan=10)
    axes = fig_spectrogram.gca()
    canvas_spectrogram.draw()
    toolbar_frame_spectrogram = Frame(master=root)
    toolbar_frame_spectrogram.grid(row=15, column=7, columnspan=3, rowspan=2)
    toolbar = NavigationToolbar2Tk(canvas_spectrogram, toolbar_frame_spectrogram)

    root.mainloop()
    return 0
