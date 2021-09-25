import cv2
import numpy as np


def orderCornerPoints(corners):

    corners = [(corner[0][0], corner[0][1]) for corner in corners]
    top_r, top_l, bottom_l, bottom_r = corners[0], corners[1], corners[2], corners[3]
    return (top_l, top_r, bottom_r, bottom_l)


def PerspectiveTransform(image, corners):

    ordered_corners = orderCornerPoints(corners)
    top_l, top_r, bottom_r, bottom_l = ordered_corners

    width_A = np.sqrt(((bottom_r[0] - bottom_l[0])
                      ** 2) + ((bottom_r[1] - bottom_l[1]) ** 2))
    width_B = np.sqrt(((top_r[0] - top_l[0]) ** 2) +
                      ((top_r[1] - top_l[1]) ** 2))
    width = max(int(width_A), int(width_B))

    height_A = np.sqrt(((top_r[0] - bottom_r[0]) ** 2) +
                       ((top_r[1] - bottom_r[1]) ** 2))
    height_B = np.sqrt(((top_l[0] - bottom_l[0]) ** 2) +
                       ((top_l[1] - bottom_l[1]) ** 2))
    height = max(int(height_A), int(height_B))

    dimensions = np.array([[0, 0], [width - 1, 0], [width - 1, height - 1],
                           [0, height - 1]], dtype="float32")

    ordered_corners = np.array(ordered_corners, dtype="float32")

    matrix = cv2.getPerspectiveTransform(ordered_corners, dimensions)

    return cv2.warpPerspective(image, matrix, (width, height))


def rotateImage(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])

    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY

    return cv2.warpAffine(image, M, (nW, nH))


def find_ROI(img, omrType):

    img = cv2.imread(img)
    image = img.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 127, 255, 1)

    contours, h = cv2.findContours(thresh, 1, 2)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    approx = cv2.approxPolyDP(
        contours[0], 0.01*cv2.arcLength(contours[0], True), True)

    if len(approx) == 4:

        # cv2.drawContours(img, [contours[0]], 0, (0, 0, 255), 2)
        transformed = PerspectiveTransform(image, approx)

    else:

        return image

    if (omrType):

        h, w, c = transformed.shape
        if (w > h):
            rotated = rotateImage(transformed, -90)
        else:
            rotated = transformed

    else:

        h, w, c = transformed.shape
        if (w < h):
            rotated = rotateImage(transformed, -90)
        else:
            rotated = transformed

    return rotated
