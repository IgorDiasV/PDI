import random
import cv2
import numpy as np

STEP = 5
JITTER = 3
RAIO = 3

caminho = 'imagens/ctec.jpeg'
yrange = []
xrange = []

image = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)


width = image.shape[1]
height = image.shape[0]

xrange = list(range(0, height // STEP))
yrange = list(range(0, width // STEP))

xrange = [x * STEP + STEP // 2 for x in xrange]
yrange = [y * STEP + STEP // 2 for y in yrange]

points = np.ones((height, width), dtype=np.uint8) * 255

random.shuffle(xrange)

for i in xrange:
    random.shuffle(yrange)
    for j in yrange:
        x = i + random.randint(-JITTER, JITTER)-1
        y = j + random.randint(-JITTER, JITTER)-1
        gray = int(image[x, y])
        cv2.circle(points, (y, x), RAIO, (gray, gray, gray), -1, cv2.LINE_AA)

cv2.imshow("pontos", points)
cv2.waitKey()
