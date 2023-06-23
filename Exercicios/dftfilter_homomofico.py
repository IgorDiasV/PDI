import cv2
import numpy as np
import math
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

    filter2D = np.float32(np.zeros((image.shape[0], image.shape[1])))

    centerX = image.shape[1] // 2
    centerY = image.shape[0] // 2

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if (((i - centerY)**2 + (j - centerX)**2) <= (radius**2)):
                filter2D[i, j] = 1

    planes = [filter2D.copy(), np.float32(np.zeros(filter2D.shape))]
    filter = cv2.merge(planes, filter)
    return filter.copy()

def filtro(Yl, Yh, c, d0, padded):

    dft_M = padded.shape[0] 
    dft_N = padded.shape[1] 
    filter2D = np.float32(np.zeros((image.shape[0], image.shape[1])))

    for i in range(0,dft_M) :
        for j in range(0, dft_N) :
            filter2D[i, j] = (Yh - Yl) * (1 - math.exp(-c * (((i - dft_M / 2) * (i - dft_M / 2) + (j - dft_N / 2) * (j - dft_N / 2)) / (d0 * d0)))) + Yl
        
    

    # Mat comps[] = { tmp,tmp };
    # merge(comps, 2, filter2D);
    cv2.imshow("teste", filter2D)
    cv2.waitKey()
    filter2D = cv2.normalize(filter2D, None, 0, 1, cv2.NORM_MINMAX)
    # imshow("filtro", tmp);
    planes = [filter2D.copy(), np.float32(np.zeros(filter2D.shape))]
    filter = np.float32(np.zeros_like(padded))
    filter = cv2.merge(planes, filter)

    
    return filter

image = cv2.imread('imagens/imagem_histograma_desbalanceado_original.jpeg', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Erro abrindo imagem")
    exit(1)

dft_M = cv2.getOptimalDFTSize(image.shape[0])
dft_N = cv2.getOptimalDFTSize(image.shape[1])
padded = cv2.copyMakeBorder(image, 0, dft_M - image.shape[0], 0, dft_N - image.shape[1], cv2.BORDER_CONSTANT, value=0)
planos = [np.float32(padded), np.float32(np.zeros_like(padded))]


complexImage = cv2.merge(planos)

complexImage = cv2.dft(complexImage)
complexImage = swapQuadrants(complexImage)
filter = np.float32(np.zeros_like(padded))

filter = filtro(-10.5,-10.39,-10.2,-1000.64,padded.copy())
# filter = makeFilter(complexImage.copy(), filter.copy())


complexImage = cv2.mulSpectrums(complexImage, filter, 0)

complexImage = swapQuadrants(complexImage)
complexImage = cv2.idft(complexImage)

planos = cv2.split(complexImage)
result = planos[0]

result = cv2.normalize(result, None, 0, 1, cv2.NORM_MINMAX)

cv2.imshow("image", result)
cv2.imwrite("dft-filter.png", result * 255)

cv2.waitKey(0)
cv2.destroyAllWindows()
