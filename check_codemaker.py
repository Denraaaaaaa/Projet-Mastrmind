import common

def check_codemaker(log):
    
    # Récupération des données du log dans une liste de string
    with open(log, 'r') as fichier_log:
        contenu = fichier_log.readlines() # de la forme ['comb\n', '(0,1)\n']
        
    # Dictionnaire qui va permettre de décrire la partie enregistrée dans le log
    game = {} # de la forme { combinaison : (évaluation) }

    for i in range(0, len(contenu), 2): # Toute les deux lignes
        game[contenu[i][:-1]] = contenu[i+1][:-1] # [:-1] sert à enlever le '\n' à la fin.
    solution = contenu[-2][:-1] # la solution est l'avant dernier élément de la liste
    
    for combinaison in game:
        if str(common.evaluation(combinaison, solution)) != game[combinaison]: # On vérifie notre condition de triche
            return False # Si codemaker triche on renvoi False
    return True # Si codemaker ne triche pas on renvoi True

#%% Tests

print(check_codemaker("test.txt"))










