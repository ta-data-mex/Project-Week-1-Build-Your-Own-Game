import numpy as np
import random

dicc_palabras = {'animal': ['cobaya', 'gato', 'conejo', 'huron', 'tigre', 'tortuga', 'camaron', 'aguila', 'lobo', 'gusano'],
                 'capital': ['paris', 'ontario', 'bolivia', 'madrid', 'brasilia', 'tokio', 'praga', 'singapur', 'moscu', 'berlin'],
                 'ironhack': ['ironhack', 'data', 'java', 'analisis', 'jupyter', 'pycharm', 'mongodb', 'python', '']}
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']


def nombre(jugador):
    jugador = input('Nombre Jugador:')
    return 'Bienvenido ' + jugador + '¡Prepárate para jugar:'


matriz2 = np.ones((10, 10))
#print(matriz2)

matrizjuego = [None] * 10
for i in range(0,10):
    matrizjuego[i] = [None] * 10

for i in range(0,10):
    for j in range(0,10):
        matrizjuego[i][j] = alfabeto[random.randint(0,26)]

matrizjuego = np.array(matrizjuego)
print(matrizjuego)
