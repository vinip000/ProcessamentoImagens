import numpy as np
from matplotlib import pyplot as plt
import cv2

# Lê a imagem em cores
img = cv2.imread("image.png", cv2.IMREAD_COLOR)

# Verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem.")
    exit()

# Calcula e plota o histograma para cada canal de cor
cores = ('b', 'g', 'r')
for i, cor in enumerate(cores):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=cor, label=f'Canal {cor.upper()}')

plt.title("Histograma da Imagem Colorida")
plt.xlabel("Valor dos Pixels")
plt.ylabel("Frequência")
plt.legend()
plt.show()