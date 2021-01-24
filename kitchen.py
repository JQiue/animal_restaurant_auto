import time
import random
import pyautogui
import base

x ,y, r, b = base.first()

driedFishPosition = [
  [50, 300],
  [380, 340],
  [200, 650],
  [145, 400],
  [85, 400],
  [340, 510],
]
for origin in driedFishPosition:
    origin[0]=origin[0] + x
    origin[1]=origin[1] + y


def pickUpDriedFish(mouseMoveSpeed):
  for items in driedFishPosition:
    pyautogui.moveTo(items[0], items[1], mouseMoveSpeed)
    pyautogui.click()