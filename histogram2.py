import cv2
import numpy as np
import matplotlib.pyplot as plt

def showHistogram():
    filename = "images/lena.jpg"

    gray_img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
    plt.plot(hist, color='black')

    color_img = cv2.imread(filename, cv2.IMREAD_COLOR)
    for i, c in enumerate(('blue', 'green', 'red')):
        hist = cv2.calcHist([color_img], [i], None, [256], [0, 256])
        plt.plot(hist, color=c)

    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showHistogram()