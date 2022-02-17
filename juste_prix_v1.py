#importation de random-->genere des chiffres au hasard
import random
#affichage du message de bienvenue 
print("Bienvenue au jeu, Le juste prix")
#affiche un nombre au hazard
reponse=random.randint(1, 100)
#demader au jouer un prix
print("Entrer un chiffre entre 1 et 100")
proposition = input()
proposition = int(proposition)
#verification de la proposition du joueur, tant que la proposition !=reponse
while proposition != reponse:
    if proposition < reponse:
        print("C'est plus")
    if proposition > reponse:
        print("C'est moins")
    print("Entrer un chiffre")
    proposition = input()
    proposition = int(proposition)
print("Félicitation! Tu as trouvé le juste prix")