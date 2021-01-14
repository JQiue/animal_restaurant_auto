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