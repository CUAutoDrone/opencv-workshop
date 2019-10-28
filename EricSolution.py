import cv2 as cv
import numpy as np

targets = [
    ("Image 1", cv.imread("img/1.jpg"), 4, 4),
    ("Image 2", cv.imread("img/2.jpg"), 2, 4),
    ("Image 3", cv.imread("img/3.jpg"), 5, 8)
]

for target in targets:
    name = target[0]
    img = target[1]
    minFind = target[2]
    maxFind = target[3]

    found = -1

    # Todo: your vision pipeline here
    # update the variable found to equal the number
    # of pumpkins in [img]

    # uncomment this line to pass one of the test cases
    # found = 3

    # convert to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # HSV threshold
    lower_orange = np.array([0, 130, 175])
    upper_orange = np.array([64, 255, 255])
    mask = cv.inRange(hsv, lower_orange, upper_orange)

    # erode
    kernel = np.ones((5, 5), np.uint8)
    erode = cv.erode(mask, kernel, iterations= 2)

    # dilate
    dilate = cv.dilate(erode, kernel, iterations=3)

    # count contours
    contours, hierarchy = cv.findContours(dilate, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    found = len(contours)

    if found < minFind or found > maxFind:
        print("FAILED :( " + name + " count= " + str(found))
    else:
        print("PASSED :D " + name + " count= " + str (found))