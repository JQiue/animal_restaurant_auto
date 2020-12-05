import pyautogui

def toLeft():
  pyautogui.moveTo(227, 467, 0.5)
  pyautogui.dragTo(260, 467, 0.3)


def toRight():
  pyautogui.moveTo(227, 467, 0.5)
  pyautogui.dragTo(180, 467, 0.3)

def toUp():
  pyautogui.moveTo(227, 467, 0.5)
  pyautogui.dragTo(227, 520, 0.3)

def toDown():
  pyautogui.moveTo(227, 467, 0.5)
  pyautogui.dragTo(227, 420, 0.3)
