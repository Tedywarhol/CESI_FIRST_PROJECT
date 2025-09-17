import tkinter as tk
from tkinter import messagebox

# Constantes
GRAVITE = 9.81  # m/s²
CAPACITE_POULIE = 1000  # N

class UTRA_GRU_App:
    def __init__(self, root):
        self.root = root
        self.root.title("UTRA GRU")
        self.root.geometry("500x600")
        
        # Variables
        self.hauteur_var = tk.DoubleVar()
        self.longueur_var = tk.DoubleVar()
        self.nb_poulies_var = tk.IntVar()
        self.force_var = tk.DoubleVar()
        self.masse_var = tk.DoubleVar()
        
        # Titre principal
        titre_frame = tk.Frame(root)
        titre_frame.pack(pady=10)
        
        tk.Label(titre_frame, text="UTRA GRU", font=("Arial", 16, "bold")).pack()
        tk.Label(titre_frame, text="ON OFF", font=("Arial", 12)).pack()
        
        # Section hauteur
        hauteur_frame = tk.LabelFrame(root, text="CHARGE SOULEVÉ A QUELLE HAUTEUR")
        hauteur_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(hauteur_frame, text="Hauteur (m):").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(hauteur_frame, textvariable=self.hauteur_var).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(hauteur_frame, text="Valider", command=self.valider_hauteur).grid(row=0, column=2, padx=5, pady=5)
        
        # Section longueur
        longueur_frame = tk.LabelFrame(root, text="CHARGE SOULEVÉ A QUELLE LONGUEUR")
        longueur_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(longueur_frame, text="Longueur (m):").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(longueur_frame, textvariable=self.longueur_var).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(longueur_frame, text="Valider", command=self.valider_longueur).grid(row=0, column=2, padx=5, pady=5)
        
        # Section nombre de poulies
        poulies_frame = tk.LabelFrame(root, text="NOMBRE DE POULIE NÉCESSAIRE")
        poulies_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(poulies_frame, text="Nombre de poulies:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(poulies_frame, textvariable=self.nb_poulies_var).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(poulies_frame, text="Valider", command=self.valider_poulies).grid(row=0, column=2, padx=5, pady=5)
        
        # Section force nécessaire
        force_frame = tk.LabelFrame(root, text="LA FORCE NÉCESSAIRE POUR SOULÈVER")
        force_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(force_frame, text="Force (N):").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(force_frame, textvariable=self.force_var).grid(row=0, column=1, padx=5, pady=5)
        
        # Section valeur de la charge
        charge_frame = tk.LabelFrame(root, text="La valeur de la charge")
        charge_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(charge_frame, text="Masse (kg) - MAX 300 kg:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(charge_frame, textvariable=self.masse_var).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(charge_frame, text="Calculer", command=self.calculer_force).grid(row=0, column=2, padx=5, pady=5)
        
        # Message de bienvenue
        bienvenue_frame = tk.Frame(root)
        bienvenue_frame.pack(pady=20)
        
        tk.Label(bienvenue_frame, text="Hello Bienvenue", font=("Arial", 14)).pack()
        tk.Label(bienvenue_frame, text="Veuillez déposer une charge", font=("Arial", 12)).pack()
        tk.Label(bienvenue_frame, text="NB : MAX = 300 KG", font=("Arial", 10, "bold")).pack()
        
    def valider_hauteur(self):
        try:
            hauteur = self.hauteur_var.get()
            if hauteur <= 0:
                messagebox.showerror("Erreur", "La hauteur doit être positive")
            else:
                messagebox.showinfo("Succès", f"Hauteur validée: {hauteur} m")
        except:
            messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide")
    
    def valider_longueur(self):
        try:
            longueur = self.longueur_var.get()
            if longueur <= 0:
                messagebox.showerror("Erreur", "La longueur doit être positive")
            else:
                messagebox.showinfo("Succès", f"Longueur validée: {longueur} m")
        except:
            messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide")
    
    def valider_poulies(self):
        try:
            nb_poulies = self.nb_poulies_var.get()
            if nb_poulies <= 0:
                messagebox.showerror("Erreur", "Le nombre de poulies doit être positif")
            else:
                messagebox.showinfo("Succès", f"Nombre de poulies validé: {nb_poulies}")
        except:
            messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide")
    
    def calculer_force(self):
        try:
            masse = self.masse_var.get()
            if masse <= 0:
                messagebox.showerror("Erreur", "La masse doit être positive")
                return
            if masse > 300:
                messagebox.showerror("Erreur", "La masse ne peut pas dépasser 300 kg")
                return
            
            # Calcul du poids (force due à la gravité)
            poids = masse * GRAVITE
            
            # Calcul du nombre de poulies nécessaires
            nb_poulies_necessaires = int(poids / CAPACITE_POULIE) + 1
            
            # Calcul de la force nécessaire par poulie
            force_par_poulie = poids / nb_poulies_necessaires
            
            # Mise à jour des variables
            self.nb_poulies_var.set(nb_poulies_necessaires)
            self.force_var.set(round(force_par_poulie, 2))
            
            messagebox.showinfo("Résultats", 
                               f"Pour une masse de {masse} kg:\n"
                               f"- Poids total: {round(poids, 2)} N\n"
                               f"- Nombre de poulies nécessaires: {nb_poulies_necessaires}\n"
                               f"- Force par poulie: {round(force_par_poulie, 2)} N")
        
        except:
            messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide")

if __name__ == "__main__":
    root = tk.Tk()
    app = UTRA_GRU_App(root)
    root.mainloop()