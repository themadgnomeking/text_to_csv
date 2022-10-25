from tkinter import *
from tkinter import filedialog
from tkinter import ttk

root = Tk()
root.geometry("700x350")

style=ttk.Style(root)

def open_win_diag():
    file = filedialog.askopenfilename()
    f = open(root.file, 'r')

label = Label(root, text = "Click the button to brows the file", font = "Arial 15 bold")
label.pack(pady = 20)

button = ttk.Button(root, text="Open", command = open_win_diag)
button.pack(pady = 5)

root.mainloop()