import move
import base
import pyautogui
import time

x ,y = base.first()

salesmanPosition = [149+x,728+y]
publicCityClickPosition=[412+x,788+y]

def fuck_fox():
    for i in (10):
        o, x, y = base.scan('fox')
        pyautogui.moveTo(x,y)
        pyautogui.click()
        pyautogui.click()
        time.sleep(0.1)

def fuck_bird():
    time.sleep(5)
    for i in (10):
        o, x, y = base.scan('bird')
        pyautogui.moveTo(x,y)
        pyautogui.click()
        pyautogui.click()
        time.sleep(0.1)

def fuck_tv():
    time.sleep(5)
    o, x, y = base.scan('tv')
    pyautogui.moveTo(x, y)
    pyautogui.click()








