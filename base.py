import win32gui
import win32ui
import win32con
import win32api
import keyboard
import multiprocessing
import sys
import time
import cv2
from PIL import Image




def get_hwnd():
    return win32gui.FindWindow(None, '动物餐厅')
    
def get_cordinates(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    return left, top, right, bottom

def first():
    hwnd = get_hwnd()
    if hwnd:
        x, y, right, bottom = get_cordinates(hwnd)
        return x, y, right, bottom
    else:
        print('no program found!\nexiting in 5 seconds')
        time.sleep(5)
        sys.exit()
        



def import_img(spimg):
    if spimg == 'bird':
        img = cv2.imread('res/img/bird.jpg')
    elif spimg == 'fox':
        img = cv2.imread('res/img/fox.jpg')
    elif spimg == 'rat':
        img = cv2.imread('res/img/rat.jpg')
    elif spimg == 'crow':
        img = cv2.imread('res/img/crow.jpg')
    elif spimg == 'tv':
        img = cv2.imread('res/img/tv.jpg')
    elif spimg == 'fine':
        img = cv2.imread('res/img/fine.jpg')
    elif spimg == 'panda':
        img = cv2.imread('res/img/panda.jpg')
    elif spimg == 'witch':
        img = cv2.imread('res/img/witch.jpg')
    elif spimg == 'witch2':
        img = cv2.imread('res/img/witch2.jpg')
    return img
    
    
    
def get_screen_img():
    #获取图像
    m,n,p,q=first()
    width = p - m
    height = q - n
    hwnd = get_hwnd()
    hWndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, 'main.bmp')
    saveDC.DeleteDC()
    win32gui.DeleteObject(saveBitMap.GetHandle())
    img=Image.open('main.bmp')
    img.save('main.jpg')

def scan(object):
    target = cv2.imread("main.jpg")
    template = import_img(object)
    # 获得模板图片的高宽尺寸
    theight, twidth = target.shape[:2]
    # 执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(target, template, cv2.TM_SQDIFF_NORMED)
    # 归一化处理
    # 寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 匹配值转换为字符串
    # 对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    # 对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
#    strmin_val = str(min_val)
    cv2.waitKey()
    cv2.destroyAllWindows()
    a = min_loc[0] + 50
    b = min_loc[1] + 50
    x = int(a)
    y = int(b)
    if min_val>0.06:
        return 0,x,y
    else:
        return 1,x,y


def scene_check():
    time.sleep(1)
    
    
    