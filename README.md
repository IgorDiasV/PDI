# Processamento Digital de Imagens

# Exercícios realizados durante a disciplina

## Primeira Unidade
## Processamento de Imagens no Domínio Espacial
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

![Imagem com uma região em negativo](/Exercicios/imagens/biel_negativo.png)
###### Figura 1 - Imagem com uma região em negativo

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

![Imagem com os quadrantes trocados](/Exercicios/imagens/biel_troca_quadrantes.png)
###### Figura 2 - Imagem com os quadrantes trocados

## 3.2. Exercícios
### YAML X PNG

A ideia desse exercício é verificar se existe alguma diferença entre salvar um arquivo de imagem utilizando png e utilizando yaml. Sabendo que o png realiza uma compressão de dados e o yaml armazena bem mais informação é esperado que ocorra uma diferença entre os dois arquivos e é o que foi constatado na execução da tarefa. Abaixo podemos ver a diferença encontrada quando comparado os pixels iniciais da imagem.

![Matriz de diferenças entre um arquivo PNG e YAML](/Exercicios/imagens/dif_yaml_png.png)
## 4.3. Exercícios 

### Esteganografia

Nesse exercício foi fornecido uma imagem que continha uma outra escondida nela. Para formar a imagem foram utilizados os 5 bits mais significativos para a imagem principal e os 3 bits menos significativos para a imagem que ficaria escondida. Para resolver esse problema foi criado duas variáveis, uma para armazenar a imagem principal e a outra para a imagem escondida. Após isso, foi percorrido todos os pixels da imagem e deslocado o valor encontrado 3 pixels para direita e depois 3 pixels para a esquerda, com isso, ficamos com apenas o valor dos 5 pixels mais significativos e atribuímos esse valor a variável que vai armazenar a imagem principal. Para a imagem escondida, precisamos apenas subtrair o valor do pixel da imagem original pelo valor encontrado dos 5 bits mais significativos. O código, a imagem original e a imagem escondida podem ser vistos abaixo.

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
###### Figura 3 - Imagem Original




![Imagem Escondida](/Exercicios/imagens/Imagem_escondida.png)
###### Figura 4 - Imagem Escondida

## Exercício 5.2

### Labeling 

O código do labeling  que foi fornecido percorre toda a imagem e sempre que encontrar um pixel com o tom de cinza 255 incrementa a contagem de objetos e aplica o floodFill do OpenCV. Para cada objeto encontrado é utilizado no floodFill um tom de cinza diferente. Foi utilizado esse algoritmo na  figura 5 que no final de execução ficou como mostrado na figura 6.

![Bolhas](/Exercicios/imagens/bolhas.png)

###### Figura 5 - Bolhas

![Figura 5 após aplicação do algoritmo](/Exercicios/imagens/resultado_labeling.png)

###### Figura 6 - Figura 5 após aplicação do algoritmo

Um dos problemas do algoritmo anterior é que em imagens que possuem mais de 255 objetos fica inviável, já que, temos apenas 256 tons de cinza. A solução que encontrei para esse problema foi atribuir um único tom de cinza para todos os objetos da imagem.

Foi solicitado um aprimoramento no algoritmo. A ideia é que o programa seja capaz de contar quantas bolhas possuem buracos e quantas não possuem, sem considerar as que estão na borda.

Esse problema foi resolvido em alguns passos simples. O primeiro passo consistiu em percorrer a primeira e a última linha e também a primeira e a última coluna. Caso seja encontrado qualquer objeto é aplicado nele o floodFill atribuindo a cor preta. Dessa forma,  removemos todas as bolhas que tocavam as bordas. O segundo passo consistiu em aplicar o algoritmo do labeling para contar quantas bolhas ainda estavam presentes na imagem. No terceiro passo foi aplicado o algoritmo do floodFill com a cor branca no posição (0, 0), com intuito de permanecer na imagem com a cor preta apenas os buracos que ficavam dentro das bolhas. Após isso, foi aplicado o algoritmo do labeling, com um ajuste para contar apenas objetos da cor preta. Feito isso, obtém-se a quantidade de bolhas que possuem buracos. Para encontrar  quantas bolhas não possuem, basta realizar uma subtração entre a quantidade de bolhas totais e as que possuem buracos. O código e o resultado da execução podem ser vistos abaixo.

```python
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

#pintando o fundo de branco, sendo asssim, restando apenas os buracos com a cor preta.
# o floodFill foi atribuido ao ponto 0,0 pois foi removido as bolhas das bordas, com isso, sabemos que nao teria nenhuma bolha nessa regiao
cv2.floodFill(imagem, None, (0, 0), 255)

buracos = 0
for x in range(height):
    for y in range(width):
        if imagem[x][y] == 0 :
            buracos+=1
            cv2.floodFill(imagem, None, (y, x), 125)


print(f"\n\n bolhas sem buraco {bolhasTotais - buracos} - bolhas com buraco {buracos}\n\n")            
cv2.imshow("imagem", imagem)
cv2.waitKey()
```

![Terminal](/Exercicios/imagens/terminal_exericio_5_2.png)

###### Figura 7 - Resultado da execução


## 6.2. Exercícios

### Equalização de Histograma


Para esse exercício foi fornecido um código que calcula o histograma de uma imagem e mostra ele na tela. A ideia dessa atividade é equalizar uma determinada imagem e mostrar a diferença provocada pela equalização. Realizar a equalização do histograma com OpenCV é extremamente simples, basta utilizar o comando equalizeHist. 
Na figura 8 é apresentado um exemplo de imagem com histograma desbalanceado e na figura 9 a mesma imagem após a aplicação da equalização de histograma.

![Imagem Com Histograma Desbalanceado](/Exercicios/imagens/imagem_histograma_desbalanceado.jpeg)

###### Figura 8 - Imagem com histograma desbalanceado


![Imagem com histograma balanceado](/Exercicios/imagens/imagem_equalizada.jpeg)

###### Figura 9 - Imagem com histograma equalizado


## 7.2. Exercícios

### Laplaciano da  Gaussiano


Para essa atividade foi pedido que fosse implementado um algoritmo que aplica o filtro laplaciano da gaussiana em  uma determinada imagem. Fazer isso é bem simples, basta aplicar o filtro gaussiano em uma imagem e após isso aplicar o laplaciana no resultado obtido. Foi fornecido um código que já realiza a aplicação desses dois filtros de forma isolada, então, foi necessário apenas fazer uma pequena modificação para aplicar o filtro em conjunto. O código adaptado pode ser visto abaixo.

```python
import cv2
import numpy as np

def printmask(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            print(m[i][j], end=",")
        print("\n")



media = [0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111]
gauss = [0.0625, 0.125, 0.0625, 0.125, 0.25, 0.125, 0.0625, 0.125, 0.0625]
horizontal = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
vertical = [-1, -2, -1, 0, 0, 0, 1, 2, 1]
laplacian = [0, -1, 0, -1, 4, -1, 0, -1, 0]
boost = [0, -1, 0, -1, 5.2, -1, 0, -1, 0]

mask = np.zeros((3, 3), dtype=np.float32)
result = np.zeros((480, 640), dtype=np.uint8)
absolut = 1
key = None
lastKey = None

cv2.namedWindow("filtroespacial")
cv2.namedWindow("original")

mask = np.array(media).reshape(3, 3)

frame = cv2.imread('imagens/ctec.jpeg')
while True:
    # _, frame = cap.read()
    framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    framegray = cv2.flip(framegray, 1)
    cv2.imshow("original", framegray)
    frame32f = np.float32(framegray)
    frameFiltered = cv2.filter2D(frame32f, -1, mask, anchor=(1, 1), delta=0, borderType=cv2.BORDER_DEFAULT)
    if lastKey == ord('d'):
        maskLaplaciano = np.array(laplacian).reshape(3, 3)
        frameFiltered = cv2.filter2D(frameFiltered, -1, maskLaplaciano, anchor=(1, 1), delta=0, borderType=cv2.BORDER_DEFAULT)

    if absolut:
        frameFiltered = cv2.convertScaleAbs(frameFiltered)

    result = np.uint8(frameFiltered)

    cv2.imshow("filtroespacial", result)

    key = cv2.waitKey(10)
    if key!=-1:
        lastKey = key
    if key == 27:
        break
    elif key == ord('a'):
        absolut = not absolut
    elif key == ord('m'):
        mask = np.array(media).reshape(3, 3)
        printmask(mask)
    elif key == ord('g'):
        mask = np.array(gauss).reshape(3, 3)
        printmask(mask)
    elif key == ord('h'):
        mask = np.array(horizontal).reshape(3, 3)
        printmask(mask)
    elif key == ord('v'):
        mask = np.array(vertical).reshape(3, 3)
        printmask(mask)
    elif key == ord('l'):
        print(key)
        mask = np.array(laplacian).reshape(3, 3)
        printmask(mask)
    elif key == ord('b'):
        mask = np.array(boost).reshape(3, 3)
        printmask(mask)
    elif key == ord('d'):
        mask = np.array(gauss).reshape(3, 3)

```

A seguir, temos a imagem original, com aplicação do filtro laplaciano e com a aplicação do filtro laplaciano do gaussiano


![Imagme do CTEC](/Exercicios/imagens/ctec.jpeg)
###### Figura 10 - Imagme do CTEC


![Filtro Laplaciano](/Exercicios/imagens/laplaciano.png)
###### Figura 11 - Figura 10 com filtro laplaciano


![Filtro Laplaciano Gaussiano](/Exercicios/imagens/laplagaus.png)
###### Figura 12 - Figura 10 com o filtro laplaciano do gaussiano

## Segunda Unidade
## Processamento de Imagens no Domínio da Frequência

## 9.2. Exercícios

Nessa prática foi pedido para calcular o espectro de magnitude da figura 13 utilizando o código dftimage. O resultado pode ser visto na na figura 14.

![](/Exercicios/imagens/figura7.png)
###### Figura 13 - Senoide

![](/Exercicios/imagens/espectro_figura7.png)
###### Figura 14 - Espectro de magnitude da figura 12

## 10.2. Exercícios

## Filtro Homomórfico

A ideia dessa atividade é implementar um filtro homomórfico e com ele melhorar a iluminação de uma determinada figura. 
O filtro é feito baseado em uma equação que possui 4 parâmetros, os valores desses parâmetros vão variar de acordo com a figura utilizada, por isso, foi adicionado 4 sliders que permitem modificar  os valores desses parâmetros enquanto visualiza o resultado da aplicação do filtro.  O código implementado pode ser visto abaixo.

```python
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


```

O filtro foi aplicado na Figura 8, o resultado e os valores utilizados nos parâmetros podem ser vistos na Figura 15. Na figura 16 é mostrado o filtro gerado.

![](/Exercicios/imagens/ajuste_do_histograma.png)
###### Figura 15 - Correção na iluminação da figura 6


![](/Exercicios/imagens/filtro.png)
###### Figura 16 - Filtro utilizado na figura 6