import cv2
from services.contour_ import PerspectiveTransform

def find_ROI(img):

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
    
    gray = cv2.cvtColor(transformed, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 127, 255, 1)

    contours, h = cv2.findContours(thresh, 1, 2)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    approx = cv2.approxPolyDP(
        contours[0], 0.01*cv2.arcLength(contours[0], True), True)

    

    for i in range(1, len(contours)):

        approx = cv2.approxPolyDP(
            contours[i], 0.01*cv2.arcLength(contours[i], True), True)

        if len(approx) == 4:

            c_area = cv2.contourArea(contours[i])
            if (c_area < 200000 and c_area > 100000):
                print(cv2.contourArea(contours[i]))

                cv2.drawContours(transformed, [contours[i]], 0, (0, 0, 255), 2)
    
    img = cv2.resize(transformed, (564, 820), interpolation=cv2.INTER_AREA)
    cv2.imshow('img',img)
    # cv2.imshow('im2', transformed)
    cv2.waitKey(0)

find_ROI('im.jpg')