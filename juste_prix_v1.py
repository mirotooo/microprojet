import random
print("Bienvenue au juste prix!")
#affiche un nombre au hazard
juste_prix =random.randint(1, 100)
print("Entrer un chiffre entre 1 et 100")
proposition = input()
proposition = int(proposition)
#vérification de la proposition du joueur, tant que la proposition !=réponse
while proposition != juste_prix:
    if proposition < juste_prix:
        print("C'est plus")
    if proposition > juste_prix:
        print("C'est moins")
    print("Entrer un chiffre")
    proposition = input()
    proposition = int(proposition)
print("Félicitations! Tu as trouvé le juste prix qui est",juste_prix)
