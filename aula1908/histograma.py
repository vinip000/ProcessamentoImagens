import numpy as np
from matplotlib import pyplot as plt
import cv2

# Lê a imagem em cores
img = cv2.imread("imagemteste.jpg", cv2.IMREAD_GRAYSCALE)

# Verifica se a imagem foi carregada corretamente
if img is None:
    print("Erro ao carregar a imagem.")
    exit()

# Calcula e plota o histograma para cada canal de cor
histogram = np.zeros(256)
for pixel in img.flatten():
    histogram[pixel] += 1

x = np.linspace(0, 255, 256)
plt.bar(x, histogram)
plt.xlabel("intensidade")
plt.ylabel("Frequência")
plt.show()

histogram_normnalized = histogram/histogram.sum()

plt.plot (x, histogram_normnalized)
plt.xlabel("intensidade")
plt.ylabel("Frequência")
plt.show()