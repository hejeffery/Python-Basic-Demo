# coding=utf-8

# time时间模块

import time

print time.time()

localtime = time.localtime(time.time())
print localtime

localtime = time.asctime(time.localtime(time.time()))
print localtime

localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print localtime