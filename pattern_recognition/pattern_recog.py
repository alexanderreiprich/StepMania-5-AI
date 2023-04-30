import cv2 as cv
import numpy as np
import time

class RecognizePattern:

  def __init__(self):
    self.template_results = cv.imread(r'assets\your_results.jpg', cv.IMREAD_GRAYSCALE)
    self.template_0 = cv.imread(r'assets\0.png', cv.IMREAD_GRAYSCALE)
    self.template_1 = cv.imread(r'assets\1.png', cv.IMREAD_GRAYSCALE)
    self.template_2 = cv.imread(r'assets\2.png', cv.IMREAD_GRAYSCALE)
    self.template_3 = cv.imread(r'assets\3.png', cv.IMREAD_GRAYSCALE)
    self.template_4 = cv.imread(r'assets\4.png', cv.IMREAD_GRAYSCALE)
    self.template_5 = cv.imread(r'assets\5.png', cv.IMREAD_GRAYSCALE)
    self.template_6 = cv.imread(r'assets\6.png', cv.IMREAD_GRAYSCALE)
    self.template_7 = cv.imread(r'assets\7.png', cv.IMREAD_GRAYSCALE)
    self.template_8 = cv.imread(r'assets\8.png', cv.IMREAD_GRAYSCALE)
    self.template_9 = cv.imread(r'assets\9.png', cv.IMREAD_GRAYSCALE)
    self.template_numbers = [
      self.template_0,
      self.template_1,
      self.template_2,
      self.template_3,
      self.template_4,
      self.template_5,
      self.template_6,
      self.template_7,
      self.template_8,
      self.template_9
    ]

  def convert(self):
    i = 0
    for i in range(10):
      cur_temp = self.template_numbers[i]
      threshold = 128
      im_bw = cv.threshold(cur_temp, threshold, 255, cv.THRESH_BINARY)[1]
      cv.imwrite(r'assets\bw_' + str(i) + ".png", im_bw)

  def analyze_results(self, img):
    threshold = 0.9
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    res = cv.matchTemplate(img_gray, self.template_results, cv.TM_CCOEFF_NORMED)
    if (res >= threshold).any():
      return True
    return False

  def analyze_score(self, img):
    threshold = 0.82
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    found_array = []
    index_template = 0
    for index_template in range(10):
      res = cv.matchTemplate(img_gray, self.template_numbers[index_template], cv.TM_CCOEFF_NORMED)
      loc = np.where(res >= threshold)
      for pt in zip(*loc[::-1]):
        found_array.append([pt[0], index_template])
        
    sorted_array = sorted(found_array, key=lambda x: x[0])
    result = ""
    for array in sorted_array:
      result += str(array[1])
    if result == "":
      result = "0"
    return(int(result))
