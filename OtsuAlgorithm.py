import cv2
import numpy as np

def main():
    filename = "Images/coin.bmp"
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('image', img)

    Hist = np.zeros((256))
    ysize = img.shape[0]
    xsize = img.shape[1]

    for y in range(ysize):
        for x in range(xsize):
            Hist[img.item(y, x)] = Hist[img.item(y, x)] + 1

    Prob = np.empty((256), dtype="float32")
    for i in range(256):
        Prob[i] = Hist[i] / img.size

    wsv_min = float('inf')
    wsv_t = 0

    for t in range(256):
        q1 = q2 = 0.0

        for i in range(t):
            q1 += Prob[i]
        for i in range(t, 256):
            q2 += Prob[i]
        if q1 == 0 or q2 == 0:
            continue

        u1 = u2 = 0.0

        for i in range(t):
            u1+= i*Prob[i]
        u1 /= q1
        for i in range(t, 256):
            u2 += i*Prob[i]
        u2 /= q2

        s1 = s2 = 0.0
        for i in range(t):
            s1+= pow(i-u1, 2) * Prob[i]
        s1 /= q1
        for i in range(t, 256):
            s2 += pow(i-u2, 2) * Prob[i]
        s2 /= q2

        wsv = q1 * s1 + q2 * s2
        if wsv < wsv_min:
            wsv_min = wsv
            wsv_t = t

    for y in range(ysize):
        for x in range(xsize):
            if img.item(y, x) < wsv_t:
                img.itemset((y, x), 0)
            else:
                img.itemset((y, x), 255)

    cv2.imshow('result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()