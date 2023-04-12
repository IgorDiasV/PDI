import cv2
imagem = cv2.imread("imagens/bolhas.png", cv2.IMREAD_GRAYSCALE)

width = imagem.shape[1]
height = imagem.shape[0]

nobjects = 0
for x in range(height):
    for y in range(width):
        if imagem[x][y] == 255 :

            nobjects+=1


            cv2.floodFill(imagem, None, (y, x), nobjects)
            
   

print(f'foi encontrado um total de {nobjects} bolhas')

cv2.imshow("imagem", imagem)
cv2.waitKey()

