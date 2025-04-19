#!/usr/bin/env python3
import itertools # Import de Itertools, bibliothèque qui offre des fonctions pour créer des combinaisons et des permutations.

LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']
# Notez que vos programmes doivent continuer à fonctionner si on change les valeurs par défaut ci-dessus

def evaluation(combinaison, solution):
    bp = 0                                   
    mp = 0
    
    # assert type(combinaison) == str
    # assert type(solution) == str
    assert len(combinaison) == len(solution) == LENGTH
    
    combinaison_l = list(combinaison)
    solution_l = list(solution)

    # On va d'abord parcourir le mot pour savoir combien de couleurs sont bien placés. On fait cela pour donner la priorité au couleurs bien placées lors de l'analyse du mot.
    # En effet un mot pourrait commencer par exemple par une couleur mal placés en trop et donc ne pas prendre en compte une potentielle couleur bien placé plus tard dans la solution
    for i in range(LENGTH):                  
        if combinaison_l[i] == solution_l[i]:
            combinaison_l[i] = None
            solution_l[i] = None
            bp += 1
            
    # Couleurs mal placées
    for k in range(LENGTH):                  
        if (combinaison_l[k] in solution_l) and (combinaison_l[k] != None): # Si la couleur est encore présente dans la solution
            
        # solution_l.index(combinaison_l[k]) donne l'indice de la première occurence de combinaison_l[k] dans solution_l
            solution_l[solution_l.index(combinaison_l[k])] = None 
            
            # On aurait pu utiliser un dictionnaire d'occurences plutot que de chercher l'indice de la couleur dans solution_l
            # Cependant après avoir comparer les temps d'exécution des deux méthodes sur des listes de petites taille, l'utilisation d'index est plus optimisée, 
            # Cette utilisation d'index donne cependant à la boucle des couleurs mal placées une complexité en O(n^2) pour O(n) pour un dictionnaire d'occurences
            # Les dictionnaires seraient donc plus optimisés pour des combinaisons de grande taille or ce n'est pas le cas de la mastermind donc on utilise ici .index.
            
            combinaison_l[k] = None
            mp += 1
            
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
import time

def test_evaluation():
    # Calcul un temps moyen d'execution car la fonction evaluation s'execute trop rapidement pour pouvoir etre mesuré en une fois
    # Par exemple :
        
    # start_time = time.time()
    # ev = evaluation('BBCB', 'CCBB')  
    # end_time = time.time()
    # print(f"Évaluation : {ev}")
    # print(f"Temps d'exécution : {end_time - start_time:.20f} secondes")
    
    # Va renvoyer :
        
    # Évaluation : (1, 2)
    # Temps d'exécution : 0.00000000000000000000 secondes
    
    def mesurer_temps_moyen(combinaison, solution, repetitions=100000):
        start_time = time.time() # Début
        for i in range(repetitions):
            evaluation(combinaison, solution)
        end_time = time.time() # Fin
        temps_total = end_time - start_time  # Temps total écoulé
        return temps_total / repetitions  # Temps moyen d'exécution

    print("Test 1 :")
    temps_moyen = mesurer_temps_moyen('BBCB', 'CCBB')
    print(f"Évaluation : {evaluation('BBCB', 'CCBB')}") # résultat attendu : (1, 2) pour tester que les premiers B ne soient pas considérés comme mal placés
    print(f"Temps moyen d'exécution : {temps_moyen:.10f} secondes")

    print("Test 2 :")
    temps_moyen = mesurer_temps_moyen("ABCD", "ABCD")
    print(f"Évaluation : {evaluation('ABCD', 'ABCD')}") # résultat attendu : (4, 0) pour tester que le programme marche lorsqu'il s'agit du bon mot
    print(f"Temps moyen d'exécution : {temps_moyen:.10f} secondes")

    print("Test 3 :")
    temps_moyen = mesurer_temps_moyen("BACB", "DACB")
    print(f"Évaluation : {evaluation('BACB', 'DACB')}") # résultat attendu : (3, 0) pour tester que le premier B ne soit pas compté comme mal placé
    print(f"Temps moyen d'exécution : {temps_moyen:.10f} secondes")

    print("Test 4 :")
    temps_moyen = mesurer_temps_moyen("AAAA", "BBBB")
    print(f"Évaluation : {evaluation('AAAA', 'BBBB')}") # résultat attendu : (0, 0) pour tester que le programme marche si il n'y aucun plot de correct
    print(f"Temps moyen d'exécution : {temps_moyen:.10f} secondes")

    print("Test 5 :")
    temps_moyen = mesurer_temps_moyen("RRVB", "JORV")
    print(f"Évaluation : {evaluation('RRVB', 'JORV')}") # résultat attendu : (0, 2)
    print(f"Temps moyen d'exécution : {temps_moyen:.10f} secondes")

    # print("Test 6 : Vérification des erreurs")
    # try:
    #     evaluation(4555, "JORV")  # Devrait lever une AssertionError
    # except AssertionError:
    #     print("Erreur détectée : combinaison doit être une chaîne de caractères.")

# Appelle la fonction de test
test_evaluation()

# donner_possible

# print(donner_possibles('RRVB',(0, 2)))


# maj_possible