import common
import random

def init():
    """
    Cette fonction permet d'initialiser les vari'
    """
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))
    
def codemaker(combinaison):
    global solution
    return common.evaluation(combinaison, solution)