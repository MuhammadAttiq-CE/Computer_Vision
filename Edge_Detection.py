import cv2 as cv
import numpy as np

camera = cv.VideoCapture(0)

while True:
    _, frame = camera.read()

    laplacian = cv.Laplacian(frame, cv.CV_64F)
    laplacian = np.uint8(laplacian)

    edges = cv.Canny(frame, 150, 150)
    cv.imshow('Canny', edges)

    if cv.waitKey(5) == ord('X'):
        break

camera.release()
cv.destroyAllWindows()
