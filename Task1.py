

import tkinter as tk 

from tkinter import *

window = tk.Tk()
window.title("tk")
window.geometry("500x50")

input1 = tk.Entry(window,text="Entry widgets can be typed in", width=25)
x = tk.Label(window, text="x")
input2 = tk.Entry(window,text="Entry widgets can be typed in", width=25)
equal = tk.Button(window,text="=")
answer = tk.Entry(window,text="Entry widgets can be typed in", width=25 )

input1.pack()
x.pack()
input2.pack()
equal.pack()
answer.pack()

input1.place(x=10, y=10, width=100, height=25)
x.place(x=125, y=12.1)
input2.place(x=150, y=10, width=100, height=25)
equal.place(x=260, y=11, width=17.5, height=22.5)
answer.place(x=287.5, y=10, width=203, height=25)

window.mainloop()

#done
