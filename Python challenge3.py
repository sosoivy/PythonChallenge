# -*- coding: utf-8 -*-
"""
Created on Thu May 05 23:09:31 2016

@author: IVY
"""
import re
import urllib
 Pre = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
 testlist = re.findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]',Pre)
 print(''.join(x[4:5] for x in testlist))