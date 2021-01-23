import time
import random
import pyautogui
import base

x ,y, r, b = base.first()


orderPositions = [
  [140, 400],
  [240, 400],
  [340, 400],
  [140, 530],
  [240, 530],
  [340, 530]
]
for origin in orderPositions:
    origin[0]=origin[0] + x
    origin[1]=origin[1] + y
    

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
  [170, 610],
  [220, 620],
  [220, 620]
]
for origin in driedFishPosition:
    origin[0]=origin[0] + x
    origin[1]=origin[1] + y


salesmanPosition = [149+x,728+y]
foxPosition = [130+x, 370+y]
publicCityClickPosition=[412+x,788+y]





# 点菜
def orderDishes(mouseMoveSpeed):
  time.sleep(random.randint(0, 3))
  for items in orderPositions:
    pyautogui.moveTo(items[0], items[1], mouseMoveSpeed)
    pyautogui.click()

# 拾取鱼干
def pickUpDriedFish(mouseMoveSpeed):
  for items in driedFishPosition:
    pyautogui.moveTo(items[0], items[1], mouseMoveSpeed)
    pyautogui.click()

# 干掉推销员
def closeYourMic(mouseMoveSpeed):
  pyautogui.moveTo(salesmanPosition[0], salesmanPosition[1], mouseMoveSpeed)
  pyautogui.click()

# 去nm的臭鼬
def fuckFox(mouseMoveSpeed):
  pyautogui.moveTo(foxPosition[0], foxPosition[1], mouseMoveSpeed)
  for i in range(20):
    pyautogui.click()

#  
def locateToPublicCityClick(publicCityClickCount, mouseMoveSpeed):
  pyautogui.moveTo(publicCityClickPosition[0], publicCityClickPosition[1], mouseMoveSpeed)
  for i in range(random.randint(1, publicCityClickCount)):
    pyautogui.click()