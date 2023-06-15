import cv2
import numpy as np
import math

SIDE = 256
PERIODOS = 8

ss_img = ""
ss_yml = ""

ss_yml = f"senoide-{SIDE}.yml"
image = np.zeros((SIDE, SIDE), dtype=np.float32)

fs = cv2.FileStorage(ss_yml, cv2.FILE_STORAGE_WRITE)

for i in range(SIDE):
    for j in range(SIDE):
        image[i, j] = 127 * math.sin(2 * math.pi * PERIODOS * j / SIDE) + 128

fs.write("mat", image)
fs.release()

cv2.normalize(image, image, 0, 255, cv2.NORM_MINMAX)
image = image.astype(np.uint8)
ss_img = f"senoide-{SIDE}.png"
cv2.imwrite(ss_img, image)

fs = cv2.FileStorage(ss_yml, cv2.FILE_STORAGE_READ)
image = fs.getNode('mat').mat()
fs.release()

cv2.normalize(image, image, 0, 255, cv2.NORM_MINMAX)
image = image.astype(np.uint8)

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()