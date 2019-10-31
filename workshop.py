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

    # Todo: your vision pipeline here
    # update the variable found to equal the number
    # of pumpkins in [img]

    # uncomment this line to pass one of the test cases
    # found = 3

    if found < minFind or found > maxFind:
        print("FAILED :( " + name + " found " + str(found))
    else:
        print("PASSED :D " + name)