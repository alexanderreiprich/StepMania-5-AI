from PIL import Image
import pytesseract

class RecognizeNumber:
  def analyzeImage(self, img):
    
    text = pytesseract.image_to_string(img)
    print(text)