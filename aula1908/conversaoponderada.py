import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("imagemteste.jpg", 1)

cv2.imshow("Imagem Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Aplicando conversão ponderada manualmente (usando numpy)
img_grayscale_pondered_np = 0.114 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.299 * img[:, :, 2]

# Usando cv2.split para obter os canais
B, G, R = cv2.split(img)
img_grayscale_pondered_cv2 = 0.114 * B + 0.587 * G + 0.299 * R

# Convertendo para uint8
img_grayscale_pondered = np.array(img_grayscale_pondered_np, dtype=np.uint8)

# Exibindo a imagem resultante
cv2.imshow('img_grayscale_pondered', img_grayscale_pondered)
cv2.waitKey(0)
cv2.destroyAllWindows()