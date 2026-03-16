# 一、函数的多返回值

# def calculate(num1, num2):
#     res1 = num1 + num2
#     res2 = num1 * num2
#     return res1, res2
#
#
# res1, res2 = calculate(1, 2)
# print(res1, res2)
# print(calculate(1, 2)) # 元组



# 二、参数的打包与解包


# 1. 打包接收参数：
# *args ：打包所有的位置参数（会形成一个元组）
# **kwargs ：打包所有的关键字参数（会形成一个字典）
# def show_info(*args, **kwargs):
#     print(args, kwargs)
#
# show_info(1, 2,name='zhangsan',age=18,gender='male') #(1, 2) {'name': 'zhangsan', 'age': 18, 'gender': 'male'}


# 2. 解包传递参数
# *变量名 ：将元组拆解成一个一个独立的位置参数
# **变量名 ：将字典拆解一个一个个 key=value 形式的关键字参数
# def show_info(num1,num2,num3,name,age,gender):
#     print(num1,num2,num3)
#     print(name,age,gender)
#
# nums = (10,20,30)
# person={'name':'zhangsan','age':18,'gender':'male'}
# # 直接解包传入
# show_info(*nums,**person)

# 3.打包接收参数 和 解包传递参数组合使用