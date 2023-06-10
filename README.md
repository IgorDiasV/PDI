# Processamento Digital de Imagens

# Exercícios realizados durante a disciplina

## Primeira Unidade

## 2.2. Exercícios 

### Negativo de uma imagem
O objetivo desse exercício era calcular o negativo de uma  região, de uma imagem qualquer. Essa região é determinada pelo usuário. Para isso, é necessário utilizar um laço duplo que vai percorrer todos os pixels da região escolhida e trocar seus valores. Os novos valores dos pixels vão ser calculados da seguinte forma: 255 - x. x é o tom de cinza atual do pixel. O código completo pode ser visto abaixo.

```python
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
```

Aplicando o código nas coordenadas de P1(50, 100) e P2(170, 220) obtemos o seguinte resultado: 	

![Imagem com uma região em negativo](/Exercicios/imagens/biel_negativo.png )

### Troca de quadrantes da imagem 

Essa segunda parte do exercício consistia em dividir a imagem em 4 quadrantes e trocar o primeiro quadrante com o terceiro e o segundo com o quarto. Para isso, foi necessário criar uma cópia da imagem original e percorrer parte dela, onde, em cada iteração era atribuído o valor de um determinado pixel da imagem original a um pixel em um outro quadrante na imagem de cópia. 

```python
import cv2
import numpy as np
img = cv2.imread("imagens/biel.png", cv2.IMREAD_COLOR)
img2 = img.copy() 
linhas = np.shape(img)[0]
colunas = np.shape(img)[1]

centro =  linhas//2
#tracando os quadrantes da imagem
for x in range(centro, linhas):
    for y in range(centro, colunas):
        img2[x-centro][y-centro]=img[x][y]    # primeiro quadraadnte recebe o quarto
        img2[x][y] = img[x-centro][y-centro]  # quarto quadrante recebe o primeiro
        img2[x-centro][y] = img[x][y-centro]  # segundo quadrante recebo o terceiro
        img2[x][y-centro] = img[x-centro][y]  # terceiro quadrante recebo o segundo

#exibindo imagem
cv2.namedWindow("Exercicio 2.2 Trocando os quadrantes", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Exercicio 2.2 Trocando os quadrantes", img2)
cv2.waitKey()
```
resultado da troca de quadrantes:

![Imagem com os quadrantes trocados](/Exercicios/imagens/biel_troca_quadrantes.png )

## 4.3. Exercícios 

### Esteganografia

Nesse exercício foi fornecido uma imagem que continha uma outra escondida nela. Para formar a imagem foram utilizados os 5 bits mais significativos para a imagem principal e os 3 bits menos significativos para a imagem que ficaria escondida. Para resolver esse problema foi criado duas variáveis para armazenar, uma para armazenar a imagem principal e a outra para a imagem escondida. Após isso, foi percorrido todos os pixels da imagem e deslocado o valor encontrado 3 pixels para direita e depois 3 pixels para a esquerda, com isso, ficamos com apenas o valor dos 5 pixels mais significativos e atribuímos esse valor a variável que vai armazenar a imagem principal. Para a imagem escondida, precisamos apenas subtrair o valor do pixel da imagem original pelo valor encontrado dos 5 bits mais significativos. O código, a imagem original e a imagem escondida podem ser vistos abaixo.

```python
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
```

![Imagem original](/Exercicios/imagens/desafio-esteganografia.png)
###### Imagem Original

</br>
</br>

![Imagem Escondida](/Exercicios/imagens/Imagem_escondida.png)
###### Imagem Escondida
