print("Bienvenue !\n")
print(" - Tapez 1 pour convertir un décimal en binaire.")
print(" - Tapez 2 pour convertir un décimal en hexadécimal.")
print(" - Tapez 3 pour convertir un binaire en décimal.")
print(" - Tapez 4 pour convertir un hexadécimal en décimal.")
print(" - Tapez 'q' ou 'Q' pour quitter le programme.")
conv = input("\n> ")

# Gestion de la sortie du programme
if conv.lower() == 'q':
    print("Au revoir !")
else:
    conv = int(conv)
    
    # Conversion décimal en binaire
    if conv == 1:
        nbr = int(input("Entrez le nombre à convertir : "))
        rep = bin(nbr)
        print("Le nombre décimal",nbr,"est égal à",rep[2:],"en binaire.")
        
    # Conversion décimal en hexadécimal
    if conv == 2:
        nbr = int(input("Entrez le nombre à convertir : "))
        rep = hex(nbr)
        print("Le nombre décimal",nbr,"est égal à",rep[2:],"en hexadécimal.")
        
    # Conversion binaire en décimal
    if conv == 3:
        nbr = input("Entrez le nombre binaire à convertir : ")
        rep = int(nbr, 2)
        print("Le nombre binaire",nbr,"est égal à",rep,"en décimal.")
        
    # Conversion hexadécimal en décimal
    if conv == 4:
        nbr = input("Entrez le nombre hexadécimal à convertir : ")
        rep = int(nbr, 16)
        print("Le nombre hexadécimal",nbr,"est égal à",rep,"en décimal.")
        
    # Gestion du choix invalide
    if conv not in [1,2,3,4]:
        print("Choix invalide. Veuillez choisir un nombre entre 1 et 4 ou 'q' pour quitter.")