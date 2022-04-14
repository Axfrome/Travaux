from tkinter import *
from random import randrange


global x1, y1, x2, y2
x1, y1, x2, y2 = 0, 20, 20, 0

def dammier():    
    can.delete(ALL)
    global x1, y1, x2, y2
    x1, y1, x2, y2 = 0, 20, 20, 0
    i = 0
    can.create_rectangle(x1,y1,x2,y2,fill='blue')
    dam = 0
    while dam <5:    
        while i < 5:
            can.create_rectangle(x1,y1,x2,y2,fill='blue')
            x1, y1, x2, y2 = x1+40, y1, x2+40, y2
            i = i + 1
        y1 = y1+20
        y2 = y2+20
        x1 = 20
        x2 = 40
        i = 0
        while i < 5:
                can.create_rectangle(x1,y1,x2,y2,fill='blue')
                x1, y1, x2, y2 = x1+40, y1, x2+40, y2
                i = i + 1
        i = 0
        y1 = y1+20
        y2 = y2+20
        x1 = 0
        x2 = 20
        dam = dam+1

global x00, y00, x11, y11

def pion():
    global x00, y00, x11, y11
    x00 = 2
    y00 = 2
    x11 = 20
    y11 = 20
    longueur = randrange(10)
    etage = randrange(10)

    #longueur multiple de 20 x00 et x11 par 20 et hauteur y00 et y11 par 20
    
    can.create_oval(longueur*20, etage*20,longueur*20+20 ,etage*20+20, fill="red")

def reset():
    can.delete(ALL)




fen = Tk()
can = Canvas(fen, width =200, height =200, bg ='ivory')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(fen, text ='dammier', command =dammier)
b1.pack(side =LEFT, padx =3, pady =3)
b2 = Button(fen, text ='pion', command =pion)
b2.pack(side =RIGHT, padx =3, pady =3)
b3 = Button(fen, text ='reset', command =reset)
b3.pack(side =BOTTOM, padx =3, pady =3)
fen.mainloop()