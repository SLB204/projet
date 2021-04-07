import tkinter as tk
import tkinter.font as tkFont

fen=tk.Tk()
fen.title('Compte bancaire')
fen.geometry("400x200")
fen.configure(bg='thistle')


bouton_compte = tk.Button (fen,text='Compte Bancaire',height=5, width=27,activebackground='light steel blue',command=fen.destroy)


bouton_compte.pack( padx=85,pady=85,side= 'bottom')


fen.mainloop()

 #_________________________________________________________ #

from tkinter import *
from tkinter.messagebox import *

def Verification():

    if Motdepasse.get() == 'projet2':

        showinfo('Résultat','Mot de passe correct.\nVeuillez appuyer sur OK pour pour être redirigé vers votre compte où vous pourrez convertir votre argent !')

        command= Mafenetre.destroy()

    else:

        showwarning('Résultat','Mot de passe incorrect.\nVeuillez recommencer !')
        Motdepasse.set('')


Mafenetre = Tk()
Mafenetre.title('Authentification')
Mafenetre.configure(bg='thistle')


Label1 = Label(Mafenetre, text = 'Mot de passe ')
Label1.pack(side = LEFT, padx = 5, pady = 5)


Motdepasse= StringVar()
Champ = Entry(Mafenetre, textvariable= Motdepasse, show='*')
Champ.focus_set()
Champ.pack(side = 'left', padx = 5, pady = 5)


Bouton = Button(Mafenetre, text ='Valider',activebackground='light steel blue', command = Verification)
Bouton.pack(side ='left', padx = 5, pady = 5)

Mafenetre.mainloop()

 #_____________________________________________________________ #


fenetre = tk.Tk()
fenetre.title("Convertisseur de cryptomonnaie")
fenetre.geometry("400x200")
fenetre.configure(bg='thistle')



frm_entry = tk.Frame(master=fenetre)
ent_prix = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="Cryptomonnaies")


ent_prix.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")


def cryptomonnaie_to_euro():
    cryptomonnaie = ent_prix.get()
    euro = (1000 * float(cryptomonnaie))
    label_result["text"] = f"{round(euro, 2)} euro"



btn_convert = tk.Button(master=fenetre, text="\N{RIGHTWARDS BLACK ARROW}", command=cryptomonnaie_to_euro)

label_result = tk.Label(master=fenetre, text="euros")


frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
label_result.grid(row=0, column=2, padx=10)


bouton_quitter = Button(fenetre, text='Quitter et déconnexion',activebackground='light steel blue', command=fenetre.destroy)
bouton_quitter.grid(row = 2, column =0, padx=3, pady=3, sticky =' sw')


fenetre.mainloop()
