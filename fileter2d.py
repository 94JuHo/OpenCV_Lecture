import cv2
import numpy as np
from tkinter.filedialog import askopenfilename

def showImage():
    filename = askopenfilename()
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    kernel = np.array([[-1, -1, -1],\
                       [-1, 9, -1],\
                       [-1, -1, -1]])
    result = cv2.filter2D(img, -1, kernel)

    cv2.imshow('image', img)
    cv2.imshow('result', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
showImage()