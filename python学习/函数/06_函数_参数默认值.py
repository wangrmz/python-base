
# 参数默认值
'''
定义函数时，通过行参名=xxx的形式，为参数指定一个默认值
默认参数必须放在必选参数的后面，因为某个行参一旦设置了默认值，它后面所有的行参，也必须要写默认值
'''
def greet(name,gender,age,height,msg='你好'):
    print(f'我叫{name},性别{gender},年龄是{age},身高是{height}')
    '''
    f 的作用：格式化字符串（f-string）
    f 是 Python 3.6+ 引入的一种字符串格式化方式，全称是 formatted string literals（格式化字符串字面量）。

     简单来说
     f 放在字符串前面，表示这个字符串里可以直接用大括号 {} 嵌入变量，Python 会自动把变量的值替换进去。
     可以不需要传统方式的拼接，format，或者%拼接
    '''
    print(f'我想说:{msg}')

greet('张三','男',18,172,'hello')
greet('张三','男',18,172)


print('测试默认值')
print('测试默认值',end='!!!')