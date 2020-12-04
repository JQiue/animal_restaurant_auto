import time
import random
import pyautogui
import kitchen
import scence

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
  [170, 610],
  [220, 620],
  [220, 620]
]

# 定位到宣传按钮
def locateToPublicCityClick(count, mouseMoveSpeed):
  pyautogui.moveTo(412, 788, mouseMoveSpeed)
  for i in range(count):
    pyautogui.click()

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
  pyautogui.moveTo(149, 728, mouseMoveSpeed)
  pyautogui.click()

# 去nm的臭鼬
def fuckFox(mouseMoveSpeed):
  pyautogui.moveTo(130, 370, mouseMoveSpeed)
  for i in range(20):
    pyautogui.click()

def run(count = 10000 , publicCityClick = 64, mouseMoveSpeed = 0.05):
  for i in range(count):
    print('上菜...')
    orderDishes(mouseMoveSpeed)
    print('拾取鱼干...')
    pickUpDriedFish(mouseMoveSpeed)
    print('宣传...')
    locateToPublicCityClick(publicCityClick, mouseMoveSpeed)
    if(i + 1) % 5:
      print("前往厨房")
      scence.goToKitchen()
      print("拾取鱼干")
      kitchen.pickUpDriedFish(mouseMoveSpeed=mouseMoveSpeed )
      print("前往餐厅")
      scence.goToRestaurant()