# -*- coding: utf-8 -*-
"""
Created on Sun May 15 22:32:10 2016

@author: IVY
"""

import base64
import wave

infile = open('indian.wav.txt','r')
msg = infile.read()  #这里补上Page Source里的字符串
open('indian.wav', 'wb').write(base64.decodestring(msg))

india = wave.open('indian.wav', 'r')
india_frames = india.readframes(india.getnframes())
india_swap = wave.open('indian_swap.wav', 'w')
india_swap.setnchannels(1)
india_swap.setframerate(india.getframerate())
india_swap.setsampwidth(india.getsampwidth())

india_swap_frames = []
for i in range(0, len(india_frames), 2):
    # 每一帧前后颠倒
    india_swap_frames.append(india_frames[i+1])
    india_swap_frames.append(india_frames[i])

india_swap_frames = ''.join(india_swap_frames)
india_swap.writeframes(india_swap_frames)
india_swap.close()
india.close()
