# -*- coding:utf-8 -*-

import datetime

# 闰年
years = [y for y in range(1006, 1997) if str(y)[-1] == '6' and y % 4 == 0]

# date和weekday对应
year_c = []
for y in years:
    d = datetime.date(y, 1, 27)
    if d.weekday() == 1:
        year_c.append(y)

# second youngest
print year_c[-2]