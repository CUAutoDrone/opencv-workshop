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
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_orange = np.array([0, 69, 174])
    upper_orange = np.array([63, 255, 255])

    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    cv2.imshow("HSV Threshold", mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    erosion_size = 2
    erosion_element = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * erosion_size + 1, 2 * erosion_size + 1),
                                        (erosion_size, erosion_size));

    erosion_output = cv2.erode(mask, erosion_element, iterations=1)
    cv2.imshow("Erosion", erosion_output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    dilation_size = 2
    dilation_element = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * dilation_size + 1, 2 * dilation_size + 1),
                                       (dilation_size, dilation_size))
    dilation_output = cv2.dilate(erosion_output, dilation_element, iterations=2)
    cv2.imshow("Dilation", dilation_output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    contours, _ = cv2.findContours(dilation_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    found = len(contours)
    print("The number of contours found is " + str(found))

    if found < minFind or found > maxFind:
        print("FAILED :( " + name)
    else:
        print("PASSED :D " + name)