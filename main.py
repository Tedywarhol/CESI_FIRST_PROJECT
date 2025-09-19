import tkinter as tk
from tkinter import messagebox
import os

# ================== FENETRE PRINCIPALE 
ultraGru = tk.Tk()
ultraGru.geometry('720x360')
ultraGru.title("Ultra Gru")
ultraGru.configure(bg='#d9d9d9')
ultraGru.resizable(width=False, height=False)

# ================== VARIABLES ==================
hauteur = tk.IntVar()
masse = tk.IntVar()
distance_file = "distance.txt"   # fichier contenant la distance

# ================== FONCTIONS ==================
def demarrer():
    """Active l'interface et permet la saisie"""
    enterMasse.config(state="normal")
    enterHauteur.config(state="normal")
    validerMasse.config(state="normal")
    validerHauteur.config(state="normal")
    messagebox.showinfo("INFO", "Le calculateur est activé.\nEntrez la masse et la hauteur.")

def arreter():
    """Désactive l'interface et réinitialise"""
    enterMasse.config(state="disabled")
    enterHauteur.config(state="disabled")
    validerMasse.config(state="disabled")
    validerHauteur.config(state="disabled")
    distanceAffiche.config(text=" ")
    poulieAffiche.config(text=" ")
    forceAffiche.config(text=" ")
    messagebox.showinfo("INFO", "Le calculateur est désactivé.")

def calculer():
    """Calcule la force et le nombre de poulies"""
    try:
        m = masse.get()
        h = hauteur.get()

        # Vérifications limites
        if m <= 0 or h <= 0:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs positives.")
            return
        if m > 300:
            messagebox.showerror("Erreur", "Masse maximale : 300 Kg")
            return
        if h > 4:
            messagebox.showerror("Erreur", "Hauteur maximale : 4 m")
            return

        # Calcul force (Newton)
        g = 9.81
        F = m * g

        # Recommandation poulies (chaque poulie divise l’effort par 2)
        poulies = 0
        effort = F
        while effort > 200 and poulies < 3 :
            poulies += 1
            effort = F / (2 ** poulies)

        # Mise à jour affichage
        forceAffiche.config(text=f"{effort:.2f} N")
        poulieAffiche.config(text=f"{poulies}")

    except Exception as e:
        messagebox.showerror("Erreur", f"Problème de calcul : {e}")

def maj_distance():
    """Lit la distance depuis un fichier texte et met à jour l'affichage"""
    if os.path.exists(distance_file):
        try:
            with open(distance_file, "r") as f:
                d = f.read().strip()
                if d.isdigit():
                    distanceAffiche.config(text=f"{d} m")
                else:
                    distanceAffiche.config(text="Invalide")
        except:
            distanceAffiche.config(text="Erreur")
    ultraGru.after(1000, maj_distance)  # rafraîchit toutes les secondes

# ================== BOUTONS ON/OFF ==================
on = tk.Button(ultraGru, text='ON', font=('open sans', 15, 'bold'),
               fg='white', bg='black', command=demarrer)
on.place(x=5, y=20)

off = tk.Button(ultraGru, text='OFF', font=('open sans', 15, 'bold'),
                bg='white', fg='black', command=arreter)
off.place(x=50, y=20)

# ================== LOGO ==================
logoCESI = tk.PhotoImage(file='src/cesi_logo.png')
CESI = tk.Label(ultraGru, image=logoCESI, bg='#d9d9d9')
CESI.place(x=500, y=-50)

# ================== MASSE ==================
masseText = tk.Label(ultraGru, text='NB : MAX = 300 Kg',
                     font=('arial', 10, 'bold'), fg='red', bg='#d9d9d9')
masseText.place(x=550, y=150) 
masseText = tk.Label(ultraGru, text="LA VALEUR DE LA CHARGE",
                     font=('open sans', 10, 'bold'), bg='#d9d9d9', fg='black')
masseText.place(x=520, y=200)
enterMasse = tk.Entry(ultraGru, textvariable=masse,
                      font=('arial', 10, 'bold'), fg='white', bg='#545454', state="disabled")
enterMasse.place(x=520, y=220)
validerMasse = tk.Button(ultraGru, text='Valider',
                         font=('Arial', 8, 'bold'), fg='white', bg='black',
                         state="disabled", command=calculer)
validerMasse.place(x=620, y=218)

# ================== HAUTEUR ==================
hauteurText = tk.Label(ultraGru, text='CHARGE SOULEVÉ  A QUELLE HAUTEUR',
                       font=('open sans', 10, 'bold'), bg='#d9d9d9', fg='black')
hauteurText.place(x=5, y=70)
enterHauteur = tk.Entry(ultraGru, textvariable=hauteur,
                        font=('arial', 10, 'bold'), fg='white', bg='#545454', state="disabled")
enterHauteur.place(x=5, y=90)
validerHauteur = tk.Button(ultraGru, text='Valider',
                           font=('Arial', 8, 'bold'), fg='white', bg='black',
                           state="disabled", command=calculer)
validerHauteur.place(x=150, y=88)

# ================== DISTANCE ==================
distanceText = tk.Label(ultraGru, text='DISTANCE',
                        font=('open sans', 10, 'bold'), fg='black', bg='#d9d9d9')
distanceText.place(x=5, y=130)
distanceAffiche = tk.Label(ultraGru, text='                           ',
                           font=('open sans', 10, 'bold'), fg='black', bg='white', border='4')
distanceAffiche.place(x=5, y=150)

# ================== POULIES ==================
poulieText = tk.Label(ultraGru, text='NOMBRE DE POULIE NECESSAIRE',
                      font=('open sans', 10, 'bold'), fg='black', bg='#d9d9d9')
poulieText.place(x=5, y=190)
poulieAffiche = tk.Label(ultraGru, text='                           ',
                         font=('open sans', 10, 'bold'), fg='black', bg='white', border='4')
poulieAffiche.place(x=5, y=220)

# ================== FORCE ==================
forceText = tk.Label(ultraGru, text='FORCE NECESSAIRE POUR SOULEVER',
                     font=('open sans', 10, 'bold'), fg='black', bg='#d9d9d9')
forceText.place(x=5, y=260)
forceAffiche = tk.Label(ultraGru, text='                            ',
                        font=('open sans', 10, 'bold'), fg='black', bg='white', border='4')
forceAffiche.place(x=5, y=280)

# ================== LANCEMENT ==================
maj_distance()
ultraGru.mainloop()
