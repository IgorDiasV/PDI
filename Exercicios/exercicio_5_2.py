import cv2
imagem = cv2.imread("imagens/bolhas.png",cv2.IMREAD_GRAYSCALE)
width = imagem.shape[1]
height = imagem.shape[0]


#removendo as bolhas da parte superior e inferior
for x in [0,height-1]:
    for y in range(width):
        if imagem[x][y] == 255 :


            cv2.floodFill(imagem, None, (y, x), 0)


#removendo as bolhas das laterais
#          
for x in range(height):
    for y in [0,width-1]:
        if imagem[x][y] == 255 :


            cv2.floodFill(imagem, None, (y, x), 0)  


cv2.imshow("imagem", imagem)
cv2.waitKey()
#contando quantas bolhas tem ao todo e atribuindo uma cor qualquer
bolhasTotais = 0
for x in range(height):
    for y in range(width):
        if imagem[x][y] == 255 :
            bolhasTotais+=1
            cv2.floodFill(imagem, None, (y, x), 125)




print(f"bolhas restantes {bolhasTotais}")


#pintando o fundo de branco, sendo asssim, restando apenas os buracos com a cor preta.
# o floodFill foi atribuido ao ponto 0,0 pois foi removido as bolhas das bordas, com isso, sabemos que nao teria nenhuma bolha nessa regiao
cv2.floodFill(imagem, None, (0, 0), 255)

buracos = 0
for x in range(height):
    for y in range(width):
        if imagem[x][y] == 0 :
            buracos+=1
            cv2.floodFill(imagem, None, (y, x), 125)


print(f" bolhas sem buraco {bolhasTotais - buracos} - bolhas com buraco {buracos}")            
cv2.imshow("imagem", imagem)
cv2.waitKey()