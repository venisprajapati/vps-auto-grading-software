import cv2
import glob
import os
from services.functions import ResizeImagewithAspectRatio, BlackAndWhiteImage, ScanID, ScanMCQs
from services.contour_ import find_ROI


# This file contains code of applying some image processing algorithm to scanned omr images then extract required mcq with count of pixels to count marked or ticked bubbles in mcq form omr sheet././

def ScanOmrs(total_mcqs):

    image_list = glob.glob('./uploads/omrs/*.jpg')
    image_list += glob.glob('./uploads/omrs/*.jpeg')
    image_list += glob.glob('./uploads/omrs/*.png')

    id_point = (21, 50)
    start_point = [(21, 221), (134, 50), (134, 221), (247, 50), (247, 221), (360, 50), (360, 221), (473, 50), (473, 221),
                   (21, 410), (21, 581), (134, 410), (134, 581), (247, 410), (247,
                                                                              581), (360, 410), (360, 581), (473, 410), (473, 581),
                   (21, 772), (134, 772), (247, 772), (360, 772), (473, 772)]
    total_bubble_count_in_column = [10, 10, 10, 10, 10, 10, 10, 10,
                                    10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 2, 2, 2, 2, 2]

    ScannedOmrs = []

    for im in image_list:

        if total_mcqs > 90:

            img = find_ROI(im, True)
            img = ResizeImagewithAspectRatio(
                img, width=564, inter=cv2.INTER_AREA)
            img = cv2.resize(img, (564, 820), interpolation=cv2.INTER_AREA)

        else:

            img = find_ROI(im, False)
            img = ResizeImagewithAspectRatio(
                img, width=564, inter=cv2.INTER_AREA)
            img = cv2.resize(img, (564, 394), interpolation=cv2.INTER_AREA)

        image = BlackAndWhiteImage(img)

        sheet = {}

        IdPortion = image[id_point[1]:id_point[1] +
                          17*10, id_point[0]:id_point[0] + 22*4]
        id = ScanID(IdPortion)
        sheet["id"] = id

        Counter = 1

        for pts in range(0, len(start_point)):

            start_x = start_point[pts][0]
            start_y = start_point[pts][1]

            total_bubble_count = total_bubble_count_in_column[pts]

            for box in range(0, total_bubble_count):

                if Counter <= total_mcqs:

                    ScanPortion = image[start_y:start_y +
                                        17, start_x:start_x + 22*4]
                    MCQ = ScanMCQs(ScanPortion)
                    start_y += 17

                    sheet[Counter] = MCQ
                    Counter += 1

                else:
                    break

        ScannedOmrs.append(sheet)

    directory = './uploads/omrs'
    for f in os.listdir(directory):
        os.remove(os.path.join(directory, f))

    return ScannedOmrs
