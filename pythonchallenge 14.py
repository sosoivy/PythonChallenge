# -*- coding: utf-8 -*-
"""
Created on Thu May 12 23:50:05 2016

@author: IVY
"""

from PIL import Image  
im = Image.open(r'wire.png')  
result = Image.new(im.mode,(100,100))  
direction = [(1,0),(0,1),(-1,0),(0,-1)]  
x,y = -1,0  
k = 0  
steps = 200  
while steps/2>0:  
    for vector in direction:  
        step = steps/2  
        for i in range(step):  
            x = x + vector[0]  
            y = y + vector[1]  
            pixel = im.getpixel((k,0))  
            result.putpixel((x,y),pixel)  
            k +=1  
        steps -= 1  
result.show()  