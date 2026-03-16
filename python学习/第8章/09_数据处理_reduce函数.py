# reduce函数：对一组数据不断进行“合并”，最终归并成一个结果。
# 语法格式：reduce(合并函数，可迭代对象,初始值)
# 备注：reduce函数需要从 functools模块中引入才能使用

# 从functools 模块中引入reduce
from functools import reduce
# 数值统计
nums = [1,2,3,4,5,6,7,8,9]

# 普通的函数
# def count(a,b):
#     return a+b
#
# result = reduce(count, nums,10)# 第一个数是初始值
result = reduce(lambda x,y:x+y, nums,10)
print(result)

# 字符串拼接
str_list = ['a','b','c','d','e','f','g']
result = reduce(lambda x,y:x+y,str_list)
print(result)