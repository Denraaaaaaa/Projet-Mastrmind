#!/usr/bin/env python3
import itertools      # Import de Itertools, bibliothèque qui offre des fonctions pour créer des combinaisons et des permutations.

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']
# Notez que vos programmes doivent continuer à fonctionner si on change les valeurs par défaut ci-dessus

def evaluation(combinaison, solution):
    bp = 0                                   # bp pour "bien placé" 
    mp = 0                                   # mp pour "mal placé"
    recurrence = {}                          # Ce dictionnaire permettera de savoir combien de fois faudra-t-il traiter un element de la combinaison.
    assert type(combinaison) == str
    assert len(combinaison) == len(solution) == LENGTH    # Si la combinaison n'est pas de meme taille que la solution ce n'est pas une combinaison valide 
    
    for caractere in combinaison:            # pour chaque éléments de la combinaison
        recurrence[caractere] = solution.count(caractere) # solution.count(caractere) renvoi le nombre de fois où caractere est présent dans solution

    # On sait que maintenant les deux combinaisons sont de même taille 
    for i in range(LENGTH):                  # On va d'abord parcourir le mot pour savoir combien de plot sont bien placés. On fait cela pour donner la priorité au plot bien placé lors de l'analyse du mot.
                                             # En effet un mot pourrait commencer par exemple par une lettre mal placé en trop et donc ne pas prendre en compte une potentielle lettre bien placé plus tard dans la solution
        if combinaison[i] == solution[i]:
            bp += 1
            recurrence[combinaison[i]] -= 1  # À chaque fois qu'on en trouve un, on baisse son nombre d'apparition dans la solution
            
    for k in range(LENGTH):                  # On va ensuite chercher les plots mal placés
        if combinaison[k] in solution and recurrence[combinaison[k]] > 0:   # recurrence[combinaison[k]] > 0 permet d'être sur qu'il y a encore le plot étudié de présent dans la solution
            mp += 1
            recurrence[combinaison[k]] -= 1  # À chaque fois qu'on en trouve un, on baisse son nombre d'apparition dans la solution
            
    return (bp, mp)
    
# print(evaluation('BBCB', 'CCBB')) # resultat attendu : (1, 2) pour tester que les premiers B ne soient pas considérés comme mal placés 
# print(evaluation("ABCD", "ABCD")) # resultat attendu : (4, 0) pour tester que le programme marche lorsqu'il s'agit du bon mot
# print(evaluation("BACB", "DACB")) # resultat attendu : (3, 0) pour tester que le premier B ne soit pas compté comme mal placé
# print(evaluation("AAAA", "BBBB")) # resultat attendu : (0, 0) pour tester que le programme marche si il n'y aucun plot de correct
# print(evaluation("RRVB", "JORV")) # resultat attendu : (0, 2)
# print(evaluation(4555, "JORV")) # Pour verifier l'AssertionError


def donner_possibles(combinaison, ev):
    combinaisons_possible = set()                                              # Création de l'ensemble
    combinaisons = set(c1 + c2 + c3 + c4 for c1 in COLORS for c2 in COLORS for c3 in COLORS for c4 in COLORS)   # Ensemble des combinaisons de 4 couleurs possibles
    for comb in combinaisons: 
        if evaluation(comb,combinaison) == ev:
            combinaisons_possible.add(comb)
    return combinaisons_possible

# print(donner_possible('RRVB',(0, 2)))




def maj_possibles(comb_possible, combinaison, ev):
    if ev == None:
        return comb_possible
    for comb in comb_possible:
        if evaluation(comb,combinaison) != ev:
            comb_possible.remove(comb)
    return comb_possible
    
# print(maj_possibles(donner_possible('RRVB', (0, 1))), 'RRRR', (0, 0))
