# -*- coding: utf-8 -*-
"""
Created on Thu May 05 23:21:22 2016

@author: IVY
"""

import urllib,re
 
def read(nothing):
    try:
        head = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
        s = urllib.urlopen(head + nothing).read()
        print s
        # 使用正则表达式匹配抓取到的页面中的最后一个数字
        pat = re.compile('([0-9]+)')
        nothing = re.findall(pat,s)[-1]
        # 返回函数本身 使函数一直执行下去
        return read(nothing)
    except:
        if 'Divide' in s:
            return read(str(int(nothing)/2))
        else:
            pass
 
if __name__ == '__main__':
    read('12345')
    raw_input('<PRESS ENTER>')