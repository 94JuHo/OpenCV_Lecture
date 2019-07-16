import cv2
import numpy as np
import math
from tkinter.filedialog import askopenfilename

def main():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    simg = img
    cv2.imshow('image', img)

    kernel = np.array([[1, 2, 1],\
                       [2, 4, 2],\
                       [1, 2, 1]])

    ysize = img.shape[0]
    xsize = img.shape[1]

    for y in range(1, ysize-1):
        for x in range(1, xsize-1):
            newValue = 0
            for mr in range(3):
                for mc in range(3):
                    newValue += kernel[mr, mc] * img.item(y+mr-1, x+mc-1)
            newValue = math.floor(newValue/16)
            simg.itemset((y,x), newValue)

    cv2.imshow('result', simg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()