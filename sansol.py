import cv2
import numpy as np

def Clamping(num):
    if num < 0:
        num = 0
    if num > 255:
        num = 255
    return num

def main():
    filename = "Images/lena.jpg"
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2. imshow('image', img)

    delta = 60

    ysize = img.shape[0]
    xsize = img.shape[1]

    for y in range(ysize):
        for x in range(xsize):
            value = img.item(y, x) + delta
        img.itemset((y, x), Clamping(value))

    cv2.imshow('result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()