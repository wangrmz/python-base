# 函数类型注解：给函数的【参数】和【返回值】添加类型说明。
# 语法格式：函数名(参数1: 类型, 参数2: 类型) ➡️ 返回值类型
# 类似java的函数声明
# public int add(int a,int b){
#     return a+b
# }

# 企业级开发必须写类型注解，方便后期的维护，以及代码的可读性


# 示例1:设置参数类型注解、设置返回类型注解
def add(a: int, b: int) -> int:
    return a + b


result = add(3, 4)
# result = add(3,'20')
print(result)


# 示例2:参数有默认值（Python可以推导出参数的类型）、设置返回值类型
def add(a=1, b=1) -> int:
    return a + b


# 示例3:设置多个返回值类型
def show_nums_info(nums: list[int]) -> tuple[int, int, float]:
    max_value = max(nums)
    min_value = min(nums)
    result = max_value / min_value
    return max_value, min_value, result


info = show_nums_info(list(range(1, 10)))
print(info)  # (9, 1, 9.0)


# 示例4:设置 * args的类型注解，要求 args中的每个参数都必须是 int 类型
def add(*args: int) -> int:
    return sum(args)


result = add(1, 2, 3, 4, 5)
print(result)

# 示例5:设置 * kwargs的类型注解，要求 kwargs中的每个参数都必须是 int 类型 或者 str类型
def show_info(**kwargs: int | str):
   print(kwargs)

show_info(name='张三', age=18, gender='male') #{'name': '张三', 'age': 18, 'gender': 'male'}

# 获取函数的注解信息
print(show_info.__annotations__) #{'kwargs': int | str}
print(add.__annotations__) #{'args': <class 'int'>, 'return': <class 'int'>}
