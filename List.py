# coding=utf-8

list1 = [1, 2, 3, 4, 5]
# 获取列表中的第3个元素
print list1[2]

list2 = [1, 2, 3, [4, 5]]
# 获取列表中的最后1个元素
print list2[-1]

# 切片
list3 = [1, 2, 3, 4, 5]
#  正向,从左至右
# 打印列表中的第1个元素~最后1个元素,步长为2。默认的步长是1
print list3[1 : : 2]

# 反向,从右至左
# 打印列表中的最后1个元素~倒数第3个元素,步长必须是-1
print list3[-1 : -4 : -1]

# 列表的相加
list4 = [1, 2]
list5 = [3, 4]
print list4 + list5

# 使用extend
list6 = [1, 2, 3, 4, 5]
list7 = [6, 7]
list6.extend(list7)
print list6

# 使用append
list8 = [1, 2, 3, 4]
list8.append(5)
print list8

# 使用insert
list9 = [1, 2, 3, 4, 5]
# 第1个参数是位置,第2个参数是值
# 如果插入的位置大于实际的长度,会插入列表的末尾。如果插入的位置是负数且小于实际的长度,比如list9中的第一个参数是-99,相当于插入第0个位置
list9.insert(8, 88)
print list9

# 列表是可变的,所以可以修改
# 注意:下标不能越界,无论是正向还是反向
list10 = [1, 2, 3, 4]
list10[2] = 99
print list10

# 判断成员关系用 in 或者是 not in
list11 = [1, 2, 3, 4]
print 5 in list11
print 1 in list11

# 列表的排序
# 注意:sort()方法返回的值是none。排序会改变原来的列表
list12 = [4, 3, 88, 1, 4, 9]
list12.sort()
print list12

# 列表的反转
# 注意:reverse()方法返回的值是none。排序会改变原来的列表
list13 = [1, 2, 3, 4, 5]
list13.reverse()
print list13

# 推导式
# 生成1~5的列表
# 注意:range(起始点, 终点, 步长),终点是开区间
print [a for a in range(1, 6)]
print [a for a in range(1, 6, 2)]
print [a for a in range(1, 6) if a & 1 == 0] # if是条件,这里是取偶数
print ["hello %d" % a for a in xrange(10)] # 生成格式化的字符串
print [(a, b) for a in range(1, 5) for b in range(1, 5)] # 生成元组
print ["%d haha" % a for a in range(1, 11)] # 生成格式化的字符串
print [(a, b) for a in range(0, 3, 2) for b in range(0, 3, 2)] # 生成元组

# 内置list方法
# 注意:传入的参数必须是可迭代的对象,比如字符串,元组
list14 = "abc"
print list(list14)
list14 = (1, 2, 3)
print list(list14)

# 下面的操作就是删除引用
list15 = [8, 9, 10, 11]
list16 = list15[:]
del list15
print list16

# pop pop可以pop任意索引的值
# 注意:pop是的索引值不能越界
list17 = [1, 2, 3, 4, 5]
popValue1 = list17.pop(3)
popValue2 = list17.pop()
print popValue1
print popValue2


