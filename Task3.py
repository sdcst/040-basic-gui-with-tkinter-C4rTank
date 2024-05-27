
import tkinter as tk 

from tkinter import *

window = tk.Tk()
window.title("Example")
window.geometry("257x135")

dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto)
poc = tk.Label(window, text="Pochacco!")
text_b = tk.Label(window,text="A cuddly little puppy! This is from the same\ncreators who brought you Keropi and Kero Kero", bg="#b3ffff")

dog.pack()
poc.pack()
text_b.pack()

dog.place(x=75, y=0)
poc.place(x=150, y=37.5)
text_b.place(x=0, y=100)



window.mainloop()

#done