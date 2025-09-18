import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
import serial   # communication série avec Arduino

# --- CONFIG PORT ARDUINO ---
# ⚠️ Adapter le port série selon ton système :
#   Windows : "COM3" ou autre
#   Linux/Mac : "/dev/ttyUSB0" ou "/dev/ttyACM0"
arduino = serial.Serial('COM3', 9600, timeout=1) # Remplacer par les valeur de port du Arduino que j'ai


class UTRA_GRU_App:
    def __init__(self, root):
        self.root = root
        self.root.title("ULTRA GRU")
        self.root.geometry("500x700")
        self.root.configure(bg='white')
        
        # Variables
        self.hauteur_var = tk.DoubleVar()
        self.longueur_var = tk.DoubleVar(value=0.0)   # Distance en temps réel
        self.nb_poulies_var = tk.IntVar(value=0)
        self.force_var = tk.DoubleVar(value=0.0)
        self.masse_var = tk.DoubleVar()
        
        # Titre principal
        title_frame = tk.Frame(root, bg='white')
        title_frame.pack(pady=10)
        
        tk.Label(title_frame, text="ULTRA GRU", font=("Arial", 16, "bold"), bg='white').pack()
        tk.Label(title_frame, text="ON OFF", font=("Arial", 12), highlightcolor='red', bg='white').pack()
        
        # Séparateur
        ttk.Separator(root, orient='horizontal').pack(fill='x', padx=20, pady=5)
        
        # Section hauteur
        hauteur_frame = tk.Frame(root, bg='white')
        hauteur_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(hauteur_frame, text="CHARGE SOULEVÉE À QUELLE HAUTEUR", 
                font=("Arial", 10, "bold"), bg='white').pack(anchor='w')
        tk.Label(hauteur_frame, text="Enter the height", font=("Arial", 9), bg='white').pack(anchor='w')
        
        entry_hauteur = tk.Frame(hauteur_frame, bg='white', relief="sunken")
        entry_hauteur.pack(fill='x', pady=5)
        tk.Entry(entry_hauteur, textvariable=self.hauteur_var, width=15).pack(side='left', padx=(0, 10))
        tk.Button(entry_hauteur, text="Valider", command=self.valider_hauteur, 
                 bg='#E0E0E0', relief='flat').pack(side='left')
        
        # Section distance
        longueur_frame = tk.Frame(root, bg='white')
        longueur_frame.pack(pady=10, padx=20, fill='x')
        
        tk.Label(longueur_frame, text="DISTANCE (capteur ultrason)", 
                font=("Arial", 10, "bold"), bg='white').pack(anchor='w')
        tk.Label(longueur_frame, text="Actual distance", font=("Arial", 9), bg='white').pack(anchor='w')
        result_distance = tk.Frame(longueur_frame, bg='white')
        result_distance.pack(fill='x', pady=5)
        tk.Label(result_distance, textvariable=self.longueur_var, 
                font=("Arial", 10), bg='white', width=10, relief='sunken').pack(side='left')
        tk.Label(result_distance, text="cm", font=("Arial", 10), bg='white').pack(side='left', padx=(5, 0))
        
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
        
        logo_path = os.path.join("src", "cesi_logo.png")
        try:
            logo_image = Image.open(logo_path)
            logo_image = logo_image.resize((100, 100), Image.LANCZOS)
            self.cesi_logo = ImageTk.PhotoImage(logo_image)
            tk.Label(cesi_frame, image=self.cesi_logo, bg='white').pack()
        except:
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
    
        # Lancer la lecture du capteur Arduino
        self.lire_distance()

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
    
    def lire_distance(self):
        """Lire en continu la distance depuis Arduino et mettre à jour l'UI"""
        try:
            if arduino.in_waiting > 0:
                data = arduino.readline().decode('utf-8').strip()
                if data.replace('.', '', 1).isdigit():  # Vérifie nombre
                    distance = float(data)
                    self.longueur_var.set(distance)
                    # Optionnel : avertir si < 30 cm
                    if distance < 30:
                        messagebox.showwarning("Attention", f"Obstacle proche : {distance} cm")
        except:
            pass
        # relance après 500ms
        self.root.after(500, self.lire_distance)
    
    def calculer_tout(self):
        try:
            masse = self.masse_var.get()
            if masse <= 0:
                messagebox.showerror("Erreur", "La masse doit être positive")
                return
            if masse > 300:
                messagebox.showerror("Erreur", "La masse ne peut pas dépasser 300 kg")
                return
            
            hauteur = self.hauteur_var.get()
            if hauteur <= 0 or hauteur > 4:
                messagebox.showerror("Erreur", "Veuillez entrer une hauteur valide (0-4 m)")
                return
            
            g = 9.81
            poids = masse * g
            
            nb_poulies = max(1, int(poids / 1000) + (1 if poids % 1000 > 0 else 0))
            self.nb_poulies_var.set(nb_poulies)
            
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
