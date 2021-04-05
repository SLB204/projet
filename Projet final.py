import tkinter as tk
import tkinter.font as tkFont

fen=tk.Tk()
fen.title('Compte bancaire')
fen.geometry("400x200")
fen.configure(bg='blue')


bouton_compte = tk.Button (fen,text='Compte Bancaire',height=5, width=27,activebackground='yellow',command=fen.destroy)


bouton_compte.pack(side= tk.BOTTOM)

fen.mainloop()

fenetre = tk.Tk()
fenetre.title("Convertisseur de cryptomonnaie")
fenetre.geometry("400x200")
fenetre.resizable(width=False, height=False)




frm_entry = tk.Frame(master=fenetre)
ent_poids = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="Cryptomonnaies")




ent_poids.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")




btn_convert = tk.Button(
master=fenetre, text="\N{RIGHTWARDS BLACK ARROW}", command=cryptomonnaie_to_euro)

label_result = tk.Label(master=fenetre, text="euros")


frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
label_result.grid(row=0, column=2, padx=10)

def cryptomonnaie_to_euro():
    cryptomonnaie = ent_prix.get()
    euro = (1000 * float(cryptomonnaie))
    label_result["text"] = f"{round(euro, 2)} euro"



fen.mainloop()
