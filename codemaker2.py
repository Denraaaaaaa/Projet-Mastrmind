import common
import random
import itertools

def init():
    # Initialisation des variables globales
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))
    global solutions_encore_possible
    
    # Produit cartésien de COLORS avec elle même LENGTH-fois dans une liste.
    produit_cartesien = list(itertools.product(common.COLORS, repeat = common.LENGTH))  
    solutions_encore_possible = set(''.join(tup) for tup in produit_cartesien)
    
def codemaker(combinaison):
    global solution
    global solutions_encore_possible
    assert type(combinaison) == str
    assert type(solution) == str

    for solution_possible in solutions_encore_possible:
        maximum = -1 # Maximum négatif pour être sur que n'importe quelle première solution sera acceptée car n >= 0.
        
        # Ensemble des solutions qui seront encore possible après avoir proposé la combinaison si solution_possible est solution.
        encore_possible_partiel = common.maj_possibles(solutions_encore_possible, combinaison, common.evaluation(combinaison, solution_possible))
        n = len(encore_possible_partiel)
        
        # Recherche de la solution donnant le plus de possiblités 
        if n >= maximum:
            maximum = n
            solution = solution_possible
            
    # Mise à jour des solutions encore possibles après l'évaluation
    solutions_encore_possible = common.maj_possibles(solutions_encore_possible, combinaison, common.evaluation(combinaison, solution))
    return common.evaluation(combinaison, solution)