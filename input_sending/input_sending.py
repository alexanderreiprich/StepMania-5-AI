import pydirectinput

class SendInput:

  def holdKey(self, key):
    pydirectinput.keyDown(key)

  def releaseKey(self, key):
    pydirectinput.keyUp(key)