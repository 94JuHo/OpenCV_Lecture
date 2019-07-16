import cv2
import numpy as np
from tkinter.filedialog import askopenfilename

def main():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)

    array = np.zeros(9)
    ysize = img.shape[0]
    xsize = img.shape[1]

    for y in range(1, ysize-1):
        for x in range(1, xsize-1):
            for mr in range(3):
                for mc in range(3):
                    array[mr*3+mc] = img.item(y+mr-1, x+mc-1)
            array.sort()
            img.itemset((y,x), array[4])

    cv2.imshow('result',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()