
# -*- encoding: utf-8 -*-
 
import time
import pyautogui as pag
import base


try:
    while True:
        print("Press Ctrl-C to end")
        screenWidth, screenHeight = pag.size()  # 获取屏幕的尺寸
        x1, y1, r, b = base.first()
        x, y = pag.position()  # 返回鼠标的坐标

        print("Screen size: (%s %s),  Position : (%s, %s)\n" % (screenWidth, screenHeight, x-x1, y-y1))  # 打印坐标
 
        time.sleep(1)  # 每个1s中打印一次 , 并执行清屏
except KeyboardInterrupt:
    print('end')