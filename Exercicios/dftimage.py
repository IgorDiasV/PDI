import cv2
import numpy as np

def swapQuadrants(image):
    tmp = np.zeros_like(image)
    A, B, C, D = np.split(image, 4)

    # swap quadrants (Top-Left with Bottom-Right)
    np.copyto(tmp, A)
    np.copyto(A, D)
    np.copyto(D, tmp)

    # swap quadrant (Top-Right with Bottom-Left)
    np.copyto(tmp, B)
    np.copyto(B, C)
    np.copyto(C, tmp)

def swapQuadrantsteste(imagem):
    #tracando os quadrantes da imagem
    qtd_colunas  = np.shape(imagem)[0]
    centro = int(qtd_colunas/2)
    imagem_modificada = imagem.copy()
    for x in range(centro, qtd_colunas):
        for y in range(centro, qtd_colunas):
            imagem_modificada[x-centro][y-centro]=imagem[x][y]    # primeiro quadraadnte recebe o quarto
            imagem_modificada[x][y] = imagem[x-centro][y-centro]  # quarto quadrante recebe o primeiro
            imagem_modificada[x-centro][y] = imagem[x][y-centro]  # segundo quadrante recebo o terceiro
            imagem_modificada[x][y-centro] = imagem[x-centro][y]  # terceiro quadrante recebo o segundo
    return imagem_modificada.copy()

path_imagem = 'imagens/figura7.png'
image = cv2.imread(path_imagem, cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Erro abrindo imagem", path_imagem)
    exit()

# expande a imagem de entrada para o melhor tamanho no qual a DFT pode ser executada,
# preenchendo com zeros a lateral inferior direita.
dft_M = cv2.getOptimalDFTSize(image.shape[0])
dft_N = cv2.getOptimalDFTSize(image.shape[1])
padded = cv2.copyMakeBorder(image, 0, dft_M - image.shape[0], 0, dft_N - image.shape[1], cv2.BORDER_CONSTANT, value=0)

# prepara a matriz complexa para ser preenchida
# primeiro a parte real, contendo a imagem de entrada
planos = [np.float32(padded), np.float32(np.zeros_like(padded))]

# combina os planos em uma unica estrutura de dados complexa
complexImage = cv2.merge(planos)

# calcula a DFT
complexImage = cv2.dft(complexImage)
complexImage = swapQuadrantsteste(complexImage)

# planos[0] : Re(DFT(image)
# planos[1] : Im(DFT(image)
planos = cv2.split(complexImage)

# calcula o espectro de magnitude e de fase (em radianos)
magn, fase = cv2.cartToPolar(planos[0], planos[1], angleInDegrees=False)
fase = cv2.normalize(fase, None, 0, 1, cv2.NORM_MINMAX)

# caso deseje apenas o espectro de magnitude da DFT, use:
magn = cv2.magnitude(planos[0], planos[1])

# some uma constante para evitar log(0)
# log(1 + sqrt(Re(DFT(image))^2 + Im(DFT(image))^2))
magn += 1

# calcula o logaritmo da magnitude para exibir
# com compressao de faixa dinamica
magn = np.log(magn)
magn = cv2.normalize(magn, None, 0, 1, cv2.NORM_MINMAX)
print(magn)
# exibe as imagens processadas
cv2.imshow("Imagem", image)
cv2.imshow("Espectro de magnitude", magn)
cv2.imshow("Espectro de fase", fase)
# cv2.imwrite('imagens/espectro_figura7.png', magn)
cv2.waitKey(0)
cv2.destroyAllWindows()
