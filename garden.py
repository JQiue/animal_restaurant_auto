import pyautogui
import time

driedFishPosition = [
  [50, 270]
]

potPosition = [
  [136, 411],
  [226, 546],
  [311, 405],
  [226, 546],
  [135, 525],
  [226, 546]
]

flowerPosition = [
  [197, 392],
  [175, 383],
  [360, 392],
  [358, 386],
  [193, 506],
  [179, 500]
]

starsPosition = [
  [214, 247],
  [285, 247],
  [363, 247]
]

def pickUpDriedFish(mouseMoveSpeed):
  for items in driedFishPosition:
    pyautogui.moveTo(items[0], items[1], mouseMoveSpeed)
    pyautogui.click()

def sowFlower(mouseMoveSpeed):
  for items in potPosition:
    pyautogui.moveTo(items[0], items[1], mouseMoveSpeed)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.click()

def decorateFlower(mouseMoveSpeed):
  for items in flowerPosition:
    pyautogui.moveTo(items[0], items[1], mouseMoveSpeed)
    pyautogui.click()

def pickUpStar(mouseMoveSpeed):
  for items in starsPosition:
    pyautogui.moveTo(items[0], items[1], mouseMoveSpeed)
    pyautogui.click()