import cv2
import glob
import os
from services.functions import ResizeImagewithAspectRatio, BlackAndWhiteImage, ScanID, ScanMCQs
from services.contour_ import find_ROI


def ScanOmrs(total_mcqs):

    image_list = glob.glob('./uploads/omrs/*.jpg')
    image_list += glob.glob('./uploads/omrs/*.jpeg')
    image_list += glob.glob('./uploads/omrs/*.png')

    id_point = (21, 49)
    start_point = [(21, 220), (134, 49), (134, 220), (247, 49), (247, 220), (360, 49), (360, 220), (473, 49), (473, 220),
                   (21, 448), (21, 619), (134, 448), (134, 619), (247, 448), (247, 619), (360, 448), (360, 619), (473, 448), (473, 619)]

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

            for box in range(0, 10):

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
