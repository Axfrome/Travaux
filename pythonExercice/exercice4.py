from tkinter import *
fen1 = Tk()

 #creation
Label(fen1, text ='premier champ :').grid(sticky=E)
Label(fen1, text ='deuxieme :').grid(sticky=E)
Label(fen1, text ='troisième :').grid(sticky=E)
entr1 =Entry(fen1)
entr2 =Entry(fen1)
entr3 =Entry(fen1)
entr1.grid(row =0, column =1)
entr2.grid(row =1, column =1)
entr3.grid(row =2, column =1)
chek1 = Checkbutton(fen1, text='case a cocher, pour voir')
chek1.grid(columnspan=2)

#création2
can1 = Canvas(fen1, width=160, height=160, bg='white')
can1.grid(row=0, column=2, rowspan=4, padx=10, pady=5)

#demarrage
fen1.mainloop()