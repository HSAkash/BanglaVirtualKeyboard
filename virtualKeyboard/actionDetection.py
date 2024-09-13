# Without models
import numpy as np
import constants.Constants as const
from utils.key_utils import calculateIntDidtance, getAngle


class ActionDetection:
    def __init__(self):
        self.frames = []
        self.actionTypes = ('up','down','left','right','thumb')
        self.isFrameCollect = False
        self.actionEvaluation = False
        self.fullIndex = 0
        self.collectedIndex = 0

    def is_thumbsUp(self, frame=[], **kwargs):
        if len(frame) == 0:
            return False

        thumb_tip = frame[4]
        index_tip = frame[8]
        middle_tip = frame[12]
        ring_tip = frame[16]
        pinky_tip = frame[20]

        index_mcp = frame[5]
        index_pip = frame[6]

        middle_mcp = frame[9]
        middle_pip = frame[10]

        ring_mcp = frame[13]
        ring_pip = frame[14]

        pinky_mcp = frame[17]
        pinky_pip = frame[18]

        
        if (
                thumb_tip[2] < index_tip[2] and
                thumb_tip[2] < middle_tip[2] and
                thumb_tip[2] < ring_tip[2] and
                thumb_tip[2] < pinky_tip[2]
            ) and (
                np.abs(index_mcp[1] - index_pip[1]) > np.abs(index_mcp[1] - index_tip[1]) and
                np.abs(middle_mcp[1] - middle_pip[1]) > np.abs(middle_mcp[1] - middle_tip[1]) and
                np.abs(ring_mcp[1] - ring_pip[1]) > np.abs(ring_mcp[1] - ring_tip[1]) and
                np.abs(pinky_mcp[1] - pinky_pip[1]) > np.abs(pinky_mcp[1] - pinky_tip[1])  # Check if thumbs up is detected by comparing distances between fingers
            )and (
                    index_tip[0] < index_mcp[0] and
                    middle_tip[0] < middle_mcp[0] and
                    ring_tip[0] < ring_mcp[0] and
                    pinky_tip[0] < pinky_mcp[0]  # Check if thumb is above other fingers
                ):

            return True
        return False
    
    def is_UpOrDown(self):
        action_frames = np.array(self.frames)
        self.frames = []
        action_frames[:,0], action_frames[:,1] = action_frames[:,1].copy() , action_frames[:,0].copy() 
        best_fit_line = np.polyfit(action_frames[:,0], action_frames[:,1], 1)
        best_fit_line = np.poly1d(best_fit_line)

        centerPoint = (action_frames[0][0], int(best_fit_line(action_frames[0][0])))
        pt1 = (action_frames[-1][0], int(best_fit_line(action_frames[-1][0])))
        pt2 = (pt1[0], centerPoint[1])
        angle = getAngle(pt1, centerPoint, pt2)
        if angle < 20:
            
            if action_frames[0][0] > action_frames[-1][0]:
                return 'up'
            else:
                return 'down'
        return "idle"


    def is_LeftOrRight(self):
        action_frames = np.array(self.frames)
        self.frames = []
        best_fit_line = np.polyfit(action_frames[:,0], action_frames[:,1], 1)
        best_fit_line = np.poly1d(best_fit_line)

        centerPoint = (action_frames[0][0], int(best_fit_line(action_frames[0][0])))
        pt1 = (action_frames[-1][0], int(best_fit_line(action_frames[-1][0])))
        pt2 = (pt1[0], centerPoint[1])
        angle = getAngle(pt1, centerPoint, pt2)
        if angle < 20:
            if action_frames[0][0] > action_frames[-1][0]:
                return 'right'
            else:
                return 'left'
        return "idle"
            

    def detect_action(self, frame=[]):
        if self.isFrameCollect:
            self.fullIndex += 1

        if frame and self.is_thumbsUp(frame):
            return "thumb"

        if frame:
            # _________________Other actions________________
            signTipX, signTipY = frame[8][1], frame[8][2]
            midTipX, midTipY = frame[12][1], frame[12][2]
            cal_distance = calculateIntDidtance((midTipX, midTipY), (signTipX, signTipY))

            thumb_tip = frame[4]
            index_tip = frame[8]
            middle_tip = frame[12]
            ring_tip = frame[16]
            pinky_tip = frame[20]

            index_mcp = frame[5]
            index_pip = frame[6]

            middle_mcp = frame[9]
            middle_pip = frame[10]

            ring_mcp = frame[13]
            ring_pip = frame[14]

            pinky_mcp = frame[17]
            pinky_pip = frame[18]

            if not self.isFrameCollect and cal_distance < const.action_finger_distance :
                self.isFrameCollect = True
        
            elif self.isFrameCollect and cal_distance > const.action_finger_distance :
                self.isFrameCollect = False
                self.actionEvaluation = True
        
        if frame and self.isFrameCollect:
            self.frames.append((frame[8][1], frame[8][2]))
            self.collectedIndex += 1

        if self.fullIndex - self.collectedIndex >= const.FRAME_IGNORED:
            self.actionEvaluation = True

        if self.actionEvaluation:
            action_frames = np.array(self.frames)
            self.isFrameCollect = False
            self.actionEvaluation = False
            self.fullIndex = 0
            self.collectedIndex = 0

            x_axis_distance = abs(action_frames[0][0] - action_frames[-1][0])
            y_axis_distance = abs(action_frames[0][1] - action_frames[-1][1])
            if  x_axis_distance > y_axis_distance and x_axis_distance > \
                const.window_width*const.action_distance_percentance:
                    return self.is_LeftOrRight()
            elif x_axis_distance < y_axis_distance and y_axis_distance > \
                const.window_height*const.action_distance_percentance:
                    return self.is_UpOrDown()
                

        return "idle"