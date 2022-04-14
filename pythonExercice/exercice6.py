# -*- code:latin1 -*-

from tkinter import *

def degree(event):
    chaine.configure(text = "degree fahreneit = " + str(eval(entree.get())*1.80+32))

def degree2(event):
    chaine1.configure(text = "degree celcius = " + str(eval(entree1.get())-32/1.8))

fenetre1 = Tk()
fenetre1.title("Temperature")
label6 = Label(fenetre1, text="Veuillez entrez une temperature en degree celcisus : ")
label6.pack(fill=BOTH,)
entree = Entry(fenetre1)
entree.bind("<Return>", degree)
chaine = Label(fenetre1)
entree.pack()
chaine.pack()

label7 = Label(fenetre1, text="veuillez entrez une temperature en degree farheneit : ")
label7.pack(fill=BOTH,)
entree1 = Entry(fenetre1)
entree1.bind("<Return>", degree2)
chaine1 = Label(fenetre1)
entree1.pack()
chaine1.pack()

fenetre1.mainloop()