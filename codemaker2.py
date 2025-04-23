import common
import random
import itertools
import time 

def init():
    # Initialisation des variables globales
    global solution
    solution = '' # Initialisation vide de solution. car elle sera choisit plus tard et le codebreaker n'en a pas besoin pour sa première combinaison
    global solutions_encore_possible
    
    # Produit cartésien de COLORS avec elle même LENGTH-fois dans une liste.
    produit_cartesien = list(itertools.product(common.COLORS, repeat = common.LENGTH))  
    solutions_encore_possible = set(''.join(tup) for tup in produit_cartesien) # len(COLORS)^{LENGTH} éléments

# Nouveau codemaker
def codemaker(combinaison):
    global solution
    global solutions_encore_possible

    # Tests de conformité
    assert type(combinaison) == str
    assert type(solution) == str

    # Dictionnaire evaluations va stocker des evaluations (clé) et pour chaque clés une liste de solutions donnant cette évaluation (valeur).
    evaluations = {}
    maximum = -1 # maximum < 0 car len(evaluations[scores]) > 0 donc la première solution testée sera toujours la meilleure au début

    # Assignation des solutions possibles à leurs évaluations
    for solution_possible in solutions_encore_possible:
        ev = common.evaluation(combinaison, solution_possible) # On stock l'évaluation dans une variable pour ne pas avoir à la recalculer
        if ev in evaluations:
            evaluations[ev].append(solution_possible)
        else:
            evaluations[ev] = [solution_possible]

    for evaluation in evaluations:
        n = len(evaluations[evaluation]) # Nombre de solutions associées à ce score
        if n > maximum:
            maximum = n
            pire_evaluation = evaluation

    # à la fin de la boucle, pire_score stockera le score avec le plus grand nombre de solutions le donnant, l'adjectif pire est utilisé car il s'agit du pire score à obtenir pour le codebreaker.
    solution = random.choice(evaluations[pire_evaluation]) # Choix aléatoire d'une des bonnes solutions (peu importe laquelle puisqu'elles donnent la même évaluation)
    # Mise à jour de solutions_encore_possible
    solutions_encore_possible = common.maj_possibles(solutions_encore_possible, combinaison, pire_evaluation)

    return pire_evaluation

# # Ancien codemaker (trop lent) cf. compte rendu
# def codemaker(combinaison):
#     """
#     Ce qui va pas avec celle là : pour chaque solution je fait un copie de l'ensemble des 4096 possibiltés et puis je parcours beaucoup de fois encore_possible_partiel (dans maj_possible)
#     De plus je fais potentiellement des évluations pour rien
#     """
#     global solution
#     global solutions_encore_possible
#     assert type(combinaison) == str
#     assert type(solution) == str
#
#     # Début de l'exécution
#     start_time = time.time()
#     for solution_possible in solutions_encore_possible:
#
#         # Copie pour eviter des problèmes lors de l'itération
#         encore_possible_partiel = solutions_encore_possible.copy()
#         maximum = -1 # Maximum négatif pour être sur que n'importe quelle première solution sera acceptée car n >= 0.
#         ev = common.evaluation(combinaison, solution_possible) # Stock l'évaluation pour éviter des calculs inutiles
#
#         # Ensemble des solutions qui seront encore possible après avoir proposé la combinaison si solution_possible est solution.
#         encore_possible_partiel = common.maj_possibles(encore_possible_partiel, combinaison, ev)
#
#         n = len(encore_possible_partiel)
#
#         # Recherche de la solution donnant le plus de possiblités
#         if n >= maximum:
#             maximum = n
#             solution = solution_possible
#             ev_solution = ev
#             meilleur_encore_possible = encore_possible_partiel
#     # Fin de l'exécution
#     end_time = time.time()
#     print(f"\nTemps d'exécution de la recherche de la solution optimale : {end_time-start_time:.6f} secondes\n")
#
#     # Mise à jour des solutions encore possibles après l'évaluation
#     solutions_encore_possible = meilleur_encore_possible
#
#     return ev_solution
