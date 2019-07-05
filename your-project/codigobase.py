#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 16:50:36 2019

@author: rodolfo | gustavo
"""

#Juego 

import random 
from random import randint
import re

textooptativo = open("texto.txt", "r")
lista_texto = list(textooptativo.readlines())
#print(lista_texto)
#print(type(lista_texto))
txtplano = "".join(lista_texto)
#txtplano = re.replace("\n", " ", txtplano)
texto = re.sub("[,.]", "", txtplano).split()
#print(texto)

texto2 = []
for t in texto: 
    texto2.append(t)
#print(texto2)

txtplano2 = " ".join(texto2)
#print(type(txtplano2))

txtplano2 = list(txtplano2.lower().split())
#print(txtplano2)


import random
from random import randint

#words = ["crown", "united kingdom", "royalty", "castle", "empress", "buckingham", "tiara", "viscount", "royal estate", "throne"]
player1 = 1
nivelx = 3
vidas = 3

def nivel(x):
  global player1
  return player1


print("Arrenge the letters to save our Queen")
while player1 == 1 and nivelx > 0:
    b = txtplano2[randint(0,9)]
    a = list(b)
    random.shuffle(a)
    print(a)
    while vidas >=1:
       player = input(" ")
       if player == b:
         if nivelx != 1:
           print ("You got a hit, deal %i more" % (nivelx -1))
           nivel(player1)
         elif nivelx == 1:
           print("You win")
         nivelx -= 1
         break
       elif player != b:
         if vidas ==1:
           print("The Dragon ate the Queen, You lose!!!")
           player1 = 'perdiste'
           break
         else:
            print("Our Queen is still in danger")
            vidas -= 1
            print("Try again, your sword have %i hits!" % vidas)
            print(a)
