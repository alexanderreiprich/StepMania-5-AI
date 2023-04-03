# from input_sending_test.input_sending import SendInput
# from pattern_recognition_test.pattern_recog import RecognizePattern
from image_analysis_test.take_screenshot import Screenshot
# from number_recognition_test.number_recog import RecognizeNumber
import pygetwindow
import pytesseract
import win32gui
import time
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'G:\Programme\Tesseract\tesseract.exe'

# recognizePattern = RecognizePattern([])

stepWindow = pygetwindow.getWindowsWithTitle('StepMania')
hwnd = stepWindow[0]._hWnd
bbox = win32gui.GetWindowRect(hwnd)

i = 0


while i < 100:
  image = Screenshot.screenshot(hwnd, bbox)
  arrowArray = recognizePattern.analyzeImage(image)
  feedback = RecognizeNumber()
  # useInput.interpretLocationsGameplay(locations=arrowArray)
  i += 1
  feedback = RecognizeNumber()
  print(i)

recognizePattern.exportVideo()