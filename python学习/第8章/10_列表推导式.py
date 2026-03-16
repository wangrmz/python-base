# 列表推导式：用一条简洁语句，从可选代对象中，生成新列表的语法结构。
# 备注：列表推导式本质上是对 for循环 + append() 的一种简写形式。
# 语法格式：[表达式 for 变量 in 可选代对象]

# 需求：让列表中的每个元素，都变成原来的2倍，得到一个新的列表

# 方式一：用map函数
# nums = [10, 20, 30, 40, 50]
# result = map(lambda x: x * 2, nums)
# print(list(result))

# 方式二：使用for循环+append()
# nums = [10, 20, 30, 40, 50]
# result=[]
# for x in nums:
#     result.append(x * 2)
# print(result)

# 方式三：使用列表推导式
# nums = [10, 20, 30, 40, 50]
# result=[x * 2 for x in nums]
# print(result) # [20, 40, 60, 80, 100]

# 带条件的列表推导式
# nums = [10, 20, 30, 40, 50]
# # 左边是表达式，右边是条件，有则写么有则无
# result = [x * 2 for x in nums if x > 20]
# print(result) #[60, 80, 100]


# 字典推导式
# names=['张三','李四','王五']
# scores=[60,70,80]
# # {'张三':60}
# result ={ names[i]:scores[i] for i in range(len(names))}
# print(result) # {'张三': 60, '李四': 70, '王五': 80}

# 集合推导式
names=['张三','李四','王五']
result={n + '!' for n in names}
print(result) #{'王五!', '张三!', '李四!'}





















