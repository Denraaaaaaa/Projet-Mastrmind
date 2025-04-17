import common
import random

def init():
    global combinaisons_encore_possible 
    combinaisons_encore_possible = None
    global traite
    traite = []
    return

def codebreaker(evaluation):
    global combinaisons_encore_possible
    global traite 
    
    if evaluation == None :
        combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH))
        traite.append(combinaison)
        return combinaison
      
    elif combinaisons_encore_possible == None :
        combinaisons_encore_possible = common.donner_possibles(traite[0], evaluation)
        
    else :
        combinaisons_encore_possible = common.maj_possibles(combinaisons_encore_possible, traite[-1], evaluation)
    
    # Ici on transforme l'ensemble des combinaisons possible en une liste car la fonction random.choice ne marche pas avec des ensembles
    combinaison = random.choice(list(combinaisons_encore_possible))
    print(combinaisons_encore_possible)
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
