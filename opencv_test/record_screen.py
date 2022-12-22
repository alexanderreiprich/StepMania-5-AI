import cv2
import numpy as np 
from PIL import ImageGrab, Image

fps = 20
start = 3
end = 8

curScreen = ImageGrab.grab().convert(('L'))
print(curScreen.getdata())
height, width = curScreen.size

video = cv2.VideoWriter('video.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (height, width))

imageNum = 0
while True:
  imageNum += 1

  grabbedImg = ImageGrab.grab().convert(('L'))
  convertImg = np.array(grabbedImg)
  array = np.arange(0, 2073600, 1, np.uint8)
  array = np.reshape(array, (1920, 1080))

  frame = array

  if (imageNum > fps * start):
    video.write(frame)

  if (cv2.waitKey(50) == ord('q') or imageNum > fps * end):
    break

video.release()
cv2.destroyAllWindows()