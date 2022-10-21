import random

borne_min = 0
borne_max = 100


# je definis une fonction pour choisir les bornes min et max
def borne():
    global borne_min
    global borne_max
    # je demande a l utilisateur s il veut choisir les bornes
    choix_borne = input("Voulez vous choisir vos bornes ? Oui(O) Non(N) :")
    if choix_borne.upper() == "O":
        borne_min = int(input("Quelle est votre borne minimale :"))
        borne_max = int(input("Quelle est votre borne maximale :"))
        # si la borne max est plus petite que la min, j inverse les deux
        if borne_min > borne_max:
            borne_min, borne_max = borne_max, borne_min
            # j en retourne le resultat
        return borne_min, borne_max


borne()
# le texte de base est modifie en fonction des bornes min et max
print(f"J’ai choisi un nombre au hasard entre {borne_min} et {borne_max}.")
print("À vous de le deviner...")
guess = 0
final_answer = "O"
value = 0


def choose_number():
    global value
    # le nombre a deviner est choisis entre la borne min et max
    value = random.randint(borne_min, borne_max)
    return value


# tant que le joueur fait une nouvelle partie, la parti recommence
while final_answer.upper() == "O":
    choose_number()
    guess_count = 0
    # tant que l'essai n est pas egal au nombre secret, j execute le code
    while guess != value:
        guess = int(input("Entrez votre essai : "))
        if guess > value:
            print(f"Mauvaise choix, le nombre est plus petit que {guess}")
            guess_count += 1
        elif guess < value:
            print(f"Mauvais réponse, le nombre est plus grand que {guess}")
            guess_count += 1
        else:
            guess_count += 1
            print("Bravo ! Bonne réponse.")
            print(f"Vous avez reussis en : {guess_count} essai(s).")
            final_answer = input("Souhaitez vous faire une nouvelle partie Oui (O) Non (N): ")
            # si l utilisateur souhaite recommencer la partie, nous executons le meme code une deuxieme fois
            if final_answer.upper() == "O":
                borne()
                print(f"J’ai choisi un nombre au hasard entre {borne_min} et {borne_max}.")
                print("À vous de le deviner...")
            else:
                print("Vous avez quittez le jeu.")
