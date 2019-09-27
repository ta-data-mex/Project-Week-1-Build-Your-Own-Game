import numpy as np
import random

# Diccionario de palabras a utilizar para llenar la sopa de letras
dicc_palabras = {'animal': ['cobaya', 'gato', 'conejo', 'huron', 'tigre', 'tortuga', 'camaron', 'aguila', 'lobo',
                            'gusano'],
                 'capital': ['paris', 'ontario', 'bolivia', 'madrid', 'brasilia', 'tokio', 'praga', 'singapur',
                             'moscu', 'berlin'],
                 'ironhack': ['ironhack', 'data', 'github', 'analisis', 'jupyter', 'pycharm', 'mongodb', 'python',
                              'alex', 'ramiro']}
alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z']  # para rellenar la matriz


encontradas = [] # Lista que guarda las palabras encontradas.


def elegir_tema_sopa(tema):
    tema = dicc_palabras[tema]
    return tema


# print(elegir_tema_sopa('animal'))
# print(elegir_tema_sopa('capital'))
# print(elegir_tema_sopa('ironhack'))

# return [['c', 'o', 'b', 'a', 'y', 'a'], ['g', 'a', 't', 'o'], ['c', 'o', 'n', 'e', 'j', 'o'],
def descomponer_array_tema(tema):
    tema = elegir_tema_sopa(tema) #lista de palabras del diccionario
    temp = []
    for item in tema:
        temp.append([i for i in item])
    print(temp)

    return temp


print('final: ', descomponer_array_tema('animal'))


def nombre(jugador):
    jugador = input('Nombre Jugador:')
    return 'Bienvenido ' + jugador + '¡Prepárate para jugar:'


def crearMatriz(num):
    n = num
    matrizjuego = [None] * n
    for i in range(len(matrizjuego)):
        matrizjuego[i] = [None] * n

    for i in range(0,n):
        for j in range(0,n):
            matrizjuego[i][j] = alfa[random.randint(0,26)]
    matrizjuego = np.array(matrizjuego)
    return matrizjuego


def info_pos_actual(matrix,nxn,esFila,pos):
    #Muestra y guarda la información de la posición del arreglo en la que se encuentra en una lista.
    temp_valores = []
    temp_espacios = 0

    for i in range(nxn):
        if esFila:
            if matrix[pos][i] != '':  #Es fila
                temp_valores.append(temp_espacios)
                temp_valores.append(matrix[pos][i])
            else:
                temp_espacios += 1
        else:
            if matrix[i][pos] != '':  #Es columna
                temp_valores.append(temp_espacios)
                temp_valores.append(matrix[i][pos])
                temp_espacios = 0
            else:
                temp_espacios += 1
    if temp_espacios == nxn:
        temp_valores.append(temp_espacios)
        temp_valores.append("0")
    return temp_valores






print(crearMatriz(18))

#def acomodar_palabra(nxn,matrix,palabras):

