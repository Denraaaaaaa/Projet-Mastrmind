import common
import random
import itertools
import time 

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
    
    start_time = time.time()
    for solution_possible in solutions_encore_possible:
        maximum = -1 # Maximum négatif pour être sur que n'importe quelle première solution sera acceptée car n >= 0.
        ev = common.evaluation(combinaison, solution_possible)
        
        # Ensemble des solutions qui seront encore possible après avoir proposé la combinaison si solution_possible est solution.
        encore_possible_partiel = common.maj_possibles(solutions_encore_possible, combinaison, ev)
        n = len(encore_possible_partiel)
        
        # Recherche de la solution donnant le plus de possiblités 
        if n >= maximum:
            maximum = n
            solution = solution_possible 
            ev_solution = ev
            meilleur_encore_possible = encore_possible_partiel
    end_time = time.time()
    print(f"\nTemps d'exécution de la recherche de la solution optimale : {end_time-start_time:.6f} secondes\n")
    
    # Mise à jour des solutions encore possibles après l'évaluation
    solutions_encore_possible = meilleur_encore_possible
    
    return ev_solution
