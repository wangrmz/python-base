'''
可变集合，不可变集合
定义结合
集合的特点：内部的元素无序，不能通过下标访问元素，会自动去除重复元素

'''
# 定义有内容的可变集合
# s1={10,20,30,40,50,60,70,80,90,10}
# s2={'hello','world','北京'}
# s3={10,'你好',1,True,12.4}
#
# print(type(s1),s1)
# print(type(s2),s2)
# print(type(s3),s3)

# s2.add('天气真好')

# 定义有内容的不可变集合
# <class 'frozenset'> frozenset({70, 40, 10, 80, 50, 20, 90, 60, 30})
# <class 'frozenset'> frozenset({'world', 'hello', '北京'})
# <class 'frozenset'> frozenset({1, 10, '你好', 12.4})
# s1=frozenset({10,20,30,40,50,60,70,80,90,10})
# s2=frozenset({'hello','world','北京'})
# s3=frozenset({10,'你好',1,True,12.4})

# print(type(s1),s1)
# print(type(s2),s2)
# print(type(s3),s3)

#  frozenset接收的参数，可以是任意可迭代的对象，但最终返回的一定是【不可变集合】
# <class 'frozenset'> frozenset({70, 40, 10, 80, 50, 20, 90, 60, 30})
# <class 'frozenset'> frozenset({'北京', 'world', 'hello'})
# <class 'frozenset'> frozenset({'h', 'o', 'l', 'e'})
# s1=frozenset([10,20,30,40,50,60,70,80,90,10])  # 接收列表
# s2=frozenset(('hello','world','北京')) # 接收元组
# s3=frozenset('hello') #接收字符串
#
# print(type(s1),s1)
# print(type(s2),s2)
# print(type(s3),s3)

# 定义空集合
# <class 'set'> set()
# <class 'dict'> {}
# <class 'frozenset'> frozenset()
# s1=set() #可变集合
# s2={} # 这样定义的是空字典
# s3= frozenset() # 不可变集合，开发中基本不用
# print(type(s1),s1)
# print(type(s2),s2)
# print(type(s3),s3)


# 集合中不能嵌套【可变集合】，但是可以嵌套【不可变集合】，只有不可变的东西才能安全放进集合里
# 元组不可变，元组就可以放进去
# 不可变：集合不支持下标，但底层依然需要给其中的每个元素，分配一个‘编号’，这个编号就是哈希值，用来快速定位元素
# 内容一旦变化，哈希值就会变化，无法通过原来的哈希值找到这个元素

s1={10.20,30.40,50}
s2=frozenset({100,200,300,400,500,600})
t1=[66,77,88]
t2=('hello','world')
s4={11,22,33,t2}
# s3={11,22,33,t1}


















