import cv2

img = cv2.imread("imagens/biel.png", cv2.IMREAD_COLOR)
img2 = img.copy() 

#tracando os quadrantes da imagem
for x in range(128, 256):
    for y in range(128, 256):
        img2[x-128][y-128]=img[x][y]    # primeiro quadraadnte recebe o quarto
        img2[x][y] = img[x-128][y-128]  # quarto quadrante recebe o primeiro
        img2[x-128][y] = img[x][y-128]  # segundo quadrante recebo o terceiro
        img2[x][y-128] = img[x-128][y]  # terceiro quadrante recebo o segundo

#exibindo imagem
cv2.namedWindow("Exercicio 2.2 Trocando os quadrantes", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Exercicio 2.2 Trocando os quadrantes", img2)
cv2.waitKey()