import random
print("Bienvenue au jeu! Le juste prix.")
print("Le juste prix est entre 1 et 100.")
#affiche un nombre au hazard
juste_prix=random.randint(1, 100)
proposition = 0
limite = 10
compteur=1
#vérification de la proposition du joueur, tant que la proposition !=réponse
while proposition != juste_prix and compteur <= limite :
    print("Tentative", compteur,"sur", limite)
    proposition = input("Tu dois entrer un nombre.")
    proposition = int(proposition)
    if proposition < juste_prix:
        print("C'est plus")
    elif proposition > juste_prix:
        print("C'est moins")
    elif proposition == juste_prix:
        break
    compteur+=1
if proposition != juste_prix:
    print("Tu as perdu! Le jute prix était", juste_prix,"!")
else:
    print("Félicitations! Tu as trouvé le juste prix en", compteur,"tentatives!","C'était bien",juste_prix,"!")
