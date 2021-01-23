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

    if(i + 1) % 10 == 0:
      time.sleep(random.randint(5, 30))
      move.toLeft()
      garden.sowFlower(mouseMoveSpeed)
      move.toRight()





def monitor():
  p1 = multiprocessing.Process(target=run,args=())
  p1.start()
  time.sleep(3)
  tm = 0
  print("开始查找咯")
  while tm==0 :
    time.sleep(0.1)
    fox_exist, fox_x, fox_y = base.check_character('fox')
    bird_exist, bird_x, bird_y = base.check_character('bird')
    tv_exist, tv_x, tv_y = base.check_character('tv')
    panda_exist, panda_x, panda_y = base.check_character('panda')
    fine_exist, fine_x, fine_y = base.check_character('fine')


    if fox_exist == 1:
      p1.terminate()
      event.fuck_fox()
      p1 = multiprocessing.Process(target=run, args=())
      p1.start()
    elif bird_exist == 1:
      p1.terminate()
      event.fuck_bird()
      p1 = multiprocessing.Process(target=run, args=())
      p1.start()
    elif tv_exist == 1:
      p1.terminate()
      event.fuck_tv()
      p1 = multiprocessing.Process(target=run, args=())
      p1.start()
    elif panda_exist == 1:
      p1.terminate()
      event.fuck_panda()
      p1 = multiprocessing.Process(target=run, args=())
      p1.start()
    elif fine_exist == 1:
      p1.terminate()
      event.fuck_fine()
      p1 = multiprocessing.Process(target=run, args=())
      p1.start()


    print("fox" + str(fox_exist))
    print("bird" + str(bird_exist))
    print("tv" + str(tv_exist))
    print("panda" + str(panda_exist))
    print("fine" + str(fine_exist))



if __name__=='__main__':
  print('空格开始')
  keyboard.wait('space')
  p2 = multiprocessing.Process(target=monitor, args=())
  p2.start()

  print('按下空格键退出程序') 
  keyboard.wait('space')
  sys.exit()

