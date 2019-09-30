import numpy as np
import random

dicc_palabras = {'animal': ['cobaya', 'gato', 'conejo', 'huron', 'tigre'],  # Diccionario para llenar la sopa de letras
                 'capital': ['paris', 'ontario', 'berlin', 'madrid', 'brasilia'],
                 'ironhack': ['codigo', 'data', 'github', 'analisis', 'jupyter', ]}
alfa = ['b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z']  # para rellenar la matriz


def elegir_tema_sopa():  # Escoge un tema del diccionario de palabras
    switch = True  # Para control del while
    while switch:  # While para validar hasta que la opcion sea correcta;
        tema = input("Elige un tema para jugar entre 'animal' 'capital' o 'ironhack': ").lower()
        if tema == 'animal' or tema == 'capital' or tema == 'ironhack':
            switch = False
            return dicc_palabras[tema]  # Retorna las palabras del tema en el diccionario
        else:
            print("'Opcion inválida, elige un tema entre 'animal', 'capital' o 'ironhack' ")
            continue


def descomponer_array_tema():
    tema_list = elegir_tema_sopa() #lista de palabras del diccionario
    temp = []
    for item in tema_list:
        temp.append([i for i in item])  # Descompone cada palabra en caracteres y guarda cada palabra partida en lista
    matriztemp = np.array(temp) #  Convierte la lista con la palabra partida en un arreglo NUMPY

    return tema_list, temp  # Devuelve el arreglo de palabras descompuesta por caracter y la lista original


def crearMatriz(num):  # Funcion que define el tamaño de la matriz de juego y la inicializa con letras aleatorias
    n = num
    matrizjuego = [None] * n
    for i in range(len(matrizjuego)):
        matrizjuego[i] = [None] * n

    for i in range(0,n):
        for j in range(0, n):
            matrizjuego[i][j] = alfa[random.randint(0, 23)]  # Llenado desde la lista 'alfa'
    matrizjuego = np.array(matrizjuego)  # Convierte la lista en un arreglo Numpy
    return matrizjuego  # Devuelve una matriz NUMPY de nxn con letras del alfabeto aleatoriamente


def acomodar():
    switch = True
    while switch:
        lista, tema = descomponer_array_tema()
        sopa = crearMatriz(18)
        int_rndm = random.randint(2,8)
        int_rndm2 = random.randint(1,3)

        for x in range(len(tema)):
            for y in range(len(tema[x])):
                sopa[x*int_rndm2][y+int_rndm] = tema[x][y]
                switch = False
    numpysopa = np.array(sopa)
    return numpysopa, lista  # Regresa la sopa de letra con las palabras a buscar ya acomodadas en el array


def palabras_encontradas():
    sopa, lista = acomodar()
    palabras = []  # Almacena las palabras encontradas.
    encontradas = 0
    faltantes = len(lista)
    print(sopa)

    while len(palabras) < len(lista):
        #global encontradas, faltantes
        intento = input("Escribe la palabra encontrada: ").lower()
        if intento in lista and intento not in palabras:
            encontradas += 1
            faltantes -= 1
            palabras.append(intento)
        print('Palabra encontrada: ', palabras)
        print(f'Encontraste: {encontradas}, faltan {faltantes} palabras')
    return "¡JUEGO TERMINADO!"

gameOn = True
while gameOn:
    respuesta = input("¿Desea jugar una partida de Sopa de Letras? Simon/nelprro: ").lower()
    if respuesta == 'simon':
        palabras_encontradas()
        print("--------------------------------")
        print("¡JUEGO TERMINADO!")
        print("¡ENCONTRASTE TODAS LAS PALABRAS!")
        print("--------------------------------")
    elif respuesta == 'nelprro':
        print("Bye perro")
        gameOn = False
