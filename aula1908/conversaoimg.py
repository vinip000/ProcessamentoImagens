import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("imagemteste.jpg", 1)

cv2.imshow("Imagem Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

img_grayscale_basic = img.mean(axis=2)
img_grayscale_basic = np.array(img_grayscale_basic, dtype=np.uint8)
cv2.imshow('img_grayscale_basic', img_grayscale_basic)
cv2.waitKey(0)
cv2.destroyAllWindows()