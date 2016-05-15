# -*- coding: utf-8 -*-
"""
Created on Sun May 15 23:43:37 2016

@author: IVY
"""

import httplib
import base64
from pprint import pprint
import re

def get_range(page, base, limit):
    conn = httplib.HTTPConnection('www.pythonchallenge.com')
    headers = {'Authorization': 'Basic ' + base64.b64encode('butter:fly'),
               'Range': 'bytes=%s-%s' % (base, limit)}
    conn.request('GET', page, '', headers)
    return conn.getresponse()