import cv2
import numpy as np

def swapQuadrants(imagem):
    #tracando os quadrantes da imagem
    qtd_colunas  = np.shape(imagem)[1]
    qtd_linhas  = np.shape(imagem)[0]

    # centro = int(qtd_colunas/2)
    centerX = image.shape[0] // 2
    centerY = image.shape[1] // 2
    imagem_modificada = imagem.copy()
    for x in range(centerX, qtd_linhas):
        for y in range(centerY, qtd_colunas):
            imagem_modificada[x-centerX][y-centerY]=imagem[x][y]    # primeiro quadraadnte recebe o quarto
            imagem_modificada[x][y] = imagem[x-centerX][y-centerY]  # quarto quadrante recebe o primeiro
            imagem_modificada[x-centerX][y] = imagem[x][y-centerY]  # segundo quadrante recebo o terceiro
            imagem_modificada[x][y-centerY] = imagem[x-centerX][y]  # terceiro quadrante recebo o segundo
    return imagem_modificada.copy()

def makeFilter(image, filter, radius=20):
    filter2D = np.zeros((image.shape[0], image.shape[1]), dtype=np.float32)
    centerX = image.shape[1] // 2
    centerY = image.shape[0] // 2

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if (i - centerY)**2 + (j - centerX)**2 <= radius**2:
                filter2D[i, j] = 1

    planes = [filter2D, np.zeros(filter2D.shape, dtype=np.float32)]
    filter = cv2.merge(planes, filter)
    return filter

image = cv2.imread('imagens/biel2.png', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Erro abrindo imagem")
    exit(1)

dft_M = cv2.getOptimalDFTSize(image.shape[0])
dft_N = cv2.getOptimalDFTSize(image.shape[1])
padded = cv2.copyMakeBorder(image, 0, dft_M - image.shape[0], 0, dft_N - image.shape[1], cv2.BORDER_CONSTANT, value=0)
planos = [padded, np.zeros(padded.shape, dtype=np.float32)]
planos[0] = planos[0].astype(float)
planos[1] = planos[1].astype(float)
complexImage = cv2.merge(planos)

cv2.dft(complexImage, complexImage)
complexImage = swapQuadrants(complexImage)

filter = np.zeros(complexImage.shape, dtype=np.float32)
filter = makeFilter(complexImage, filter)

complexImage = complexImage.astype(float)
filter = filter.astype(float)
complexImage = cv2.mulSpectrums(complexImage, filter, 0)

swapQuadrants(complexImage)
cv2.idft(complexImage, complexImage)

cv2.split(complexImage, planos)
result = planos[0]

cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX)

cv2.imshow("image", result)
cv2.imwrite("dft-filter.png", result * 255)

cv2.waitKey(0)
cv2.destroyAllWindows()
