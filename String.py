# coding=utf-8

# String 字符串

str = "abc"

# capitalize() 把字符串的第一个字符转为大写
print str.capitalize()

# 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print str.center(20)

string = u"字符串"
print len(string)

# count(),计算str中某个字符出现的次数,参数1:需要计算的字符;参数2:起始位置;参数3:结束位置
str1 = "aabbccddaa"
print str1.count("a" , 0, len(str1))
print str1.count("a")

# endswith(),判断字符串是否以某个字符串结尾
print str1.endswith("aa")

# isalnum(),如果字符串中至少有一个字符并且所有字符都是字母或数字则返回True, 否则返回False
str2 = "abcd1234"
print str2.isalnum()

# isalpha(),如果字符串中至少有一个字符并且所有字符都是字母则返回True, 否则返回False
print str2.isalpha()

str3 = "123456"
# isdigit(),如果字符串中只包含数字则返回True, 否则返回False
print str3.isdigit()

# islower(),如果字符串中包含至少一个区分大小写的字符,并且所有这些(区分大小写的)字符都是小写,则返回True，否则返回False
print str1.islower()

# isupper(),如果字符串中包含至少一个区分大小写的字符,并且所有这些(区分大小写的)字符都是大写,则返回True，否则返回False
print str3.isupper()

# split(),以分割字符串,第二个参数是仅分割的个数。第二参数可选
str4 = "abc,def,ghi,jlk"
print str4.split(",", 1)
