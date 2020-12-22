import cv2
import numpy as np
import matplotlib.pyplot as plot

class find_image:
    listData = []

    def __init__(self, gray, thresh, contours):
        self.listData = []
        min_rect_len = 80
        max_rect_len = 290

        # bo detnawae 4 goshakan
        c = 0
        im = []
        # cv2.imshow('iiiii', thresh)

        boundingBoxes = [cv2.boundingRect(c) for c in contours]
        (cnts, boundingBoxes) = zip(*sorted(zip(thresh, boundingBoxes), key=lambda b: b[1][1], reverse=True))
        # contours = contours[0] if len(contours) == 2 else contours[1]
        for contour in boundingBoxes:
            (x, y, w, h) = contour
            # print(w, '   ', h)
            if (h > min_rect_len and w > min_rect_len) and (h < max_rect_len and w < max_rect_len):
                # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
                # s = str(c) + " " + str(w) + " " + str(h)
                cv2.putText(gray, str(c), (x + 20, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
                # area = cv2.contourArea(contours)
                # if area < 9500:
                #     cv2.drawContours(thresh, [c], -1, (0, 0, 0), -1)
                # print(area)
                im.append(thresh[y+14: y + h-14, x+12: x + w-12])
                # print(x, y, w, h)
                c += 1
        cv2.imshow('i', gray)

        # bo zanini zhmarae rectangle
        print(c)
        self.count = c

        # bo awae bzanin awa X yan O

        # fig = plot.figure()

        c = 0
        for i in im:
            # cv2.imshow(str(i.shape), i)
            # bo detnawae circle
            circles = cv2.HoughCircles(i, cv2.HOUGH_GRADIENT, 1.2, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
            # bo detnawae X
            edges = cv2.Canny(i, 50, 150, apertureSize=3)
            lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 40, minLineLength=30, maxLineGap=30)
            # print(lines)
            if circles is not None:
                self.listData.append([c, 'O'])
                # ax = fig.add_subplot(6, 6, c)
                # cv2.imshow(str(i.shape), i)
            if lines is not None:
                # print(lines)
                # cv2.imshow(str(i.shape), i)
                self.listData.append([c, 'X'])
                # ax = fig.add_subplot(6, 6, c)
                # plot.imshow(i)
            # else:
            #     self.listData.append([c, ' '])
            c += 1
        print("1 ", self.listData)
        # plot.show()












 # for contour in contours:
        #     (x, y, w, h) = cv2.boundingRect(contour)
        #     if (h > min_rect_len and w > min_rect_len) and (h < max_rect_len and w < max_rect_len):
        #         # cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
        #         cv2.putText(gray, str(c), (x + 20, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        #         im.append(thresh[y + 3: y + h - 3, x + 3: x + w - 4])
        #         # print(x, y, w, h)
        #         c += 1
        # cv2.imshow('i', gray)