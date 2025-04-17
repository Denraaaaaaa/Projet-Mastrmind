import common
import random

def init():
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))
    global solutions_encore_possible
    solutions_encore_possible = None
    
def codemaker(combinaison):
    global solution
    global solutions_encore_possible
    assert type(combinaison) == str
    assert type(solution) == str
    if solutions_encore_possible == None:
        solutions_encore_possible = common.donner_possibles(combinaison, common.evaluation(combinaison, solution))
        
    for solution_possible in solutions_encore_possible:
        maximum = 0
        
        n = len(common.maj_possibles(solutions_encore_possible, combinaison, common.evaluation(combinaison, solution_possible)))
        if n >= maximum:
            solution = solution_possible
            
    return common.evaluation(combinaison, solution)