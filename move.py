import pyautogui

def toLeft():
  pyautogui.moveTo(25, 442, 0.5)
  pyautogui.click()


def toRight():
  pyautogui.moveTo(419, 442, 0.5)
  pyautogui.click()

def toUp():
  pyautogui.moveTo(150, 207, 0.5)
  pyautogui.click()

def toDown():
  pyautogui.moveTo(166, 800, 0.5)
  pyautogui.click()