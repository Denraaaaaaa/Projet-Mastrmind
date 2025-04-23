import common
import random
import itertools

def init():
    global combinaisons_encore_possible
    global traite
    traite = []

    # Produit cartésien de COLORS avec elle même LENGTH-fois dans une liste.
    combinaisons_encore_possible = set(''.join(tup) for tup in list(itertools.product(common.COLORS, repeat=common.LENGTH)))

def codebreaker(evaluation):
    global combinaisons_encore_possible
    global traite

    toutes_les_combinaisons = set(''.join(tup) for tup in list(itertools.product(common.COLORS, repeat=common.LENGTH)))

    # Si il ne s'agit pas de la première combinaison
    if evaluation != None:
        common.maj_possibles(combinaisons_encore_possible, traite[-1], evaluation)

    # De la forme { combinaison : taille de l'ensemble des possible dans le pire cas }
    combinaisons_anti_cheat = {} # Nomination d'anti-cheat car ici l'objectif va être de limiter les effets de la triche ou autrement dit du pire cas
    minimum = float('inf') # l'infini positif (pour être sûr d'être minoré dès la première proposition)

    for combinaison in toutes_les_combinaisons : # Pour chaque combinaisons parmis les len(common.COLORS)^{LENGTH}

        # On va procéder comme dans le codemaker2
        evaluations_pire_cas = {}
        maximum = -1

        # On va prédire la taille de l'ensemble des combinaisons possibles après l'évaluation donnée dans le pire cas
        for solution_possible in combinaisons_encore_possible:
            ev = common.evaluation(combinaison, solution_possible) # On stock l'évaluation dans une variable pour ne pas avoir à la recalculer
            if ev in evaluations_pire_cas:
                evaluations_pire_cas[ev].append(solution_possible)
            else:
                evaluations_pire_cas[ev] = [solution_possible]

        # Nombre de solutions restantes dans le pire cas
        for evaluation in evaluations_pire_cas:
            n = len(evaluations_pire_cas[evaluation]) # Nombre de solutions restantes après l'évaluation
            if n > maximum:
                maximum = n 

        combinaisons_anti_cheat[combinaison] = n

    # Recherche de la taille minimale
    for combinaison in combinaisons_anti_cheat:
        n = combinaisons_anti_cheat[combinaison]
        if n < minimum:
            minimum = n

    # L'utilisation de compréhension de listes est plus optimisée que de faire une boucle. Utilisation de listes et pas d'ensembles car random.choice ne marche pas avec les ensembles
    bonnes_combinaisons = [combi for combi in combinaisons_anti_cheat if combinaisons_anti_cheat[combi] == n]
    bonnes_combinaisons_possible = [combi for combi in bonnes_combinaisons if combi in combinaisons_encore_possible]

    if not bonnes_combinaisons_possible: # Si la liste est vide
        combinaison = random.choice(bonnes_combinaisons)
    else: # Si elle n'est pas vide il vaut toujours mieux utiliser une combinaison possible
        combinaison = random.choice(bonnes_combinaisons_possible)

    traite.append(combinaison)
    return combinaison