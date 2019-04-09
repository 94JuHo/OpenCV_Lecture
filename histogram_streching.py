import cv2
import numpy as np

def main():
    filename="images/coin.bmp"
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)

    Hist = np.zeros((256))
    ysize= img.shape[0]
    xsize = img.shape[1]

    for y in range(ysize):
        for x in range(xsize):
            Hist[img.item(y, x)] = Hist[img.item(y, x)]+ 1

    low = 0
    high = 255

    for i in range(256):
        if Hist[i] != 0:
            low = i
            break

    for i in range(255, -1, -1):
        if Hist[i] != 0:
            high = i
            break

    for y in range(ysize):
        for x in range(xsize):
            value = round((img.item(y, x) - low) / (high-low) * 255)
            img.itemset((y, x) , value)

    cv2.imshow('result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()