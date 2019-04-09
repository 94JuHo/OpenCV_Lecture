import cv2
import numpy as np
import math

def main():
    filename = "images/lena.jpg"
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)

    Hist = np.zeros((256))
    maxValue = 0
    ysize = img.shape[0]
    xsize = img.shape[1]

    for y in range(ysize):
        for x in range(xsize):
            Hist[img.item(y,x)] = Hist[img.item(y,x)] + 1
            if(Hist[img.item(y,x)] > maxValue):
                maxValue = Hist[img.item(y,x)]


    imgHist = np.zeros((256, 256), dtype="uint8")

    for i in range(256):
        value = Hist[i]
        normalized = math.floor(value * 255 / maxValue)
        for j in range(255, 255-normalized, -1):
            imgHist.itemset((j, i), 255)

    cv2.imshow('histogram', imgHist)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()