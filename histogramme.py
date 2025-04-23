import play
import codemaker0
import codebreaker0
import codebreaker1
import codemaker1
import codemaker2
import codebreaker2
import matplotlib.pyplot as plt

nb_parties = int(input("Combien de parties voulez vous simuler ?\n"))

y = []

codebreaker = int(input("Quel est le numéro du codebreaker ?\n"))
codemaker = int(input("Quel est le numéro du codemaker ?\n"))

print("Chargement\n")

for i in range(nb_parties):
    y.append(play.play(codemaker1,codebreaker0, True))
    
    pourcentage = 100*(i/nb_parties)
    if pourcentage%1==0:
        print(pourcentage,"%")

    
esperance=0
s = 0 
for i in y:
    s += i

esperance = s/nb_parties
E_th = input("Quelle est l'éspérance théorique ?\n")

print("Terminé ! L'espérance experimentale de la variable vaut", esperance)


# Création de l’histogramme
plt.figure(figsize=(10, 5))
plt.hist(y, bins=40, color='dodgerblue', edgecolor='black', alpha=1)
# plt.hist(y,bins=40, range = (0,8000))
plt.axvline(esperance, color='red', linestyle='dashed', linewidth=1, label=f'Esp. exp. = {esperance}')
plt.axvline(8**4, color='gold', linestyle='dashed', linewidth=1, label=f'Esp. théor. = {E_th}')

# Ajout des labels
plt.xlabel("Nombre d'essais avant réussite")
plt.ylabel("Fréquence")
plt.title(f"Distribution du nombre d'essais (codebreaker{codebreaker} contre codemaker{codemaker}) sur {nb_parties} essais")
plt.legend()
plt.grid()

# Sauvegarde de l'histogramme
plt.savefig(f"histogramme codebreaker{codebreaker} contre codemaker{codemaker} pour {nb_parties} essais esp.exp de {esperance}.png", transparent = True)

# Affichage de l’histogramme
plt.show()

