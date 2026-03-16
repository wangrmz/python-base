# 装饰器
# 1. 装饰器是一种【可调用对象】（通常是函数），它能接收一个函数作为参数，并且会返回一个新函数。
# 2. 装饰器可以在不修改原函数代码的前提下，增强或改变原函数的功能。

# 实际应用：在不改变原函数的前提下，给函数统一加上：日志、计时、校验、缓存等功能

# 关键点：
# 1. 接收被装饰的函数、同时返回新函数（wrapper）
# 2. 装饰器“吐出来”的是 wrapper 函数，以后别人调用的也是 wrapper 函数。
# 3. 为了保证参数的兼容性，wrapper 函数要通过 *args 和 **kwargs 接收参数。
# 4. wrapper 函数中主要做的是：调用原函数（被装饰的函数）、执行其它逻辑，但要记得将原函数的返回值 return 出去。


# def say_hello(func):
#     def wrapper(*args,**kwargs):
#         # *********
#         print('你好我要开始计算了')
#         return func(*args,**kwargs)
#     return wrapper
#
# @say_hello
# def add(x, y):
#     result = x + y
#     print(f'{x}和{y}相加的结果是：{result}')
#     return result
#
# #正常调用，使用装饰器后可以正常调用
# add1 = add(100, 200)
# print(add1)

# 需求：在不修改add函数的前提下，给add函数增加一些额外的功能，例如：计算前先打印一句欢迎语
# 实现方案：使用装饰器
# 下面这行代码，是手动装饰，写起来麻烦，不推荐，推荐：@装饰器名
# add = say_hello(add)
# result = add(100, 200)
# print(result)


# 进阶：带参数的装饰器(三层嵌套，外层接受配置，中间层接受函数，内层)
def say_hello(msg):
    def outer(func):
        def wrapper(*args, **kwargs):
            print('你好我要开始{msg}计算了')
            return func(*args, **kwargs)
        return wrapper
    return outer


@say_hello('加法')
def add(x, y, z):
    result = x + y + z
    print(f'{x}和{y}和{z}相加的结果是：{result}')
    return result


@say_hello('减法')
def sub(x, y):
    result = x - y
    print(f'{x}和{y}相减的结果是：{result}')
    return result

# 正常调用，使用装饰器后可以正常调用
# add1 = add(100, 200,300)
# print(add1)

# 进阶：多个装饰器一起使用
def test1(func):
    print('我是test1装饰器')
    def wrapper(*args, **kwargs):
        print('test1追加的逻辑')
        return func(*args, **kwargs)
    return wrapper

def test2(func):
    print('我是test2装饰器')
    def wrapper(*args, **kwargs):
        print('test2追加的逻辑')
        return func(*args, **kwargs)
    return wrapper

@test1
@test2
def add(x,y):
    result = x + y
    print(f'{x}和{y}相加的结果是：{result}')
    return    result

# test1追加的逻辑
# test2追加的逻辑
# 100和200相加的结果是：300
# 300
result = add(100, 200)
print(result)

# 分析：add=test1(test2(add))
# 谁离add近谁先工作，也就是说这里是test2先工作
