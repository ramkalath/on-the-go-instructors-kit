 
import numpy as numpy
import cv2
import sys
import Tkinter as tk
import ttk
import time
import os

SUNKABLE_BUTTON = 'SunkableButton.TButton'
path = "./my_program.fifo"
os.mkfifo(path)

def button1_start():
    global button_status
    global button1
    global button2
    button_status = 1
    time.sleep(0.1)
    button1.state(['pressed', 'disabled'])
    style.configure(SUNKABLE_BUTTON, relief=tk.SUNKEN, foreground='black')
    button2.state(['!pressed', '!disabled'])
    style.configure(SUNKABLE_BUTTON, relief=tk.RAISED, foreground='black')
    fifo = open(path, "w")
    fifo.write(str(button_status)+"\n")
    fifo.close()
    # print button_status


def button2_start():
    global button_status
    global button1
    global button2
    button_status = 2
    time.sleep(0.1)
    button2.state(['pressed', 'disabled'])
    style.configure(SUNKABLE_BUTTON, relief=tk.SUNKEN, foreground='black')
    button1.state(['!pressed', '!disabled'])
    style.configure(SUNKABLE_BUTTON, relief=tk.RAISED, foreground='black')
    fifo = open(path, "w")
    fifo.write(str(button_status)+"\n")
    fifo.close()
    # print button_status

if __name__ == "__main__":
    fifo = open(path, "w")
    fifo.write("1\n")
    fifo.close()
    global button_status
    root = tk.Tk()
    root.geometry("250x30")
    style = ttk.Style()

    global button1
    button1 = ttk.Button(root, text="face", command=button1_start, style=SUNKABLE_BUTTON)
    button1.pack(side="left", fill=tk.BOTH, expand=True)
    button1.state(['pressed', 'disabled'])
    style.configure(SUNKABLE_BUTTON, relief=tk.SUNKEN, foreground='black')

    global button2
    button2 = ttk.Button(
        root, text="note", command=button2_start, style=SUNKABLE_BUTTON)
    button2.pack(side="left", fill=tk.BOTH, expand=True)
    root.mainloop()