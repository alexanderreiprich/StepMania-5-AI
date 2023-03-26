import pydirectinput
import time

class SendInput:
  def sendKey(self, key):
    pydirectinput.keyUp(key)
    pydirectinput.keyDown(key)

  def interpretLocations(self, locations):
    topArrow = locations[0]
    if (topArrow[1] <= 130):
      time.sleep(0.3)
      self.sendKey('d')