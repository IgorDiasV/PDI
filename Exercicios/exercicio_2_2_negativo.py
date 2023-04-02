import cv2

#carregando imagem
img = cv2.imread("imagens/biel.png", cv2.IMREAD_COLOR)

#capturando os pontos 
x1 = int(input("digite o valor de x do primeiro ponto: "))
y1 = int(input("digite o valor de y do primeiro ponto: "))
x2 = int(input("digite o valor de x do segundo ponto: "))
y2 = int(input("digite o valor de y do segundo ponto: "))

#realizando o negativo da região escolhida
for i in range(x1,x2):
    for j in range(y1,y2):
        img[i][j]= 255 - img[i][j]


#exibindo imagem
cv2.namedWindow("Exercicio 2.2 Negativo", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Exercicio 2.2 Negativo", img)
cv2.waitKey()


