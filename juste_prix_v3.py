import random
print("Bienvenue au juste prix!")
print("Choisissez votre mode de jeu: Facile (f) Normal (n) Personnalisé (p)")
mode = input()
if mode != "f" and mode != "n" and mode != "p":
    print("Mode invalide! Mode par défaut: facile")
    mode = "f"
limite = 0
prix = 100
if mode == "p":
    print("Choisissez le prix maximal:")
    prix = int(input())
    print("Choisissez le nombre de tentatives:")
    limite = int(input())
elif mode == "n":
    limite = 10

print("Le juste prix est entre 1 et", prix)
juste_prix = random.randint(1, prix)
proposition = 0
compteur=1
#vérification de la proposition du joueur, tant que la proposition !=réponse
while proposition != juste_prix:
    if mode != 'f' and compteur > limite and limite != 0:
        break
    if mode == "f" or limite == 0:
        print("Tentative ", compteur)
    else:
        print("Tentative ", compteur, " sur ", limite)
    print("Entrez un chiffre")
    proposition = input()
    proposition = int(proposition)
    if proposition < juste_prix:
        print("C'est plus")
    elif proposition > juste_prix:
        print("C'est moins")
    elif proposition == juste_prix:
        break
    
    compteur+=1

if proposition != juste_prix:
    print("Tu as perdu! Le juste prix était",juste_prix)
else:
    print("Félicitations! Tu as trouvé le juste prix en", compteur, "tentatives!")
