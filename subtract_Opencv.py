import cv2
import numpy as np

def ShowImage():
    file1 = "Images/ic_ref.raw.jpg"
    file2 = "Images/ic_test.raw.jpg"

    img1 = cv2.imread(file1, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image1',img1)

    img2 = cv2.imread(file2, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image2', img2)

    result = cv2.subtract(img1, img2)
    cv2.imshow('result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
ShowImage()