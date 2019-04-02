import cv2
import numpy as np

def showImage():
    filename = "Images/lena.jpg"
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)

    ysize = img.shape[0]
    xsize = img.shape[1]
    for y in range(ysize):
        for x in range(xsize):
            if img.item(y, x) < 128:
                img.itemset((y, x), 0)
            else:
                img.itemset((y, x), 255)
    cv2.imshow('bin-image', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

showImage()