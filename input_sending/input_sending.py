import pydirectinput
import time

class SendInput:

  def tapKey(self, key):
    pydirectinput.keyDown(key)
    pydirectinput.keyUp(key)

  def holdKeyForDuration(self, key, duration):
    self.holdKey(key)
    time.sleep(duration)
    self.releaseKey(key)

  def holdKey(self, key):
    pydirectinput.keyDown(key)

  def releaseKey(self, key):
    pydirectinput.keyUp(key)

  def interpretLocations(self, locations, delay):
    topArrow = locations[0]
    time.sleep(delay)
    self.tapKey('d')
    # if (topArrow[1] <= 130):
    #   time.sleep(delay)
    #   self.sendKey('d')