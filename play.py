import common

def play(codemaker, codebreaker, quiet=False):
    """
    Fonction principale de ce programme :
    Fait jouer ensemble le codebreaker et le codemaker donnés en arguments
    Renvoie le nombre de coups joués pour trouver la solution

    Attention, il ne *doit* pas être nécessaire de modifier cette fonction 
    pour faire fonctionner vos codemaker et codebreaker (dans le cas contraire,
    ceux-ci ne seront pas considérés comme valables)
    """
    n_essais = 0
    codebreaker.init()
    codemaker.init()
    ev = None
    if not quiet:
        print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
    while True:
        combinaison = codebreaker.codebreaker(ev)
        # print(f"Combinaison : {combinaison}")
        # print(f"Combinaisons encore possibles : {codebreaker.combinaisons_encore_possible} , taille : {len(codebreaker.combinaisons_encore_possible)}")
        ev = codemaker.codemaker(combinaison)
        # print(f"Évualuation : {ev}")
        # print(f"Solution : {codemaker.solution}")
        n_essais += 1
        # print(f"nombre d'essai : {n_essais}")
        if not quiet:
            print("Essai {} : {} ({},{})".format(n_essais, combinaison, ev[0], ev[1]))
        if ev[0] >= common.LENGTH:
            if not quiet:
                print("Bravo ! Trouvé {} en {} essais".format(combinaison, n_essais))
            return n_essais

#%% Fonction play_log
def play_log(codemaker, codebreaker, nom_fichier, quiet=False):
    with open(nom_fichier, "w") as fichier : # Ouverture et fermeture du fichier après modifications en mode "w" pour « write »

        # Fonction play
        n_essais = 0
        codebreaker.init()
        codemaker.init()
        ev = None
        if not quiet:
            print('Combinaisons de taille {}, couleurs disponibles {}'.format(common.LENGTH, common.COLORS))
        while True:
            combinaison = codebreaker.codebreaker(ev)
            ev = codemaker.codemaker(combinaison)
            n_essais += 1
            fichier.write(str(combinaison) + "\n") # Écriture de la combinaison donnée dans le log
            fichier.write(str(ev) + "\n") # Écriture de l'évaluation reçue dans le log
            if not quiet:
                print("Essai {} : {} ({},{})".format(n_essais, combinaison, ev[0], ev[1]))
            if ev[0] >= common.LENGTH:
                if not quiet:
                    print("Bravo ! Trouvé {} en {} essais".format(combinaison, n_essais))
                return n_essais
       
#%% Partie
if __name__ == '__main__':
    # Les lignes suivantes sont à modifier / supprimer selon ce qu'on veut faire, quelques exemples :

    # Faire jouer ensemble codemaker0.py et codebreaker0.py pour 5 parties :
    import codebreaker0
    import codemaker0
    import codebreaker1
    import codemaker1
    import codebreaker2
    import codemaker2
    import codebreaker3
    
    #repetition = 4
    #for i in range(repetition):
    #    partie = play(codemaker1, codebreaker2, quiet = False)
    #    print(partie)
    
    # play_log(codemaker2, codebreaker2, "fichier_log.txt", quiet = False)

    #  Faire jouer un humain contre codemaker0.py :
    #import codemaker0
    #import human_codebreaker
    #play(codemaker0, human_codebreaker)

    # Et plus tard, vous pourrez faire jouer vos nouvelles version du codebreaker et codemaker :
    #import codebreaker2
    #import codemaker2
    #play(codemaker2, codebreaker2)

    # Ou encore :
    #import codebreaker1
    #import human_codemaker
    #play(human_codemaker, codebreaker1)
