# 迭代器是一次性的，状态只会向前推进，且不会自动重置（迭代器在遍历的过程中会被“消耗”）
# region
from filecmp import clear_cache


# names = ['张三', '李四', '王五']

# 获取到迭代器,只能依次向前推进
# it = iter(names)
# print(next(it))
# print(next(it))
# print(next(it))

# for name in names:
#     print(name)
#
# for item in names:
#     print(item)

# endregion


# 需求：让for循环可以遍历Person的实例对象
# 实现方式1
# region
# class Person:
#     def __init__(self, name, age,gender,address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#
#     def __iter__(self):
#         return PersonIterator(self)
#
#     # def __str__(self):
#     #     return f'{self.name}, {self.age}, {self.gender}, {self.address}'
#
# class PersonIterator:
#     def __init__(self, p):
#         # 将外部传进来的数据保存好
#         self.p = p
#         # 设置迭代器的初始化状态（指针位置）
#         self.index = 0
#
#         # 配置迭代器要迭代的内容
#         self.attr=[p.name,p.age,p.gender,p.address]
#
#     # 迭代的__iter__方法返回迭代器自身
#     def __iter__(self):
#         return self
#     # 每次调用__next__方法，会根据当前的状态，返回下一个元素
#     def __next__(self):
#         if self.index >= len(self.attr):
#             raise StopIteration
#         # 获取要返回的内容
#         value = self.attr[self.index]
#         # 更新迭代器的状态
#         self.index += 1
#         # 返回value
#         return value
#
#
# # 目标：让for循环可以遍历Person的实例对象
# p1 =Person('张三',18,'男','昌平')
# # 测试使用迭代器
# for item in p1:
#     print(item)


# endregion

# 实现方式2
# region
# class Person:
#     def __init__(self, name, age, gender, address):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         # 设置迭代器的初始化状态（指针位置）
#         self.__index = 0
#         # 配置迭代器要迭代的内容
#         self.__attr = [self.name, self.age, self.gender, self.address]
#
#     def __iter__(self):
#         self.__index = 0 # 重置为0
#         return self
#
#     # 每次调用__next__方法，会根据当前的状态，返回下一个元素
#     def __next__(self):
#         if self.__index >= len(self.__attr):
#             raise StopIteration
#         # 获取要返回的内容
#         value = self.__attr[self.__index]
#         # 更新迭代器的状态
#         self.__index += 1
#         # 返回value
#         return value
#
#
# # def __str__(self):
# #     return f'{self.name}, {self.age}, {self.gender}, {self.address}'
#
#
# # 目标：让for循环可以遍历Person的实例对象
# # 可迭代对象，且是迭代器
# p1 = Person('张三', 18, '男', '昌平')
# # 测试使用迭代器
# for item in p1:
#     print(item)

# endregion


# 进阶

# region

class Person:
    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        # 设置迭代器的初始化状态（指针位置）
        self.__index = 0
        # 配置迭代器要迭代的内容
        self.__attr = [self.name, self.age, self.gender, self.address]

    def __iter__(self):
        self.__index = 0  # 重置为0
        return self

    # 每次调用__next__方法，会根据当前的状态，返回下一个元素
    def __next__(self):
        if self.__index >= len(self.__attr):
            raise StopIteration
        # 获取要返回的内容
        value = self.__attr[self.__index]
        if isinstance(value, str):
            value = value.upper()
        # 更新迭代器的状态
        self.__index += 1
        # 返回value
        return value


# def __str__(self):
#     return f'{self.name}, {self.age}, {self.gender}, {self.address}'


# 目标：让for循环可以遍历Person的实例对象
# 可迭代对象，且是迭代器
p1 = Person('张三', 18, '男', '昌平')
# 测试使用迭代器
for item in p1:
    print(item)

# endregion
