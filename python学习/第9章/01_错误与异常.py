# 错误：代码本身有语法错误，解释器无法执行代码 -无法通过异常处理机制解决
# age =18
# if age >= 18
#     print('成年人')


# 异常：代码在语法上没有问题，但是在执行过程中出现了问题 --可以通过异常处理机制解决
# 一些开发中常见的异常：
# 1.ZeroDivisionError:当除数为 0 时触发
# num1=100
# num2=0
# result= num1 / num2 #ZeroDivisionError: division by zero

# 2. TypeError:当操作的数据类型不正确或者不兼容时触发
# result = '10' + 5 # TypeError: can only concatenate str (not "int") to str

# 3.AttributeError:当对象没有指定的属性或者方法时触发
# AttributeError: 'Person' object has no attribute 'gender'
# 演示1
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


# p1=Person('张三',18)
# print(p1.name)
# print(p1.gender)

# 演示2 AttributeError: 'list' object has no attribute 'add'
# nums=[1,2,3,4,5]
# nums.add(9)

# IndexError:当索引超出范围（索引越界）时触发
# IndexError: list index out of range
# nums=[1,2,3,4,5]
# print(nums[5])

# 5.NameError：当使用了不存在的变量时触发
# NameError: name 'school' is not defined
# print(school)

# 6.KeyError：当访问字典中不存在的key时触发
# KeyError: 'gender'
# person={'name':'zhangsan','age':19}
# print(person['gender'])

# 7.ValueError:当值不合法，但是类型正确时触发
# int('100')
# int('hello')  # ValueError: invalid literal for int() with base 10: 'hello'
