# 类装饰器：
# 1. 包含 __call__ 方法的类，就是类装饰器。
# 2. 像调用函数一样，去调用类装饰器的实例对象，就会触发 __call__ 方法的调用。
# 3. __call__ 方法通常接收一个函数作为参数，并且会返回一个新函数。


# class SayHello:
#     def __call__(self,func):
#         def wrapper(*args, **kwargs):
#             print('你好，我要开始计算了')
#             res = func(*args, **kwargs)
#             return res
#         return wrapper
#
# # 使用语法糖 这里是类装饰器，必须使用()
# @SayHello()
# def add(a,b):
#     res= a+b
#     print(f'{a}和{b}相加的结果是：{res}')
#     return res

# 正常调用
# result = add(1,2)
# print(result)

# 使用SayHello 去装饰 add 函数（手动装饰）
# say=SayHello()
# add = say(add)
# result = add(10, 20)
# print(result)

# 带参数的类装饰器
# class SayHello:
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print(f'你好，我要开始{self.msg}计算了')
#             res = func(*args, **kwargs)
#             return res
#
#         return wrapper
#
#
# # 使用语法糖 这里是类装饰器，必须使用()
# @SayHello('加法')
# def add(a, b):
#     res = a + b
#     print(f'{a}和{b}相加的结果是：{res}')
#     return res
#
# result = add(1,2)
# print(result)

# 多个类装饰器的使用
class test1:
    # 关于__init__,如果不需要其他额外的参数就可以不定义初始化方法
    # def __init__(self):
    #     pass
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('我是test1追加的逻辑')
            res = func(*args, **kwargs)
            return res
        return wrapper
class test2:
    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('我是test2追加的逻辑')
            res = func(*args, **kwargs)
            return res
        return wrapper

# 定义好类装饰器后去使用
@test1()
@test2()
def add(a, b):
    res = a + b
    print(f'{a}和{b}相加的结果是：{res}')
    return res

# 调用
# 我是test1追加的逻辑
# 我是test2追加的逻辑
# 1和2相加的结果是：3
# 3
result = add(1,2)
print(result)