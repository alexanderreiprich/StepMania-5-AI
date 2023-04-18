from PIL import ImageGrab
import mss.tools
import win32gui
import pygetwindow
import time
import numpy as np
import cv2

class Screenshot:
  def screenshot(self, hwnd, bbox, crop):
    # win32gui.SetForegroundWindow(hwnd)
    img = ImageGrab.grab(bbox)
    size = img.size
    img = img.crop(crop)

    # convert ImageGrab image to OpenCV image
    opencvImg = img.convert('RGB')
    opencvImg = np.array(opencvImg)
    opencvImg = opencvImg[:, :, ::-1].copy()
    #opencvImg = opencvImg[:, :, :3].copy()
    return opencvImg

  def downscaleImage(self, img, size, shape):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, size)
    channel = np.reshape(resized, shape)
    return channel

  def screenshotGameplay():
    win32gui.SetForegroundWindow(hwnd)
    img = ImageGrab.grab(bbox)
    size = img.size
    img = img.crop((110, 35, 400, 530))

    # convert ImageGrab image to OpenCV image
    opencvImg = img.convert('RGB')
    opencvImg = np.array(opencvImg)
    opencvImg = opencvImg[:, :, ::-1].copy()
    return opencvImg

  def screenshotCombo(hwnd, bbox):
    win32gui.SetForegroundWindow(hwnd)
    img = ImageGrab.grab(bbox)
    size = img.size
    img = img.crop((550, 300, 650, 430))

    # img.save(r'assets\combo.png')

    # convert ImageGrab image to OpenCV image
    opencvImg = img.convert('RGB')
    opencvImg = np.array(opencvImg)
    opencvImg = opencvImg[:, :, ::-1].copy()
    return opencvImg
