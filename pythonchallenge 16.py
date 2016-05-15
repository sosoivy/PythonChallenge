# -*- coding:utf-8 -*-

from PIL import Image
import numpy as np

im = Image.open('mozart.gif')
imdata = list(im.getdata())
imdata = np.array(imdata)
imdata = imdata.reshape((480, 640))
imdata2 = np.zeros(imdata.shape)

for row in range(imdata.shape[0]):
    # 紫色线段坐标
    idx = np.where(imdata[row, :] == 195)
    idx = idx[0][0] - 1
    # 循环平移，将紫色段移到每一行开头
    imdata2[row, :] = np.r_[imdata[row, idx : 640], imdata[row, 0 : idx]]

imdata2.shape = (480 * 640, )
im.putdata(imdata2)
im.show()