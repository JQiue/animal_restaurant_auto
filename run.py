import keyboard
import multiprocessing
import random
import time
import restaurant
import garden
import kitchen
import move
import base
import event
import sys


mouseMoveSpeed = 0.1
def run(count = 50000, publicCityClickCount = 64):
  print('开始咯...')
  # #归位
  # move.toLeft()
  # move.toLeft()
  # move.toLeft()
  # move.toLeft()
  # move.toRight()
  # move.toRight()
  #开始循环
  for i in range(count):
    restaurant.locateToPublicCityClick(publicCityClickCount, mouseMoveSpeed)
    restaurant.orderDishes(mouseMoveSpeed)
    restaurant.pickUpDriedFish(mouseMoveSpeed)
    if (i + 1) % 10 == 0:
      allfries()
      time.sleep(random.randint(5, 30))
    if (i + 1) % 51 == 0:
      flowers()



def allfries():
    move.toRight()
    time.sleep(0.2)
    kitchen.pickUpDriedFish(mouseMoveSpeed=mouseMoveSpeed)
    move.toLeft()
    move.toLeft()
    time.sleep(0.2)
    garden.pickUpDriedFish(mouseMoveSpeed=mouseMoveSpeed)
    move.toRight()

def flowers():
    time.sleep(random.randint(5, 30))
    move.toLeft()
    garden.sowFlower(mouseMoveSpeed)
    move.toRight()



if __name__=='__main__':
  print('空格开始')
  keyboard.wait('space')
  p1 = multiprocessing.Process(target=run, args=())
  p1.start()
  print('按下空格键退出程序') 
  keyboard.wait('space')
  p1.terminate()
  print('再按一下关闭')
  keyboard.wait('space')



