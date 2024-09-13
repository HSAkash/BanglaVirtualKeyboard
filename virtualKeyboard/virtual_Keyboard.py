import cv2
import numpy as np 
import time
from virtualKeyboard.handTracker import HandTracker
from pynput.keyboard import Controller
from utils.key_utils import calculateIntDidtance, getAngle
import constants.Constants as const
from virtualKeyboard.keyboard import bd_keyboard, en_keyboard, fixed_keyboard
from utils.keyboardPrioritize import (
    KPWin,
    KPLinux,
    KPMac,
)
import platform
from virtualKeyboard.actionDetection import ActionDetection
from virtualKeyboard.action import Action

actionDetection_class = ActionDetection()
action_class = Action()

"""
Set the window size.
"""
def set_window_size(window_name, width, height):
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, width, height)



"""
Get the mouse position.
Track index finger to simulate mouse movement.
Track index finger and thumb tip to simulate mouse click.
"""
def getMousPos(event , x, y, flags, param):
    global clickedX, clickedY
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONUP:
        clickedX, clickedY = x, y
    if event == cv2.EVENT_MOUSEMOVE:
        mouseX, mouseY = x, y

def vk(cam_index, h_flip, v_flip):
    global clickedX, clickedY
    global mouseX, mouseY
    # ___________________________Keyboard__________________________________
    showKey, exitKey, changeKey, textBox = fixed_keyboard()

    cap = cv2.VideoCapture(cam_index)
    set_window_size(const.WINDOW_NAME, int(const.camera_width*1.5), int(const.camera_height*1.5))

    if platform.system() == "win32":
        KPWin(const.WINDOW_NAME)

    ptime = 0

    # initiating the hand tracker
    tracker = HandTracker(detectionCon=0.8)

    # getting frame's height and width
    frameWidth = const.camera_width
    frameHeight = const.camera_height

    showKey.x = int(frameWidth*1.5) - 85
    exitKey.x = int(frameWidth*1.5) - 85
    changeKey.x = int(frameWidth*1.5) - 85

    clickedX, clickedY = 0, 0
    mouseX, mouseY = 0, 0

    show = False
    counter = 0
    previousClick = 0

    keyboard = Controller()

    action_frames = []
    while True:
        if counter >0:
            counter -=1
            
        signTipX = 0
        signTipY = 0

        midTipX = 0
        midTipY = 0

        thumbTipX = 0
        thumbTipY = 0

        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.resize(frame,(int(frameWidth*1.5), int(frameHeight*1.5)))

        # frame fill with white color
        # frame = np.ones((int(frameHeight*1.5), int(frameWidth*1.5), 3), np.uint8)*255

        # horizontal flip
        if h_flip:
            frame = cv2.flip(frame, 1)
        # virtcal flip
        if v_flip:
            frame = cv2.flip(frame, 0)
        #find hands
        frame = tracker.findHands(frame)
        lmList = tracker.getPostion(frame, draw=False)
        actionType = actionDetection_class.detect_action(lmList)
        # if actionType != "idle":
        #     print(f"actionType: {actionType}\n\n")
        # if action == "thumb":
        #     print("thumb")
        action_class.action_perform(actionType)
        if lmList:
            signTipX, signTipY = lmList[8][1], lmList[8][2]
            midTipX, midTipY = lmList[12][1], lmList[12][2]
            thumbTipX, thumbTipY = lmList[4][1], lmList[4][2]

            if calculateIntDidtance((signTipX, signTipY), (thumbTipX, thumbTipY)) < const.click_finger_distance:
                centerX = int((signTipX+thumbTipX)/2)
                centerY = int((signTipY + thumbTipY)/2)
                cv2.line(frame, (signTipX, signTipY), (thumbTipX, thumbTipY), (0,255,0),2)
                cv2.circle(frame, (centerX, centerY), 5, (0,255,0), cv2.FILLED)        
        
        ctime = time.time()
        fps = int(1/(ctime-ptime))

        cv2.putText(frame,str(fps) + " FPS", (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,0),2)
        showKey.drawKey(frame,(255,255,255), (0,0,0),0.1, fontScale=0.5)
        exitKey.drawKey(frame,(255,255,255), (0,0,0),0.1, fontScale=0.5)
        if show:
            changeKey.drawKey(frame,(255,255,255), (0,0,0),0.1, fontScale=0.5)
        cv2.setMouseCallback(const.WINDOW_NAME, getMousPos)

        if showKey.isOver(clickedX, clickedY):
            show = not show
            showKey.text = "Hide" if show else "Show"
            clickedX, clickedY = 0, 0
            action_class.changeMode()

        if changeKey.isOver(clickedX, clickedY):
            action_class.leftRightKeyboardAction()


        if exitKey.isOver(clickedX, clickedY):
            #break
            exit()

        #checking if sign finger is over a key and if click happens
        alpha = 0.5
        if show:
            textBox.drawKey(frame, (255,255,255), (0,0,0), 0.3)
            idClicked = calculateIntDidtance((signTipX, signTipY), (thumbTipX, thumbTipY)) < const.click_finger_distance
            for k in action_class.keyboard:
                if (k.isOver(mouseX, mouseY) or k.isOver(signTipX, signTipY)) and idClicked:
                    alpha = 0.1
                    # writing using mouse right click
                    if k.isOver(clickedX, clickedY):                              
                        if k.text == '<--':
                            textBox.text = textBox.text[:-1]
                        elif k.text == 'clr':
                            textBox.text = ''
                        elif len(textBox.text) < 60:
                            if k.text == 'Space':
                                textBox.text += " "
                            else:
                                textBox.text += k.text
                                
                    # writing using fingers
                    if (k.isOver(thumbTipX, thumbTipY)):
                        clickTime = time.time()
                        if clickTime - previousClick > 0.4:                               
                            if k.text == '<--':
                                textBox.text = textBox.text[:-1]
                            elif k.text == 'clr':
                                textBox.text = ''
                            elif len(textBox.text) < 60:
                                if k.text == 'Space':
                                    textBox.text += " "
                                else:
                                    # print(f"key : {k.text}")
                                    # print(k.text.encode('utf-8')=='')
                                    textBox.text += k.text
                                    #simulating the press of actuall keyboard
                                    keyboard.press(k.text)
                            previousClick = clickTime
                k.drawKey(frame,(255,255,255), (0,0,0), alpha=alpha)
                alpha = 0.5
            clickedX, clickedY = 0, 0        
        ptime = ctime
        cv2.imshow(const.WINDOW_NAME, frame)
        if platform.system() == "Linux":
            KPLinux(const.WINDOW_NAME)
        elif platform.system() == "Darwin":
            KPMac(const.WINDOW_NAME)

        ## stop the video when 'q' is pressed
        pressedKey = cv2.waitKey(1)
        if pressedKey == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()