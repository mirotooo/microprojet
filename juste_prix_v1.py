#importation de random-->genere des chiffres au hasard
import random
#affichage du message de bienvenue 
print("Bienvenue au jeu, Le juste prix")
print("le juste prix est entre 1 et 100")
reponse=random.randint(1, 100)
#affiche un nombre au hazard
print("Nombre qu'il faut trouver", reponse)
#demader au jouer un prix
print("Entrer un chiffre entre 1 et 100")
proposition = input()
proposition = int(proposition)
#verification de la proposition du joueur

while proposition != reponse:
    if proposition < reponse:
        print("C'est plus")
    if proposition > reponse:
        print("C'est moins")
    print("Entrer un chiffre")
    proposition = input()
    proposition = int(proposition)
print("Félicitation! Tu as trouvé le juste prix")