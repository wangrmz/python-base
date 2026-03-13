# 以下这五个函数：既能定义对应的【空容器】，又能将【其他类型】转换为对应的数据类型

# list 函数：1. 定义空列表。2. 将【可迭代对象】转换为列表
# res1=list(range(10))
# res2=list('欢迎来到python')
# res3=list((10,20,30,40,50))
# res4=list({'张三':22}) # 默认取的是keys，如果需要value，则需要res4=list({'张三':22}.values()),都需要就写items
# print(res1,type(res1))
# print(res2,type(res2))
# print(res3,type(res3))
# print(res4,type(res4))

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <class 'list'>
# ['欢', '迎', '来', '到', 'p', 'y', 't', 'h', 'o', 'n'] <class 'list'>
# [10, 20, 30, 40, 50] <class 'list'>
# ['张三'] <class 'list'>

# tuple 函数：1. 定义空元组。2. 将【可迭代对象】转换为元组
# res1=tuple(range(10))
# res2=tuple('欢迎来到python')
# res3=tuple((10,20,30,40,50))
# res4=tuple({'张三':22}) # 默认取的是keys，如果需要value，则需要res4=list({'张三':22}.values()),都需要就写items
# print(res1,type(res1))
# print(res2,type(res2))
# print(res3,type(res3))
# print(res4,type(res4))

# (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) <class 'tuple'>
# ('欢', '迎', '来', '到', 'p', 'y', 't', 'h', 'o', 'n') <class 'tuple'>
# (10, 20, 30, 40, 50) <class 'tuple'>
# ('张三',) <class 'tuple'>


# set 函数：1. 定义空集合。2. 将【可迭代对象】转换为集合
# res1=set(range(10))
# res2=set('欢迎来到python')
# res3=set((10,20,30,40,50))
# res4=set({'张三':22}) # 默认取的是keys，如果需要value，则需要res4=list({'张三':22}.values()),都需要就写items
# print(res1,type(res1))
# print(res2,type(res2))
# print(res3,type(res3))
# print(res4,type(res4))

# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} <class 'set'>
# {'o', '欢', 't', '到', 'n', 'p', 'y', 'h', '迎', '来'} <class 'set'>
# {40, 10, 50, 20, 30} <class 'set'>
# {'张三'} <class 'set'>

# str 函数：1. 定义空字符串。2. 将【任意类型】转换为字符串
# res1=str(range(10))
# res2=str('欢迎来到python')
# res3=str((10,20,30,40,50))
# res4=str({'张三':22}) # 默认取的是keys，如果需要value，则需要res4=list({'张三':22}.values()),都需要就写items
# print(res1,type(res1))
# print(res2,type(res2))
# print(res3,type(res3))
# print(res4,type(res4))

# range(0, 10) <class 'str'> 惰性转换只是记录了开始和结束
# 欢迎来到python <class 'str'>
# (10, 20, 30, 40, 50) <class 'str'>
# {'张三': 22} <class 'str'>

# dict 函数：1. 定义空字典。2. 将【可迭代对象】转换为字典
# 交给dict函数的必须是键值对
# res1=dict({'张三':72,'李四':66,'王五':85})
# res2=dict([('张三',72),('李四',66),('王五',85)])
# res3=dict((('张三',72),('李四',66),('王五',85)))
# res4=dict({('张三',72),('李四',66),('王五',85)})
# print(res1,type(res1))
# print(res2,type(res2))
# print(res3,type(res3))
# print(res4,type(res4))

# {'张三': 72, '李四': 66, '王五': 85} <class 'dict'>
# {'张三': 72, '李四': 66, '王五': 85} <class 'dict'>
# {'张三': 72, '李四': 66, '王五': 85} <class 'dict'>
# {'李四': 66, '张三': 72, '王五': 85} <class 'dict'>



# 所有的数据容器，都支持成员运算符：in / not in 作用：判断某个“元素”是否在子容器中。


hobby=['抽烟','喝酒','染发']
nums=(10,20,30,40,50)
str1 ='welcome to python'
citys={'北京','天津','上海','苏州'}
score={'张三':72,'李四':66,'王五':85}

print('喝酒' in hobby)
print(20 in nums)
print('come' in str1)
print('天津' in citys)
print('李华' in score)

# True
# True
# True
# True
# False