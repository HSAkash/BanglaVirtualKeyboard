import pyautogui
from virtualKeyboard.keyboard import bd_keyboard, en_keyboard, bn_digit_keyboard
from constants.Constants import SCROLLING_DISTANCE, TIME_INTERVAL

from utils.timeLimiter import RateLimiter

class Action:
    def __init__(self):
        self.keyboards = {
            "bd_char": bd_keyboard(),
            "bd_digit": bn_digit_keyboard(),
            "enUpper": en_keyboard(),
            "enLower": en_keyboard("lower"),
        }

        self.actionMode = "mouse"
        self.letterCase = "upper"
        self.current_keyboard = "bd_char"
        self.keyboard = self.keyboards["bd_char"]


    @RateLimiter(TIME_INTERVAL)
    def upDownMouseAction(self, actionType="up"):
        if actionType == "up":
            pyautogui.scroll(-SCROLLING_DISTANCE)
        else:
            pyautogui.scroll(SCROLLING_DISTANCE)

    @RateLimiter(TIME_INTERVAL)
    def upDownKeyboardAction(self, actionType="up"):
        # if actionType == "up":
        #     pass
        # else:
        #     pass
        if self.current_keyboard == "bd_char":
            self.keyboard = self.keyboards["bd_digit"]
            self.current_keyboard = "bd_digit"
        elif self.current_keyboard == "bd_digit":
            self.keyboard = self.keyboards["bd_char"]
            self.current_keyboard = "bd_char"
        elif self.current_keyboard == "enUpper":
            self.keyboard = self.keyboards["enLower"]
            self.current_keyboard = "enLower"
        elif self.current_keyboard == "enLower":
            self.keyboard = self.keyboards["enUpper"]
            self.current_keyboard = "enUpper"
        else:
            self.keyboard = self.keyboards["bd_char"]
            self.current_keyboard = "bd_char"

    
    @RateLimiter(TIME_INTERVAL)
    def leftRightMouseAction(self, actionType="left"):
        if actionType == "left":
            pyautogui.press("left")
        elif actionType == "right":
            pyautogui.press("right")
        else:
            pyautogui.press("right")

    @RateLimiter(TIME_INTERVAL)
    def leftRightKeyboardAction(self, actionType="left"):
        # if actionType == "left":
        #     pass
        # elif actionType == "right":
        #     pass
        # else:
        #     pass

        if self.current_keyboard == "bd_char" or self.current_keyboard == "bd_digit":
            self.keyboard = self.keyboards["enUpper"]
            self.current_keyboard = "enUpper"
        elif self.current_keyboard == "enUpper" or self.current_keyboard == "enLower":
            self.keyboard = self.keyboards["bd_char"]
            self.current_keyboard = "bd_char"
        else:
            self.keyboard = self.keyboards["bd_char"]
            self.current_keyboard = "bd_char"

    @RateLimiter(5)
    def thumbAction(self):
        # press enter
        if self.actionMode == "mouse":
            pyautogui.press("enter")
        elif self.actionMode == "keyboard":
            pyautogui.press("enter")
        else:
            pass

    # @RateLimiter(TIME_INTERVAL)
    def changeMode(self):
        self.actionMode = "mouse" if self.actionMode == "keyboard" else "keyboard"

    
    def action_perform(self, actionType):
        if actionType == "up":
            if self.actionMode == "mouse":
                self.upDownMouseAction("up")
            else:
                self.upDownKeyboardAction("up")
        elif actionType == "down":
            if self.actionMode == "mouse":
                self.upDownMouseAction("down")
            else:
                self.upDownKeyboardAction("down")
        elif actionType == "left":
            if self.actionMode == "mouse":
                self.leftRightMouseAction("left")
            else:
                self.leftRightKeyboardAction("left")
        elif actionType == "right":
            if self.actionMode == "mouse":
                self.leftRightMouseAction("right")
            else:
                self.leftRightKeyboardAction("right")
        elif actionType == "thumb":
            self.thumbAction()
        elif actionType == "mode":
            self.changeMode()
        else:
            pass

