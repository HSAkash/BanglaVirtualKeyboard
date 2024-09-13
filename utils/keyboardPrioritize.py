import os


def KPWin(WINDOW_NAME):
    import win32gui
    import win32con
    hwnd = win32gui.FindWindow(None, WINDOW_NAME)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                        win32con.SWP_NOMOVE | win32con.SWP_NOSIZE
                        | win32con.SWP_SHOWWINDOW)
    
def KPLinux(WINDOW_NAME):
    os.system(f'wmctrl -r "{WINDOW_NAME}" -b add,above')

def KPMac(WINDOW_NAME):
    # os.system(f'osascript -e \'tell application "{WINDOW_NAME}" to activate\'')
    os.system(f'osascript -e \'tell application "System Events" to set frontmost of the first process whose name is "{WINDOW_NAME}" to true\'')

