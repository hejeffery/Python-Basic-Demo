# coding=utf-8

# 元组,是有序的集合,不可变对象,没有排序、修改等操作

tuple1 = (1, 2, 3, 4, 5)
print tuple1

# 可以通过下标取值
print tuple1[2]

# 支持切片
print tuple1[0 : 3]

# 如何修改元组中的值?先转成list,修改list中的值后再转成tuple。相当于重新生成了一个新的tuple对象
tuple2 = (1, 2, 3)
list = list(tuple2) # 转为list
list[1] = 99 # 修改值
tuple2 = tuple(list) # 转为tuple
print tuple2