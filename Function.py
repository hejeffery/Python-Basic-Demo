# coding=utf-8

# 函数

def hjprint(params):
    print params
    return


hjprint("abcd")

def changeValue(value):
    value = 10
    print value

# 函数的参数是不可变对象时,参数有副本机制
sourceValue = 19
changeValue(sourceValue)
print "source = %d" % sourceValue

# 函数的参数是可变对象时,参数没有副本机制,传递的是引用
def changeListValue(listvalue):
    listvalue[2] = 100
    print listvalue

sourceListValue = [1, 2, 3, 4, 5]
changeListValue(sourceListValue)
print sourceListValue


# lambda表达式
sum = lambda number1, number2: number1 + number2
print sum(2, 8)


# 作用域
total = 0
def sumnumber(arg1, arg2):
    # global total
    total = arg1 + arg2
    print "函数内是局部变量 : ", total
    return total

result = sumnumber(10, 20);
print "total = %d" % total
print "result = %d" % result