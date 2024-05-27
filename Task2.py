
import tkinter as tk 

from tkinter import *

window = tk.Tk()
window.title("T-Town Veterinnary Clinic Database")
window.geometry("650x250")

input1 = tk.Entry(window,text="Entry widgets can be typed in", width=25)
sbn = tk.Button(window,text="Search by Name")
dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto)
ClD = tk.Label(window, text="Client Database")
Next = tk.Button(window, text="Next >")
Previous = tk.Button(window, text="< Previous")
Save_Entry = tk.Button(window, text="Save Entry")

#------------------------------------------------------

Name = tk.Label(window, text="Name")
Type = tk.Label(window, text="Type")
Breed = tk.Label(window, text="Breed")
Owner = tk.Label(window, text="Owner")
Birthdate = tk.Label(window, text="Birthdate")

Name_input = tk.Entry(window,text="")
Type_input = tk.Entry(window,text="")
Breed_input = tk.Entry(window,text="")
Owner_input = tk.Entry(window,text="")
Birthdate_input = tk.Entry(window,text="")

Name.pack()
Type.pack()
Breed.pack()
Owner.pack()
Birthdate.pack()

Name_input.pack()
Type_input.pack()
Breed_input.pack()
Owner_input.pack()
Birthdate_input.pack()

Name.place(x=40, y=105)
Type.place(x=150, y=105)
Breed.place(x=275, y=105)
Owner.place(x=400, y=105)
Birthdate.place(x=550, y=105)

Name_input.place(x=10, y=130, width=100, height=25)
Type_input.place(x=120, y=130, width=100, height=25)
Breed_input.place(x=245, y=130, width=100, height=25)
Owner_input.place(x=370, y=130, width=100, height=25)
Birthdate_input.place(x=525, y=130, width=100, height=25)

#------------------------------------------------

input1.pack()
sbn.pack()
dog.pack()
ClD.pack()
Next.pack()
Previous.pack()
Save_Entry.pack()

input1.place(x=495, y=4, width=150, height=25)
sbn.place(x=366, y=4, width=125, height=25)
dog.place(x=25, y=4)
ClD.place(x=255, y=50)
Next.place(x=600, y=215)
Previous.place(x=2.5, y=215)
Save_Entry.place(x=250, y=215, width=125, height=30)


window.mainloop()

#done