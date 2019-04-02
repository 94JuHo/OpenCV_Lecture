import cv2
import numpy as np

def showImage():
    filename = "Images/lena.jpg"
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)

    lut = np.arange(255, -1, -1, dtype='uint8')

    ysize = img.shape[0]
    xsize = img.shape[1]

    for y in range(ysize):
        for x in range(xsize):
            img.itemset((y, x), lut[img.item(y, x)])

    #Opencv 방식
    #result = cv2.LUT(img, lut)

    cv2.imshow('result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
showImage()