import time
import random
import pyautogui
import base
import event
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
      time.sleep(0.1)
  event.fuck_fine()
  check_event()



def check_event():
  event.fuck_fine()
  base.get_screen_img()
  bird_exist, bird_x, bird_y = base.scan('bird')
  tv_exist, tv_x, tv_y = base.scan('tv')
  witch_exist, witch_x, witch_y = base.scan('witch')
  witch_exist2, witch_x, witch_y = base.scan('witch2')
  rat_exist, rat_x, rat_y = base.scan('rat')
  crow_exist, crow_x, crow_y = base.scan('crow')
  print("witch" + str(witch_exist+witch_exist2))
  print("bird" + str(bird_exist))
  print("tv" + str(tv_exist))
  print("rat" + str(rat_exist))
  print("crow" + str(crow_exist))
  if witch_exist+witch_exist2 != 0:
      event.fuck_witch()
  elif bird_exist == 1:
    event.fuck_bird()
  elif tv_exist == 1:
    event.fuck_tv()
  elif rat_exist == 1:
    event.fuck_rat()
  elif crow_exist == 1:
    event.fuck_crow()