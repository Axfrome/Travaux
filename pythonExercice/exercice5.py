# -*- code:latin1 -*-

from tkinter import *
from math import sqrt

#procédure générale de déplement.


def pointeur1():
    global astrechoisie
    astrechoisie = 1

def pointeur2():
    global astrechoisie
    astrechoisie = 2

def poseastre(event):
    global astrechoisie, x1, y1, x2, y2, x3, y3, vraidistance
    if astrechoisie == 1:
        chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
            ", Y =" + str(event.y))
        x1 = event.x
        y1 = event.y
        can1.coords(oval1, x1, y1, x1+30, y1+30)
        distance = str(x1-x2)
        label2.configure(text=distance0+distance)
        distance2 = str(y1-y2)
        label1.configure(text=distance00+distance2)
        vraidistance = str((sqrt((int(distance)*int(distance))+(int(distance2)*int(distance2)))))
        label3.configure(text="la distance entre les astres est de "+vraidistance)
        distance30 = str(x2-x3)
        distance31 =str(y2-y3)
        vraidistance3 = str((sqrt((int(distance30)*int(distance30))+(int(distance31)*int(distance31)))))
        force2 = (1*10*10)/(float(vraidistance3)*float(vraidistance3))
        force = (1*10*20)/float((float(vraidistance)*float(vraidistance)))
        label4.configure(text="la force entre les deux astres (rouge et bleu) est de : "+str(force))
        label5.configure(text="la force entre les deux astres (jaune et bleu) est de : "+str(force2))
        distance40 = str(x1-x3)
        distance41 =str(y1-y3)
        vraidistance4 = str((sqrt((int(distance40)*int(distance40))+(int(distance41)*int(distance41)))))
        force3 = (1*20*10)/(float(vraidistance4)*float(vraidistance4))
        label6.configure(text="la force entre les deux astres (jaune et rouge) est de : "+str(force3))

    if astrechoisie == 2:
        chaine.configure(text = "Clic détecté en X =" + str(event.x) +\
            ", Y =" + str(event.y))
        x2 = event.x
        y2 = event.y
        can1.coords(oval2, x2, y2, x2+20, y2+20)
        


def avance(gd, hb):
    global x1, y1, x2, y2, x3, y3, vraidistance
    x1, y1 = x1 +gd, y1+hb
    can1.coords(oval1, x1,y1, x1+30, y1+30)
    distance = str(x1-x2)
    label2.configure(text=distance0+distance)
    distance2 = str(y1-y2)
    label1.configure(text=distance00+distance2)
    vraidistance = str((sqrt((int(distance)*int(distance))+(int(distance2)*int(distance2)))))
    label3.configure(text="la distance entre les astres est de "+vraidistance)
    vraidistance3 = str((sqrt((int(distance30)*int(distance30))+(int(distance31)*int(distance31)))))
    force2 = (1*10*10)/(float(vraidistance3)*float(vraidistance3))
    force = (1*10*20)/float((float(vraidistance)*float(vraidistance)))
    label4.configure(text="la force entre les deux astres (rouge et bleu) est de : "+str(force))
    label5.configure(text="la force entre les deux astres (jaune et bleu) est de : "+str(force2))
    distance40 = str(x1-x3)
    distance41 =str(y1-y3)
    vraidistance4 = str((sqrt((int(distance40)*int(distance40))+(int(distance41)*int(distance41)))))
    force3 = (1*20*10)/(float(vraidistance4)*float(vraidistance4))
    label6.configure(text="la force entre les deux astres (jaune et rouge) est de : "+str(force3))
    


def avance2(gd, hb):
    global x1, y1, x2, y2, x3, y3, vraidistance
    x2, y2 = x2 +gd, y2+hb
    can1.coords(oval2, x2+20,y2+20, x2, y2)
    distance = str(x1-x2)
    label2.configure(text=distance0+distance)
    distance2 = str(y1-y2)
    label1.configure(text=distance00+distance2)
    vraidistance = str((sqrt((int(distance)*int(distance))+(int(distance2)*int(distance2)))))
    label3.configure(text="la distance entre les astres (rouge et bleu) est de "+vraidistance)
    
    distance30 = str(x2-x3)
    distance31 =str(y2-y3)
    vraidistance3 = str((sqrt((int(distance30)*int(distance30))+(int(distance31)*int(distance31)))))
    force2 = (1*10*10)/(float(vraidistance3)*float(vraidistance3))
    force = (1*10*20)/float((float(vraidistance)*float(vraidistance)))
    label4.configure(text="la force entre les deux astres (rouge et bleu) est de : "+str(force))
    label5.configure(text="la force entre les deux astres (jaune et bleu) est de : "+str(force2))
    distance40 = str(x1-x3)
    distance41 =str(y1-y3)
    vraidistance4 = str((sqrt((int(distance40)*int(distance40))+(int(distance41)*int(distance41)))))
    force3 = (1*20*10)/(float(vraidistance4)*float(vraidistance4))
    label6.configure(text="la force entre les deux astres (jaune et rouge) est de : "+str(force3))



#gestionnaire d'événements
def depl_gauche():
    avance(-10, 0)

def depl_droite():
    avance(10, 0)

def depl_haut():
    avance(0, -10)

def depl_bas():
    avance(0, 10)

def depl_gauche2():
    avance2(-10, 0)

def depl_droite2():
    avance2(10, 0)

def depl_haut2():
    avance2(0, -10)

def depl_bas2():
    avance2(0, 10)

#programmePrincipal
#les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10 #coordonnée initiale.
x2, y2 = 40, 40
x3, y3 = 100, 100
astrechoisie = 0
#création du widget principal maître:
fen1=Tk()
fen1.title("Exercice d'animation avec Tkinter")

distance0 = "la distance est sur l'axe X de "
distance = str(x1-x2)
distance00 = "la distance est sur l'axe Y de "
distance2 = str(y1-y2)
vraidistance = str((sqrt((int(distance)*int(distance))+(int(distance2)*int(distance2)))))
force = (1*10*20)/(float(vraidistance)*float(vraidistance))

distance30 = str(x2-x3)
distance31 =str(y2-y3)
vraidistance3 = str((sqrt((int(distance30)*int(distance30))+(int(distance31)*int(distance31)))))
force2 = (1*10*10)/(float(vraidistance3)*float(vraidistance3))


distance40 = str(x1-x3)
distance41 =str(y1-y3)
vraidistance4 = str((sqrt((int(distance40)*int(distance40))+(int(distance41)*int(distance41)))))
force3 = (1*20*10)/(float(vraidistance4)*float(vraidistance4))



#création de widget esclaves:
can1 = Canvas(fen1, bg= 'dark grey', height=300, width=300)
oval1 = can1.create_oval(x1, y1, x1+30, y1+30, width=2, fill='red')
oval2 = can1.create_oval(x2+10, y2+10, x2+30, y2+30, width=2, fill='blue')
oval3 = can1.create_oval(x3+10, y3+10, x3+30, y3+30, width=2, fill='yellow')
label1 = Label(fen1, text=distance00+distance2)
label1.pack(fill=BOTH,)
label2 = Label(fen1, text=distance0+distance)
label2.pack(fill=BOTH,)
label3 = Label(fen1, text="la distance entre les astres est de "+vraidistance)
label3.pack(fill=BOTH,)
label4 = Label(fen1, text="la force entre les deux astres est de : "+str(force))
label4.pack(fill=BOTH,)
label5 = Label(fen1, text="la force entre les deux astres (jaune et bleu) est de : "+str(force2))
label5.pack(fill=BOTH,)
label6 = Label(fen1, text="la force entre les deux astres (jaune et rouge) est de : "+str(force3))
label6.pack(fill=BOTH,)

can1.pack(side=LEFT)
Button(fen1, text='Quitter', command=fen1.quit).pack(side=BOTTOM)
Button(fen1, text='gauche', command=depl_gauche).pack()
Button(fen1, text='droite', command=depl_droite).pack()
Button(fen1, text='haut', command=depl_haut).pack()
Button(fen1, text='bas', command=depl_bas).pack()
Button(fen1, text='gauche2', command=depl_gauche2).pack()
Button(fen1, text='droite2', command=depl_droite2).pack()
Button(fen1, text='haut2', command=depl_haut2).pack()
Button(fen1, text='bas2', command=depl_bas2).pack()


Button(fen1, text='astre1', command=pointeur1).pack()
Button(fen1, text='astre2', command=pointeur2).pack()
can1.bind("<Button-1>", poseastre)
chaine = Label(fen1)
chaine.pack()


#boucle pricipal

fen1.mainloop()