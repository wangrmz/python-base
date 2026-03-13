
# 集合A.difference(集合B):
# 作用：找出集合A中，不同于集合B的元素（集合A和集合B都不变，返回的是一个新的集合）

# s1={10,20,30,40,50}
# s2={30,40,50,60,70}
# difference = s1.difference(s2) #{10, 20}
# print(difference)


# 集合A.difference_update(集合B)
# 作用:从集合A中删除集合B中存在的元素（集合A会被修改，集合B不会修改）
# 返回值：无
# s1={10,20,30,40,50}
# s2={30,40,50,60,70}
# s1.difference_update(s2) #{20, 10}
# print(s1)

# 集合A.union(集合B)
# 作用：合并两个集合，集合A和集合B都不变
# 返回值：返回一个新的集合
# s1={10,20,30,40,50}
# s2={30,40,50,60,70}
# union = s1.union(s2) #{70, 40, 10, 50, 20, 60, 30}
# print(union)

# 集合A.issubset(集合B)
# 作用：判断集合A是不是集合B的子集
# 规则：如果集合A中的所有元素，都在集合B中，那就返回Ture,否则返回False
# 返回值：布尔值
# s1={10,20,30,40,50}
# s2={10,20,30,40,50,60,70}
# difference = s1.issubset(s2) # True
# print(difference)

# 集合A.issupset(集合B)
# 作用：判断集合A是不是集合B的超集
# 规则：如果集合B中的所有元素，都在集合A中，那就返回Ture,否则返回False
# 返回值：布尔值
# s1={10,20,30,40,50}
# s2={10,20,30,40,50,60,70}
# difference = s2.issuperset(s1) # True
# print(difference)


# 集合A.isdisjoint(集合B)
# 作用：判断集合A和集合B是否没有交接
# 规则：如果没有交接，返回True,但凡存在一个公共元素，就返回False
# 返回值：布尔值

s1={10,20,30,40,50}
s2={50,60,70}
difference = s2.isdisjoint(s1) # False
print(difference)









