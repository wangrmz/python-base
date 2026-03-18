# 知识点1：能被for循环遍历的对象，被称之为可迭代对象

# region
# names=['张三','李四','王五']
# citys=('北京','上海','深圳')
# msg ='hello'
# age =10
# def test():
#     pass
#
# for name in names:
#     print(name)
# endregion

# 知识点2:可迭代对象（iterable）能调用到__iter__方法
# region
# names=['张三','李四','王五']
# citys=('北京','上海','深圳')
# msg ='hello'
# age =10
# def test():
#     pass
#
# # print(names.__iter__())
# print(hasattr(names,'__iter__'))
# print(hasattr(citys,'__iter__'))
# print(hasattr(msg,'__iter__'))
# print(hasattr(age,'__iter__'))
# print(hasattr(test,'__iter__'))
# endregion

# 知识点3:可迭代对象（iterable）调用__iter__方法会得到对应的迭代器iterator
# 备注1:__iter__是一个魔法方法，当调用iter函数时，__iter__会自动调用
# 备注2:可迭代对象.__iter__() 等价于 iter(可迭代对象)
# 备注3:如果iter(obj)能得带一个迭代器（iterator），那么obj就是可迭代对象

# region
# names = ['张三', '李四', '王五']
# citys = ('北京', '上海', '深圳')
# msg = 'hello'
# age = 10
#
#
# def test():
#     pass


# <list_iterator object at 0x100a7f400>
# <tuple_iterator object at 0x100a7f400>
# <str_ascii_iterator object at 0x100a3d390>
# print(names.__iter__())
# print(citys.__iter__())
# print(msg.__iter__())
# 上面的代码和这个是等价的
# print(iter(names))
# print(iter(citys))
# print(iter(msg))

# endregion

# 知识点4:迭代器iterator拥有__next__方法，每次调用都会根据当前的状态，返回下一个元素
# 备注1:迭代器.__next__() 等价于 next(迭代器)
# 备注2:当所有元素都取出来后，继续调用__next__方法，Python会抛出StopIteration异常
# region
# names = ['张三', '李四', '王五']
# it = iter(names)
# print(it.__next__())
# endregion

# for循环背后的逻辑
# region
# names = ['张三', '李四', '王五']

# for循环遍历names列表
# for name in names:
#     print(name)

# for循环背后的逻辑
# 1.iter(可迭代对象) 获取到迭代器
# it = iter(names)
# # 2.开启一个无限循环
# while True:
#     try:
#         # 3.获取所有元素
#         print(next(it))
#     except StopIteration:
#         # 4.遇到异常，退出循环
#         break

# endregion

# 知识点5:迭代器iterator也拥有__iter__方法，并且其返回值是迭代器自身
# 这里设计的原因如下：为了让for循环也能遍历迭代器（为了让iter迭代器不出错）

# region
names = ['张三', '李四', '王五']

# 获取到迭代器
# it = iter(names)
# print(it)  # <list_iterator object at 0x1030f7a00>
# print(type(it))
#
# iter__ = it.__iter__()
# print(iter__)  # <list_iterator object at 0x1030f7a00>
# print(type(iter__))

# it = iter(names)
# for item in it:
#     print(item)
# endregion

# 知识点6:迭代器协议
# 1.能被iter()接受
# 2.能被next()一步一步取值






