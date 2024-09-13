# BanglaVirtualKeyboard
This virtual Keyboard is for bangla typing. We are using a mediapipe for finding fingers positions. We also add some hand gestures for controlling keyboards. Like change language or change uppercase to lowercase, etc.

## Hand gestures:
  - Hand up to down : English to Bengali
  - Hand down to up : Bengali to English
  - Hand left to right : Upper/Lower case
  - Hand right to left : Letter to digit
  - Thumbs up : Press Enter



https://github.com/user-attachments/assets/384e10d1-0fc0-4c8e-966f-c84c706fdd12



## Keyboard layouts:
<div align="center">
  <img src="/assets/02.png" alt="Step 1: Capture Image" width="33%" style="margin: 0 10px;">
  <img src="/assets/04.png" alt="Step 2: Upload Image" width="33%" style="margin: 0 10px;">
</div>
<div align="center">
  <img src="/assets/01.png" alt="Step 1: Capture Image" width="33%" style="margin: 0 10px;">
  <img src="/assets/03.png" alt="Step 2: Upload Image" width="33%" style="margin: 0 10px;">
</div>

## Requirements
```
mediapipe==0.10.9
numpy==1.26.3
opencv-python==4.9.0.80
PyAutoGUI==0.9.54
pynput==1.7.6
pyudev; sys_platform == 'linux'
pywin32; sys_platform == 'win32'
tk; sys_platform == 'win32'
win32gui; sys_platform == 'win32'
win32con; sys_platform == 'win32'
```
## Install dependencies
```
pip install -r requirements.txt
```
## Run the code
```
python main.py
```
