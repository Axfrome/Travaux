# -*- code:latin1 -*-

from tkinter import *
p = 0
elip = 0
y = 0
def deplacement():
    global x1, y1, x2, y2, posx, posy, p, elip, y
    if posx < 200 and p == 0:
        posx = posx + 10
        if elip < 7 and y == 0:
            posy = posy + 5
            elip = elip+1
        else:
            y = 1
            posy = posy - 5
            elip = elip-1
            if elip == 0:
                y = 0
        oval1 = can1.create_oval(x1+posx, y1+posy, x2+posx, y2+posy, width=2, fill='red')
        can1.coords(oval1, x1+posx, y1+posy, x2+posx, y2+posy)
    else:
        p = 1
        if p ==1:
            posx = posx - 10
            if elip < 7 and y == 1:
                posy = posy + 5
                elip = elip+1
            else:
                y = 0
                posy = posy - 5
                elip = elip-1
                if elip == 0:
                    y = 1
            oval1 = can1.create_oval(x1+posx, y1+posy, x2+posx, y2+posy, width=2, fill='red')
            can1.coords(oval1, x1+posx, y1+posy, x2+posx, y2+posy)
        if posx == -55:
            p = 0
            y = 0

fenetre = Tk()
fenetre.title("Exercice 7")

x1, y1, x2, y2 = 100, 100, 50, 50
posx = 75
posy = 50


can1 = Canvas(fenetre, bg= 'dark grey', height=300, width=300)
oval1 = can1.create_oval(x1+posx, y1+posy, x2+posx, y2+posy, width=2, fill='red')
can1.pack()
label1=Label(fenetre, text = "cliquez pour que la balle bouge").pack()
Button(fenetre, text= 'bouge la belle', command=deplacement).pack()



fenetre.mainloop()