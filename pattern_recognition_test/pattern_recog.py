import cv2 as cv
import numpy as np

class RecognizePattern:

  def __init__(self, videoArray):
    self.videoArray = videoArray
    self.template_down = cv.imread(r'assets\arrow_down.png', cv.IMREAD_GRAYSCALE)
    self.template_left = cv.imread(r'assets\arrow_left.png', cv.IMREAD_GRAYSCALE)
    self.template_right = cv.imread(r'assets\arrow_right.png', cv.IMREAD_GRAYSCALE)
    self.template_up = cv.imread(r'assets\arrow_up.png', cv.IMREAD_GRAYSCALE)
    self.template_array = [self.template_down, self.template_left, self.template_right, self.template_up]

  def analyzeImage(self, img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    threshold = 0.85
    arrowArray = []
    for template in self.template_array:
      w, h = template.shape[::-1]
      res = cv.matchTemplate(img_gray,template, cv.TM_CCOEFF_NORMED)
      loc = np.where(res >= threshold)
      for pt in zip(*loc[::-1]):
        cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        arrowArray.append(pt)

    # cv.imwrite(r'assets\res.png', img)
    self.videoArray.append(img)
    if not arrowArray:
      arrowArray = [(999, 999)]

    return arrowArray

  def exportVideo(self):
    frame_width = 290
    frame_height = 495
    out = cv.VideoWriter('export\result.avi', cv.VideoWriter_fourcc(*'DIVX'), 30, (frame_width, frame_height))
    for k in range(len(self.videoArray)):
      out.write(self.videoArray[k])
    out.release()
