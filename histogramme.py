import play
import codemaker1
import codebreaker0
import matplotlib.pyplot as plt

nb_parties = 10000

y = []

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

print("Terminé ! L'espérance experimentale de la variable vaut", esperance)


# Création de l’histogramme
plt.figure(figsize=(10, 5))
plt.hist(y, bins=40, color='dodgerblue', edgecolor='black', alpha=1)
# plt.hist(y,bins=40, range = (0,8000))
plt.axvline(esperance, color='red', linestyle='dashed', linewidth=1, label=f'Esp. exp. = {esperance}')
plt.axvline(8**4, color='gold', linestyle='dashed', linewidth=1, label=f'Esp. théor. = {8**4}')

# Ajout des labels
plt.xlabel("Nombre d'essais avant réussite")
plt.ylabel("Fréquence (normalisée)")
plt.title("Distribution du nombre d'essais (codebreaker0)")
plt.legend()
plt.grid()

# Affichage de l’histogramme
plt.show()

