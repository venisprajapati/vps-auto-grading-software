import cv2
import glob
from services.functions import ResizeImagewithAspectRatio, BlackAndWhiteImage, ScanID, ScanMCQs
from services.contour_ import find_ROI


image_list_90 = glob.glob('test/mcq-90/*.jpg')
image_list_90 += glob.glob('test/mcq-90/*.jpeg')
image_list_90 += glob.glob('test/mcq-90/*.png')

image_list_190 = glob.glob('test/mcq-190/*.jpg')
image_list_190 += glob.glob('test/mcq-190/*.jpeg')
image_list_190 += glob.glob('test/mcq-190/*.png')


id_point = (21, 49)
start_point = [(21, 220), (134, 49), (134, 220), (247, 49), (247, 220), (360, 49), (360, 220), (473, 49), (473, 220),
               (21, 448), (21, 619), (134, 448), (134, 619), (247, 448), (247, 619), (360, 448), (360, 619), (473, 448), (473, 619)]

ScannedOmrs = []


def scan_omr(image, total_mcqs):

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


for im in image_list_90:

    img = find_ROI(im, False)
    img = ResizeImagewithAspectRatio(img, width=564, inter=cv2.INTER_AREA)
    img = cv2.resize(img, (564, 394), interpolation=cv2.INTER_AREA)

    scan_omr(img, 90)

for im in image_list_190:

    img = find_ROI(im, True)
    img = ResizeImagewithAspectRatio(img, width=564, inter=cv2.INTER_AREA)
    img = cv2.resize(img, (564, 820), interpolation=cv2.INTER_AREA)

    scan_omr(img, 190)


print(ScannedOmrs)
