import common

def check_codemaker(log):
    
    # Récupération des données du log dans une liste de string
    with open(log, 'r') as fichier_log:
        contenu = fichier_log.readlines() # de la forme ['comb\n', '(0,1)\n']
        
    # Dictionnaire qui va permettre de décrire la partie enregistrée dans le log
    game = {}
    for i in range(0, len(contenu), 2):
        game[contenu[i][:-1]] = contenu[i+1][:-1] # Clé : combinaison, valeur : évaluation lors de la partie. 
    solution = contenu[-2][:-1] # [:-1] sert à enlever le '\n' à la fin.
    
    for combinaison in game:
        if str(common.evaluation(combinaison, solution)) != game[combinaison]: # On verifie notre condition de 
            return False
    return True

print(check_codemaker("test.txt"))
