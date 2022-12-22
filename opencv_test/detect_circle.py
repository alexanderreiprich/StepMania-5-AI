import cv2
import numpy as np 

img_name = 'images/screenshot1226.jpg'

img = cv2.imread(img_name, cv2.IMREAD_COLOR )

gray = cv2.imread(img_name, cv2.IMREAD_GRAYSCALE )

gray_blurred = cv2.blur(gray, (3, 3))

minDist = 40
param1 = 170
param2 = 85
minRadius = 40
maxRadius = 400

detected_circles = cv2.HoughCircles(gray_blurred,
cv2.HOUGH_GRADIENT, 1, minDist, param1 = param1,
param2 = param2, minRadius = minRadius, maxRadius = maxRadius)

# Draw circles that are detected.
if detected_circles is not None:

  # Convert the circle parameters a, b and r to integers.
  detected_circles = np.uint16(np.around(detected_circles))

  for pt in detected_circles[0, :]:
    a, b, r = pt[0], pt[1], pt[2]

    # Draw the circumference of the circle.
    cv2.circle(img, (a, b), r, (0, 255, 0), 2)


  cv2.imshow("Detected Circle", img)
  cv2.waitKey(0)