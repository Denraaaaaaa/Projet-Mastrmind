import common
import play
import codebreaker1
import codemaker1
import codebreaker2
import codemaker2
import codebreaker3
import check_codemaker

# Tests des différentes fonctions du projet

#%% Fonction evaluation
assert common.evaluation('BBCB', 'CCBB') == (1,2)
assert common.evaluation('ABCD', 'ABCD') == (4,0)
assert common.evaluation('BACB', 'DACB') == (3,0)
assert common.evaluation('AAAA', 'BBBB') == (0,0)
assert common.evaluation('RRVB', 'JORV') == (0,2)
assert common.evaluation("RRBB", "RRBB") == (4, 0)
assert common.evaluation("RRBB", "BBRR") == (0, 4)
assert common.evaluation("RRBB", "RBBR") == (2, 2)
assert common.evaluation("RRBB", "GGYY") == (0, 0)
try:
    common.evaluation(4555, "JORV")  # Devrait lever une AssertionError
except AssertionError:
    print("Erreur détectée : combinaison doit être une chaîne de caractères.")

#%% Fonction donner_possibles
possibles = common.donner_possibles("RRBB", (4, 0))
assert "RRBB" in possibles  # RRBB doit être dans les possibilités
assert len(possibles) == 1  # Si l'évaluation est (4, 0), seule "RRBB" est possible

#%% Fonction play_log (on vérifie que le fichier est bien changé)
play.play_log(codemaker2, codebreaker2, "fichier_log.txt", quiet = False)

#%% Fonction maj_possibles
possibles = set(["RRBB", "BBRR", "RBBR", "GGYY"])
actuel = common.maj_possibles(possibles, "RRBB", (1, 2))
assert "RRBB" not in actuel  # RRBB ne correspond pas à l'évaluation

#%% Fonction codemaker1
codemaker1.init()
assert codemaker1.codemaker('RRRR') == common.evaluation('RRRR', codemaker1.solution)
assert codemaker1.codemaker('BBCB') == common.evaluation('BBCB', codemaker1.solution)
codemaker1.init()
solution = codemaker1.solution
assert len(solution) == common.LENGTH  # La solution doit avoir la bonne longueur
evaluation = codemaker1.codemaker(solution)
assert evaluation == (common.LENGTH, 0)  # La solution doit être parfaitement correcte

#%% Fonction codebreaker1
codebreaker1.init()
combinaison = codebreaker1.codebreaker(None)
assert len(combinaison) == common.LENGTH  # La combinaison doit avoir la bonne longueur

#%% Fonction codebreaker2
codebreaker2.init()
combinaison = codebreaker2.codebreaker(None)
assert len(combinaison) == common.LENGTH  # La combinaison doit avoir la bonne longueur

#%% Fonction codemaker2
codemaker2.init()
solution = codemaker2.solution
assert len(solution) == 0  # Au départ, la solution est vide
combinaison = "RRBB"
evaluation = codemaker2.codemaker(combinaison)
assert isinstance(evaluation, tuple)  # L'évaluation doit être un tuple
assert len(evaluation) == 2  # Le tuple doit contenir deux éléments

#%% Fonction check_codemaker
with open("fichier_log.txt", "w") as log:
    log.write("RRBB\n(4, 0)\n")
    log.write("RRBB\n(4, 0)\n")
assert check_codemaker.check_codemaker("fichier_log.txt") == True  # Le codemaker ne triche pas
