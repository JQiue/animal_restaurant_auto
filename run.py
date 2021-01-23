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

def run(count = 50000, publicCityClickCount = 64, mouseMoveSpeed = 0.1):
  print('开始咯...')
  #归位
  move.toLeft()
  move.toLeft()
  move.toLeft()
  move.toLeft()
  move.toRight()
  move.toRight()
  
  #开始循环
  for i in range(count):
    restaurant.locateToPublicCityClick(publicCityClickCount, mouseMoveSpeed)
    restaurant.orderDishes(mouseMoveSpeed)
    if(i + 1) % 3 == 0:
      restaurant.pickUpDriedFish(mouseMoveSpeed)
      move.toRight()
      time.sleep(0.2)
      kitchen.pickUpDriedFish(mouseMoveSpeed=mouseMoveSpeed)
      move.toLeft()
      move.toLeft()
      time.sleep(0.2)
      garden.pickUpDriedFish(mouseMoveSpeed=mouseMoveSpeed)
      move.toRight()
#      restaurant.fuckFox(mouseMoveSpeed)  有员工，暂时去除






    if(i + 1) % 10 == 0:
      time.sleep(random.randint(5, 30))
      move.toLeft()
      garden.sowFlower(mouseMoveSpeed)
      move.toRight()





def monitor():
  tm = 0
  while tm==0 :
    fox_exist, fox_x, fox_y = base.check_character('fox')
    bird_exist, bird_x, bird_y = base.check_character('bird')
    tv_exist, tv_x, tv_y = base.check_character('tv')
    if fox_exist == 1:
      p1.terminate()
      event.fuck_fox()
      p1 = multiprocessing.Process(target=run, args=())
      p1.start()
    elif bird_exist == 1:
      p1.terminate()
      event.fuck_bird()


if __name__=='__main__':
  p1 = multiprocessing.Process(target=run,args=())
  p1.start()

  print('按下空格键退出程序') 
  keyboard.wait('space')
  p1.terminate()