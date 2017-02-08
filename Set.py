# coding=utf-8

# 集合set,无序的,可变的,只能存放可迭代的对象,比如列表,元组,字典等。不能使用切片或者是索引操作
# 集合frozenset,无序的,不可变的

# 生成一个set
set1 = set("abcd")
print set1

# set的add方法
set2 = set("abcd")
set2.add("e")
print set2

# set的update方法
set3 = set(["abcd", "hello"])
set3.update("hello")
print set3

# set的remove方法
# 注意:删除不存在的元素会抛异常
set4 = set(["ab", "cd", "ef", "gh"])
set4.remove("ef")
print set4

# in和not in
set5 = set(["ab", "cd", "ef", "gh", "ij"])
print "cd" in set5
print "a" in set5
print "b" not in set5

# 集合的交集,并集,差集
set6 = set(["ab", "cd", "ef", "gh", "ij"])
set7 = set(["cd", "ef", "12"])
print set6 & set7 # 交集
print set6 | set7 # 并集
print set6 - set7 # 差集

# 集合的去重
list1 = [1, 2, 3, 4, 5, 4, 5]
list1 = list(set(list1))
list1.sort()
print list1