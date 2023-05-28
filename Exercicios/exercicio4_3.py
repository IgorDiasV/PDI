import cv2
import numpy as np

nbits = 3

esteganografia = cv2.imread('imagens/desafio-esteganografia.png', cv2.IMREAD_COLOR)

if esteganografia is None:
    print("imagem nao carregou corretamente")
    exit(-1)

shape_esteganografia = np.shape(esteganografia)
imagemPortadora = np.zeros(shape_esteganografia)
imagemEscondida = np.zeros(shape_esteganografia)

for i in range(esteganografia.shape[0]):
    for j in range(esteganografia.shape[1]):
        
        valesteganografia = esteganografia[i, j]
        valPortadora = [0,0,0]
        valEscondida = [0,0,0]
        
        valPortadora[0] = valesteganografia[0] >> nbits << nbits
        valPortadora[1] = valesteganografia[1] >> nbits << nbits
        valPortadora[2] = valesteganografia[2] >> nbits << nbits

        valEscondida[0] = (valesteganografia[0] - valPortadora[0]) << (8 - nbits)
        valEscondida[1] = (valesteganografia[1] - valPortadora[1]) << (8 - nbits)
        valEscondida[2] = (valesteganografia[2] - valPortadora[2]) << (8 - nbits)

        imagemPortadora[i, j] = [valPortadora[0], valPortadora[1], valPortadora[2]]
        imagemEscondida[i, j] = [valEscondida[0], valEscondida[1], valEscondida[2]]

cv2.imwrite("imagens/Imagem_principal.png", imagemPortadora)
cv2.imwrite("imagens/Imagem_escondida.png", imagemEscondida)