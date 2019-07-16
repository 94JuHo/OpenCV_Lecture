import cv2
import numpy as np
import matplotlib.pyplot as plt

def showHistogram():
    filename = "Images/lena.jpg"

    img = cv2.imread(filename, cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

    cv2.imshow('2DHist', hist)

    plt.imshow(hist, interpolation='nearest')
    plt.show()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

showHistogram()