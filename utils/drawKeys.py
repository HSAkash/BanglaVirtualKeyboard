import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# bangla font path
font_path ='utils/code2000.TTF'


class Key():
    def __init__(self,x,y,w,h,text):
        self.x = x
        self.y = y 
        self.w = w
        self.h = h
        self.text=text
    
    def drawKey(self, img, text_color=(255,255,255), bg_color=(0,0,0),alpha=0.5, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, thickness=2):
        
        #draw the box
        bg_rec = img[self.y : self.y + self.h, self.x : self.x + self.w]
        white_rect = np.ones(bg_rec.shape, dtype=np.uint8) #* 25
        white_rect[:] = bg_color
        res = cv2.addWeighted(bg_rec, alpha, white_rect, 1-alpha, 1.0)
        
        font = ImageFont.truetype(font_path, size=20)
        img_pil = Image.fromarray(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(img_pil)
        draw.text((5, 5), self.text, font=font, fill=(255,255,255))
        res = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
        
        # print(f"res.shape = {res.shape}", img[self.y : self.y + self.h, self.x : self.x + self.w].shape)
        img[self.y : self.y + self.h, self.x : self.x + self.w] = res

    def isOver(self,x,y):
        if (self.x + self.w > x > self.x) and (self.y + self.h> y >self.y):
            return True
        return False