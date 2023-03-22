from PIL import ImageGrab
import mss.tools
import win32gui
import pygetwindow
import time

def screenshotNew(hwnd, i):
  win32gui.SetForegroundWindow(hwnd)
  img = mss.mss().grab(bbox)
  size = img.size 
  path = r'assets\benchmarkNew\ss_{}.png'.format(i)
  mss.tools.to_png(img.rgb, img.size, output=path)

def screenshotOld(hwnd, i):
  win32gui.SetForegroundWindow(hwnd)
  img = ImageGrab.grab(bbox)
  size = img.size 
  img = img.crop((110, 35, 400, 530))
  path = r'assets\benchmarkOld\ss_{}.png'.format(i)
  img.save(path)

def benchmark():
  start = time.time()
  i = 0
  while i < 100:
    screenshotOld(hwnd, i)
    i += 1

  end = time.time()
  print (end - start)


stepWindow = pygetwindow.getWindowsWithTitle('StepMania')
hwnd = stepWindow[0]._hWnd
bbox = win32gui.GetWindowRect(hwnd)
benchmark()
