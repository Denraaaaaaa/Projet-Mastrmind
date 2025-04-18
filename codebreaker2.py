import common
import random

def init():
    # Initialisation des variables globales
    global combinaisons_encore_possible 
    global traite
    traite = []
    
    # Pour détecter la deuxième combinaison (cf. compte rendu pour la justification de ce choix)
    combinaisons_encore_possible = None 
    return

def codebreaker(evaluation):
    global combinaisons_encore_possible
    global traite 
    
    # Première combinaison (cas de base n°1)
    if evaluation == None :
        combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH))
        traite.append(combinaison)
        return combinaison
    
    # Deuxième combinaison (cas de base n°2)
    elif combinaisons_encore_possible == None :
        
        # Création de l'esemble des possibles car l'évaluation en argument est la première
        combinaisons_encore_possible = common.donner_possibles(traite[-1], evaluation) 
        
        # Ici on transforme l'ensemble des combinaisons possible en une liste car la fonction random.choice ne marche pas avec des ensembles
        combinaison = random.choice(list(combinaisons_encore_possible))
        traite.append(combinaison)
        
    # Cas général 
    else :
        combinaisons_encore_possible = common.maj_possibles(combinaisons_encore_possible, traite[-1], evaluation)
        
        # Idem ici
        combinaison = random.choice(list(combinaisons_encore_possible))
        traite.append(combinaison)
        
    return combinaison


#%% Tests

# init()
# print(codebreaker(None))
# print(traite)
# print(codebreaker((1,2)))
# print(traite)
# print(combinaisons_encore_possible, len(combinaisons_encore_possible))
# init()
# print(traite)
