import pyautogui
import time
import base

x ,y, r, b = base.first()



driedFishPosition = [
  [50, 270],
  [305, 233]
]
for origin in driedFishPosition:
    origin[0]=origin[0] + x
    origin[1]=origin[1] + y

potPosition = [
  [136, 411],
  [226, 546],
  [311, 405],
  [226, 546],
  [135, 525],
  [226, 546],
  [311, 525],
  [226, 546]
]
for origin in potPosition:
    origin[0]=origin[0] + x
    origin[1]=origin[1] + y

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