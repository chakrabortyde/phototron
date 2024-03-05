import cv2
import numpy as np


def find_centroid(contour):
    moments = cv2.moments(contour)
    if moments["m00"] != 0:
        cX = int(moments["m10"] / moments["m00"])
        cY = int(moments["m01"] / moments["m00"])
        return cX, cY
    else:
        return None, None


cap = cv2.VideoCapture(0)
x = int(input("Enter '1' for RED, "
              "'2' for GREEN, "
              "'3' for BLUE or "
              "'4' for YELLOW: "))

while True:
    _, frame = cap.read()
    frame = cv2.GaussianBlur(frame, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if x == 1:
        # lower mask (0-10)
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([10, 255, 255])
        mask0 = cv2.inRange(hsv, lower_red, upper_red)

        # upper mask (170-180)
        lower_red = np.array([170, 50, 50])
        upper_red = np.array([180, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)

        # join my masks
        mask = mask0 + mask1

    elif x == 2:
        # lower mask (0-10)
        lower_green = np.array([75, 50, 50])
        upper_green = np.array([85, 255, 255])
        mask0 = cv2.inRange(hsv, lower_green, upper_green)

        # upper mask (170-180)
        lower_green = np.array([85, 50, 50])
        upper_green = np.array([95, 255, 255])
        mask1 = cv2.inRange(hsv, lower_green, upper_green)

        # join my masks
        mask = mask0 + mask1

    elif x == 3:
        # lower mask (0-10)
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([120, 255, 255])
        mask0 = cv2.inRange(hsv, lower_blue, upper_blue)

        # upper mask (170-180)
        lower_blue = np.array([120, 50, 50])
        upper_blue = np.array([130, 255, 255])
        mask1 = cv2.inRange(hsv, lower_blue, upper_blue)

        # join my masks
        mask = mask0 + mask1

    elif x == 4:
        # lower mask (0-10)
        lower_yellow = np.array([20, 50, 50])
        upper_yellow = np.array([30, 255, 255])
        mask0 = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # upper mask (170-180)
        lower_yellow = np.array([30, 50, 50])
        upper_yellow = np.array([40, 255, 255])
        mask1 = cv2.inRange(hsv, lower_yellow, upper_yellow)

        # join my masks
        mask = mask0 + mask1
    else:
        quit()

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                                   cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)
            cx, cy = find_centroid(contour)
            if cx is not None and cy is not None:
                cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
