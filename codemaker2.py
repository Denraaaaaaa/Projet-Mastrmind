import common
import random
import itertools

def init():
    global solution
    solution = ''
    global solutions_encore_possible
    produit_cartesien = list(itertools.product(common.COLORS, repeat = common.LENGTH))  # Produit cartésien de COLORS avec elle même LENGTH-fois dans une liste. Ce qui donc l'ensemble des combinaisons de taille LENGTH possibles de coleurs de COLORS
    solutions_encore_possible = set(''.join(tup) for tup in produit_cartesien)
    
def codemaker(combinaison):
    global solution
    global solutions_encore_possible
    assert type(combinaison) == str
    assert type(solution) == str
        
    for solution_possible in solutions_encore_possible:
        maximum = -1 # Maximum négatif pour être sur que n'importe quelle première solution sera acceptée car n >= 0.
        encore_possible_partiel = common.maj_possibles(solutions_encore_possible, combinaison, common.evaluation(combinaison, solution_possible))
        n = len(encore_possible_partiel)
        if n >= maximum:
            maximum = n
            solutions_encore_possible = encore_possible_partiel
            solution = solution_possible
            
    return common.evaluation(combinaison, solution)