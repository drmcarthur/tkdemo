#!/usr/bin/python3
##
#
#
# @file MainGUI.py
# @author Daniel McArthur
# @date 2020-05-24
# @brief This is the main GUI window used to demo tk features.

# GUI imports
import tkinter as tk


if __name__ == "__main__":
    window = tk.Tk()
    greeting = tk.Label(text="Hello, Tkinter")
    but = tk.Button()
    greeting.pack()
    window.mainloop()

