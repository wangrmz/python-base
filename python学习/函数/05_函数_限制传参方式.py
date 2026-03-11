
# /前边只能用位置参数，*后只能用关键字参数，同时出现的时候/必须在“之前
def greet2(name,/,gender,*,age,height):
    print(f'我叫{name},性别{gender},年龄是{age},身高是{height}')

greet2('wangrm', gender='女', height=165, age=30)


# 参数默认值
'''
定义函数时，通过行参名=xxx的形式，为参数指定一个默认值
默认参数必须放在必选参数的后面，因为某个行参一旦设置了默认值，它后面所有的行参，也必须要写默认值
'''
def greet(name,gender,age,height,msg='你好'):
    print(f'我叫{name},性别{gender},年龄是{age},身高是{height}')
    print(f'我想说:{msg}')

greet('张三','男',18,172,'hello')
greet('张三','男',18,172)