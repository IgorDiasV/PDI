import sys
import cv2
import numpy as np

nClusters = 8
nRodadas = 1

for i in range(1,11):
    caminho = 'imagens/sushi.jpg'
    img = cv2.imread(caminho, cv2.IMREAD_COLOR)
    samples = np.float32(img.reshape(-1, 3))

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001)
    flags = cv2.KMEANS_RANDOM_CENTERS

    compactness, labels, centers = cv2.kmeans(samples, nClusters, None, criteria, nRodadas, flags)

    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    res = res.reshape((img.shape))


    cv2.imwrite(f'imagens/kmeans/sushi_rodada{i}.jpg', res)

