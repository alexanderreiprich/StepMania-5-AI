from PIL import ImageGrab
import mss.tools
import win32gui
import pygetwindow
import time
import numpy

stepWindow = pygetwindow.getWindowsWithTitle('StepMania')
hwnd = stepWindow[0]._hWnd
bbox = win32gui.GetWindowRect(hwnd)

class Screenshot:
  def screenshotGameplay(hwnd, bbox):
    win32gui.SetForegroundWindow(hwnd)
    img = ImageGrab.grab(bbox)
    size = img.size 
    img = img.crop((110, 35, 400, 530))

    # convert ImageGrab image to OpenCV image
    opencvImg = img.convert('RGB')
    opencvImg = numpy.array(opencvImg)
    opencvImg = opencvImg[:, :, ::-1].copy()
    return opencvImg

  def screenshotCombo(hwnd, bbox):
    win32gui.SetForegroundWindow(hwnd)
    img = ImageGrab.grab(bbox)
    size = img.size 
    img = img.crop((550, 300, 650, 430))

    img.save(r'assets\combo.png')

    # convert ImageGrab image to OpenCV image
    opencvImg = img.convert('RGB')
    opencvImg = numpy.array(opencvImg)
    opencvImg = opencvImg[:, :, ::-1].copy()
    return opencvImg