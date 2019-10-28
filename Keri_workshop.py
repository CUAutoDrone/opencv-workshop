import cv2
import numpy as np

targets = [
    ("Image 1", cv2.imread("img/1.jpg"), 4, 4),
    ("Image 2", cv2.imread("img/2.jpg"), 2, 4),
    ("Image 3", cv2.imread("img/3.jpg"), 5, 8)
]

for target in targets:
    name = target[0]
    img = target[1]
    minFind = target[2]
    maxFind = target[3]

    found = -1


    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_orange = np.array([0, 101, 170])
    upper_orange = np.array([round((40/180)*255), 255, 255])
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    #dilation = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((9,9),np.uint8))
    erosion = cv2.erode(mask, np.ones((5,5),np.uint8), iterations = 2)
    dilation = cv2.dilate(erosion, np.ones((5,5),np.uint8), iterations = 3)
    cv2.imshow('erode & dilation', dilation)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    contours,heirarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, 2)
    found = len(contours)

    # uncomment this line to pass one of the test cases
    # found = 3

    if found < minFind or found > maxFind:
        print("FAILED :( " + name)
    else:
        print("PASSED :D " + name)
