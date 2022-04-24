import cv2
import glob
from services.functions import ResizeImagewithAspectRatio, BlackAndWhiteImage, ScanID, ScanMCQs
from services.contour_ import find_ROI


image_list_90 = glob.glob('test/mcq-90/*.jpg')
image_list_90 += glob.glob('test/mcq-90/*.jpeg')
image_list_90 += glob.glob('test/mcq-90/*.png')

image_list_190 = glob.glob('test/mcq-200/*.jpg')
image_list_190 += glob.glob('test/mcq-200/*.jpeg')
image_list_190 += glob.glob('test/mcq-200/*.png')


id_point = (21, 50)
start_point = [(21, 221), (134, 50), (134, 221), (247, 50), (247, 221), (360, 50), (360, 221), (473, 50), (473, 221),
               (21, 410), (21, 581), (134, 410), (134, 581), (247, 410), (247, 581), (360, 410), (360, 581), (473, 410), (473, 581),
               (21, 772), (134, 772), (247, 772), (360, 772), (473, 772)]
total_bubble_count_in_column = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 2, 2, 2, 2, 2]

ScannedOmrs = []


def scan_omr(image, total_mcqs):

    image = BlackAndWhiteImage(img)

    rect_img = image.copy()

    for pts in range(0, len(start_point)):

        start_x = start_point[pts][0]
        start_y = start_point[pts][1]
        start = (start_x, start_y)
        total_bubble_count = total_bubble_count_in_column[pts]
        end = (start_x + 88, start_y + 17*total_bubble_count)
        color = (0, 255, 0)

        cv2.rectangle(rect_img, start, end, color, 1)

    # image = cv2.resize(image, (624, 524), interpolation=cv2.INTER_AREA)
    cv2.imshow('test-img', rect_img)
    cv2.waitKey(0)

    sheet = {}

    IdPortion = image[id_point[1]:id_point[1] +
                      17*total_bubble_count_in_column[0], id_point[0]:id_point[0] + 22*4]
    id = ScanID(IdPortion)
    sheet["id"] = id

    Counter = 1

    for pts in range(0, len(start_point)):

        start_x = start_point[pts][0]
        start_y = start_point[pts][1]

        for box in range(0, total_bubble_count_in_column[pts]):

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
    # print(img.shape[0], img.shape[1])
    img = ResizeImagewithAspectRatio(img, width=564, inter=cv2.INTER_AREA)
    img = cv2.resize(img, (564, 394), interpolation=cv2.INTER_AREA)

    scan_omr(img, 90)

for im in image_list_190:

    img = find_ROI(im, True)
    # print(img.shape[0], img.shape[1])
    img = ResizeImagewithAspectRatio(img, width=564, inter=cv2.INTER_AREA)
    img = cv2.resize(img, (564, 820), interpolation=cv2.INTER_AREA)

    scan_omr(img, 200)


print(ScannedOmrs)
