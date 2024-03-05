import cv2
import imutils
import numpy as np


def nothing(x):
	pass


cap = cv2.VideoCapture(0)

# Create a black image window
img = np.zeros((100, 100, 100), np.uint8)
cv2.namedWindow('HSV color picker')

# Create trackbars for color change
cv2.createTrackbar('H', 'HSV color picker', 0, 179, nothing)
cv2.createTrackbar('OFF/ON', 'HSV color picker', 0, 1, nothing)

while True:

	# Take each frame
	_, frame = cap.read()
	kernel = np.ones((10, 10), np.float32) / 100
	img = cv2.filter2D(frame, -1, kernel)

	# Convert BGR to HSV
	img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

	# Get current positions of the trackbars
	h = cv2.getTrackbarPos('H', 'HSV color picker')
	s = cv2.getTrackbarPos('OFF/ON', 'HSV color picker')

	# Show respective results
	lower_color = np.array([h - 5, 50, 50])
	upper_color = np.array([h + 5, 255, 255])
	mask = cv2.inRange(img, lower_color, upper_color)
	res = cv2.bitwise_and(frame, frame, mask=mask)
	if s == 0:
		cv2.imshow('HSV color picker', frame)
	else:
		cv2.imshow('HSV color picker', res)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
