'''
可变参数
可变位置参数：定义函数时，在行参名前加*，可以接受任意数量的位置参数，并且打包一个元组
可变位置参数：定义函数时，在行参名前加**，可以接受任意数量的关键字参数，并且打包一个字典
'''

# 位置参数
def test1(*args):
    print(args)


test1(1, 2, 3, 4)

print('*' * 20)

# 关键字参数
def test2(**args):
    print(args)


test2(name='hello', age=10, gender='male', height=170)

print('*' * 20)

# 可变位置参数，可变关键字参数，可以同时使用，但必须先写可变位置参数

def test3(*args, **Kargs):
    print(args)
    print(Kargs)


test3("test", name='hello', age=10, gender='male', height=170)

# 可变位置参数，可变关键字参数，可以和其他类型的参数一起使用

print('*' * 20)


def test4(a, b, *args, c='测试使用', **Kargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(Kargs)


test4(1, 2, "test", c='school', name='hello', age=10, gender='male', height=170)
# 使用默认值
test4(1, 2, "test", name='hello', age=10, gender='male', height=170)
