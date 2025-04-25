import itertools # Import de Itertools, bibliothèque qui offre des fonctions pour créer des combinaisons et des permutations.
import time # Import de time une bibliothèque qui va permettre de mesurer des temps durant l'exécution du programme.

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']
# Notez que vos programmes doivent continuer à fonctionner si on change les valeurs par défaut ci-dessus

#%% Fonction evaluation
def evaluation(combinaison, solution):
    assert type(combinaison) == str
    assert type(solution) == str
    assert len(combinaison) == len(solution) == LENGTH
    bp = 0
    mp = 0
    combinaison_l = list(combinaison)
    solution_l = list(solution)

    # On va d'abord donner la priorité aux couleurs bien placées lors de l'analyse du mot.
    # En effet un mot pourrait commencer par exemple par une couleur mal placée en trop et donc ne pas prendre en compte une potentielle couleur bien placé plus tard dans la solution
    for i in range(LENGTH):                  
        if combinaison_l[i] == solution_l[i]: # Si la couleur est mal placée
            combinaison_l[i] = None # On la remplace par None pour ne plus avoir à la traiter
            solution_l[i] = None # Idem
            bp += 1
            
    # Couleurs mal placées
    for k in range(LENGTH):                  
        if (combinaison_l[k] in solution_l) and (combinaison_l[k] != None): # Si la couleur est encore présente dans la solution mais qu'il ne s'agit pas d'un None
            
            # solution_l.index(combinaison_l[k]) donne l'indice de la première occurence de combinaison_l[k] dans solution_l
            solution_l[solution_l.index(combinaison_l[k])] = None
            combinaison_l[k] = None
            mp += 1

    # Renvoi de l'évaluation
    return (bp, mp)

#%% Fonction donner_possible
def donner_possibles(combinaison, ev):
    combinaisons_possible = set() # Création de l'ensemble
    produit_cartesien = list(itertools.product(COLORS, repeat = LENGTH)) # Produit cartésien de COLORS avec elle même LENGTH-fois dans une liste.
    combinaisons_exhaustives = set(''.join(tup) for tup in produit_cartesien)
    
    for comb in combinaisons_exhaustives: 
        if evaluation(comb,combinaison) == ev: # Si comb est aussi proche de combinaison que combinaison est proche de la solution
            combinaisons_possible.add(comb) 
    return combinaisons_possible

#%% Fonction maj_possible
def maj_possibles(comb_possible, combinaison, ev):
    
    # Utilisation d'une copie temporaire pour éviter des problèmes lors de l'itération
    comb_a_supp = {comb for comb in comb_possible if evaluation(comb, combinaison) != ev} # Compréhension d'ensemble est plus optimisée que de faire une boucle 
    
    # Modifie directement comb_possible en supprimant tout les éléments de comb_a_supp qui sont dans comb_possible
    comb_possible.difference_update(comb_a_supp) 
    
    return comb_possible
