import cv2
import glob
import os
from services.functions import ResizeImagewithAspectRatio, BlackAndWhiteImage, ScanID, ScanMCQs


def ScanOmrs(total_mcqs):

    image_list = glob.glob('./uploads/omrs/*.jpg')
    image_list += glob.glob('./uploads/omrs/*.jpeg')
    image_list += glob.glob('./uploads/omrs/*.png')

    id_point = (42, 64)
    start_point = [(42, 240), (156, 64), (156, 240), (274, 64), (274, 240), (390, 64), (390, 240), (506, 64), (506, 240),
                   (42, 470), (42, 646), (156, 470), (156, 646), (274, 470), (274, 646), (390, 470), (390, 646), (506, 470), (506, 646)]

    ScannedOmrs = []

    for i in image_list:
        im = cv2.imread(i)
        img = ResizeImagewithAspectRatio(im, width=624)
        image = BlackAndWhiteImage(img)

        sheet = {}

        IdPortion = image[id_point[1]:id_point[1] +
                          17*10, id_point[0]:id_point[0] + 23*4 - 2]
        id = ScanID(IdPortion)
        sheet["id"] = id

        Counter = 1

        for pts in range(0, len(start_point)):

            start_x = start_point[pts][0]
            start_y = start_point[pts][1]

            for box in range(0, 10):

                if (Counter > total_mcqs):
                    break

                ScanPortion = image[start_y:start_y +
                                    17, start_x:start_x + 23*4]
                MCQ = ScanMCQs(ScanPortion)
                start_y += 17

                sheet[Counter] = MCQ
                Counter += 1

        ScannedOmrs.append(sheet)

    directory = './uploads/omrs'
    for f in os.listdir(directory):
        os.remove(os.path.join(directory, f))

    return ScannedOmrs
