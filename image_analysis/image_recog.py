import cv2

img = cv2.imread(r'assets\arrow.png')

# cv2.imshow("img", img)
# cv2.waitKey(0)

left = img[:, 25:95]
down = img[:, 95:165]
up = img[:, 165:235]
right = img[:, 240:300]

cv2.imshow("img", right)
cv2.waitKey(0)