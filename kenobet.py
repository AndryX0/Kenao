import random
import time
fichier_tirages = 'tirages.txt'

try:
    with open(fichier_tirages, 'r') as fichier:
        lignes = fichier.readlines()
        tirages_precedents = []
        for ligne in lignes:
            tirage = [int(x.strip()) for x in ligne.split(',') if x.strip().isdigit()]
            tirages_precedents.append(tirage)
except FileNotFoundError:
    print(f"Fichier {fichier_tirages} introuvable. Les résultats ne seront pas influencés.")
    tirages_precedents = []

tableau = list(range(1, 81))
temps_total = 5
vitesse = 0.001
nombres_choisis = []

start_time = time.time()
while len(nombres_choisis) < 20:
    if time.time() - start_time >= temps_total:
        break
    if random.random() < 0.4 and tirages_precedents:
        nombre = random.choice(random.choice(tirages_precedents))
    else:
        nombre = random.choice(tableau)

    if nombre not in nombres_choisis:
        nombres_choisis.append(nombre)

    time.sleep(vitesse)

print(f"Les 20 nombres choisis sont : {nombres_choisis}")