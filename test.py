import cv2
import glob
from services.functions import ResizeImagewithAspectRatio, BlackAndWhiteImage, ScanID, ScanMCQs
from services.contour_ import find_ROI

image_list = glob.glob('test/*.jpg')

id_point = (20, 48)
start_point = [(20, 220), (134, 48), (134, 220), (248, 48), (248, 220), (362, 48), (362, 220), (474, 48), (474, 220),
               (20, 444), (20, 616), (134, 444), (134, 616), (248, 444), (248, 616), (362, 444), (362, 616), (474, 444), (474, 616)]

ScannedOmrs = []

total_mcqs = 90

for im in image_list:

    if total_mcqs > 90:

        img = find_ROI(im, True)
        img = ResizeImagewithAspectRatio(img, width=564, inter=cv2.INTER_AREA)
        img = cv2.resize(img, (564, 820), interpolation=cv2.INTER_AREA)

    else:
        img = find_ROI(im, False)
        img = ResizeImagewithAspectRatio(img, width=564, inter=cv2.INTER_AREA)
        img = cv2.resize(img, (564, 394), interpolation=cv2.INTER_AREA)

    image = BlackAndWhiteImage(img)

    rect_img = image.copy()

    for pts in range(0, len(start_point)):

        start_x = start_point[pts][0]
        start_y = start_point[pts][1]
        start = (start_x, start_y)
        end = (start_x + 88, start_y + 170)
        color = (0, 255, 0)

        cv2.rectangle(rect_img, start, end, color, 1)

    # image = cv2.resize(image, (624, 524), interpolation=cv2.INTER_AREA)
    cv2.imshow('test-img', rect_img)
    cv2.waitKey(0)

    sheet = {}

    IdPortion = image[id_point[1]:id_point[1] +
                      17*10, id_point[0]:id_point[0] + 22*4]
    id = ScanID(IdPortion)
    sheet["id"] = id

    Counter = 1

    for pts in range(0, len(start_point)):

        start_x = start_point[pts][0]
        start_y = start_point[pts][1]

        for box in range(0, 10):

            if Counter <= total_mcqs:

                # print(Counter)

                ScanPortion = image[start_y:start_y +
                                    17, start_x:start_x + 22*4]
                MCQ = ScanMCQs(ScanPortion)
                start_y += 17

                sheet[Counter] = MCQ
                Counter += 1

            else:
                break

    ScannedOmrs.append(sheet)

print(ScannedOmrs)
