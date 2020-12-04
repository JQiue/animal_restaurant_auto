import time
import random
import pyautogui

driedFishPosition = [
  [60, 320],
  [380, 340],
  [200, 650],
  [145, 400],
]

def pickUpDriedFish(mouseMoveSpeed):
  for items in driedFishPosition:
    pyautogui.moveTo(items[0], items[1], mouseMoveSpeed)
    pyautogui.click()
