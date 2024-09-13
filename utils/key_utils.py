"""
Calculate the distance between two fingers points.
"""
import numpy as np

def calculateIntDidtance(pt1, pt2):
    return int(((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)**0.5)



"""
Calculate the angle between three points.
"""
def getAngle(pt1, centerP, pt2):
    a = calculateIntDidtance(centerP, pt1)
    b = calculateIntDidtance(centerP, pt2)
    c = calculateIntDidtance(pt1, pt2)
    angle = np.arccos((a**2 + b**2 - c**2)/(2*a*b))
    return int(np.degrees(angle))


