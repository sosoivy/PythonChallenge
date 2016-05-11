# -*- coding: utf-8 -*-
"""
Created on Sun May 08 22:59:40 2016

@author: IVY
"""

import re
findnum = re.compile(r'\d+$').findall

import zipfile
zf = zipfile.ZipFile('channel.zip')

zc =[]

name = '90052.txt'
'''path = 'channel\''''
while True:
    zinfo = zf.getinfo(name)
    z=zf.open(name)
    data = findnum(z.read())
    z.close()
    zc.append(zinfo.comment)
    
'''    f = open ('channel/%s' % name)
    data = f.read().split()[-1]
    print data
    f.close
    print zf.getinfo(name).comment
    zc.append(zf.getinfo(name).comment)'''
    
    if data:
        name = '%s.txt' % data[0]
    else:
        break

print ''.join(zc)
