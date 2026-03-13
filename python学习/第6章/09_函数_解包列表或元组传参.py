def test(data):
    print(f'我是test函数，我收到的参数是：{data}')

list1 =[100,200,300,400]
tuple1=('你好','北京','欢迎你')

# 函数调用时，正常传递:列表或者元组
test(list1)
test(tuple1)

# 函数调用时，使用*对：列表或者元组进行接包后，在传递参数
def test1(*args):
    print(f'我是test函数，我收到的参数是：{args},参数的类型是：{type(args)}')
test1(*list1) # 此种写法相当于：test(100,200,300,400)
test1(*tuple1)
