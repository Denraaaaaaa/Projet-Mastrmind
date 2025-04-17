import common
import random

def init():
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))
    global combinaisons_possible
    combinaisons_possible = set(c1 + c2 + c3 + c4 for c1 in common.COLORS for c2 in common.COLORS for c3 in common.COLORS for c4 in common.COLORS)
    
def codemaker(combinaison):
    global solution
    global combinaisons_possible
    assert type(combinaison) == str
    for comb in combinaisons_possible:
        maximum = 0
        n = len(common.maj_possibles(combinaisons_possible, comb, common.evaluation(combinaison, comb)))
        if n >= maximum:
            solution = comb
            
    return common.evaluation(combinaison, solution)