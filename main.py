import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

file = open("data.txt", "r")
contenu = float(file.read())
print(contenu)


class UTRA_GRU_App:
    def __init__(self, root):
        self.root = root
        self.root.title("ULTRA GRU")
        self.root.geometry("500x700")
        self.root.configure(bg='white')
        
        # Variables
        self.hauteur_var = tk.DoubleVar()
        self.longueur_var = tk.DoubleVar(value=contenu)
        self.nb_poulies_var = tk.IntVar(value=0)
        self.force_var = tk.DoubleVar(value=0.0)
        self.masse_var = tk.DoubleVar()
        
        # Titre principal
        title_frame = tk.Frame(root, bg='white')
        title_frame.pack(pady=10)
        
        tk.Label(title_frame, text="ULTRA GRU", font=("Arial", 16, "bold"), bg='white').pack()
        tk.Label(title_frame, text="ON OFF", font=("Arial", 12), bg='white').pack()
        
        # Séparateur
        ttk.Separator(root, orient='horizontal').pack(fill='x', padx=20, pady=5)
        
        # Section hauteur
        hauteur_frame = tk.Frame(root, bg='white')
        hauteur_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(hauteur_frame, text="CHARGE SOULEVÉ A QUELLE HAUTEUR", 
                font=("Arial", 10, "bold"), bg='white').pack(anchor='w')
        tk.Label(hauteur_frame, text="Enter the height", font=("Arial", 9), bg='white').pack(anchor='w')
        
        entry_hauteur = tk.Frame(hauteur_frame, bg='white')
        entry_hauteur.pack(fill='x', pady=5)
        tk.Entry(entry_hauteur, textvariable=self.hauteur_var, width=15).pack(side='left', padx=(0, 10))
        tk.Button(entry_hauteur, text="Valider", command=self.valider_hauteur, 
                 bg='#E0E0E0', relief='flat').pack(side='left')
        
        # Section distance
        longueur_frame = tk.Frame(root, bg='white')
        longueur_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(longueur_frame, text="DISTANCE", 
                font=("Arial", 10, "bold"), bg='white').pack(anchor='w')
        tk.Label(longueur_frame, text="Actual distance", font=("Arial", 9), bg='white').pack(anchor='w')
        result_distance = tk.Frame(longueur_frame, bg='white')
        entry_distance = tk.Frame(longueur_frame, bg='white')
        result_distance.pack(fill='x', pady=5)
        tk.Label(result_distance, textvariable=self.longueur_var, 
                font=("Arial", 10), bg='white', width=10, relief='sunken').pack(side='left')
        
        # Section nombre de poulies
        poulies_frame = tk.Frame(root, bg='white')
        poulies_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(poulies_frame, text="NOMBRE DE POULIE NÉCESSAIRE", 
                font=("Arial", 10, "bold"), bg='white').pack(anchor='w')
        
        result_poulies = tk.Frame(poulies_frame, bg='white')
        result_poulies.pack(fill='x', pady=5)
        tk.Label(result_poulies, textvariable=self.nb_poulies_var, 
                font=("Arial", 10), bg='white', width=10, relief='sunken').pack(side='left')
        
        # Section force nécessaire
        force_frame = tk.Frame(root, bg='white')
        force_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(force_frame, text="LA FORCE NÉCESSAIRE POUR SOULÈVER", 
                font=("Arial", 10, "bold"), bg='white').pack(anchor='w')
        
        result_force = tk.Frame(force_frame, bg='white')
        result_force.pack(fill='x', pady=5)
        tk.Label(result_force, textvariable=self.force_var, 
                font=("Arial", 10), bg='white', width=10, relief='sunken').pack(side='left')
        tk.Label(result_force, text="N", font=("Arial", 10), bg='white').pack(side='left', padx=(5, 0))
        
        # Séparateur
        ttk.Separator(root, orient='horizontal').pack(fill='x', padx=20, pady=10)
        
        # Section CESI
        cesi_frame = tk.Frame(root, bg='white')
        cesi_frame.pack(pady=10)
        
        # Charger le logo CESI (s'il existe)
        logo_path = os.path.join("src", "cesi_logo.png")
        try:
            logo_image = Image.open(logo_path)
            logo_image = logo_image.resize((100, 50), Image.LANCZOS)
            self.cesi_logo = ImageTk.PhotoImage(logo_image)
            tk.Label(cesi_frame, image=self.cesi_logo, bg='white').pack()
        except:
            # Si le logo n'est pas trouvé, afficher du texte
            tk.Label(cesi_frame, text="CESI", font=("Arial", 16, "bold"), bg='white').pack()
        
        tk.Label(cesi_frame, text="ÉCOLE D'INGÉNIEURS", font=("Arial", 12), bg='white').pack()
        
        # Section dépôt de charge
        charge_frame = tk.Frame(root, bg='white')
        charge_frame.pack(pady=10)
        
        tk.Label(charge_frame, text="Veuillez déposer une charge", 
                font=("Arial", 12), bg='white').pack()
        tk.Label(charge_frame, text="NB : MAX = 300 KG", 
                font=("Arial", 10, "bold"), bg='white').pack()
        
        # Section valeur de la charge
        valeur_charge_frame = tk.Frame(root, bg='white')
        valeur_charge_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(valeur_charge_frame, text="LA VALEUR DE LA CHARGE", 
                font=("Arial", 10, "bold"), bg='white').pack(anchor='w')
        
        entry_charge = tk.Frame(valeur_charge_frame, bg='white')
        entry_charge.pack(fill='x', pady=5)
        tk.Entry(entry_charge, textvariable=self.masse_var, width=15).pack(side='left', padx=(0, 10))
        tk.Button(entry_charge, text="Calculer", command=self.calculer_tout, 
                 bg='#E0E0E0', relief='flat').pack(side='left')
        tk.Label(entry_charge, text="kg", font=("Arial", 10), bg='white').pack(side='left', padx=(5, 0))
    
    def valider_hauteur(self):
        try:
            hauteur = self.hauteur_var.get()
            if hauteur <= 0:
                messagebox.showerror("Erreur", "La hauteur doit être positive")
            elif hauteur > 4:
                messagebox.showerror("Erreur", "La hauteur ne peut pas dépasser 4 m")
            else:
                messagebox.showinfo("Succès", f"Hauteur validée: {hauteur} m")
        except:
            messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide")
    
    def valider_longueur(self):
        try:
            longueur = self.longueur_var.get()
            if longueur <= 0:
                messagebox.showerror("Erreur", "La longueur doit être positive")
            elif longueur > 3:
                messagebox.showerror("Erreur", "La longueur ne peut pas dépasser 3 m")
            else:
                messagebox.showinfo("Succès", f"Longueur validée: {longueur} m")
        except:
            messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide")
    
    def calculer_tout(self):
        try:
            # Vérifier la masse
            masse = self.masse_var.get()
            if masse <= 0:
                messagebox.showerror("Erreur", "La masse doit être positive")
                return
            if masse > 300:
                messagebox.showerror("Erreur", "La masse ne peut pas dépasser 300 kg")
                return
            
            # Vérifier la hauteur
            hauteur = self.hauteur_var.get()
            if hauteur <= 0 or hauteur > 4:
                messagebox.showerror("Erreur", "Veuillez d'abord entrer une hauteur valide (0-4 m)")
                return
            
            # Vérifier la longueur
            longueur = self.longueur_var.get()
            if longueur <= 0 or longueur > 3:
                messagebox.showerror("Erreur", "Veuillez d'abord entrer une longueur valide (0-3 m)")
                return
            
            # Calculs (exemple simplifié)
            g = 9.81  # gravité
            poids = masse * g  # en Newtons
            
            # Calcul du nombre de poulies nécessaires (capacité de 1000N par poulie)
            nb_poulies = max(1, int(poids / 1000) + (1 if poids % 1000 > 0 else 0))
            self.nb_poulies_var.set(nb_poulies)
            
            # Calcul de la force nécessaire par poulie
            force_par_poulie = poids / (nb_poulies * 2)
            self.force_var.set(round(force_par_poulie, 2))
            
            messagebox.showinfo("Calculs terminés", 
                               f"Pour une masse de {masse} kg:\n"
                               f"- Nombre de poulies: {nb_poulies}\n"
                               f"- Force par poulie: {round(force_par_poulie, 2)} N")
        
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = UTRA_GRU_App(root)
    root.mainloop()