import common
import tkinter as tk
from tkinter import messagebox
import codemaker1, codemaker2

# Couleurs autorisées et longueur de la combinaison (à adapter selon common.py)
COLORS = common.COLORS  # Red, Green, Blue, Yellow, Orange, Purple
LENGTH = common.LENGTH

# Une fonction factice d’évaluation pour tester l’interface
def evaluer_combinaison(proposition):
    return codemaker1.codemaker(proposition)

# Fonction appelée au clic sur "Valider"
def valider():
    combinaison = entry.get().upper()
    if len(combinaison) != LENGTH or any(c not in COLORS for c in combinaison):
        messagebox.showerror("Erreur", f"Entrez une combinaison de {LENGTH} lettres valides ({', '.join(COLORS)})")
        return
    nb_bien_place, nb_mal_place = evaluer_combinaison(combinaison)
    historique.insert(tk.END, f"{combinaison} → {nb_bien_place} bien placés, {nb_mal_place} mal placés")
    entry.delete(0, tk.END)

# Interface
fenetre = tk.Tk()
fenetre.title("Mastermind")

label = tk.Label(fenetre, text=f"Entrez une combinaison ({LENGTH} lettres parmi : {', '.join(COLORS)}) :")
label.pack(pady=10)

entry = tk.Entry(fenetre, font=("Algerian", 14), justify='center')
entry.pack(pady=5)

valider_btn = tk.Button(fenetre, text="Valider", command=valider)
valider_btn.pack(pady=10)

historique = tk.Listbox(fenetre, width=50)
historique.pack(pady=10)

fenetre.mainloop()