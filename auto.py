import keyboard
import multiprocessing
import restaurant

if __name__=='__main__':
  p1 = multiprocessing.Process(target=restaurant.run)
  p1.start() 
  print('按下空格键退出程序')
  keyboard.wait('space')
  p1.terminate()
 