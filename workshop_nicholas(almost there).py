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
     # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([0,204,188])
    upper_blue = np.array([92,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)


    kernel = np.ones((2,2),np.uint8)
    erosion = cv2.erode(mask,kernel,iterations = 5)
    kernel2 = np.ones((4,4),np.uint8)
    dilate = cv2.dilate(erosion,kernel2,iterations = 4)

    contours,hierarchy = cv2.findContours(dilate, cv2.RETR_EXTERNAL, 2)
    found = len(contours)

    cv2.drawContours(dilate, contours, -1, (0,255,0), 3)
    print(found)
    # Bitwise-AND mask and original image
    # Todo: your vision pipeline here
    # update the variable found to equal the number
    # of pumpkins in [img]

    # uncomment this line to pass one of the test cases
    # found = 3

    cv2.imshow('Hello World', dilate)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    if found < minFind or found > maxFind:
        print("FAILED :( " + name)
    else:
        print("PASSED :D " + name)
