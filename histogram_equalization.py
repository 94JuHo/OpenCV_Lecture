import cv2
import numpy as np

def main():
    filename = "images/lena.jpg"
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)

    Hist = np.zeros((256))
    ysize = img.shape[0]
    xsize = img.shape[1]

    for y in range(ysize):
        for x in range(xsize):
            Hist[img.item(y, x)] = Hist[img.item(y, x)] + 1

    normHist = np.empty((256))
    sum = 0.0
    factor = 255.0 / (ysize * xsize)

    for i in range(256):
        sum += Hist[i]
        normHist[i] = round(sum * factor)

    for y in range(ysize):
        for x in range(xsize):
            img.itemset((y, x), normHist[img.item(y, x)])

    cv2.imshow('result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()