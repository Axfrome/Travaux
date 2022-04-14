from tkinter import *


def pointeur(event):
    chaine.configure(text = "Click detecte en X =" + str(event.x) + ", Y=" + str(event.y))
    eventx = event.x
    eventy = event.y
    cadre.create_oval(eventx, eventy, eventx + 20, eventy+20, fill="red")

def reset(a=50, b=50):
    cadre.delete(ALL)


fen = Tk()
cadre = Canvas(fen, width=200, height=150, bg="light yellow")
cadre.bind("<Button-1>", pointeur)
cadre.bind("<Button-3>", reset)
b3 = Button(fen, text ='reset', command =reset)
b3.pack(side =BOTTOM, padx =3, pady =3)
cadre.pack()
chaine = Label(fen)
chaine.pack()
fen.mainloop()