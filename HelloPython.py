# coding=utf-8

print "Hello Python"

# 计算中文的长度
str1 = u"你好,中国" # 前面加上u
print len(str1)

str1 = "你好,世界" # 使用编码的方法
print len(str1.decode('utf-8'))

# 字符串的拼接,最好不要用+号,性能不高,可以使用下面的方式处理。使用%来连接
str2 = "hello"
print "%s world" % str2
print "%s world, %s" % (str2, "are you ok?")

# 字符串的拼接使用join来处理。字符串的拼接最好还是使用join来处理
print "".join(["hello", " world"])
print ";".join(["hello", "world", "are you ok?"])
