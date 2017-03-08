# coding=utf-8

# time时间模块

import time
import calendar

# 1488936250.66
print time.time()

# time.struct_time(tm_year=2017, tm_mon=3, tm_mday=8, tm_hour=9, tm_min=24, tm_sec=10, tm_wday=2, tm_yday=67, tm_isdst=0)
localtime = time.localtime(time.time())
print localtime

# Wed Mar  8 09:24:10 2017
localtime = time.asctime(time.localtime(time.time()))
print localtime

# 2017-03-08 09:24:10
localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print localtime

# Wednesday March 08 09:24:10 2017
localtime = time.strftime("%A %B %d %H:%M:%S %Y", time.localtime())
print localtime

# Wed Mar 08 09:27:28 17
localtime = time.strftime("%a %b %d %H:%M:%S %y", time.localtime())
print localtime


localCalendar = calendar.month(2017, 3)
print localCalendar

localCalendar = calendar.calendar(2017, 2, 1)
print localCalendar