import cv2

#load image
#cv2.IMREAD_COLOR: loads a color image
#cv2.IMRERAD_GRAYSCALE: loads an image in grayscale mode
#cv2.IMREAD_UNCHANGED: loads ikmkage as suche including alpha channel
img = cv2.imread('image.png', cv2.IMREAD_COLOR)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()