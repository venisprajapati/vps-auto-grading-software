import cv2
import numpy as np


# This file contains code of some functions, for example scanning ID, scanning particular mcq or bubble from omr sheet, counting black pixels and resize image with maintained aspect ratio../

def ScanID(image):
    ID = ''
    group = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E',
             5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}

    A = image[:, 0:22]
    B = image[:, 22:22*2]
    C = image[:, 22*2:22*3]
    D = image[:, 22*3:22*4]

    for i in range(0, 10):
        scan_img = A[0 + i*17:17 + i*17, :]
        if (ScanFunction(scan_img)):
            ID += str(group.get(i))
            break
        elif (i == 9):
            ID += 'A'
            break

    for i in range(0, 10):
        scan_img = B[0 + i*17:17 + i*17, :]
        if (ScanFunction(scan_img)):
            ID += str(i)
            break
        elif (i == 9):
            ID += '0'
            break

    for i in range(0, 10):
        scan_img = C[0 + i*17:17 + i*17, :]
        if (ScanFunction(scan_img)):
            ID += str(i)
            break
        elif (i == 9):
            ID += '0'
            break

    for i in range(0, 10):
        scan_img = D[0 + i*17:17 + i*17, :]
        if (ScanFunction(scan_img)):
            ID += str(i)
            break
        elif (i == 9):
            ID += '0'
            break

    return ID


def ScanMCQs(image):

    # crop_img = img[y:y+h, x:x+w]
    A = 'A' if ScanFunction(image[:, 0:22]) else ''
    B = 'B' if ScanFunction(image[:, 22:22*2]) else ''
    C = 'C' if ScanFunction(image[:, 22*2:22*3]) else ''
    D = 'D' if ScanFunction(image[:, 22*3:22*4]) else ''
    ans = A + B + C + D

    if (len(ans) == 0):
        ans = ''
        return ans

    else:
        return ans


def ScanFunction(image):

    number_of_black_pixels = np.sum(image == 0)
    # print(number_of_black_pixels, end=" ")

    if (number_of_black_pixels > 152):
        return True
    else:
        return False


def BlackAndWhiteImage(image):

    blur = cv2.GaussianBlur(image, (3, 1), 0)
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    threshold_level = 74

    mask = gray < threshold_level
    image[mask] = (0, 0, 0)
    return image


def ResizeImagewithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):

    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:

        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)
