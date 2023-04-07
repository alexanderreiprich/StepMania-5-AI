from input_sending_test.input_sending import SendInput
from pattern_recognition_test.pattern_recog import RecognizePattern
from image_analysis_test.take_screenshot import Screenshot
from number_recognition_test.number_recog import RecognizeNumber
import pygetwindow
import pytesseract
import win32gui
import time
from PIL import Image

# Change variable according to your tesseract installation path
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'G:\Programme\Tesseract\tesseract.exe'

recognizePattern = RecognizePattern([])
useInput = SendInput()

stepWindow = pygetwindow.getWindowsWithTitle('StepMania')
hwnd = stepWindow[0]._hWnd
bbox = win32gui.GetWindowRect(hwnd)
win32gui.SetForegroundWindow(hwnd)

# i = 0

# while i < 100:
#   image = Screenshot.screenshot(hwnd, bbox, (110, 35, 400, 530))
#   start = time.time()
#   arrowArray = recognizePattern.analyzeImage(image)
#   feedback = RecognizeNumber()
#   useInput.interpretLocations(arrowArray, 0.0)
#   end = time.time() - start
#   i += 1
#   print(end)

# recognizePattern.exportVideo()