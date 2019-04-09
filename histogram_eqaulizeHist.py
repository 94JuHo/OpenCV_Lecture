import cv2
import numpy as np

def showImage():
    filename="Images/lena.jpg"
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)

    equ_img = cv2.equalizeHist(img)
    cv2.imshow('equalized image', equ_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage()