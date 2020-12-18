import win32api
import win32con
from pykeyboard import PyKeyboard
from pykeyboard import PyKeyboardEvent
from pynput import keyboard #事件监听包
import time

k = PyKeyboard()

def on_press(key):
    '按下按键时执行。'
    try:
        # print('alphanumeric key {0} pressed'.format(
        #     type(key.char)))
        if key.char == 'q': #正摇b
            # win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), 0, 0)#press s
            # time.sleep(0.05)
            #
            # win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            # time.sleep(0.1)
            # win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), win32con.KEYEVENTF_KEYUP, 0)#release s
            #
            #
            # win32api.keybd_event(75, win32api.MapVirtualKey(75, 0), 0, 0)#press k
            # time.sleep(0.1)
            #
            # win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), win32con.KEYEVENTF_KEYUP, 0)#release d
            # win32api.keybd_event(75, win32api.MapVirtualKey(75, 0), win32con.KEYEVENTF_KEYUP, 0)#release j


            win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), 0, 0)  # press s
            time.sleep(0.09)

            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            time.sleep(0.05)
            win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), win32con.KEYEVENTF_KEYUP, 0)  # release s


            win32api.keybd_event(75, win32api.MapVirtualKey(75, 0), 0, 0)  # press d
            time.sleep(0.15)
            win32api.keybd_event(75, win32api.MapVirtualKey(75, 0), win32con.KEYEVENTF_KEYUP, 0)  # release j
            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), win32con.KEYEVENTF_KEYUP, 0)  # release d

        if key.char == 'e': #地雷震
            # win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            # time.sleep(0.03)
            #
            # win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), 0, 0)  # press s
            # win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), win32con.KEYEVENTF_KEYUP, 0)  # release d
            # time.sleep(0.05)
            # win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), win32con.KEYEVENTF_KEYUP, 0)  # release s
            #
            # time.sleep(0.1)
            # win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            # win32api.keybd_event(74, win32api.MapVirtualKey(74, 0), 0, 0)  # press j
            # time.sleep(0.2)

            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            time.sleep(0.09)
            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), win32con.KEYEVENTF_KEYUP, 0)  # release d

            win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), 0, 0)  # press s
            time.sleep(0.05)
            win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), win32con.KEYEVENTF_KEYUP, 0)  # release s

            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            win32api.keybd_event(74, win32api.MapVirtualKey(74, 0), 0, 0)  # press j
            time.sleep(0.15)
            win32api.keybd_event(74, win32api.MapVirtualKey(74, 0), win32con.KEYEVENTF_KEYUP, 0)  # press j
            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), win32con.KEYEVENTF_KEYUP, 0)  # release d\

        if key.char == 'z': #假震
            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            time.sleep(0.09)#0.06
            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), win32con.KEYEVENTF_KEYUP, 0)  # release d

            win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), 0, 0)  # press s
            time.sleep(0.05)
            win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), win32con.KEYEVENTF_KEYUP, 0)  # release s

            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            win32api.keybd_event(74, win32api.MapVirtualKey(85, 0), 0, 0)  # press j
            time.sleep(0.15)
            win32api.keybd_event(74, win32api.MapVirtualKey(85, 0), win32con.KEYEVENTF_KEYUP, 0)  # press j
            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), win32con.KEYEVENTF_KEYUP, 0)  # release d

        if key.char == 'c': #反摇b
            win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), 0, 0)  # press s
            time.sleep(0.09)

            win32api.keybd_event(65, win32api.MapVirtualKey(65, 0), 0, 0)  # press A
            time.sleep(0.05)
            win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), win32con.KEYEVENTF_KEYUP, 0)  # release s

            win32api.keybd_event(75, win32api.MapVirtualKey(75, 0), 0, 0)  # press j
            time.sleep(0.15)
            win32api.keybd_event(75, win32api.MapVirtualKey(75, 0), win32con.KEYEVENTF_KEYUP, 0)  # release j
            win32api.keybd_event(65, win32api.MapVirtualKey(65, 0), win32con.KEYEVENTF_KEYUP, 0)  # release a

        if key.char == "x": #岚之山
            # win32api.keybd_event(65, win32api.MapVirtualKey(65, 0), 0, 0)  # press a
            # time.sleep(0.09)
            # win32api.keybd_event(65, win32api.MapVirtualKey(65, 0), win32con.KEYEVENTF_KEYUP, 0)  # release a
            #
            # win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), 0, 0)  # press s
            # time.sleep(0.05)
            # win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), win32con.KEYEVENTF_KEYUP, 0)  # release s
            #
            # win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            # time.sleep(0.09)
            # win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), win32con.KEYEVENTF_KEYUP, 0)  # release d
            #
            # win32api.keybd_event(65, win32api.MapVirtualKey(65, 0), 0, 0)  # press a
            # time.sleep(0.09)
            # win32api.keybd_event(65, win32api.MapVirtualKey(65, 0), win32con.KEYEVENTF_KEYUP, 0)  # release a
            #
            # win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), 0, 0)  # press s
            # time.sleep(0.05)
            # win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), win32con.KEYEVENTF_KEYUP, 0)  # release s
            #
            # win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            # win32api.keybd_event(75, win32api.MapVirtualKey(75, 0), 0, 0)  # press k
            # time.sleep(0.15)
            # win32api.keybd_event(75, win32api.MapVirtualKey(75, 0), win32con.KEYEVENTF_KEYUP, 0)  # release k
            # win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), win32con.KEYEVENTF_KEYUP, 0)  # release d

            win32api.keybd_event(65, win32api.MapVirtualKey(65, 0), 0, 0)  # press a
            time.sleep(0.05)
            win32api.keybd_event(65, win32api.MapVirtualKey(65, 0), win32con.KEYEVENTF_KEYUP, 0)  # release a

            win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), 0, 0)  # press s
            time.sleep(0.05)
            win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), win32con.KEYEVENTF_KEYUP, 0)  # release s

            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            time.sleep(0.05)
            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), win32con.KEYEVENTF_KEYUP, 0)  # release d

            win32api.keybd_event(65, win32api.MapVirtualKey(65, 0), 0, 0)  # press a
            time.sleep(0.05)
            win32api.keybd_event(65, win32api.MapVirtualKey(65, 0), win32con.KEYEVENTF_KEYUP, 0)  # release a

            win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), 0, 0)  # press s
            time.sleep(0.05)
            win32api.keybd_event(83, win32api.MapVirtualKey(83, 0), win32con.KEYEVENTF_KEYUP, 0)  # release s

            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), 0, 0)  # press d
            time.sleep(0.13) #12 3

            win32api.keybd_event(75, win32api.MapVirtualKey(75, 0), 0, 0)  # press k
            time.sleep(0.03)
            win32api.keybd_event(75, win32api.MapVirtualKey(75, 0), win32con.KEYEVENTF_KEYUP, 0)  # release k
            win32api.keybd_event(68, win32api.MapVirtualKey(68, 0), win32con.KEYEVENTF_KEYUP, 0)  # release d


    except AttributeError:
        print('special key {0} pressed'.format(
            key))
    #通过属性判断按键类型。


def on_release(key):
    '松开按键时执行。'
    # print('{0} released'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def __main__():
    k = PyKeyboard()

    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


__main__()