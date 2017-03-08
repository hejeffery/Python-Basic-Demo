# coding=utf-8

# 异常处理

try:
    file = open("hejeffery.txt", "r")

except IOError:
    print "没有找到文件"

else:
    print "找到文件了"


try:
    file = open("hejeffery.txt", "r")

except IOError:
    print "没有找到文件"

finally:
    print "始终都会执行这句话"