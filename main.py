from input_sending_test.input_sending import SendInput
from pattern_recognition_test.pattern_recog import RecognizePattern
from image_analysis_test.take_screenshot import Screenshot
import pygetwindow
import win32gui
import time

stepWindow = pygetwindow.getWindowsWithTitle('StepMania')
hwnd = stepWindow[0]._hWnd
bbox = win32gui.GetWindowRect(hwnd)
useInput = SendInput()

while True:
  image = Screenshot.screenshot(hwnd, bbox)
  arrowArray = RecognizePattern.analyzeImage(image)
  useInput.interpretLocations(locations=arrowArray)
