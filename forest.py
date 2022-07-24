from ast import If
import win32api
import win32cont
from pynput import keyboard #事件监听包
from pynput import mouse
import time

# k = PyKeyboard()

def on_press(key):
    '按下按键时执行。'
    try:
        if key == keyboard.Key.f2:
            for i in range(0, 6):

                win32api.keybd_event(112, win32api.MapVirtualKey(112, 0), 0, 0)  # press f1
                time.sleep(0.05)
                win32api.keybd_event(112, win32api.MapVirtualKey(112, 0), win32con.KEYEVENTF_KEYUP, 0)  # release f1

                time.sleep(0.05)

                win32api.keybd_event(38, win32api.MapVirtualKey(38, 0), 0, 0)  # press up
                time.sleep(0.05)
                win32api.keybd_event(38, win32api.MapVirtualKey(38, 0), win32con.KEYEVENTF_KEYUP, 0)  # release up

                time.sleep(0.05)

                win32api.keybd_event(13, win32api.MapVirtualKey(13, 0), 0, 0)  # press ENTER
                time.sleep(0.05)
                win32api.keybd_event(13, win32api.MapVirtualKey(13, 0), win32con.KEYEVENTF_KEYUP, 0)  # release ENTER       

        if key.char == 'q': 
            #快速松开鼠标左键 再按下鼠标左键
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
            time.sleep(0.035)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
            time.sleep(0.05)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

            # win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), 0, 0)  # press s
            # time.sleep(0.09)

            # win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            # time.sleep(0.05)
            # win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), win32con.KEYEVENTF_KEYUP, 0)  # release s


            # win32api.keybd_event(75, win32api.MapVirtualKey(75, 0), 0, 0)  # press d
            # time.sleep(0.15)
            # win32api.keybd_event(75, win32api.MapVirtualKey(75, 0), win32con.KEYEVENTF_KEYUP, 0)  # release j
            # win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), win32con.KEYEVENTF_KEYUP, 0)  # release d


    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    #通过属性判断按键类型。

def on_release(key):
    '松开按键时执行。'
    print('{0} released'.format(
        key))
    if key == keyboard.Key.f9:
        # Stop listener
        return False

def __main__():
    # k = PyKeyboard()

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

__main__()