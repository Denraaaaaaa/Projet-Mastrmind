import common
import random

def init():
    """
    Une fonction qui ne fait rien... pour cette version triviale.
    Pour vos codebreaker plus avancés, c'est ici que vous pouvez initialiser
    un certain nombre de variables à chaque début de partie.
    """
    global traite
    traite = []


def codebreaker(evaluation):
    while True:
        """
        L'argument evaluation_p est l'évaluation qu'on reçoit pour la dernière
        combinaison qu'on a proposée (et vaut None si c'est le premier coup de la
        partie). Cette version n'utilise pas cette information, puisqu'
        elle joue au hasard.
        """
        combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH))
        if combinaison not in traite:
            traite.append(combinaison)
            return combinaison