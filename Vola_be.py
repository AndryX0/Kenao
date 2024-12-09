import random
import time

tableau = list(range(1, 81))


i = 0
temps_total = 5
vitesse = 0.001
nombres_choisis = []

start_time = time.time()
while len(nombres_choisis) < 20:
    if time.time() - start_time >= temps_total:
        break


    nombre = random.choice(tableau)

    if nombre not in nombres_choisis:
        nombres_choisis.append(nombre)

    i = (i + 1) % 80
    time.sleep(vitesse)

print(f"Les 20 nombres choisis sont : {nombres_choisis}")