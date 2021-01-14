import win32gui
import keyboard
import multiprocessing
import sys

def get_hwnd():
    return win32gui.FindWindow(None, '动物餐厅')

def get_cordinates(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    return left, top, right, bottom

def first():
    hwnd = get_hwnd()
    if hwnd:
        x, y, right, bottom = get_cordinates(hwnd)
        return x, y
    else:
        print('no program found!\nexiting in 5 seconds')
        time.sleep(5)
        sys.exit()