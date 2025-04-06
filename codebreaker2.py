import common
import random

def init():
    global combinaisons_possible
    combinaisons_possible = set(c1 + c2 + c3 + c4 for c1 in common.COLORS for c2 in common.COLORS for c3 in common.COLORS for c4 in common.COLORS)
    global traite
    traite = []
    return

def codebreaker(evaluation):
    if evaluation == None:
        combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH))
        traite.append(combinaison)
        return combinaison
    else:  
        # Ici on transforme l'ensemble des combinaisons possible en une liste car la fonction random.choice ne marche pas avec des ensembles
        combinaison = random.choice(list(common.maj_possibles(combinaisons_possible, traite[-1], evaluation)))
        traite.append(combinaison)
        return combinaison

