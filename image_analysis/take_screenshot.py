from PIL import ImageGrab
import mss.tools
import win32gui
import pygetwindow
import time
import numpy as np
import cv2

class Screenshot:

  def downscaleImageBinary(self, img, size, shape):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    black_white = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)
    resized = cv2.resize(black_white[1], size)
    channel = np.reshape(resized, shape)
    return channel
