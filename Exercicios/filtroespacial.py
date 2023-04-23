import cv2
import numpy as np

def printmask(m):
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            print(m[i][j], end=",")
        print("\n")


cap = cv2.VideoCapture(0)
media = [0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111, 0.1111]
gauss = [0.0625, 0.125, 0.0625, 0.125, 0.25, 0.125, 0.0625, 0.125, 0.0625]
horizontal = [-1, 0, 1, -2, 0, 2, -1, 0, 1]
vertical = [-1, -2, -1, 0, 0, 0, 1, 2, 1]
laplacian = [0, -1, 0, -1, 4, -1, 0, -1, 0]
boost = [0, -1, 0, -1, 5.2, -1, 0, -1, 0]

mask = np.zeros((3, 3), dtype=np.float32)
result = np.zeros((480, 640), dtype=np.uint8)
width, height = 0, 0
absolut = 1
key = None
lastKey = None
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print(f"largura={width}")
print(f"altura ={height}")
print(f"fps    ={cap.get(cv2.CAP_PROP_FPS)}")
print(f"format ={cap.get(cv2.CAP_PROP_FORMAT)}")

cv2.namedWindow("filtroespacial", cv2.WINDOW_NORMAL)
cv2.namedWindow("original", cv2.WINDOW_NORMAL)

mask = np.array(media).reshape(3, 3)

while True:
    _, frame = cap.read()
    framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    framegray = cv2.flip(framegray, 1)
    cv2.imshow("original", framegray)
    frame32f = np.float32(framegray)
    frameFiltered = cv2.filter2D(frame32f, -1, mask, anchor=(1, 1), delta=0, borderType=cv2.BORDER_DEFAULT)
    if lastKey == ord('d'):
        print('entrou')
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
        printmask(mask)