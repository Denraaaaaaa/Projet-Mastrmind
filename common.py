#!/usr/bin/env python3
import itertools # Import de Itertools, bibliothèque qui offre des fonctions pour créer des combinaisons et des permutations.

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']
# Notez que vos programmes doivent continuer à fonctionner si on change les valeurs par défaut ci-dessus

def evaluation(combinaison, solution):
    bp = 0                                   
    mp = 0
    recurrence = {} # Ce dictionnaire permettera de savoir combien de fois faudra-t-il traiter un element de la combinaison.
    assert type(combinaison) == str
    assert type(solution) == str
    assert len(combinaison) == len(solution) == LENGTH
    
    for couleur in combinaison:
        # solution.count(couleur) renvoi le nombre de fois où caractere est présent dans solution
        recurrence[couleur] = solution.count(couleur) 

    # On va d'abord parcourir le mot pour savoir combien de couleurs sont bien placés. On fait cela pour donner la priorité au couleurs bien placées lors de l'analyse du mot.
    # En effet un mot pourrait commencer par exemple par une couleur mal placés en trop et donc ne pas prendre en compte une potentielle couleur bien placé plus tard dans la solution
    for i in range(LENGTH):                  
        if combinaison[i] == solution[i]:
            bp += 1
            recurrence[combinaison[i]] -= 1 # À chaque fois qu'on en trouve un, on baisse son nombre d'apparition dans la solution  
    
    # Couleurs mal placées
    for k in range(LENGTH):                  
        if combinaison[k] in solution and recurrence[combinaison[k]] > 0: # recurrence[combinaison[k]] > 0 permet d'être sur qu'il y a encore le plot étudié de présent dans la solution
            mp += 1
            recurrence[combinaison[k]] -= 1  
            
    return (bp, mp)

def donner_possibles(combinaison, ev):
    combinaisons_possible = set() # Création de l'ensemble
    produit_cartesien = list(itertools.product(COLORS, repeat = LENGTH)) # Produit cartésien de COLORS avec elle même LENGTH-fois dans une liste.
    combinaisons_exhaustives = set(''.join(tup) for tup in produit_cartesien)
    
    for comb in combinaisons_exhaustives: 
        if evaluation(comb,combinaison) == ev: # Si comb est aussi proche de combinaison que combinaison est proche de la solution
            combinaisons_possible.add(comb) 
    return combinaisons_possible

def maj_possibles(comb_possible, combinaison, ev):
    obsolete = set() 
    for comb in comb_possible:
        if evaluation(comb,combinaison) != ev:
            obsolete.add(comb)
    return comb_possible - obsolete  # Renvoi comb_possible privé de obsolete

#%% Tests


# evaluation

# print(evaluation('BBCB', 'CCBB')) # resultat attendu : (1, 2) pour tester que les premiers B ne soient pas considérés comme mal placés 
# print(evaluation("ABCD", "ABCD")) # resultat attendu : (4, 0) pour tester que le programme marche lorsqu'il s'agit du bon mot
# print(evaluation("BACB", "DACB")) # resultat attendu : (3, 0) pour tester que le premier B ne soit pas compté comme mal placé
# print(evaluation("AAAA", "BBBB")) # resultat attendu : (0, 0) pour tester que le programme marche si il n'y aucun plot de correct
# print(evaluation("RRVB", "JORV")) # resultat attendu : (0, 2)
# print(evaluation(4555, "JORV")) # Pour verifier l'AssertionError


# donner_possible

# print(donner_possibles('RRVB',(0, 2)))


# maj_possible