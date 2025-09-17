import math
def nombrepoulies(poids, capacite):
    
    return math.ceil(poids/capacite)

fichier = open("data.txt", "r")
contenu = float(fichier.read())



#masse = float(input("Bonjour, veuillez entrer la masse en kg de la charge : "))
masse = contenu
hauteur = float(input("Veuillez entrer la hauteur en mètres de la grue : "))
distance = float(input("Veuillez entrer la distance en mètres à parcourir : "))
Cap_poulie = 1000

while (masse <= 0 or masse > 300) or (hauteur <= 0 or hauteur > 4) or (distance <= 0 or distance > 3):
    print("\n Les valeurs saisies sont incorrectes. Veuillez respecter les conditions :")
    print("- 0 < masse ≤ 300 kg")
    print("- 0 < hauteur ≤ 4 m")
    print("- 0 < distance ≤ 3 m\n")

    #masse = float(input("Entrez une masse valide : "))
    masse = float(fichier.read())
    hauteur = float(input("Entrez une hauteur valide : "))
    distance = float(input("Entrez une distance valide : "))

print("\n Données validées :")
print(f"Masse : {masse} kg")
print(f"Hauteur : {hauteur} m")
print(f"Distance : {distance} m")

poids = float( masse * 10)
nbpoulies= nombrepoulies(poids, Cap_poulie)
print(f"\n Le poids de la charge est de {poids} N.")
print(f"Le nombre de poulies nécessaires est de : {nbpoulies}.")
print(f" La force neccessaire pour soulever la charge est de {poids/nbpoulies} N.")
fichier.close()