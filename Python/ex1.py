import numpy as np 
import random

def contador_valores(matriz): 
    contador = [0] * 256
    for row in matriz:
        for valor in row:
            contador[valor] += 1
    return contador  

matriz = [
    [0, 1, 2, 2],
    [3, 255, 0, 2],
    [1, 2, 255, 255]
]

resultado = contador_valores(matriz)
for i in range(256):
    if resultado[i] > 0:
        print(f"Valor {i} aparece {resultado[i]} vezes")