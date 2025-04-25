import common
import random
import itertools

def init():
    # Initialisation des variables globales
    global combinaisons_encore_possible 
    global traite
    traite = [] # Stock les combinaisons traitées au cours de la partie. Le dernier élément étant la dernière combinaison testé
    
    # Produit cartésien de COLORS avec elle-même LENGTH-fois dans une liste.
    produit_cartesien = list(itertools.product(common.COLORS, repeat = common.LENGTH)) # De la forme [('R', 'R', 'V', 'B'), ...]
    combinaisons_encore_possible = set(''.join(tup) for tup in produit_cartesien) # De la forme {'RRVB', ...}

def codebreaker(evaluation):
    global combinaisons_encore_possible
    global traite 
    
    # Première combinaison (cas de base)
    if evaluation == None :
        # Ici on transforme l'ensemble des combinaisons possible en une liste car la fonction random.choice ne marche pas avec des ensembles
        combinaison = random.choice(list(combinaisons_encore_possible))
        traite.append(combinaison)
        return combinaison
        
    # Cas général 
    else :
        combinaisons_encore_possible = common.maj_possibles(combinaisons_encore_possible, traite[-1], evaluation) # Mise à jour de l'ensemble des possible après l'évaluation
        # Idem ici
        combinaison = random.choice(list(combinaisons_encore_possible)) # Choix aléatoire parmis les possibles
        traite.append(combinaison) # Ajout à la liste des éléments traités
        
    return combinaison

#%% Tests

# init()
# print(codebreaker(None))
# print(traite)
# print(combinaisons_encore_possible, len(combinaisons_encore_possible))
# print(codebreaker((1,2)))
# print(traite)
# print(combinaisons_encore_possible, len(combinaisons_encore_possible))
# init()
# print(traite)
# print(combinaisons_encore_possible, len(combinaisons_encore_possible))
