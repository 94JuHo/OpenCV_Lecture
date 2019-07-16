import cv2
from tkinter.filedialog import askopenfilename
import numpy as np

global memImage
global gray
def PeripheralHoleBoundaryTracking(mode, cr, cc, pixel, label):
    pdir = 0
    ndir = 0
    r = cr
    c = cc
    d = [0] * 8
    flag = False

    while True:
        d[0] = memImage.item(r, c+1)
        d[1] = memImage.item(r+1, c+1)
        d[2] = memImage.item(r+1, c)
        d[3] = memImage.item(r+1, c-1)
        d[4] = memImage.item(r, c-1)
        d[5] = memImage.item(r-1, c-1)
        d[6] = memImage.item(r-1, c)
        d[7] = memImage.item(r-1, c+1)
        if d[0] != 0 and d[1] != 0 and d[2] != 0 and d[3] != 0 and d[4] != 0 and d[5] != 0 and d[6] != 0 and d[7] != 0:
            break

        ndir = pdir - 3
        if ndir == -1:
            ndir = 7
        elif ndir == -2:
            ndir = 6
        elif ndir == -3:
            ndir = 5

        while True:
            if (d[ndir] == pixel) or (d[ndir] == label):
                flag = False

                if pdir == 1:
                    if ndir == 5:
                        flag = True
                        break
                elif pdir == 2:
                    if ndir == 5 or ndir == 6:
                        flag = True
                        break
                elif pdir == 3:
                    if ndir == 5 or ndir == 6 or ndir == 7:
                        flag = True
                        break
                elif pdir == 4:
                    if ndir == 0 or ndir == 5 or ndir == 6 or ndir == 7:
                        flag = True
                        break
                elif pdir == 5:
                    if ndir != 2 and ndir != 3 and ndir != 4:
                        flag = True
                        break
                elif pdir == 6:
                    if ndir != 3 and ndir != 4:
                        flag = True
                        break
                elif pdir == 7:
                    if ndir != 4:
                        falg = True
                        break

                if flag:
                    memImage.itemset((r,c), label)
                pdir = ndir
                break
            else:
                ndir += 1
                if ndir > 7 :
                    ndir = 0

        if ndir == 0:
            c+=1
            break
        elif ndir == 1:
            r+=1
            c+=1
            break
        elif ndir == 2:
            r+=1
            break
        elif ndir == 3:
            r+=1
            c-=1
            break
        elif ndir == 4:
            c-=1
            break
        elif ndir==5:
            r-=1
            c-=1
            break
        elif ndir==6:
            r-=1
            break
        elif ndir==7:
            r-=1
            c+=1
            break

        if (r == cr) and (c == cc):
            break

def OnRegionLabeling(image): #이진영상에 대해 레이블링 수행
    maxX, maxY = image.shape[:2]
    for y in range(maxY):
        for x in range(maxX):
            if x == 0 or y == 0 or x == maxX-1 or y == maxY-1:
                memImage.itemset((y,x), 0)
            else:
                c = image.item(y, x)
                if c != 0:
                    memImage.itemset((y,x), c*-1)

    pixValue = 0
    label = 0
#영역 레이블링 수행
    for y in range(1,maxY-1):
        for x in range(1,maxX-1):
            pixValue = memImage.item(y,x)
            if memImage.item(y, x) < 0:
                if (memImage.item(y, x-1) <= 0) and (memImage.item(y-1, x-1) <= 0):
                    label +=1
                    memImage.itemset((y,x), label)
                    PeripheralHoleBoundaryTracking(1, y, x, pixValue, label)
                elif memImage.item(y, x-1) > 0:
                    memImage.itemset((y,x), memImage.item(y, x-1))
                elif memImage.item(y, x-1) <=0 and memImage.item(y-1, x-1) > 0 :
                    memImage.itemset((y,x), memImage.item(y-1, x-1))
                    PeripheralHoleBoundaryTracking(2, y, x, pixValue, memImage.item(y-1, x-1))

    dst = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

#레이블링된 각 영역을 적절한 색상으로 표현
    for y in range(maxY):
        for x in range(maxX):
            c = memImage.item(y,x)*(255/(label+1))
            if c == 0 or c==0.0:
                c = 255
            dst[y, x] = [int(c), int(c), int(c)]
            print(int(c))

    cv2.imshow('zzz', dst)
filename = askopenfilename()
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, Otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
memImage = np.zeros(Otsu.shape[:2])
OnRegionLabeling(Otsu)

cv2.imshow('zz',memImage)
cv2.waitKey(0)
cv2.destroyAllWindows()