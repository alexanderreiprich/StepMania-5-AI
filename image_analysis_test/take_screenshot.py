from PIL import ImageGrab
import win32gui
import pygetwindow

def screenshot(hwnd):
  win32gui.SetForegroundWindow(hwnd)
  bbox = win32gui.GetWindowRect(hwnd)
  img = ImageGrab.grab(bbox)
  size = img.size 
  img = img.crop((110, 35, 435, 530))
  img.save(r'assets\ss.png')

stepWindow = pygetwindow.getWindowsWithTitle('StepMania')
hwnd = stepWindow[0]._hWnd
screenshot(hwnd)