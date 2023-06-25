import sys
import cv2
import numpy as np

caminho = 'imagens/digitos.png'


image = cv2.imread(caminho, cv2.IMREAD_UNCHANGED)

str_element = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 10))

image = cv2.morphologyEx(image, cv2.MORPH_OPEN, str_element)

cv2.imshow("morfologia", image)
cv2.imwrite('imagens/digitos_morf.png', image)
cv2.waitKey(0)
