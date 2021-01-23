import move
import base
import pyautogui
import time

x ,y, r, b = base.first()
no = [135+x,725+y]
salesmanPosition = [149+x,728+y]

def fuck_fox():
    i = 0
    while i < 10:
        i = i + 1
        o, fox_x, fox_y = base.scan('fox')
        fox_x=fox_x+x
        fox_y=fox_y+y
        pyautogui.moveTo(fox_x,fox_y,0.3)
        pyautogui.click()
        pyautogui.click()
        time.sleep(0.1)

def fuck_bird():
    time.sleep(5)
    i=0
    while i < 10:
        i=i+1
        o, bird_x, bird_y = base.scan('bird')
        bird_x=bird_x + x
        bird_y=bird_y + y
        pyautogui.moveTo(bird_x,bird_y,0.3)
        pyautogui.click()
        pyautogui.click()
        time.sleep(0.1)

def fuck_tv():
    time.sleep(5)
    o, tv_x, tv_y = base.scan('tv')
    tv_x = tv_y + x
    tv_y = tv_y + y
    pyautogui.moveTo(tv_x, tv_y,0.3)
    pyautogui.click()
    pyautogui.moveTo(no[0],no[1],0.3)
    time.sleep(1)
    pyautogui.click()

def fuck_panda():
    i = 0
    while i < 10:
        i = i + 1
        o, panda_x, panda_y = base.scan('panda')
        panda_x=panda_x+x
        panda_y=panda_y+y
        pyautogui.moveTo(panda_x,panda_y,0.3)
        pyautogui.click()
        pyautogui.click()
        time.sleep(0.1)

def fuck_fine():
    time.sleep(5)
    pyautogui.moveTo(217+y, 550+x,0.3)
    pyautogui.click()






