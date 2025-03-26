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
    if combinaison == None:
        return solution
    else:
        for comb in combinaisons_possible:
            maxi = 0
            n = len(common.donner_possibles(combinaison, common.evaluation(combinaison, comb)))
            if n >= maxi:
                solution = comb
    return solution