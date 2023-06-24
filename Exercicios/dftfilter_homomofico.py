import cv2
import numpy as np
import math

gh, gl, c, d0 = 1.0, 0.5, 1.0, 1.0
gh_slider, gl_slider, c_slider, d0_slider = 1, 1, 1, 10
gh_max, gl_max, c_max, d0_max = 200, 100, 100, 200

def swapQuadrants(imagem):

    qtd_colunas  = np.shape(imagem)[1]
    qtd_linhas  = np.shape(imagem)[0]
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

def filtro(gl, gh, c, d0, padded):

    dft_M = padded.shape[0] 
    dft_N = padded.shape[1] 
    filter2D = np.float32(np.zeros((image.shape[0], image.shape[1])))

    for i in range(0,dft_M) :
        for j in range(0, dft_N) :
            filter2D[i, j] = (gh - gl) * (1 - math.exp(-c * (((i - dft_M / 2) * (i - dft_M / 2) + (j - dft_N / 2) * (j - dft_N / 2)) / (d0 * d0)))) + gl
        
    

    cv2.imshow("filtro", filter2D)
    filter2D = cv2.normalize(filter2D, None, 0, 1, cv2.NORM_MINMAX)
    planes = [filter2D.copy(), np.float32(np.zeros(filter2D.shape))]
    filter = np.float32(np.zeros_like(padded))
    filter = cv2.merge(planes, filter)

    
    return filter

def aplicar_filtro():
    global gh, gl, c, d0
    dft_M = cv2.getOptimalDFTSize(image.shape[0])
    dft_N = cv2.getOptimalDFTSize(image.shape[1])
    padded = cv2.copyMakeBorder(image, 0, dft_M - image.shape[0], 0, dft_N - image.shape[1], cv2.BORDER_CONSTANT, value=0)
    planos = [np.float32(padded), np.float32(np.zeros_like(padded))]


    complexImage = cv2.merge(planos)

    complexImage = cv2.dft(complexImage)
    complexImage = swapQuadrants(complexImage)
    filter = np.float32(np.zeros_like(padded))

    filter = filtro(gl, gh, c, d0, padded.copy())


    complexImage = cv2.mulSpectrums(complexImage, filter, 0)

    complexImage = swapQuadrants(complexImage)
    complexImage = cv2.idft(complexImage)

    planos = cv2.split(complexImage)
    result = planos[0]

    result = cv2.normalize(result, None, 0, 1, cv2.NORM_MINMAX)

    return result.copy()

def on_trackbar_gh(value):
    global gh
    gh = value/100.0


def on_trackbar_gl(value):
    global gl
    gl = value /100.0


def on_trackbar_c(value):
    global c
    c = value/10.0


def on_trackbar_d0(value):
    global d0
    d0 = value



image = cv2.imread('imagens/imagem_histograma_desbalanceado_original.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow("original", image)
if image is None:
    print("Erro abrindo imagem")
    exit(1)


cv2.namedWindow("img_final")

TrackbarName = "gh - {}".format(gh_max)
cv2.createTrackbar(TrackbarName, "img_final", gh_slider, gh_max, on_trackbar_gh)

TrackbarName = "gl - {}".format(gl_max)
cv2.createTrackbar(TrackbarName, "img_final", gl_slider, gl_max, on_trackbar_gl)

TrackbarName = "c - {}".format(c_max)
cv2.createTrackbar(TrackbarName, "img_final", c_slider, c_max, on_trackbar_c)

TrackbarName = "d0 - {}".format(d0_max)
cv2.createTrackbar(TrackbarName, "img_final", d0_slider, d0_max, on_trackbar_d0)

while True:
    imagem_final = aplicar_filtro()

    cv2.imshow("img_final", imagem_final)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break


cv2.destroyAllWindows()

