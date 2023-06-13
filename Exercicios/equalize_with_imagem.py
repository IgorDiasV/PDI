import cv2
import numpy as np


image = cv2.imread('imagens/imagem_histograma_desbalanceado_original.jpeg')


width, height = image.shape[1], image.shape[0]



print("largura =", width)
print("altura  =", height)

nbins = 64
range_ = [0, 255]
histrange = range_
uniform = True
accumulate = False

histw = nbins
histh = nbins // 2


histImg = np.zeros((histh, histw), dtype=np.uint8)
histImg_equalize = np.zeros((histh, histw), dtype=np.uint8)


image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
equalize_image = cv2.equalizeHist(image)

planes = cv2.split(image)
planes_equalize = cv2.split(equalize_image)

histB = cv2.calcHist([planes[0]], [0], None, [nbins], histrange, accumulate=accumulate)
hist_equalize = cv2.calcHist([planes_equalize[0]], [0], None, [nbins], histrange, accumulate=accumulate)


cv2.normalize(histB, histB, 0, histImg.shape[0], cv2.NORM_MINMAX, -1)
cv2.normalize(hist_equalize, hist_equalize, 0, histImg_equalize.shape[0], cv2.NORM_MINMAX, -1)



histImg.fill(0)
histImg_equalize.fill(0)
for i in range(nbins):
    cv2.line(histImg, (i, histh), (i, histh - int(histB[i])), (255, 0, 0), 1, 8, 0)
    cv2.line(histImg_equalize, (i, histh), (i, histh - int(hist_equalize[i])), (255, 0, 0), 1, 8, 0)


image[2 * histh:3 * histh, 0:nbins] = histImg
equalize_image[2 * histh:3 * histh, 0:nbins] = histImg_equalize


cv2.imshow("image", image)
cv2.imshow("Imagem equalizada", equalize_image)
cv2.waitKey()

cv2.imwrite('imagens/imagem_histograma_desbalanceado.jpeg', image)

cv2.imwrite('imagens/imagem_equalizada.jpeg', equalize_image)

