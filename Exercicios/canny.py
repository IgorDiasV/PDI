import cv2

top_slider = 10
top_slider_max = 200

TrackbarName = "Threshold inferior"

def on_trackbar_canny(value):
    global image, border

    border = cv2.Canny(image, value, 3 * top_slider)
    # cv2.imshow("Canny", border)


caminho = 'imagens/ctec.jpeg'
image = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)

cv2.namedWindow("Canny")
cv2.createTrackbar(TrackbarName, "Canny", top_slider, top_slider_max, on_trackbar_canny)

on_trackbar_canny(top_slider)

while True:

    cv2.imshow("Canny", border)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cv2.destroyAllWindows()
