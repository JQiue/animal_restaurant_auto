import pyautogui
import base

x ,y, r, b = base.first()

def toLeft():
  pyautogui.moveTo(25+x, 442+y, 0.5)
  pyautogui.click()


def toRight():
  pyautogui.moveTo(419+x, 442+y, 0.5)
  pyautogui.click()

def toUp():
  pyautogui.moveTo(150+x, 207+y, 0.5)
  pyautogui.click()

def toDown():
  pyautogui.moveTo(166+x, 800+y, 0.5)
  pyautogui.click()