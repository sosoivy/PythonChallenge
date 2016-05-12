from PIL import Image
import numpy as np

im = Image.open('E:\Development\GitHub\PythonChallenge\cave.jpg')
width, height = im.size
imdata = list(im.getdata())
imdata = np.array(imdata)
imdata = imdata.reshape((height, width, 3))

aa = imdata[0:height:2, 0:width:2, :]
hh = imdata[0:height:2, 1:width:2, :]
vv = imdata[1:height:2, 0:width:2, :]
dd = imdata[1:height:2, 1:width:2, :]
sub_imgs = [aa, hh, vv, dd]
im2 = Image.new(im.mode, (width/2, height/2))

for img in sub_imgs:
    img = img.reshape((-1, 3)).tolist()
    img = [tuple(x) for x in img]
    im2.putdata(img)
    im2.show()