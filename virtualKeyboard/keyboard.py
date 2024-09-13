from utils.drawKeys import Key
import constants.Constants as const


def bd_keyboard():
    startX = const.startX
    startY = const.startY
    w = const.key_width
    h = const.key_height
    Bletters =list("অআইঈউঊএঐওঔকখগঘঙচছজঝঞটঠডঢণতথদধন")
    Bkeys=[]
    for i,l in enumerate(Bletters):
        if i<10:
            Bkeys.append(Key(startX + i*w + i*5, startY, w, h, l))
        elif i<20:
            
            Bkeys.append(Key(startX + (i-10)*w + i*5 -50, startY + h + 5,w,h,l))  
        else:
            Bkeys.append(Key(startX + (i-20)*w + i*5-100, startY + 2*h + 10, w, h, l)) 

    Bkeys.append(Key(startX+25, startY+3*h+15, 5*w, h, "Space"))
    # Bkeys.append(Key(startX+8*w + 50, startY+2*h+10, w, h, "clr"))
    Bkeys.append(Key(startX+5*w+30, startY+3*h+15, 5*w, h, "<--"))
    return Bkeys


def bn_digit_keyboard():
    startX = const.startX
    startY = const.startY
    w = const.key_width
    h = const.key_height
    Bletters =list("০১২৩৪৫৬৭৮৯পফবভমযরলবশষসহ")
    Bletters += [ 'া', 'ি', 'ু', 'ে', 'ো', '্',  'ং']
    Bkeys=[]
    # for i,l in enumerate(Bletters):
    #     if i<10:
    #         Bkeys.append(Key(startX + i*w + i*5, startY, w, h, l))
    for i,l in enumerate(Bletters):
        if i<10:
            Bkeys.append(Key(startX + i*w + i*5, startY, w, h, l))
        elif i<20:
            
            Bkeys.append(Key(startX + (i-10)*w + i*5 -50, startY + h + 5,w,h,l))  
        else:
            Bkeys.append(Key(startX + (i-20)*w + i*5-100, startY + 2*h + 10, w, h, l)) 
    Bkeys.append(Key(startX+25, startY+3*h+15, 5*w, h, "Space"))
    # Bkeys.append(Key(startX+8*w + 50, startY+2*h+10, w, h, "clr"))
    Bkeys.append(Key(startX+5*w+30, startY+3*h+15, 5*w, h, "<--"))
    return Bkeys


def en_keyboard(letterCase='upper'):
    startX = const.startX
    startY = const.startY
    w = const.key_width
    h = const.key_height
    if letterCase=='upper':
        Eletters =list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    else:
        Eletters =list("abcdefghijklmnopqrstuvwxyz")
    Ekeys=[]
    for i,l in enumerate(Eletters):
        if i<10:
            Ekeys.append(Key(startX + i*w + i*5, startY, w, h, l))
        elif i<19:
            Ekeys.append(Key(startX + (i-10)*w + i*5, startY + h + 5,w,h,l))  
        else:
            Ekeys.append(Key(startX + (i-19)*w + i*5, startY + 2*h + 10, w, h, l)) 

    Ekeys.append(Key(startX+25, startY+3*h+15, 5*w, h, "Space"))
    Ekeys.append(Key(startX+8*w + 50, startY+2*h+10, w, h, "clr"))
    Ekeys.append(Key(startX+5*w+30, startY+3*h+15, 5*w, h, "<--"))
    return Ekeys


def fixed_keyboard():
    startX = const.startX
    startY = const.startY
    w = const.key_width
    h = const.key_height
    showKey = Key(300,5,80,50, 'Show')
    exitKey = Key(300,65,80,50, 'Exit')
    changeKey = Key(300,125,80,50, 'Change')
    textBox = Key(startX, startY-h-5, 10*w+9*5, h,'')
    return [showKey, exitKey, changeKey, textBox]