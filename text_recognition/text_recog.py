from PIL import Image
import pytesseract

class RecognizeText:
  def is_text_in_image(self, img, text, chars):
    done = False
    
    res = pytesseract.image_to_string(img, lang='eng', config='--psm 7')[:chars]
    if res in text:
      done = True

    return done

  def get_number_from_image(self, img):
    reformatted_string = pytesseract.image_to_string(img, config='-c tessedit_char_whitelist=0123456789')
    if reformatted_string == '':
      reformatted_string = 0
    
    return int(reformatted_string)