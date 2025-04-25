import common
import random

def init():
    global traite
    traite = [] # Stock les combinaisons traitées au cours de la partie


def codebreaker(evaluation):
    while True: # Pour que la fonction propose une autre combinaison si la combinaison précédente était déjà traitée
        combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH)) # Choix aléatoire

        # Si la combinaison est nouvelle
        if combinaison not in traite:
            traite.append(combinaison) # Mise à jour de traite
            return combinaison