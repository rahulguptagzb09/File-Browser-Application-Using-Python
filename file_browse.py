import tkinter as Tk
from tkinter import filedialog
import sys

def browse_file():
    fname = filedialog.askopenfilename(filetypes = (("Template files", "*.type"), ("All files", "*")))
    print(fname)

root = Tk.Tk()
root.wm_title("Browser")
broButton = Tk.Button(master = root, text = 'Browse', width = 6, command=browse_file)
broButton.pack(side=Tk.LEFT, padx = 2, pady=2)

Tk.mainloop()
