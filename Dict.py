# coding=utf-8

# 字典,无序的,可变的。不能使用切片或者是索引操作
# 字典的key必须是不可变的对象,比如数字,字符串,元组等

# 第一种初始化方式
dict1 = {"key1" : 1, "key2" : "value2", "key3" : [1, 2, 3], "key4" : ("a", "b", "c")}
print dict1

# 第二种初始化方式
# 注意:key不要加“”号
dict2 = dict(key1 = "value1", key2 = "value2")
print dict2

# 打印key3对应的value
print dict1["key3"]

# 修改值
dict1["key4"] = ("A", "B", "C")
print dict1
dict1["key3"][1] = 44
print dict1

# 添加值
dict1["key5"] = 999
print dict1

# update方法
# 注意:update的参数是一个字典。update的字典中有和原字典有相同的key,则value会覆盖;如果和原字典没有相同的key,则添加
dict1.update({"key4" : 123, "key6" : 666})
print dict1

# 删除字典中的某一个元素,使用del
dict3 = dict(key1="value1", key2="value2")
del dict3["key2"]
print dict3

# 清空字典
dict4 = dict(key1="value1", key2="value2")
print dict4
dict4.clear()
print dict4

# pop pop有返回值,返回值是pop出来的key对应的value
# 注意:pop时的key值必须存在,否则会抛异常。但是可以给pop方法添加一个没有key值时对应的值
dict5 = {"key1" : "value1", "key2" : "value2"}
value = dict5.pop("key2")
print value
print dict5
# 给pop方法添加一个没有key值时对应的值
value2 = dict5.pop("key3", "没有该key对应的value的默认值")
print value2

# in 判断的是key而不是value
dict6 = dict(key1 = "value1", key2 = "value2")
print "key2" in dict6

# has_key
dict7 = {"key1" : "value1", "key2" : "value2"}
print dict7.has_key("key1")
print dict7.has_key("key")

# keys方法,返回的是列表
dict8 = {"key1" : "value1", "key2" : "value2"}
print dict8.keys()

# values方法,返回的是列表
dict9 = {"key1" : "value1", "key2" : "value2"}
print dict9.values()

# items方法,返回的是列表,每一个元素是元组
dict10 = {"key1" : "value1", "key2" : "value2"}
print dict10.items()

# get方法,获取值,参数是key
# 注意:get时的key值必须存在,否则会返回none。但是可以给get方法添加一个没有key值时对应的值
dict11 = {"key1" : "value1", "key2" : "value2"}
print dict11.get("key1")
print dict11.get("key3", "没有该key对应的value的默认值")