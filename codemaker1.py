import common
import random # Import de la bibliothèque random pour faire des choix aléatoires

def init():
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH)) # Choix aléatoire de la solution
    
def codemaker(combinaison):
    global solution
    return common.evaluation(combinaison, solution) # Évaluation de la combinaison par rapport à la solution