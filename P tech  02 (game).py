from random import randint
trouver=0
valeur_rechercher=randint(0,100)
while True:
    valeur_saisie=int(input("saisissez une valeur entre 0 et 100"))
    if valeur_saisie == valeur_rechercher:
        print ("GG WP EZ WIN")
        break    
    if valeur_saisie<valeur_rechercher:
        print ("le chiffre est plus grand")
    if valeur_saisie>valeur_rechercher:
        print ("le chiffre est plus petit")

#Bonjour je suis un élevé de 1er pro et j'ai créé ce jeu très basic, mais c'est la première fois que je touche à du code. J'ai fait ce code en classe sur thonny avec l'entreprise IBM. Merci
                    
