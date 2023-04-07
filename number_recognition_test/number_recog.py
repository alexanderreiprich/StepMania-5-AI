from PIL import Image
import pytesseract

class RecognizeText:
  def is_text_in_image(self, img, text, chars):
    done = False
    
    res = pytesseract.image_to_string(img)[:chars]
    if res in text:
      done = True

    return done, res

  def get_number_from_image(self, img):
    reformatted_string = pytesseract.image_to_string(img, config='-c tessedit_char_whitelist=0123456789')
    return int(reformatted_string)