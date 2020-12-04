import pyautogui

def goToKitchen():
  pyautogui.moveTo(80, 500, 0.5)
  pyautogui.dragTo(10, 500, 0.3)

def goToGarden():
  pyautogui.moveTo(10, 500, 0.5)
  pyautogui.dragTo(80, 500, 0.3)

def goToRestaurant():
  pyautogui.moveTo(10, 500, 0.5)
  pyautogui.dragTo(80, 500, 0.3)