import cv2
import numpy as np

def Clamping(num):
    if num < 0:
        num = 0
    if num > 255 :
        num = 255
    return num

def Subtract(image1, image2):
    temp = image1.copy()
    ysize = image1.shape[0]
    xsize = image1.shape[1]

    for y in range(ysize):
        for x in range(xsize):
            value = Clamping(image1.item(y, x) - image2.item(y, x))
            temp.itemset((y, x), value)
    return temp

def main():
    file1 = "Images/ic_ref.raw.jpg"
    file2 = "Images/ic_test.raw.jpg"

    img1 = cv2.imread(file1, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image1', img1)

    img2 = cv2.imread(file2, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image2', img2)

    result = Subtract(img1, img2)
    cv2.imshow('result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()