# -*- coding: utf-8 -*-
"""
Created on Thu May 05 23:11:30 2016

@author: IVY
"""

import re
import urllib
ocr = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
data = re.findall(r'<!--(.*?)-->',ocr,re.S)
data = data[1]
for i in data:
    if i in 'aeilquty': print i,