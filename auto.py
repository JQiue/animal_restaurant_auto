import pyautogui
import time
import random

mouseMoveSpeed = 0.22

orderPositions = [
  [140, 400],
  [240, 400],
  [340, 400],
  [140, 530],
  [240, 530],
  [340, 530]
]

driedFishPosition = [
  [200, 400],
  [300, 400],
  [400, 400],
  [200, 530],
  [300, 530],
  [400, 530],
  [80, 370],
  [200, 720],
  [220, 650],
  [170, 610]
]

# 定位到宣传按钮
def locateToPbulicCityClick(count):
  pyautogui.moveTo(412, 788, mouseMoveSpeed)
  for i in range(count):
    pyautogui.click()

# 点菜
def orderDishes():
  time.sleep(random.randint(0, 3))
  for items in orderPositions:
    pyautogui.moveTo(items[0], items[1], mouseMoveSpeed)
    pyautogui.click()

# 拾取鱼干
def pickUpDriedFish():
  for items in driedFishPosition:
    pyautogui.moveTo(items[0], items[1], mouseMoveSpeed)
    pyautogui.click()

# 干掉推销员
def closeYourMic():
  pyautogui.moveTo(149, 728, mouseMoveSpeed)
  pyautogui.click()

# 去nm的臭鼬
def fuckFox():
  pyautogui.moveTo(130, 370, mouseMoveSpeed)
  for i in range(20):
    pyautogui.click()

for i in range(10000):
  orderDishes()
  locateToPbulicCityClick(64)
  pickUpDriedFish()
  if (i + 1) % 50 == 0:
    print("任务冷却五秒后继续......")
    time.sleep(5)
  if (i + 1) % 1 == 0:  
    fuckFox()

