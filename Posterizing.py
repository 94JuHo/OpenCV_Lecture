import cv2
import numpy as np

def CreateLUT():
    LUT = np.arange(256)
    for i in range(256):
        LUT[i] = LUT[i] // 50 * 50
    return LUT

def main():
    filename = "Images/lena.jpg"
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)

    lut = CreateLUT()

    ysize = img.shape[0]
    xsize = img.shape[1]

    for y in range(ysize):
        for x in range(xsize):
            img.itemset((y, x), lut[img.item(y, x)])

    cv2.imshow('result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()