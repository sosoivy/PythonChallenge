# -*- coding: utf-8 -*-
"""
Created on Mon May 09 23:50:02 2016

@author: IVY
"""

from PIL import Image  
  
if __name__ == '__main__':  
  
    img = Image.open('oxygen.png')  
      
    #left,top,right,bottom  
    box = (0, 43, 608, 52)  
      
    belt = img.crop(box)  
      
    #get a sequence object containing pixel values  
    pixels = belt.getdata()  
      
    print('mode: %s' % img.mode)  
    print('amount of pixel: %d' % len(pixels))  
    print(pixels[0])  
      
    #convert mode RGBA to mode L  
    lBelt = belt.convert('L')  
  
    #get a sequence object containing pixel values  
    lPixels = lBelt.getdata()  
      
    #黑白条中的像素点有规律：每一行的像素点都是一样的，并且一行中也有相同的像素。  
    #但有一点不好处理的是：字母间可以通过能否组成单词来判断是否有重复值，但数字  
    #就不能通过这种方法来判断了  
    str = []  
      
    #step 7是通过试验出来的  
    for i in range(0, 608, 7):  
        str.append(chr(lPixels[i]))  
        x = lPixels[i]  
          
    print(''.join(str))  