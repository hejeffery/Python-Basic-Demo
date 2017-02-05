# coding=utf-8

print "Hello Python"

# 计算中文的长度
str1 = u"你好,中国" # 前面加上u
print len(str1)

str1 = "你好,世界" # 使用编码的方法
print len(str1.decode('utf-8'))